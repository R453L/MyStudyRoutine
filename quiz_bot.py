import os
import json
import random
import asyncio
from datetime import datetime, timezone, timedelta
import httpx

BOT_TOKEN  = os.environ["BOT_TOKEN"]
GROUP_ID   = os.environ["GROUP_ID"]   # গ্রুপের chat id (negative number)
STATE_FILE = "state.json"
BASE_URL   = f"https://api.telegram.org/bot{BOT_TOKEN}"

# questions.py থেকে import
from questions import EEE_QUESTIONS, NON_DEPT_QUESTIONS

BD_TZ = timezone(timedelta(hours=6))

# ─── State load (bot.py এর same state file ব্যবহার করে) ──
def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"day_index": 0, "week": 1,
            "eee_order": list(range(7)),
            "non_queues": {}, "non_pointers": {}}

# ─── আজকের EEE day label বের করো ─────────────────────────
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

# ─── Telegram API helpers ─────────────────────────────────
async def send_poll(question, options, correct_idx, explanation):
    """Telegram quiz poll — ক্লিক করলেই ঠিক/ভুল দেখাবে"""
    async with httpx.AsyncClient(timeout=20) as client:
        r = await client.post(f"{BASE_URL}/sendPoll", json={
            "chat_id":              GROUP_ID,
            "question":             question[:300],
            "options":              [o[:100] for o in options],
            "type":                 "quiz",
            "correct_option_id":    correct_idx,
            "explanation":          explanation[:200] if explanation else "",
            "is_anonymous":         False,
        })
        r.raise_for_status()
        return r.json()["result"]["message_id"]

async def send_text(text):
    async with httpx.AsyncClient(timeout=20) as client:
        r = await client.post(f"{BASE_URL}/sendMessage", json={
            "chat_id":    GROUP_ID,
            "text":       text,
            "parse_mode": "HTML",
        })
        r.raise_for_status()
        return r.json()["result"]["message_id"]

# ─── Main Quiz Sender ─────────────────────────────────────
async def main():
    state   = load_state()
    day_idx = state.get("day_index", 0)
    week    = state.get("week", 1)
    eee_order = state.get("eee_order", list(range(7)))

    now      = datetime.now(BD_TZ)
    days     = ["সোমবার","মঙ্গলবার","বুধবার","বৃহস্পতিবার","শুক্রবার","শনিবার","রবিবার"]
    day_name = days[now.weekday()]

    # আজকের EEE subject
    eee_key = EEE_DAY_KEYS[eee_order[day_idx]]
    eee_topics = EEE_QUESTIONS.get(eee_key, [])

    # ── Header ───────────────────────────────────────────
    await send_text(
        f"🌙 <b>রাতের Quiz Session</b>\n"
        f"📅 {day_name} | Week {week}\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📚 <b>Non-Department MCQ</b> আসছে..."
    )
    await asyncio.sleep(2)

    # ── Non-Dept MCQ (প্রতি subject থেকে ৫টা) ───────────
    for subj in NON_DEPT_KEYS:
        topics = NON_DEPT_QUESTIONS.get(subj, [])
        if not topics:
            continue

        all_mcqs = []
        for t in topics:
            all_mcqs.extend(t["mcq"])

        # ৫টা random বাছাই
        selected = random.sample(all_mcqs, min(5, len(all_mcqs)))

        await send_text(f"🔵 <b>{subj}</b>")
        await asyncio.sleep(1)

        for mcq in selected:
            await send_poll(
                question    = mcq["q"],
                options     = mcq["options"],
                correct_idx = mcq["answer"],
                explanation = mcq.get("explanation", ""),
            )
            await asyncio.sleep(1.5)

    # ── EEE MCQ + Math ────────────────────────────────────
    await send_text(
        f"━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"⚡ <b>EEE MCQ: {eee_key}</b>"
    )
    await asyncio.sleep(2)

    for topic_data in eee_topics:
        topic_name = topic_data["topic"]
        mcqs       = topic_data.get("mcq", [])
        math       = topic_data.get("math", None)

        await send_text(f"📌 <b>{topic_name}</b>")
        await asyncio.sleep(1)

        # ৫টা MCQ poll
        for mcq in mcqs[:5]:
            await send_poll(
                question    = mcq["q"],
                options     = mcq["options"],
                correct_idx = mcq["answer"],
                explanation = mcq.get("explanation", ""),
            )
            await asyncio.sleep(1.5)

        # ১টা Math (spoiler এ solution)
        if math:
            math_text = (
                f"📐 <b>Math Problem:</b>\n"
                f"{math['q']}\n\n"
                f"<tg-spoiler>✅ <b>Solution:</b>\n{math['solution']}</tg-spoiler>"
            )
            await send_text(math_text)
            await asyncio.sleep(2)

    # ── Footer ────────────────────────────────────────────
    await send_text(
        "━━━━━━━━━━━━━━━━━━━━━━━\n"
        "✅ <b>আজকের Quiz শেষ!</b>\n"
        "🔁 সকালের routine দেখতে pinned message চেক করো।\n"
        "💪 <i>ভালো করেছো — চালিয়ে যাও!</i>"
    )

    print(f"✅ Quiz sent for day_index={day_idx}, eee={eee_key}")

if __name__ == "__main__":
    asyncio.run(main())
