import os
import json
import random
import asyncio
from datetime import datetime
import httpx

# ─── Config ───────────────────────────────────────────────
BOT_TOKEN   = os.environ["BOT_TOKEN"]
CHAT_ID     = os.environ["CHAT_ID"]          # group chat id (negative number)
STATE_FILE  = "state.json"                   # tracks shuffle state
BASE_URL    = f"https://api.telegram.org/bot{BOT_TOKEN}"

# ─── EEE Department Topics (7 days) ──────────────────────
EEE_TOPICS = [
    {
        "day_label": "Circuit Theory & Network Analysis",
        "topics": [
            "KVL, KCL — Mesh & Nodal Analysis (Math practice)",
            "Thevenin & Norton Theorem (Numerical)",
            "Star-Delta Conversion, Wheatstone Bridge",
            "AC Circuit — Impedance, Phasor, Power Factor",
        ]
    },
    {
        "day_label": "Electronics — Devices & Circuits",
        "topics": [
            "Diode — V-I Characteristics, Half/Full wave Rectifier",
            "BJT — CE/CB/CC Config, Biasing, h-parameter",
            "MOSFET & JFET — Characteristics & Operating Region",
            "Op-Amp — Inverting, Non-inverting, Differentiator, Integrator",
        ]
    },
    {
        "day_label": "Power Engineering",
        "topics": [
            "Transformer — Turns ratio, Efficiency, OC/SC Test",
            "DC Motor & Generator — EMF, Torque, Speed equation",
            "Induction Motor — Slip, Torque-Speed Curve",
            "Power System — Per Unit System, Fault Analysis",
        ]
    },
    {
        "day_label": "Signals & Control Systems",
        "topics": [
            "Fourier Series & Fourier Transform (Numerical)",
            "Laplace Transform — Transfer Function",
            "Control — Block Diagram, Mason's Rule, Stability",
            "Bode Plot, Root Locus, PID Controller",
        ]
    },
    {
        "day_label": "Digital Electronics & Microprocessor",
        "topics": [
            "Number System — Binary, Hex, BCD Conversion",
            "Boolean Algebra & K-Map Simplification",
            "Flip-Flop, Counter, Register, ADC/DAC",
            "8085/8086 — Architecture, Instruction Set, Interrupts",
        ]
    },
    {
        "day_label": "Electromagnetics & Communication",
        "topics": [
            "Electrostatics — Coulomb's Law, Gauss's Law, Capacitance",
            "Magnetostatics — Ampere's Law, Faraday's Law, Inductance",
            "Transmission Line — Characteristic impedance, VSWR",
            "Communication — AM/FM Modulation, SNR, Bandwidth",
        ]
    },
    {
        "day_label": "Mixed Revision + Power & DSP",
        "topics": [
            "Power Factor Correction, 3-phase Circuit Calculation",
            "Z-Transform, Sampling Theorem, Filter Design",
            "Previous Job Exam MCQ Practice (BPSC/BREB/DESCO)",
            "All formula revision — Circuit + Power + Electronics",
        ]
    },
]

# ─── Non-Department Topics (7 days) ──────────────────────
NON_DEPT_TOPICS = [
    {
        "day_label": "বাংলা ভাষা ও সাহিত্য",
        "topics": [
            "ব্যাকরণ — সন্ধি, সমাস, কারক-বিভক্তি",
            "বাংলা সাহিত্যের যুগ বিভাগ ও বিখ্যাত লেখক",
            "বানান শুদ্ধি ও বাগধারা",
            "প্রবন্ধ সাহিত্য — রবীন্দ্রনাথ, বঙ্কিমচন্দ্র",
        ]
    },
    {
        "day_label": "English Language & Literature",
        "topics": [
            "Grammar — Tense, Voice, Narration",
            "Vocabulary — Synonyms, Antonyms, Idioms",
            "English Literature — Shakespeare, Milton, Keats",
            "Sentence Correction & Error Finding",
        ]
    },
    {
        "day_label": "বাংলাদেশ বিষয়াবলি",
        "topics": [
            "মুক্তিযুদ্ধ — ইতিহাস, গুরুত্বপূর্ণ তারিখ",
            "বাংলাদেশের সংবিধান — মূলনীতি, সংশোধনী",
            "অর্থনীতি — GDP, রপ্তানি, শিল্প",
            "প্রশাসনিক বিভাগ, নদ-নদী, জেলা",
        ]
    },
    {
        "day_label": "আন্তর্জাতিক বিষয়াবলি",
        "topics": [
            "জাতিসংঘ — গঠন, সংস্থা, সদর দপ্তর",
            "আন্তর্জাতিক সংগঠন — IMF, WTO, WHO",
            "সাম্প্রতিক আন্তর্জাতিক ঘটনা",
            "বিশ্বের বিখ্যাত চুক্তি ও সম্মেলন",
        ]
    },
    {
        "day_label": "সাধারণ বিজ্ঞান",
        "topics": [
            "পদার্থবিজ্ঞান — তাপ, আলো, শব্দ",
            "রসায়ন — মৌল, যৌগ, পর্যায় সারণি",
            "জীববিজ্ঞান — কোষ, রোগ, পুষ্টি",
            "দৈনন্দিন বিজ্ঞান — গ্যাস, তড়িৎ, চুম্বক",
        ]
    },
    {
        "day_label": "কম্পিউটার ও তথ্যপ্রযুক্তি",
        "topics": [
            "কম্পিউটার প্রজন্ম, হার্ডওয়্যার, সফটওয়্যার",
            "নেটওয়ার্ক — LAN, WAN, OSI Model, TCP/IP",
            "ডেটাবেস — SQL, DBMS",
            "সাইবার সিকিউরিটি, ইন্টারনেট, ই-গভর্ন্যান্স",
        ]
    },
    {
        "day_label": "গাণিতিক যুক্তি",
        "topics": [
            "সংখ্যাতত্ত্ব — ল.সা.গু, গ.সা.গু, ভাজ্যতা",
            "বীজগণিত — সমীকরণ, অসমতা",
            "জ্যামিতি — ত্রিভুজ, বৃত্ত, ক্ষেত্রফল",
            "পরিসংখ্যান — গড়, মধ্যক, প্রচুরক",
        ]
    },
]


# ─── State management ─────────────────────────────────────
def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    # First run — create shuffled orders
    eee_order  = list(range(7))
    non_order  = list(range(7))
    random.shuffle(eee_order)
    random.shuffle(non_order)
    return {"day_index": 0, "eee_order": eee_order, "non_order": non_order, "week": 1}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def advance_state(state):
    state["day_index"] += 1
    if state["day_index"] >= 7:
        state["day_index"] = 0
        state["week"] += 1
        # Reshuffle for new week
        eee_order = list(range(7))
        non_order = list(range(7))
        random.shuffle(eee_order)
        random.shuffle(non_order)
        state["eee_order"] = eee_order
        state["non_order"] = non_order
    save_state(state)
    return state


# ─── Message builder ──────────────────────────────────────
def build_message(state):
    idx      = state["day_index"]
    week     = state["week"]
    eee_day  = EEE_TOPICS[state["eee_order"][idx]]
    non_day  = NON_DEPT_TOPICS[state["non_order"][idx]]

    bd_days  = ["রবিবার","সোমবার","মঙ্গলবার","বুধবার","বৃহস্পতিবার","শুক্রবার","শনিবার"]
    today    = bd_days[datetime.utcnow().weekday() % 7]   # approx BD day
    date_str = datetime.utcnow().strftime("%d/%m/%Y")

    lines = [
        f"📅 *{today} | {date_str} | Week {week}*",
        f"━━━━━━━━━━━━━━━━━━",
        f"",
        f"⚡ *EEE: {eee_day['day_label']}*",
    ]
    for i, t in enumerate(eee_day["topics"], 1):
        lines.append(f"  {i}. {t}")

    lines += [
        f"",
        f"📚 *Non-Dept: {non_day['day_label']}*",
    ]
    for i, t in enumerate(non_day["topics"], 1):
        lines.append(f"  {i}. {t}")

    lines += [
        f"",
        f"━━━━━━━━━━━━━━━━━━",
        f"💪 *আজকের লক্ষ্য: ৮+ ঘন্টা পড়া!*",
        f"🔁 টপিক প্রতি সপ্তাহে র‍্যান্ডম shuffle হয়।",
    ]
    return "\n".join(lines)


# ─── Telegram API calls ───────────────────────────────────
async def send_message(text: str) -> int:
    async with httpx.AsyncClient() as client:
        r = await client.post(f"{BASE_URL}/sendMessage", json={
            "chat_id": CHAT_ID,
            "text": text,
            "parse_mode": "Markdown",
        })
        r.raise_for_status()
        return r.json()["result"]["message_id"]

async def pin_message(message_id: int):
    async with httpx.AsyncClient() as client:
        r = await client.post(f"{BASE_URL}/pinChatMessage", json={
            "chat_id": CHAT_ID,
            "message_id": message_id,
            "disable_notification": True,
        })
        r.raise_for_status()


# ─── Main ─────────────────────────────────────────────────
async def main():
    state      = load_state()
    message    = build_message(state)
    msg_id     = await send_message(message)
    await pin_message(msg_id)
    advance_state(state)
    print(f"✅ Sent & pinned message_id={msg_id}  week={state['week']}  next_index={state['day_index']}")

if __name__ == "__main__":
    asyncio.run(main())
