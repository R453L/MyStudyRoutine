import os
import json
import random
import asyncio
from datetime import datetime, timezone, timedelta
import httpx

BOT_TOKEN  = os.environ["BOT_TOKEN"]
CHAT_ID    = os.environ["CHAT_ID"]
STATE_FILE = "state.json"
BASE_URL   = f"https://api.telegram.org/bot{BOT_TOKEN}"

BD_TZ = timezone(timedelta(hours=6))

# ════════════════════════════════════════════════════════
# EEE TOPICS  —  7 day blocks, each block has many topics
# so that the full syllabus is covered in one week
# ════════════════════════════════════════════════════════
EEE_DAYS = [
    {
        "label": "⚡ Circuit Theory & Network Analysis",
        "topics": [
            "KVL ও KCL — branch current method",
            "Mesh Analysis (matrix form সহ)",
            "Nodal Analysis (supernode সহ)",
            "Thevenin Theorem — step-by-step numerical",
            "Norton Theorem ও Thevenin↔Norton রূপান্তর",
            "Superposition Theorem (multi-source circuit)",
            "Maximum Power Transfer — proof ও numerical",
            "Star ↔ Delta Conversion",
            "Wheatstone Bridge — balance condition ও galvanometer current",
            "AC Circuit — Impedance, Reactance, Admittance",
            "Phasor diagram — series RLC",
            "Power Factor, Real/Reactive/Apparent Power",
            "Resonance — series ও parallel (Q-factor, bandwidth)",
        ],
    },
    {
        "label": "🔬 Electronics — Devices & Circuits",
        "topics": [
            "Diode — V-I characteristics, ideal vs practical",
            "Half-wave Rectifier — Vdc, Idc, ripple factor",
            "Full-wave Rectifier (bridge) — efficiency, PIV",
            "Filter circuits — capacitor filter, ripple voltage",
            "Zener diode — voltage regulation",
            "BJT — CB, CE, CC configuration comparison",
            "BJT Biasing — fixed, voltage divider, feedback",
            "BJT h-parameter — Ai, Av, Ri, Ro",
            "FET (JFET) — characteristics, pinch-off, IDSS",
            "MOSFET — enhancement vs depletion, operating regions",
            "Op-Amp — ideal characteristics, CMRR, slew rate",
            "Inverting & Non-inverting amplifier — gain calculation",
            "Summing amplifier, Differentiator, Integrator",
            "Comparator, Schmitt trigger",
        ],
    },
    {
        "label": "🔌 Power Engineering",
        "topics": [
            "Transformer — EMF equation, turns ratio",
            "Transformer — equivalent circuit, voltage regulation",
            "OC Test — core loss, no-load current calculation",
            "SC Test — copper loss, equivalent impedance",
            "Transformer efficiency — condition for max efficiency",
            "All-day efficiency",
            "Auto-transformer — saving of copper",
            "DC Generator — EMF equation, types, OCC",
            "DC Motor — back EMF, torque equation, speed control",
            "DC Motor — starters, speed-torque characteristics",
            "3-phase Induction Motor — rotating field, slip",
            "Induction Motor — torque equation, max torque condition",
            "Induction Motor — equivalent circuit, efficiency",
            "Synchronous Machine — excitation, Vφ equation",
            "Power System — per-unit system calculation",
            "Symmetrical fault — short circuit MVA",
            "Power factor correction — capacitor sizing",
            "3-phase circuit — star/delta, balanced load",
        ],
    },
    {
        "label": "📡 Signals & Control Systems",
        "topics": [
            "Signal types — energy vs power signal",
            "Fourier Series — trigonometric & exponential form",
            "Fourier Transform — properties ও pairs",
            "Laplace Transform — properties, pairs, ROC",
            "Inverse Laplace — partial fraction method",
            "Transfer Function — poles, zeros, order",
            "Block diagram reduction — rules ও numerical",
            "Signal Flow Graph — Mason's gain formula",
            "Time domain — step response, 2nd order system",
            "Steady-state error — type 0/1/2 system",
            "Stability — Routh-Hurwitz criterion",
            "Root Locus — construction rules",
            "Bode Plot — gain margin, phase margin",
            "PID Controller — effect of P, I, D",
            "Nyquist criterion — stability from plot",
        ],
    },
    {
        "label": "💻 Digital Electronics & Microprocessor",
        "topics": [
            "Number system — Binary, Octal, Hex, BCD conversion",
            "1's complement ও 2's complement arithmetic",
            "Boolean algebra — theorems ও postulates",
            "K-Map — 2/3/4 variable simplification (SOP & POS)",
            "Logic gates — universal gates (NAND, NOR) implementation",
            "Combinational circuits — half/full adder, subtractor",
            "Multiplexer ও Demultiplexer",
            "Encoder, Decoder, Priority encoder",
            "Flip-Flop — SR, JK, D, T — truth table ও timing",
            "Master-Slave JK FF — race condition",
            "Counter — synchronous ও asynchronous, MOD-N",
            "Shift Register — SISO, SIPO, PISO, PIPO",
            "ADC — successive approximation, flash type",
            "DAC — R-2R ladder, weighted resistor",
            "8085 architecture — registers, flags, buses",
            "8085 instruction set — data transfer, arithmetic, branch",
            "Interrupts — types, priority, ISR",
            "Memory interfacing — address decoding",
        ],
    },
    {
        "label": "📶 Electromagnetics & Communication",
        "topics": [
            "Coulomb's Law — force between charges",
            "Electric field E, potential V — relation ও numerical",
            "Gauss's Law — application to sphere, cylinder, plane",
            "Capacitance — parallel plate, spherical, coaxial",
            "Biot-Savart Law — magnetic field calculation",
            "Ampere's Law — H field for infinite wire, solenoid",
            "Faraday's Law — induced EMF, Lenz's law",
            "Maxwell's equations — integral ও differential form",
            "EM wave — velocity, wavelength, intrinsic impedance",
            "Poynting vector — power density",
            "Transmission line — characteristic impedance Z₀",
            "Transmission line — reflection coefficient, VSWR",
            "Smith chart — basics",
            "Antenna — gain, directivity, radiation pattern",
            "AM modulation — index, bandwidth, power",
            "FM modulation — deviation, Carson's rule",
            "SNR, noise figure, sensitivity",
            "Sampling theorem — Nyquist rate, aliasing",
        ],
    },
    {
        "label": "🔄 DSP, Power Electronics & Revision",
        "topics": [
            "Z-Transform — definition, ROC, properties",
            "Inverse Z-Transform — partial fraction",
            "DFT — N-point, properties",
            "FFT — radix-2 butterfly diagram",
            "FIR filter — window method design",
            "IIR filter — Butterworth design",
            "Power Electronics — SCR (thyristor) operation",
            "Half-wave ও full-wave controlled rectifier",
            "DC chopper — step up/down, duty cycle",
            "Inverter — single phase bridge, PWM",
            "AC voltage controller — firing angle",
            "Previous BPSC/BREB exam MCQ practice",
            "Formula sheet revision — সব বিষয়",
        ],
    },
]

# ════════════════════════════════════════════════════════
# NON-DEPT TOPICS  —  প্রতিদিন সব সাবজেক্ট থেকে ১টা করে
# ════════════════════════════════════════════════════════
NON_DEPT = {
    "বাংলা ভাষা ও সাহিত্য": [
        "সন্ধি — স্বর, ব্যঞ্জন, বিসর্গ সন্ধি (উদাহরণ সহ)",
        "সমাস — ৬ প্রকার, উদাহরণ ও ব্যাসবাক্য",
        "কারক ও বিভক্তি — ৬ কারক, চিহ্নিতকরণ",
        "বাংলা সাহিত্যের যুগ — প্রাচীন/মধ্য/আধুনিক",
        "রবীন্দ্রনাথ ঠাকুর — জীবন, রচনা, পুরস্কার",
        "কাজী নজরুল ইসলাম — জীবন ও সাহিত্যকর্ম",
        "বানান শুদ্ধি — সাধারণ ভুল বানান",
        "বাগধারা ও প্রবাদ — অর্থ ও প্রয়োগ",
        "উপসর্গ ও প্রত্যয় — বাংলা ও তৎসম",
        "ছন্দ — মাত্রাবৃত্ত, অক্ষরবৃত্ত, স্বরবৃত্ত",
        "বিপরীত শব্দ ও প্রতিশব্দ",
        "বাক্য শুদ্ধি — গঠনগত ভুল সংশোধন",
    ],
    "English Language & Literature": [
        "Tense — 12 tenses with structure & examples",
        "Voice — Active to Passive (all tenses)",
        "Narration — Direct to Indirect speech rules",
        "Preposition — common usage & tricky ones",
        "Articles — a/an/the rules & exceptions",
        "Synonym & Antonym — high-frequency words",
        "Idioms & Phrases — common expressions",
        "Sentence correction — subject-verb agreement",
        "Vocabulary — one word substitution",
        "Shakespeare — plays, characters, famous quotes",
        "English Literature periods — overview",
        "Comprehension passage — reading strategy",
    ],
    "বাংলাদেশ বিষয়াবলি": [
        "মুক্তিযুদ্ধ — পটভূমি, ৭ই মার্চ, ১৬ই ডিসেম্বর",
        "সংবিধান — মূলনীতি, সংশোধনী, অনুচ্ছেদ",
        "বাংলাদেশের ভূগোল — নদ-নদী, সীমানা, বিভাগ",
        "বাংলাদেশের অর্থনীতি — GDP, রপ্তানি, রেমিট্যান্স",
        "জাতীয় বিষয় — জাতীয় প্রতীক, দিবস, পুরস্কার",
        "বাংলাদেশের ইতিহাস — ব্রিটিশ আমল থেকে স্বাধীনতা",
        "বর্তমান সরকার ব্যবস্থা — সংসদ, মন্ত্রণালয়",
        "বিখ্যাত ব্যক্তিত্ব — বিজ্ঞানী, সাহিত্যিক, রাজনীতিবিদ",
    ],
    "আন্তর্জাতিক বিষয়াবলি": [
        "জাতিসংঘ — গঠন, অঙ্গসংস্থা, সদর দপ্তর",
        "আন্তর্জাতিক সংগঠন — IMF, WB, WTO, WHO",
        "বিশ্বের দেশ — রাজধানী, মুদ্রা, ভাষা",
        "সাম্প্রতিক আন্তর্জাতিক ঘটনা ও চুক্তি",
        "আঞ্চলিক সংগঠন — SAARC, ASEAN, EU, AU",
        "বিশ্বযুদ্ধ — কারণ, ফলাফল, গুরুত্বপূর্ণ তথ্য",
        "নোবেল পুরস্কার — ইতিহাস ও বিখ্যাত বিজয়ী",
        "পরিবেশ চুক্তি — কিয়োটো, প্যারিস, COP",
    ],
    "সাধারণ বিজ্ঞান": [
        "পদার্থবিজ্ঞান — গতিসূত্র, কাজ-শক্তি-ক্ষমতা",
        "তাপগতিবিদ্যা — তাপমাত্রা, তাপ পরিবহন",
        "আলোর প্রতিফলন ও প্রতিসরণ — লেন্স, দর্পণ",
        "শব্দ — তরঙ্গ, কম্পাঙ্ক, অতিশব্দ",
        "রসায়ন — পর্যায় সারণি, যোজনী, মৌল",
        "অ্যাসিড-ক্ষার — pH, নিরপেক্ষকরণ",
        "জীববিজ্ঞান — কোষ, DNA, বংশগতি",
        "মানবদেহ — অঙ্গতন্ত্র, রোগ-প্রতিরোধ",
        "পুষ্টি — ভিটামিন, খনিজ, অভাবজনিত রোগ",
        "দৈনন্দিন বিজ্ঞান — সাবান, গ্লাস, সিমেন্ট",
    ],
    "কম্পিউটার ও তথ্যপ্রযুক্তি": [
        "কম্পিউটার প্রজন্ম ও শ্রেণিবিভাগ",
        "হার্ডওয়্যার — CPU, RAM, ROM, Storage",
        "অপারেটিং সিস্টেম — কাজ, প্রকার",
        "নেটওয়ার্ক — LAN/WAN, OSI 7 layer, TCP/IP",
        "ইন্টারনেট — প্রোটোকল, IP, DNS, HTTP",
        "Database — DBMS, SQL commands",
        "সাইবার নিরাপত্তা — ভাইরাস, ফায়ারওয়াল, এনক্রিপশন",
        "ই-গভর্ন্যান্স ও ডিজিটাল বাংলাদেশ",
        "প্রোগ্রামিং ধারণা — algorithm, flowchart",
        "MS Office — Word, Excel, PowerPoint shortcuts",
    ],
    "গাণিতিক যুক্তি": [
        "সংখ্যাতত্ত্ব — ল.সা.গু, গ.সা.গু, ভাজ্যতা নিয়ম",
        "শতকরা — লাভ-ক্ষতি, ছাড়, সুদ",
        "অনুপাত ও সমানুপাত",
        "বীজগণিত — সমীকরণ, উৎপাদক বিশ্লেষণ",
        "সূচক ও লগারিদম",
        "ত্রিকোণমিতি — অনুপাত, সূত্র, মান",
        "জ্যামিতি — ত্রিভুজ, বৃত্ত, চতুর্ভুজ",
        "পরিমিতি — ক্ষেত্রফল, আয়তন",
        "সম্ভাবনা — basic probability",
        "পরিসংখ্যান — গড়, মধ্যক, প্রচুরক, পরিসর",
        "বয়স, কাজ, সময়-দূরত্ব সমস্যা",
        "সেট তত্ত্ব — union, intersection, Venn diagram",
    ],
}

NON_DEPT_SUBJECTS = list(NON_DEPT.keys())


# ════════════════════════════════════════════════════════
# STATE
# ════════════════════════════════════════════════════════
def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    eee_order = list(range(7))
    random.shuffle(eee_order)
    # per subject: shuffled topic indices
    non_queues = {subj: list(range(len(NON_DEPT[subj]))) for subj in NON_DEPT_SUBJECTS}
    for subj in non_queues:
        random.shuffle(non_queues[subj])
    return {"day_index": 0, "week": 1, "eee_order": eee_order, "non_queues": non_queues, "non_pointers": {s: 0 for s in NON_DEPT_SUBJECTS}}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def next_non_topic(state, subj):
    queue   = state["non_queues"][subj]
    pointer = state["non_pointers"][subj]
    if pointer >= len(queue):
        random.shuffle(queue)
        pointer = 0
    topic = NON_DEPT[subj][queue[pointer]]
    state["non_pointers"][subj] = pointer + 1
    state["non_queues"][subj]   = queue
    return topic

def advance_state(state):
    state["day_index"] += 1
    if state["day_index"] >= 7:
        state["day_index"] = 0
        state["week"]     += 1
        eee_order = list(range(7))
        random.shuffle(eee_order)
        state["eee_order"] = eee_order
    save_state(state)


# ════════════════════════════════════════════════════════
# MESSAGE BUILDER
# ════════════════════════════════════════════════════════
def build_message(state):
    now      = datetime.now(BD_TZ)
    days     = ["সোমবার","মঙ্গলবার","বুধবার","বৃহস্পতিবার","শুক্রবার","শনিবার","রবিবার"]
    day_name = days[now.weekday()]
    date_str = now.strftime("%d/%m/%Y")
    week     = state["week"]

    eee = EEE_DAYS[state["eee_order"][state["day_index"]]]

    lines = [
        f"📅 <b>{day_name}  |  {date_str}  |  Week {week}</b>",
        "━━━━━━━━━━━━━━━━━━━━━━━",
        "",
        f"<b>{eee['label']}</b>",
        "",
    ]
    for i, t in enumerate(eee["topics"], 1):
        lines.append(f"  <code>{i:02d}.</code> {t}")

    lines += [
        "",
        "━━━━━━━━━━━━━━━━━━━━━━━",
        "📚 <b>Non-Department Topics</b>",
        "",
    ]

    subject_emojis = {
        "বাংলা ভাষা ও সাহিত্য":         "🔵",
        "English Language & Literature":  "🟢",
        "বাংলাদেশ বিষয়াবলি":             "🟡",
        "আন্তর্জাতিক বিষয়াবলি":          "🟠",
        "সাধারণ বিজ্ঞান":                 "🔴",
        "কম্পিউটার ও তথ্যপ্রযুক্তি":     "🟣",
        "গাণিতিক যুক্তি":                 "⚪",
    }

    for subj in NON_DEPT_SUBJECTS:
        emoji = subject_emojis.get(subj, "▪️")
        topic = next_non_topic(state, subj)
        lines.append(f"{emoji} <b>{subj}</b>")
        lines.append(f"    ➤ {topic}")
        lines.append("")

    lines += [
        "━━━━━━━━━━━━━━━━━━━━━━━",
        "💪 <b>আজকের লক্ষ্য: ৮+ ঘন্টা পড়া!</b>",
        "🔁 <i>টপিক প্রতি সপ্তাহে র‍্যান্ডম shuffle হয়</i>",
    ]

    return "\n".join(lines)


# ════════════════════════════════════════════════════════
# TELEGRAM
# ════════════════════════════════════════════════════════
async def send_message(text: str) -> int:
    async with httpx.AsyncClient() as client:
        r = await client.post(f"{BASE_URL}/sendMessage", json={
            "chat_id":    CHAT_ID,
            "text":       text,
            "parse_mode": "HTML",
        })
        r.raise_for_status()
        return r.json()["result"]["message_id"]

async def pin_message(message_id: int):
    async with httpx.AsyncClient() as client:
        r = await client.post(f"{BASE_URL}/pinChatMessage", json={
            "chat_id":              CHAT_ID,
            "message_id":           message_id,
            "disable_notification": True,
        })
        r.raise_for_status()

async def main():
    state   = load_state()
    message = build_message(state)
    msg_id  = await send_message(message)
    await pin_message(msg_id)
    advance_state(state)
    print(f"✅ Done — week={state['week']} next_day_index={state['day_index']}")

if __name__ == "__main__":
    asyncio.run(main())
