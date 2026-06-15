import os
import json
import asyncio
import base64
import httpx
from datetime import datetime, timezone, timedelta

BOT_TOKEN    = os.environ["BOT_TOKEN"]
GROUP_ID     = os.environ["GROUP_ID"]
GEMINI_KEY   = os.environ["GEMINI_API_KEY"]
BANK_FILE    = "questions_bank.json"
BASE_URL     = f"https://api.telegram.org/bot{BOT_TOKEN}"
GEMINI_URL   = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_KEY}"
BD_TZ        = timezone(timedelta(hours=6))

# ── Load/Save question bank ───────────────────────────────
def load_bank():
    if os.path.exists(BANK_FILE):
        with open(BANK_FILE) as f:
            return json.load(f)
    return {"non_dept": [], "last_processed_update_id": 0}

def save_bank(bank):
    with open(BANK_FILE, "w", encoding="utf-8") as f:
        json.dump(bank, f, ensure_ascii=False, indent=2)

# ── Telegram API ──────────────────────────────────────────
async def get_updates(offset=0):
    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.get(f"{BASE_URL}/getUpdates", params={
            "offset": offset,
            "limit": 100,
        })
        r.raise_for_status()
        return r.json()["result"]

async def get_file_url(file_id):
    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.get(f"{BASE_URL}/getFile", params={"file_id": file_id})
        r.raise_for_status()
        file_path = r.json()["result"]["file_path"]
        return f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_path}"

async def download_image(url):
    async with httpx.AsyncClient(timeout=60) as client:
        r = await client.get(url)
        r.raise_for_status()
        return base64.b64encode(r.content).decode("utf-8")

# ── Gemini Vision ─────────────────────────────────────────
async def extract_questions_from_image(image_b64):
    prompt = """এই ছবিতে MCQ প্রশ্ন আছে। প্রতিটা প্রশ্ন extract করো।

নিচের JSON format এ return করো (শুধু JSON, অন্য কিছু না):
{
  "questions": [
    {
      "q": "প্রশ্নের text",
      "options": ["ক. option1", "খ. option2", "গ. option3", "ঘ. option4"],
      "answer": 0,
      "explanation": "সংক্ষিপ্ত ব্যাখ্যা"
    }
  ]
}

নিয়ম:
- answer হবে সঠিক option এর index (0=ক, 1=খ, 2=গ, 3=ঘ)
- উত্তর ছবিতে 'উ. ক/খ/গ/ঘ' আকারে দেওয়া থাকে
- options এ ক/খ/গ/ঘ prefix রাখো
- explanation সংক্ষিপ্ত রাখো (৫০ শব্দের মধ্যে)
- শুধু JSON return করো"""

    payload = {
        "contents": [{
            "parts": [
                {"text": prompt},
                {"inline_data": {"mime_type": "image/jpeg", "data": image_b64}}
            ]
        }]
    }

    async with httpx.AsyncClient(timeout=60) as client:
        r = await client.post(GEMINI_URL, json=payload)
        r.raise_for_status()
        text = r.json()["candidates"][0]["content"]["parts"][0]["text"]

    # JSON parse
    text = text.strip()
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
    text = text.strip()

    return json.loads(text)

# ── Find /save commands in group ──────────────────────────
async def find_save_commands(updates, last_id):
    """
    /save command খোঁজো।
    Command টা হয়:
    1. ছবির caption এ /save লেখা
    2. অথবা কোনো message এ /save লেখা যেটা ছবির reply
    """
    # সব messages index করো
    messages = {}
    for update in updates:
        msg = update.get("message", {})
        if not msg:
            continue
        mid = msg.get("message_id")
        if mid:
            messages[mid] = msg

    save_groups = []  # list of image sets to process

    for update in updates:
        msg = update.get("message", {})
        if not msg:
            continue

        update_id = update.get("update_id", 0)
        if update_id <= last_id:
            continue

        text = msg.get("text", "") or msg.get("caption", "")

        # /save command detect
        if "/save" not in text.lower():
            continue

        print(f"Found /save command in message {msg.get('message_id')}")

        # এই message এ কি ছবি আছে?
        images = []

        # reply to a message?
        reply = msg.get("reply_to_message", {})
        if reply:
            # reply করা message এ ছবি আছে?
            if reply.get("photo"):
                images.append(reply["photo"][-1]["file_id"])
            # media group (album)?
            media_group_id = reply.get("media_group_id")
            if media_group_id:
                # same media group এর সব ছবি খোঁজো
                for mid, m in messages.items():
                    if m.get("media_group_id") == media_group_id and m.get("photo"):
                        fid = m["photo"][-1]["file_id"]
                        if fid not in images:
                            images.append(fid)

        # command message নিজেই ছবি?
        if msg.get("photo"):
            fid = msg["photo"][-1]["file_id"]
            if fid not in images:
                images.append(fid)

        if images:
            save_groups.append(images)
            print(f"  → {len(images)} image(s) to process")

    return save_groups

# ── Main ──────────────────────────────────────────────────
async def main():
    bank = load_bank()
    last_id = bank.get("last_processed_update_id", 0)

    print(f"📥 Fetching updates from Telegram (offset={last_id+1})...")
    updates = await get_updates(offset=last_id + 1)

    if not updates:
        print("No new updates found.")
        return

    # সর্বোচ্চ update_id save করো
    max_update_id = max(u["update_id"] for u in updates)

    # /save command এর ছবি খোঁজো
    save_groups = await find_save_commands(updates, last_id)

    if not save_groups:
        print("No /save commands found.")
        bank["last_processed_update_id"] = max_update_id
        save_bank(bank)
        return

    total_added = 0

    for i, image_ids in enumerate(save_groups):
        print(f"\n🖼️ Processing group {i+1}: {len(image_ids)} image(s)")

        for j, file_id in enumerate(image_ids):
            print(f"  Image {j+1}/{len(image_ids)}: downloading...")
            try:
                file_url  = await get_file_url(file_id)
                image_b64 = await download_image(file_url)

                print(f"  Sending to Gemini...")
                result = await extract_questions_from_image(image_b64)
                questions = result.get("questions", [])

                print(f"  ✅ Extracted {len(questions)} questions")

                for q in questions:
                    # duplicate check
                    existing = [x["q"] for x in bank["non_dept"]]
                    if q["q"] not in existing:
                        q["added_at"] = datetime.now(BD_TZ).strftime("%Y-%m-%d")
                        bank["non_dept"].append(q)
                        total_added += 1

                await asyncio.sleep(3)  # Gemini rate limit

            except Exception as e:
                print(f"  ❌ Error: {e}")
                continue

    bank["last_processed_update_id"] = max_update_id
    save_bank(bank)

    print(f"\n✅ Done! Added {total_added} new questions.")
    print(f"📊 Total in bank: {len(bank['non_dept'])} questions")

if __name__ == "__main__":
    asyncio.run(main())
