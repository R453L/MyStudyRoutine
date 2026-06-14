import os, json, random, asyncio, math
from datetime import datetime, timezone, timedelta
import httpx

BOT_TOKEN  = os.environ["BOT_TOKEN"]
GROUP_ID   = os.environ["GROUP_ID"]
STATE_FILE = "state.json"
BATCH_NUM  = int(os.environ.get("BATCH_NUM", "0"))
BASE_URL   = f"https://api.telegram.org/bot{BOT_TOKEN}"

from topics import EEE_DAYS, NON_DEPT, NON_DEPT_SUBJECTS
from questions import EEE_QUESTIONS, NON_DEPT_QUESTIONS

BD_TZ = timezone(timedelta(hours=6))

# topics.py label → questions.py key
EEE_LABEL_TO_QKEY = {
    "⚡ DC Circuit (Part-1)":                    "Part-1: DC Circuit",
    "🔌 AC Circuit (Part-1)":                    "Part-1: AC Circuit",
    "🏭 Power System (Part-2)":                  "Part-2: Power System",
    "🔧 Electrical Machine (Part-3)":            "Part-3: Electrical Machine",
    "💡 Electronics (Part-4)":                   "Part-4: Electronics",
    "📡 Communication & Signals (Part-5) — A":  "Part-5: Communication & Signals",
    "📶 Communication & Signals (Part-5) — B":  "Part-5: Communication & Signals",
}

SUBJECT_EMOJI = {
    "বাংলা ভাষা ও সাহিত্য":         "🔵",
    "English Language & Literature":  "🟢",
    "বাংলাদেশ বিষয়াবলি":             "🟡",
    "আন্তর্জাতিক বিষয়াবলি":          "🟠",
    "সাধারণ বিজ্ঞান":                 "🔴",
    "কম্পিউটার ও তথ্যপ্রযুক্তি":     "🟣",
    "গাণিতিক যুক্তি":                 "⚪",
}

# ── API ───────────────────────────────────────────────────
async def api_call(endpoint, payload, retries=6):
    async with httpx.AsyncClient(timeout=30) as client:
        for attempt in range(retries):
            r = await client.post(f"{BASE_URL}/{endpoint}", json=payload)
            if r.status_code == 429:
                wait = r.json().get("parameters", {}).get("retry_after", 20) + 10
                print(f"⏳ Rate limit. Waiting {wait}s (attempt {attempt+1})")
                await asyncio.sleep(wait)
                continue
            if not r.is_success:
                print(f"❌ {r.status_code}: {r.text[:200]}")
                return None
            return r.json()["result"]
    return None

async def send_poll(q, options, correct_idx, explanation):
    await api_call("sendPoll", {
        "chat_id":           GROUP_ID,
        "question":          q[:300],
        "options":           [o[:100] for o in options],
        "type":              "quiz",
        "correct_option_id": correct_idx,
        "explanation":       explanation[:200] if explanation else "",
        "is_anonymous":      False,
    })
    await asyncio.sleep(12)

async def send_text(text):
    await api_call("sendMessage", {
        "chat_id":    GROUP_ID,
        "text":       text,
        "parse_mode": "HTML",
    })
    await asyncio.sleep(5)

# ── State ─────────────────────────────────────────────────
def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    eee_order = list(range(7))
    random.shuffle(eee_order)
    return {"day_index": 0, "week": 1, "eee_order": eee_order,
            "non_queues": {}, "non_pointers": {}}

# ── Build schedule ────────────────────────────────────────
def build_schedule(day_idx, eee_order, week):
    random.seed(f"{day_idx}-{week}")

    # আজকের EEE day
    eee_day   = EEE_DAYS[eee_order[day_idx]]
    eee_label = eee_day["label"]
    qkey      = EEE_LABEL_TO_QKEY.get(eee_label, "")
    eee_qtopics = EEE_QUESTIONS.get(qkey, [])

    schedule = []

    # Batch 0: বাংলা + English
    # Batch 1: বাংলাদেশ + আন্তর্জাতিক
    # Batch 2: বিজ্ঞান + কম্পিউটার
    # Batch 3: গণিত
    non_groups = [
        [NON_DEPT_SUBJECTS[0], NON_DEPT_SUBJECTS[1]],
        [NON_DEPT_SUBJECTS[2], NON_DEPT_SUBJECTS[3]],
        [NON_DEPT_SUBJECTS[4], NON_DEPT_SUBJECTS[5]],
        [NON_DEPT_SUBJECTS[6]],
    ]
    for group in non_groups:
        items = []
        for subj in group:
            all_mcqs = []
            for t in NON_DEPT_QUESTIONS.get(subj, []):
                all_mcqs.extend(t["mcq"])
            selected = random.sample(all_mcqs, min(5, len(all_mcqs)))
            items.append({"subj": subj, "mcqs": selected})
        schedule.append({"type": "non_dept", "items": items})

    # EEE: 2 topics per batch
    for i in range(0, len(eee_qtopics), 2):
        schedule.append({
            "type":   "eee",
            "label":  eee_label,
            "topics": eee_qtopics[i:i+2],
        })

    return schedule

# ── Main ──────────────────────────────────────────────────
async def main():
    state     = load_state()
    day_idx   = state.get("day_index", 0)
    week      = state.get("week", 1)
    eee_order = state.get("eee_order", list(range(7)))

    now      = datetime.now(BD_TZ)
    days     = ["সোমবার","মঙ্গলবার","বুধবার","বৃহস্পতিবার","শুক্রবার","শনিবার","রবিবার"]
    day_name = days[now.weekday()]

    schedule   = build_schedule(day_idx, eee_order, week)
    eee_batches = [b for b in schedule if b["type"] == "eee"]
    total       = len(schedule)

    if BATCH_NUM >= total:
        print(f"⏭️ BATCH_NUM={BATCH_NUM} >= total={total}. Skipping (today has fewer topics).")
        return

    batch = schedule[BATCH_NUM]

    # ── Non-Dept batch ─────────────────────────────────
    if batch["type"] == "non_dept":
        for item in batch["items"]:
            subj  = item["subj"]
            emoji = SUBJECT_EMOJI.get(subj, "📚")
            await send_text(
                f"{emoji} <b>{subj}</b>\n"
                f"📅 {day_name} | Week {week} | Batch {BATCH_NUM+1}/{total}"
            )
            for mcq in item["mcqs"]:
                await send_poll(
                    mcq["q"], mcq["options"],
                    mcq["answer"], mcq.get("explanation", "")
                )

    # ── EEE batch ──────────────────────────────────────
    elif batch["type"] == "eee":
        eee_batch_idx = BATCH_NUM - 4
        await send_text(
            f"⚡ <b>{batch['label']}</b>\n"
            f"📅 {day_name} | Week {week} "
            f"| EEE Batch {eee_batch_idx+1}/{len(eee_batches)}"
        )
        for topic_data in batch["topics"]:
            await send_text(f"📌 <b>{topic_data['topic']}</b>")
            for mcq in topic_data.get("mcq", [])[:5]:
                await send_poll(
                    mcq["q"], mcq["options"],
                    mcq["answer"], mcq.get("explanation", "")
                )
            math = topic_data.get("math")
            if math:
                await send_text(
                    f"📐 <b>Math:</b>\n{math['q']}\n\n"
                    f"✅ <b>Solution:</b>\n<code>{math['solution']}</code>"
                )

        # শেষ EEE batch হলে footer
        if eee_batch_idx + 1 == len(eee_batches):
            await send_text(
                "━━━━━━━━━━━━━━━━━━━━━━━\n"
                "✅ <b>আজকের সব Quiz শেষ!</b>\n"
                "💪 <i>অনেক ভালো করেছো — চালিয়ে যাও!</i>"
            )

    print(f"✅ Batch {BATCH_NUM}/{total-1} sent. day={day_idx} week={week}")

if __name__ == "__main__":
    asyncio.run(main())
