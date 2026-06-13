import os
import json
import random
import asyncio
from datetime import datetime, timezone, timedelta
import httpx

BOT_TOKEN  = os.environ["BOT_TOKEN"]
GROUP_ID   = os.environ["GROUP_ID"]
STATE_FILE = "state.json"
# কোন batch পাঠাতে হবে (0-7), workflow থেকে pass হবে
BATCH_NUM  = int(os.environ.get("BATCH_NUM", "0"))
BASE_URL   = f"https://api.telegram.org/bot{BOT_TOKEN}"

from questions import EEE_QUESTIONS, NON_DEPT_QUESTIONS

BD_TZ = timezone(timedelta(hours=6))

EEE_DAY_KEYS = [
    "Circuit Theory & Network Analysis",
    "Electronics — Devices & Circuits",
    "Power Engineering",
    "Signals & Control Systems",
    "Digital Electronics & Microprocessor",
    "Electromagnetics & Communication",
    "DSP, Power Electronics & Revision",
]
NON_DEPT_KEYS = list(NON_DEPT_QUESTIONS.keys())

# ── API call with retry ───────────────────────────────────
async def api_call(endpoint, payload, retries=6):
    async with httpx.AsyncClient(timeout=30) as client:
        for attempt in range(retries):
            r = await client.post(f"{BASE_URL}/{endpoint}", json=payload)
            if r.status_code == 429:
                wait = r.json().get("parameters", {}).get("retry_after", 20) + 10
                print(f"⏳ Rate limit. Waiting {wait}s...")
                await asyncio.sleep(wait)
                continue
            if not r.is_success:
                print(f"❌ {r.status_code}: {r.text}")
                return None
            return r.json()["result"]
    return None

async def send_poll(question, options, correct_idx, explanation):
    result = await api_call("sendPoll", {
        "chat_id":           GROUP_ID,
        "question":          question[:300],
        "options":           [o[:100] for o in options],
        "type":              "quiz",
        "correct_option_id": correct_idx,
        "explanation":       explanation[:200] if explanation else "",
        "is_anonymous":      False,
    })
    await asyncio.sleep(12)
    return result

async def send_text(text):
    # strip unsupported tags, use plain HTML only
    result = await api_call("sendMessage", {
        "chat_id":    GROUP_ID,
        "text":       text,
        "parse_mode": "HTML",
    })
    await asyncio.sleep(5)
    return result

# ── State ─────────────────────────────────────────────────
def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"day_index": 0, "week": 1, "eee_order": list(range(7))}

# ── Build batch list ──────────────────────────────────────
# Batch 0-6: Non-Dept subjects (একটা করে)
# Batch 7: EEE topics
def build_batches(eee_key):
    batches = []

    # Batch 0-6: Non-Dept (৭টা subject আলাদা আলাদা batch)
    for subj in NON_DEPT_KEYS:
        topics   = NON_DEPT_QUESTIONS.get(subj, [])
        all_mcqs = []
        for t in topics:
            all_mcqs.extend(t["mcq"])
        selected = random.sample(all_mcqs, min(5, len(all_mcqs)))
        batches.append({"type": "non_dept", "subj": subj, "mcqs": selected})

    # Batch 7: EEE (সব topics একসাথে)
    eee_topics = EEE_QUESTIONS.get(eee_key, [])
    batches.append({"type": "eee", "key": eee_key, "topics": eee_topics})

    return batches

# ── Main ──────────────────────────────────────────────────
async def main():
    state     = load_state()
    day_idx   = state.get("day_index", 0)
    week      = state.get("week", 1)
    eee_order = state.get("eee_order", list(range(7)))
    eee_key   = EEE_DAY_KEYS[eee_order[day_idx]]

    now      = datetime.now(BD_TZ)
    days     = ["সোমবার","মঙ্গলবার","বুধবার","বৃহস্পতিবার","শুক্রবার","শনিবার","রবিবার"]
    day_name = days[now.weekday()]

    # random seed fix করো যেন সব batch এ same questions আসে
    random.seed(f"{day_idx}-{week}")
    batches = build_batches(eee_key)

    if BATCH_NUM >= len(batches):
        print(f"❌ Invalid BATCH_NUM={BATCH_NUM}, max={len(batches)-1}")
        return

    batch = batches[BATCH_NUM]

    if batch["type"] == "non_dept":
        subj  = batch["subj"]
        mcqs  = batch["mcqs"]
        emoji_map = {
            "বাংলা ভাষা ও সাহিত্য":         "🔵",
            "English Language & Literature":  "🟢",
            "বাংলাদেশ বিষয়াবলি":             "🟡",
            "আন্তর্জাতিক বিষয়াবলি":          "🟠",
            "সাধারণ বিজ্ঞান":                 "🔴",
            "কম্পিউটার ও তথ্যপ্রযুক্তি":     "🟣",
            "গাণিতিক যুক্তি":                 "⚪",
        }
        emoji = emoji_map.get(subj, "📚")
        await send_text(
            f"{emoji} <b>{subj}</b>\n"
            f"📅 {day_name} | Week {week} | Batch {BATCH_NUM+1}/8"
        )
        for mcq in mcqs:
            await send_poll(mcq["q"], mcq["options"], mcq["answer"], mcq.get("explanation",""))

    elif batch["type"] == "eee":
        await send_text(
            f"⚡ <b>EEE Quiz: {eee_key}</b>\n"
            f"📅 {day_name} | Week {week} | Final Batch"
        )
        for topic_data in batch["topics"]:
            await send_text(f"📌 <b>{topic_data['topic']}</b>")
            for mcq in topic_data.get("mcq", [])[:5]:
                await send_poll(mcq["q"], mcq["options"], mcq["answer"], mcq.get("explanation",""))
            math = topic_data.get("math")
            if math:
                await send_text(
                    f"📐 <b>Math:</b> {math['q']}\n\n"
                    f"✅ <b>Solution:</b>\n<code>{math['solution']}</code>"
                )

        await send_text("✅ <b>আজকের সব Quiz শেষ! ভালো করেছো 💪</b>")

    print(f"✅ Batch {BATCH_NUM} done.")

if __name__ == "__main__":
    asyncio.run(main())
