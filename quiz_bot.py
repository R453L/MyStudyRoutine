import os
import json
import random
import asyncio
from datetime import datetime, timezone, timedelta
import httpx

BOT_TOKEN  = os.environ["BOT_TOKEN"]
GROUP_ID   = os.environ["GROUP_ID"]
STATE_FILE = "state.json"
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

# ── Rate-limit safe API call with retry ──────────────────
async def api_call(endpoint: str, payload: dict, retries: int = 6):
    async with httpx.AsyncClient(timeout=30) as client:
        for attempt in range(retries):
            r = await client.post(f"{BASE_URL}/{endpoint}", json=payload)
            if r.status_code == 429:
                retry_after = r.json().get("parameters", {}).get("retry_after", 15)
                wait = retry_after + 3
                print(f"⏳ Rate limited. Waiting {wait}s (attempt {attempt+1})")
                await asyncio.sleep(wait)
                continue
            r.raise_for_status()
            return r.json()["result"]
        raise Exception(f"Failed after {retries} retries on {endpoint}")

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
    await asyncio.sleep(5)  # 5s between each poll
    return result["message_id"]

async def send_text(text):
    result = await api_call("sendMessage", {
        "chat_id":    GROUP_ID,
        "text":       text,
        "parse_mode": "HTML",
    })
    await asyncio.sleep(3)
    return result["message_id"]

# ── State ─────────────────────────────────────────────────
def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"day_index": 0, "week": 1, "eee_order": list(range(7))}

# ── Main ──────────────────────────────────────────────────
async def main():
    state     = load_state()
    day_idx   = state.get("day_index", 0)
    week      = state.get("week", 1)
    eee_order = state.get("eee_order", list(range(7)))

    now      = datetime.now(BD_TZ)
    days     = ["সোমবার","মঙ্গলবার","বুধবার","বৃহস্পতিবার","শুক্রবার","শনিবার","রবিবার"]
    day_name = days[now.weekday()]

    eee_key    = EEE_DAY_KEYS[eee_order[day_idx]]
    eee_topics = EEE_QUESTIONS.get(eee_key, [])

    # ── Header
    await send_text(
        f"🌙 <b>রাতের Quiz Session</b>\n"
        f"📅 {day_name} | Week {week}\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📚 <b>Non-Department MCQ শুরু হচ্ছে...</b>"
    )

    # ── Non-Dept: প্রতি subject থেকে ৫টা MCQ
    for subj in NON_DEPT_KEYS:
        topics = NON_DEPT_QUESTIONS.get(subj, [])
        if not topics:
            continue

        all_mcqs = []
        for t in topics:
            all_mcqs.extend(t["mcq"])

        selected = random.sample(all_mcqs, min(5, len(all_mcqs)))

        await send_text(f"🔵 <b>{subj}</b>")

        for mcq in selected:
            await send_poll(
                question    = mcq["q"],
                options     = mcq["options"],
                correct_idx = mcq["answer"],
                explanation = mcq.get("explanation", ""),
            )

    # ── EEE MCQ + Math
    await send_text(
        f"━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"⚡ <b>EEE: {eee_key}</b>"
    )

    for topic_data in eee_topics:
        topic_name = topic_data["topic"]
        mcqs       = topic_data.get("mcq", [])
        math       = topic_data.get("math", None)

        await send_text(f"📌 <b>{topic_name}</b>")

        for mcq in mcqs[:5]:
            await send_poll(
                question    = mcq["q"],
                options     = mcq["options"],
                correct_idx = mcq["answer"],
                explanation = mcq.get("explanation", ""),
            )

        if math:
            await send_text(
                f"📐 <b>Math Problem:</b>\n"
                f"{math['q']}\n\n"
                f"<tg-spoiler>✅ <b>Solution:</b>\n{math['solution']}</tg-spoiler>"
            )

    # ── Footer
    await send_text(
        "━━━━━━━━━━━━━━━━━━━━━━━\n"
        "✅ <b>আজকের Quiz শেষ!</b>\n"
        "💪 <i>ভালো করেছো — চালিয়ে যাও!</i>"
    )
    print(f"✅ Quiz done — eee={eee_key}")

if __name__ == "__main__":
    asyncio.run(main())
