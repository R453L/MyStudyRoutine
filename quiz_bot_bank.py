import os, json, random, asyncio
from datetime import datetime, timezone, timedelta
import httpx

BOT_TOKEN  = os.environ["BOT_TOKEN"]
GROUP_ID   = os.environ["GROUP_ID"]
BANK_FILE  = "questions_bank.json"
BASE_URL   = f"https://api.telegram.org/bot{BOT_TOKEN}"
BD_TZ      = timezone(timedelta(hours=6))

# কতটা poll পাঠাবে প্রতিদিন
POLLS_PER_DAY = 10

def load_bank():
    if os.path.exists(BANK_FILE):
        with open(BANK_FILE) as f:
            return json.load(f)
    return {"non_dept": [], "sent_indices": [], "last_reset": ""}

def save_bank(bank):
    with open(BANK_FILE, "w", encoding="utf-8") as f:
        json.dump(bank, f, ensure_ascii=False, indent=2)

async def api_call(endpoint, payload, retries=5):
    async with httpx.AsyncClient(timeout=30) as client:
        for attempt in range(retries):
            r = await client.post(f"{BASE_URL}/{endpoint}", json=payload)
            if r.status_code == 429:
                wait = r.json().get("parameters", {}).get("retry_after", 15) + 5
                print(f"⏳ Rate limit. Waiting {wait}s...")
                await asyncio.sleep(wait)
                continue
            if not r.is_success:
                print(f"❌ {r.status_code}: {r.text[:100]}")
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
    await asyncio.sleep(3)

async def main():
    bank      = load_bank()
    questions = bank.get("non_dept", [])

    if not questions:
        print("❌ Question bank empty! Send images with /save command first.")
        await send_text(
            "❌ <b>Question bank খালি!</b>\n"
            "ছবি group এ পাঠাও এবং reply এ <code>/save</code> লেখো।"
        )
        return

    now      = datetime.now(BD_TZ)
    days     = ["সোমবার","মঙ্গলবার","বুধবার","বৃহস্পতিবার","শুক্রবার","শনিবার","রবিবার"]
    day_name = days[now.weekday()]
    date_str = now.strftime("%d/%m/%Y")

    # sent_indices track করো — সব গেলে reset
    sent = set(bank.get("sent_indices", []))
    available = [i for i in range(len(questions)) if i not in sent]

    if len(available) < POLLS_PER_DAY:
        # সব প্রশ্ন শেষ — reset করো
        print("🔄 All questions sent. Resetting...")
        sent = set()
        available = list(range(len(questions)))
        bank["sent_indices"] = []

    # আজকের random প্রশ্ন বাছাই
    today_indices = random.sample(available, min(POLLS_PER_DAY, len(available)))

    await send_text(
        f"📚 <b>Non-Dept Quiz</b>\n"
        f"📅 {day_name} | {date_str}\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"আজকের {len(today_indices)}টা প্রশ্ন শুরু হচ্ছে..."
    )

    for idx in today_indices:
        q = questions[idx]
        await send_poll(
            q["q"],
            q["options"],
            q["answer"],
            q.get("explanation", ""),
        )

    # sent list আপডেট
    bank["sent_indices"] = list(sent | set(today_indices))
    bank["last_sent"]    = date_str
    save_bank(bank)

    await send_text(
        f"✅ <b>আজকের Quiz শেষ!</b>\n"
        f"📊 Bank এ মোট: {len(questions)} প্রশ্ন\n"
        f"💪 <i>চালিয়ে যাও!</i>"
    )
    print(f"✅ Sent {len(today_indices)} polls. Bank: {len(questions)} total.")

if __name__ == "__main__":
    asyncio.run(main())
