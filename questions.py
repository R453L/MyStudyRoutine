# questions.py — Rony Parvej EEE Job Solution অনুযায়ী

EEE_QUESTIONS = {

# ══════════════════════════════════════════════════════════
# DAY 1 — DC Circuit
# ══════════════════════════════════════════════════════════
"Part-1: DC Circuit": [

  {"topic": "Series & Parallel Circuit",
   "mcq": [
     {"q":"10Ω ও 40Ω parallel এর equivalent resistance কত?","options":["8Ω","50Ω","25Ω","4Ω"],"answer":0,"explanation":"R_eq = (10×40)/(10+40) = 400/50 = 8Ω"},
     {"q":"Series circuit এ সবচেয়ে বেশি voltage drop কোথায়?","options":["সবচেয়ে ছোট R এ","সবচেয়ে বড় R এ","সব R এ সমান","কোনোটাই না"],"answer":1,"explanation":"V=IR, series এ I সমান, তাই বড় R এ বেশি voltage"},
     {"q":"Parallel circuit এ সবচেয়ে বেশি current কোন শাখায়?","options":["সবচেয়ে বড় R এ","সবচেয়ে ছোট R এ","সব শাখায় সমান","মাঝামাঝি R এ"],"answer":1,"explanation":"I=V/R, parallel এ V সমান, ছোট R এ বেশি current"},
     {"q":"3টি সমান R রেজিস্টর parallel এ সংযুক্ত। equivalent resistance কত?","options":["3R","R/3","R","R²"],"answer":1,"explanation":"n সমান R parallel: R_eq = R/n = R/3"},
     {"q":"Current divider rule এ I1 = ?","options":["I×R1/(R1+R2)","I×R2/(R1+R2)","I×(R1+R2)/R2","I/R1"],"answer":1,"explanation":"Current divider: I1 = I×R2/(R1+R2) — বিপরীত R দিয়ে ভাগ"},
   ],
   "math":{"q":"R1=6Ω, R2=12Ω parallel, এই combination টি R3=4Ω এর সাথে series এ। Total voltage V=20V। প্রতিটি রেজিস্টরে current ও voltage বের করো।",
           "solution":"R12 = (6×12)/(6+12) = 72/18 = 4Ω\nR_total = R12 + R3 = 4 + 4 = 8Ω\nI_total = V/R_total = 20/8 = 2.5A\nV_R3 = 2.5×4 = 10V\nV_R12 = 20 - 10 = 10V\nI_R1 = 10/6 = 1.67A\nI_R2 = 10/12 = 0.83A\nCheck: 1.67+0.83 = 2.5A ✓"}},

  {"topic": "Delta-Star & Star-Delta Conversion",
   "mcq": [
     {"q":"সমান তিনটি Delta resistance R থেকে Star resistance হবে?","options":["3R","R","R/3","R²/3"],"answer":2,"explanation":"R_star = R_delta/3 (symmetric)"},
     {"q":"Star-Delta conversion এ R_ab (delta) = ?","options":["Ra+Rb","(Ra×Rb+Rb×Rc+Rc×Ra)/Rc","Ra×Rb/Rc","Ra+Rb+Rc"],"answer":1,"explanation":"R_ab = (Ra×Rb + Rb×Rc + Rc×Ra)/Rc"},
     {"q":"3টি সমান Star resistance 9Ω। equivalent Delta resistance কত?","options":["3Ω","9Ω","27Ω","81Ω"],"answer":2,"explanation":"R_delta = 3×R_star = 3×9 = 27Ω"},
     {"q":"Wheatstone bridge এর balance condition কী?","options":["P+Q=R+S","P×S=Q×R","P/Q=R/S","P-Q=R-S"],"answer":2,"explanation":"Balance: P/Q = R/S, তাই PS = QR"},
     {"q":"Balanced Wheatstone bridge এ galvanometer current কত?","options":["Maximum","Minimum","Zero","Infinite"],"answer":2,"explanation":"Balanced bridge: V_BD=0, তাই Ig=0"},
   ],
   "math":{"q":"Delta: R_ab=30Ω, R_bc=60Ω, R_ca=90Ω। Equivalent Star resistance Ra, Rb, Rc বের করো।",
           "solution":"Sum = R_ab+R_bc+R_ca = 30+60+90 = 180Ω\nRa = R_ab×R_ca/Sum = 30×90/180 = 15Ω\nRb = R_ab×R_bc/Sum = 30×60/180 = 10Ω\nRc = R_bc×R_ca/Sum = 60×90/180 = 30Ω"}},

  {"topic": "Source Transformation",
   "mcq": [
     {"q":"Voltage source V ও series resistance R কে Norton equivalent এ রূপান্তর করলে Norton current In = ?","options":["V×R","V/R","R/V","V+R"],"answer":1,"explanation":"In = V/R (short circuit current)"},
     {"q":"Current source I ও parallel resistance R কে Thevenin equivalent এ রূপান্তর করলে Vth = ?","options":["I/R","I+R","I×R","R/I"],"answer":2,"explanation":"Vth = I×R (open circuit voltage)"},
     {"q":"Source transformation এ resistance এর মান কেমন থাকে?","options":["পরিবর্তন হয়","একই থাকে","দ্বিগুণ হয়","অর্ধেক হয়"],"answer":1,"explanation":"Source transformation এ R এর মান অপরিবর্তিত থাকে"},
     {"q":"Ideal voltage source এর internal resistance কত?","options":["∞","0","R","1Ω"],"answer":1,"explanation":"Ideal voltage source: r = 0Ω"},
     {"q":"Ideal current source এর internal resistance কত?","options":["0","1Ω","R","∞"],"answer":3,"explanation":"Ideal current source: r = ∞"},
   ],
   "math":{"q":"12V voltage source ও 4Ω series resistance কে Norton equivalent এ রূপান্তর করো। তারপর 6Ω load এ current বের করো।",
           "solution":"Norton: In = 12/4 = 3A, Rn = 4Ω\nLoad current (current divider):\nIL = In × Rn/(Rn+RL) = 3 × 4/(4+6) = 1.2A\nVerify (Thevenin): Vth=12V, Rth=4Ω\nIL = 12/(4+6) = 1.2A ✓"}},

  {"topic": "KCL & KVL — branch current method",
   "mcq": [
     {"q":"KVL অনুযায়ী একটি closed loop এ voltage এর algebraic sum কত?","options":["∞","0","Max V","Min V"],"answer":1,"explanation":"KVL: ΣV = 0 (energy conservation)"},
     {"q":"KCL অনুযায়ী node এ ΣI = ?","options":["∞","Maximum","0","Minimum"],"answer":2,"explanation":"KCL: Σ(in) = Σ(out), তাই net ΣI = 0"},
     {"q":"3টি node এর circuit এ independent KCL equation কতটি?","options":["3","1","2","4"],"answer":2,"explanation":"Independent KCL = nodes - 1 = 3-1 = 2"},
     {"q":"Mesh analysis এ supermesh তৈরি হয় কখন?","options":["Voltage source দুই mesh এ","Current source দুই mesh এ","Resistor দুই mesh এ","কোনো source নেই"],"answer":1,"explanation":"Current source দুই mesh এর shared branch এ থাকলে supermesh"},
     {"q":"10Ω এ 5A current। voltage drop কত?","options":["2V","15V","50V","0.5V"],"answer":2,"explanation":"V = IR = 5×10 = 50V"},
   ],
   "math":{"q":"Loop 1: 10V source, R1=2Ω, R3=4Ω (shared)। Loop 2: 5V source, R2=3Ω, R3=4Ω (shared)। Mesh analysis দিয়ে I1, I2 ও R3 এর current বের করো।",
           "solution":"Mesh 1: 2I1 + 4(I1-I2) = 10 → 6I1 - 4I2 = 10 ...(1)\nMesh 2: 3I2 + 4(I2-I1) = 5 → -4I1 + 7I2 = 5 ...(2)\n(1)×7: 42I1 - 28I2 = 70\n(2)×4: -16I1 + 28I2 = 20\nযোগ: 26I1 = 90 → I1 = 3.46A\n(1): I2 = (6×3.46-10)/4 = 2.69A\nI_R3 = I1-I2 = 0.77A"}},

  {"topic": "Thevenin's Theorem",
   "mcq": [
     {"q":"Vth কীভাবে পাওয়া যায়?","options":["Load short করে","Load open করে","Source বন্ধ করে","Load সরিয়ে short"],"answer":1,"explanation":"Vth = open circuit voltage at terminals"},
     {"q":"Rth বের করতে independent source কীভাবে বন্ধ করতে হয়?","options":["V→open, I→short","V→short, I→open","উভয়ই short","উভয়ই open"],"answer":1,"explanation":"V source→short circuit, I source→open circuit"},
     {"q":"Maximum power transfer এ RL = ?","options":["0","∞","Rth","2Rth"],"answer":2,"explanation":"MPT: RL = Rth"},
     {"q":"Pmax = ? (Thevenin circuit এ)","options":["Vth²/Rth","Vth²/2Rth","Vth²/4Rth","Vth/4Rth"],"answer":2,"explanation":"Pmax = Vth²/(4Rth) যখন RL=Rth"},
     {"q":"Thevenin equivalent এ কী থাকে?","options":["I source + parallel R","V source + series R","I source + series R","V source + parallel R"],"answer":1,"explanation":"Thevenin = Vth (series) + Rth"},
   ],
   "math":{"q":"Circuit: 30V source, R1=6Ω (series), R2=3Ω (parallel with load terminals)। Thevenin equivalent বের করো ও RL=3Ω তে current নির্ণয় করো।",
           "solution":"Vth (RL open): voltage divider\nVth = 30×3/(6+3) = 10V\nRth (source short): R1||R2 = (6×3)/(6+3) = 2Ω\nLoad current: IL = Vth/(Rth+RL) = 10/(2+3) = 2A\nPL = IL²×RL = 4×3 = 12W"}},

  {"topic": "Superposition Theorem",
   "mcq": [
     {"q":"Superposition কোন ধরনের circuit এ প্রযোজ্য?","options":["Non-linear","Linear bilateral","Unilateral","যেকোনো"],"answer":1,"explanation":"Superposition শুধু linear bilateral circuit এ কাজ করে"},
     {"q":"Superposition এ dependent source কীভাবে ট্রিট করতে হয়?","options":["বন্ধ করতে হয়","সবসময় চালু রাখতে হয়","Open করতে হয়","Short করতে হয়"],"answer":1,"explanation":"Dependent source কখনো বন্ধ করা যায় না"},
     {"q":"Superposition দিয়ে সরাসরি power বের করা যায় না কারণ?","options":["P=V/I (linear)","P=I²R (nonlinear)","P=V²R (nonlinear)","Power সবসময় zero"],"answer":1,"explanation":"P=I²R — nonlinear, superposition প্রযোজ্য নয়"},
     {"q":"Superposition এ voltage source বন্ধ = ?","options":["Open circuit","Short circuit","Remove করা","Reverse করা"],"answer":1,"explanation":"V source বন্ধ = 0V source = short circuit"},
     {"q":"3টি independent source থাকলে superposition এ কতবার solve করতে হবে?","options":["1","2","3","6"],"answer":2,"explanation":"প্রতিটি source এর জন্য একবার = 3 বার"},
   ],
   "math":{"q":"V1=12V (R1=4Ω series) ও I1=2A (parallel)। R_load=6Ω তে voltage বের করো Superposition দিয়ে।",
           "solution":"Step 1 (V1 চালু, I1 open):\nR_total = 4+6 = 10Ω\nI = 12/10 = 1.2A\nVL1 = 1.2×6 = 7.2V\n\nStep 2 (I1 চালু, V1 short):\nR1||RL = (4×6)/(4+6) = 2.4Ω\nVL2 = I1×2.4 = 2×2.4 = 4.8V\n\nVL = VL1 + VL2 = 7.2 + 4.8 = 12V"}},

  {"topic": "Norton's Theorem",
   "mcq": [
     {"q":"Norton current In = ?","options":["Open circuit voltage/R","Short circuit current at terminals","Load current","Source current"],"answer":1,"explanation":"In = short circuit current at the terminals"},
     {"q":"Norton ও Thevenin এ resistance এর সম্পর্ক?","options":["Rn=2Rth","Rn=Rth/2","Rn=Rth","Rn=Rth²"],"answer":2,"explanation":"Rn = Rth (একই পদ্ধতিতে বের করা হয়)"},
     {"q":"Norton থেকে Thevenin: Vth = ?","options":["In/Rn","In-Rn","In×Rn","Rn/In"],"answer":2,"explanation":"Vth = In × Rn"},
     {"q":"Norton equivalent এ কী থাকে?","options":["V source + series R","I source + parallel R","V source + parallel R","I source + series R"],"answer":1,"explanation":"Norton = In (parallel) + Rn"},
     {"q":"20V, 5Ω series circuit এর Norton current কত?","options":["100A","4A","0.25A","20A"],"answer":1,"explanation":"In = V/R = 20/5 = 4A (short circuit)"},
   ],
   "math":{"q":"24V source, R1=8Ω (series), R2=4Ω (parallel with terminal)। Norton equivalent বের করো ও RL=4Ω তে power নির্ণয় করো।",
           "solution":"In (terminal short): R2 shorted\nIn = 24/8 = 3A\nRn = R1||R2 = (8×4)/(8+4) = 2.67Ω\nVerify: Vth = In×Rn = 3×2.67 = 8V\nWith RL=4Ω:\nIL = In×Rn/(Rn+RL) = 3×2.67/(2.67+4) = 1.2A\nPL = IL²×RL = 1.44×4 = 5.76W"}},

  {"topic": "Maximum Power Transfer",
   "mcq": [
     {"q":"Max power transfer হয় যখন?","options":["RL=0","RL=∞","RL=Rth","RL=2Rth"],"answer":2,"explanation":"MPT: RL = Rth"},
     {"q":"Max power transfer এ efficiency কত?","options":["25%","50%","75%","100%"],"answer":1,"explanation":"η = 50% (বাকি 50% Rth তে নষ্ট)"},
     {"q":"Vth=10V, Rth=5Ω। Maximum power কত?","options":["20W","10W","5W","2.5W"],"answer":2,"explanation":"Pmax = Vth²/4Rth = 100/20 = 5W"},
     {"q":"Communication system এ MPT কেন ব্যবহার হয়?","options":["Efficiency বেশি","Signal strength maximize করতে","Cost কমাতে","Voltage বাড়াতে"],"answer":1,"explanation":"Communication এ signal power maximize গুরুত্বপূর্ণ, efficiency নয়"},
     {"q":"Power system এ MPT preferred নয় কারণ?","options":["Voltage কম","50% efficiency খুব কম","Current বেশি","Frequency বদলায়"],"answer":1,"explanation":"Power transmission এ 50% loss অগ্রহণযোগ্য"},
   ],
   "math":{"q":"Vth=100V, Rth=25Ω। (a) Maximum power কত? (b) RL=25Ω এ power কত? (c) RL=100Ω এ power কত? তুলনা করো।",
           "solution":"(a) Pmax = Vth²/4Rth = 10000/100 = 100W (RL=25Ω)\n(b) RL=25Ω=Rth: IL=100/50=2A, P=4×25=100W ✓\n(c) RL=100Ω: IL=100/125=0.8A, P=0.64×100=64W\nতুলনা: RL≠Rth হলে power কমে যায়"}},
],

# ══════════════════════════════════════════════════════════
# DAY 2 — AC Circuit
# ══════════════════════════════════════════════════════════
"Part-1: AC Circuit": [

  {"topic": "Sinusoid & Phasors",
   "mcq": [
     {"q":"v(t)=Vm×sin(ωt+φ) এ ω = ?","options":["2πf","f/2π","1/f","f²"],"answer":0,"explanation":"ω = 2πf (angular frequency, rad/s)"},
     {"q":"RMS value = Peak value × ?","options":["√2","1/√2","2","π"],"answer":1,"explanation":"Vrms = Vm/√2 = 0.707Vm"},
     {"q":"Pure inductor এ V ও I এর phase relationship?","options":["In phase","V leads I by 90°","I leads V by 90°","180° apart"],"answer":1,"explanation":"ELI: Inductor এ V leads I by 90°"},
     {"q":"Pure capacitor এ V ও I এর phase relationship?","options":["In phase","V leads I by 90°","I leads V by 90°","180°"],"answer":2,"explanation":"ICE: Capacitor এ I leads V by 90°"},
     {"q":"Phasor এ j এর মান কত?","options":["1","−1","√(−1)","0"],"answer":2,"explanation":"j = √(−1) (imaginary unit)"},
   ],
   "math":{"q":"v(t) = 141.4sin(314t + 30°)V। Vrms, frequency, period ও phasor form বের করো।",
           "solution":"Vm = 141.4V\nVrms = 141.4/√2 = 100V\nω = 314 rad/s → f = 314/2π = 50Hz\nT = 1/f = 1/50 = 0.02s = 20ms\nPhasor: V = 100∠30° V"}},

  {"topic": "AC Power Analysis — Real, Reactive, Apparent Power",
   "mcq": [
     {"q":"Apparent power S এর unit?","options":["W","VAR","VA","kWh"],"answer":2,"explanation":"S = VA (Volt-Ampere)"},
     {"q":"Reactive power Q এর unit?","options":["W","VAR","VA","J"],"answer":1,"explanation":"Q = VAR (Volt-Ampere Reactive)"},
     {"q":"Power factor = ?","options":["P/Q","Q/S","P/S","S/P"],"answer":2,"explanation":"PF = P/S = cosφ"},
     {"q":"S² = ?","options":["P²+Q","P+Q²","P²+Q²","(P+Q)²"],"answer":2,"explanation":"S² = P² + Q² (power triangle)"},
     {"q":"Lagging power factor মানে?","options":["Capacitive load","Resistive load","Inductive load","No load"],"answer":2,"explanation":"Lagging PF = inductive load (voltage leads current)"},
   ],
   "math":{"q":"V=230V, I=10A, PF=0.866 lagging। P, Q, S ও φ বের করো। Power factor improve করতে কত VAR capacitor লাগবে যদি unity PF করতে হয়?",
           "solution":"S = VI = 230×10 = 2300VA\nPF = cosφ = 0.866 → φ = 30°\nP = S×cosφ = 2300×0.866 = 1992W\nQ = S×sinφ = 2300×0.5 = 1150VAR (inductive)\n\nUnity PF এর জন্য capacitor VAR = Q = 1150VAR\nC = Q/(V²×ω) = 1150/(230²×314) = 69.3μF"}},

  {"topic": "R-L-C Circuit — series, phasor diagram",
   "mcq": [
     {"q":"Series RLC এ resonance এ impedance কত?","options":["Maximum","Minimum=R","Zero","Infinite"],"answer":1,"explanation":"Resonance: XL=XC cancel, Z=R (minimum)"},
     {"q":"XL = ?","options":["1/ωL","ωL","ω/L","L/ω"],"answer":1,"explanation":"XL = ωL = 2πfL"},
     {"q":"XC = ?","options":["ωC","1/ωC","ω/C","C/ω"],"answer":1,"explanation":"XC = 1/ωC = 1/2πfC"},
     {"q":"Series RLC এ X = XL-XC > 0 হলে circuit কেমন?","options":["Capacitive","Resistive","Inductive","Resonant"],"answer":2,"explanation":"XL > XC → net inductive → lagging PF"},
     {"q":"Resonant frequency f0 = ?","options":["2π√(LC)","1/(2π√LC)","√(LC)/2π","πf/√LC"],"answer":1,"explanation":"f0 = 1/(2π√LC)"},
   ],
   "math":{"q":"Series RLC: R=10Ω, L=0.1H, C=100μF, f=50Hz, V=200V। Z, I, VR, VL, VC, PF ও P বের করো।",
           "solution":"XL = 2π×50×0.1 = 31.42Ω\nXC = 1/(2π×50×100×10⁻⁶) = 31.83Ω\nX = XL-XC = -0.41Ω (slightly capacitive)\nZ = √(10²+0.41²) ≈ 10.008Ω\nI = 200/10.008 = 19.98A ≈ 20A\nVR = 20×10 = 200V\nVL = 20×31.42 = 628.4V\nVC = 20×31.83 = 636.6V\nPF = R/Z = 10/10.008 ≈ 1.0 (near resonance)\nP = I²R = 400×10 = 4000W"}},

  {"topic": "Resonance — Q-factor, Bandwidth",
   "mcq": [
     {"q":"Q-factor = ?","options":["R/XL","XL/R","R×XL","XL-R"],"answer":1,"explanation":"Q = XL/R = ω0L/R at resonance"},
     {"q":"Bandwidth BW = ?","options":["Q×f0","f0/Q","f0×Q²","Q/f0"],"answer":1,"explanation":"BW = f0/Q"},
     {"q":"High Q-factor মানে?","options":["Wide bandwidth","Narrow bandwidth","No resonance","Flat response"],"answer":1,"explanation":"High Q → narrow BW → sharp resonance"},
     {"q":"Parallel resonance এ impedance কেমন?","options":["Minimum","Maximum","Zero","R"],"answer":1,"explanation":"Parallel resonance: Z maximum"},
     {"q":"Q-factor এর unit কী?","options":["Ohm","Dimensionless","Hz","Watt"],"answer":1,"explanation":"Q-factor dimensionless (ratio)"},
   ],
   "math":{"q":"Series RLC: R=5Ω, L=50mH, C=5μF। f0, Q-factor, BW, lower ও upper cutoff frequency বের করো।",
           "solution":"f0 = 1/(2π√LC) = 1/(2π√(0.05×5×10⁻⁶))\n= 1/(2π×5×10⁻⁴) = 318.3Hz\nXL at f0 = 2π×318.3×0.05 = 100Ω\nQ = XL/R = 100/5 = 20\nBW = f0/Q = 318.3/20 = 15.9Hz\nf1 = f0-BW/2 = 310.4Hz\nf2 = f0+BW/2 = 326.2Hz"}},

  {"topic": "3-Phase Analysis",
   "mcq": [
     {"q":"Balanced 3-phase system এ line voltage ও phase voltage (star) এর সম্পর্ক?","options":["VL=Vφ","VL=√3×Vφ","VL=3Vφ","VL=Vφ/√3"],"answer":1,"explanation":"Star: VL = √3×Vφ"},
     {"q":"Delta connection এ line current ও phase current এর সম্পর্ক?","options":["IL=Iφ","IL=√3×Iφ","IL=3×Iφ","IL=Iφ/√3"],"answer":1,"explanation":"Delta: IL = √3×Iφ"},
     {"q":"3-phase power P = ?","options":["VL×IL×cosφ","√3×VL×IL×cosφ","3×VL×IL×cosφ","VL²/R"],"answer":1,"explanation":"P = √3×VL×IL×cosφ"},
     {"q":"3-phase 4-wire system এ neutral wire এ balanced load এ current কত?","options":["Maximum","Full load current","Zero","Iφ/3"],"answer":2,"explanation":"Balanced load: IN=0 (3 phasors cancel)"},
     {"q":"Two wattmeter method এ total power P = ?","options":["W1+W2","W1-W2","W1×W2","(W1+W2)/2"],"answer":0,"explanation":"P = W1 + W2"},
   ],
   "math":{"q":"3-phase star connected load: R=10Ω per phase, VL=400V, f=50Hz। Phase voltage, line current, total power ও power factor বের করো।",
           "solution":"Vφ = VL/√3 = 400/1.732 = 231V\nIL = Iφ = Vφ/R = 231/10 = 23.1A\nP = √3×VL×IL×cosφ = 1.732×400×23.1×1\n= 16000W = 16kW\n(Pure resistive: PF = 1)\nVerify: P = 3×Iφ²×R = 3×534×10 = 16kW ✓"}},

  {"topic": "Transient Analysis — RC, RL",
   "mcq": [
     {"q":"RC circuit এ time constant τ = ?","options":["R/C","RC","R+C","C/R"],"answer":1,"explanation":"τ = RC (seconds)"},
     {"q":"RL circuit এ time constant τ = ?","options":["RL","R/L","L/R","R+L"],"answer":2,"explanation":"τ = L/R (seconds)"},
     {"q":"5τ সময় পরে capacitor কতটুকু charge হয়?","options":["50%","63.2%","86.5%","99.3%"],"answer":3,"explanation":"5τ তে ≈99.3% charge (fully charged ধরা হয়)"},
     {"q":"RC circuit এ 1τ সময়ে voltage কতটুকু পৌঁছায়?","options":["50%","63.2%","86.5%","100%"],"answer":1,"explanation":"1τ: V = V0(1-e⁻¹) = 63.2% of final value"},
     {"q":"Inductor এ initial current 0 হলে switching এ VC(0+) = ?","options":["∞","0","V_source","V_source/2"],"answer":2,"explanation":"Inductor: current continuity, V can jump. Capacitor: voltage continuity"}  ,
   ],
   "math":{"q":"RC circuit: R=10kΩ, C=100μF, V=50V (DC step)। (a) τ কত? (b) t=τ তে VC কত? (c) t=3τ তে VC কত? (d) পুরো চার্জ হতে কত সময়?",
           "solution":"τ = RC = 10×10³×100×10⁻⁶ = 1s\n(a) τ = 1s\n(b) t=τ: VC = 50(1-e⁻¹) = 50×0.632 = 31.6V\n(c) t=3τ: VC = 50(1-e⁻³) = 50×0.950 = 47.5V\n(d) 5τ = 5s তে practically fully charged (99.3%)"}},
],

# ══════════════════════════════════════════════════════════
# DAY 3 — Power System
# ══════════════════════════════════════════════════════════
"Part-2: Power System": [

  {"topic": "Power Factor Improvement",
   "mcq": [
     {"q":"Power factor improve করতে কী ব্যবহার হয়?","options":["Inductor","Resistor","Capacitor","Transformer"],"answer":2,"explanation":"Inductive load এর lagging PF ঠিক করতে capacitor ব্যবহার হয়"},
     {"q":"Power factor improvement এ real power (kW) কী হয়?","options":["বাড়ে","কমে","অপরিবর্তিত","দ্বিগুণ"],"answer":2,"explanation":"PF improvement: P অপরিবর্তিত, Q কমে, S কমে"},
     {"q":"Synchronous condenser কী?","options":["DC motor","Unloaded synchronous motor for PF correction","Capacitor bank","Transformer"],"answer":1,"explanation":"Synchronous condenser = no-load synchronous motor, PF correction এ ব্যবহার"},
     {"q":"PF improvement এ কারেন্ট কমলে কী সুবিধা?","options":["Voltage বাড়ে","I²R loss কমে","Frequency বাড়ে","Power বাড়ে"],"answer":1,"explanation":"কম current → কম I²R copper loss → efficiency বাড়ে"},
     {"q":"Unity power factor এ Q = ?","options":["Maximum","S","P","Zero"],"answer":3,"explanation":"Unity PF: φ=0°, Q = S×sin0° = 0"},
   ],
   "math":{"q":"একটি factory: P=500kW, PF=0.7 lagging, V=11kV। (a) কত kVA demand? (b) PF=0.95 করতে কত kVAR capacitor লাগবে?",
           "solution":"(a) S = P/PF = 500/0.7 = 714.3 kVA\nQ1 = S×sinφ1 = 714.3×sin(45.57°) = 510.2 kVAR\n\n(b) New: φ2 = cos⁻¹(0.95) = 18.19°\nQ2 = P×tanφ2 = 500×tan(18.19°) = 164.2 kVAR\nQC = Q1-Q2 = 510.2-164.2 = 346 kVAR capacitor"}},

  {"topic": "Transmission Line",
   "mcq": [
     {"q":"Short transmission line (< 80km) এ কোনটি neglect করা হয়?","options":["Resistance","Inductance","Capacitance","উভয় L ও C"],"answer":2,"explanation":"Short line: shunt capacitance neglected"},
     {"q":"Transmission line এর characteristic impedance Z0 = ?","options":["√(Z/Y)","Z×Y","Z+Y","Z/Y"],"answer":0,"explanation":"Z0 = √(Z/Y) where Z=series impedance, Y=shunt admittance"},
     {"q":"Transmission line এ Ferranti effect কী?","options":["No load এ receiving end voltage > sending end","Load বাড়লে voltage বাড়ে","Short circuit এ voltage বাড়ে","Current বাড়লে voltage বাড়ে"],"answer":0,"explanation":"Ferranti effect: no-load/light load এ VR > VS (capacitive effect)"},
     {"q":"ABCD parameter এ A এর মান?","options":["VS/VR (IR=0)","IS/VR","VS/IS","IR/VR"],"answer":0,"explanation":"A = VS/VR when IR=0 (open circuit at receiving end)"},
     {"q":"Surge impedance loading (SIL) এ power factor কত?","options":["0","0.8","1.0","0.5"],"answer":2,"explanation":"SIL: load = Z0, PF = unity"},
   ],
   "math":{"q":"Short transmission line: VS=11kV, R=10Ω, XL=20Ω, load=1000kW, PF=0.8 lag। Receiving end voltage VR ও voltage regulation বের করো।",
           "solution":"IL = P/(√3×VR×PF) — iteration needed\nAssume VR ≈ 10kV initially\nIL = 1000×10³/(√3×10000×0.8) = 72.17A\ncosφ=0.8, sinφ=0.6\nVS = VR + IL(Rcosφ + XLsinφ) (approx single phase)\nVS_ph = 10000/√3 + 72.17(10×0.8 + 20×0.6)\n= 5774 + 72.17×(8+12) = 5774 + 1443 = 7217V\nVS_line = 7217×√3 = 12.5kV\nVR% = (VS-VR)/VR × 100 = (12.5-10)/10 × 100 = 25%"}},

  {"topic": "Per Unit System",
   "mcq": [
     {"q":"Per unit value = ?","options":["Actual/Base","Base/Actual","Actual×Base","Actual-Base"],"answer":0,"explanation":"pu = Actual value / Base value"},
     {"q":"Per unit system এর সুবিধা কী?","options":["জটিল calculation","Transformer ratio eliminate হয়","Voltage বাড়ে","Current কমে"],"answer":1,"explanation":"pu system এ transformer turns ratio automatically handled"},
     {"q":"Base impedance Zbase = ?","options":["Vbase/Ibase","Vbase²/Sbase","Sbase/Vbase²","Vbase×Ibase"],"answer":1,"explanation":"Zbase = Vbase²/Sbase (3-phase)"},
     {"q":"1 pu impedance মানে?","options":["1Ω","Base impedance এর সমান","0Ω","∞"],"answer":1,"explanation":"1 pu = base value এর সমান"},
     {"q":"New base তে pu impedance: Zpu_new = Zpu_old × ?","options":["(Sbase_new/Sbase_old)×(Vbase_old/Vbase_new)²","(Sbase_old/Sbase_new)","(Vbase_new/Vbase_old)²","1"],"answer":0,"explanation":"Zpu_new = Zpu_old×(Sbase_new/Sbase_old)×(Vbase_old²/Vbase_new²)"},
   ],
   "math":{"q":"100MVA, 11kV generator, Zg=0.1pu। System base: 200MVA, 11kV। Generator এর pu impedance new base এ বের করো।",
           "solution":"Zpu_new = Zpu_old × (Sbase_new/Sbase_old) × (Vbase_old/Vbase_new)²\n= 0.1 × (200/100) × (11/11)²\n= 0.1 × 2 × 1\n= 0.2 pu\n\nBase impedance (new) = Vbase²/Sbase = 11²×10⁶/200×10⁶ = 0.605Ω\nActual Z = 0.2×0.605 = 0.121Ω"}},

  {"topic": "Symmetrical Fault",
   "mcq": [
     {"q":"3-phase symmetrical fault সবচেয়ে serious কারণ?","options":["Voltage কম","সর্বোচ্চ fault current","Frequency বাড়ে","Power কমে"],"answer":1,"explanation":"3-phase fault: সর্বোচ্চ fault current, সবচেয়ে বিপজ্জনক"},
     {"q":"Fault MVA = ?","options":["Vbase/Zf","Vbase²/Zf","Sbase/Zf(pu)","Sbase×Zf(pu)"],"answer":2,"explanation":"Fault MVA = Sbase/Zf(pu)"},
     {"q":"Subtransient reactance (Xd'') ব্যবহার হয় কখন?","options":["Steady state","First few cycles after fault","After 1 second","No load"],"answer":1,"explanation":"Xd'' = subtransient, fault এর প্রথম কয়েক cycle এ"},
     {"q":"Circuit breaker rating কোন current এর উপর ভিত্তি করে?","options":["Normal load current","Subtransient fault current","Steady state fault current","Starting current"],"answer":1,"explanation":"CB rated on maximum fault current = subtransient"},
     {"q":"Fault impedance Zf=0 মানে?","options":["High impedance fault","Bolted (solid) fault","Open circuit","Normal operation"],"answer":1,"explanation":"Zf=0: bolted fault (direct short circuit)"},
   ],
   "math":{"q":"Generator: 50MVA, 11kV, Xd''=0.15pu। 3-phase bolted fault at terminals। Fault current (A) ও Fault MVA বের করো।",
           "solution":"Fault MVA = Sbase/Xd'' = 50/0.15 = 333.3 MVA\nBase current = Sbase/(√3×Vbase) = 50×10⁶/(√3×11000) = 2624A\nFault current = Base current/Xd'' = 2624/0.15 = 17493A ≈ 17.5kA\n\nVerify: Fault MVA = √3×VL×IF = √3×11×17.5 = 333.3 MVA ✓"}},
],

# ══════════════════════════════════════════════════════════
# DAY 4 — Electrical Machine
# ══════════════════════════════════════════════════════════
"Part-3: Electrical Machine": [

  {"topic": "Transformer — EMF, OC/SC test, efficiency",
   "mcq": [
     {"q":"Transformer EMF equation: E = ?","options":["4.44fNΦm","2.22fNΦm","fNΦm","8.88fNΦm"],"answer":0,"explanation":"E = 4.44fNΦm (RMS value)"},
     {"q":"OC test এ কোন loss পাওয়া যায়?","options":["Copper loss","Iron (core) loss","Dielectric loss","Stray loss"],"answer":1,"explanation":"OC test: rated voltage apply, iron loss = Woc"},
     {"q":"SC test এ কোন loss পাওয়া যায়?","options":["Iron loss","Copper loss","Both","None"],"answer":1,"explanation":"SC test: rated current pass করা, copper loss = Wsc"},
     {"q":"Max efficiency হয় যখন?","options":["Copper loss > Iron loss","Iron loss = Copper loss","No load","Full load সবসময়"],"answer":1,"explanation":"η_max: Pi = Pc (x²Pcfl)"},
     {"q":"All-day efficiency গুরুত্বপূর্ণ কোন transformer এ?","options":["Power transformer","Distribution transformer","Auto transformer","Welding transformer"],"answer":1,"explanation":"Distribution transformer 24hr energized → all-day efficiency important"},
   ],
   "math":{"q":"100kVA transformer: OC test: V=400V, I=2A, W=500W। SC test: V=20V, I=250A, W=2000W। Full load (PF=0.8) efficiency ও max efficiency load বের করো।",
           "solution":"Iron loss Pi = 500W\nFull load copper loss Pc = 2000W\nFL output = 100×0.8 = 80kW\nη_FL = 80000/(80000+500+2000) = 80000/82500 = 96.97%\n\nMax η load: x = √(Pi/Pc) = √(500/2000) = 0.5\nLoad at max η = 0.5×100 = 50kVA\nOutput = 50×0.8 = 40kW\nLoss = 500+500 = 1000W\nη_max = 40000/41000 = 97.56%"}},

  {"topic": "DC Motor — back EMF, torque, speed control",
   "mcq": [
     {"q":"DC motor এর back EMF Eb = ?","options":["V+IaRa","V-IaRa","IaRa","V×Ia"],"answer":1,"explanation":"Eb = V - IaRa (back EMF opposes applied voltage)"},
     {"q":"DC motor torque T ∝ ?","options":["φ/Ia","φ×Ia","Ia/φ","1/φIa"],"answer":1,"explanation":"T = kφIa"},
     {"q":"DC series motor no-load এ কী হয়?","options":["Speed কমে","Speed অতিরিক্ত বাড়ে (dangerous)","Speed স্থির","Motor বন্ধ"],"answer":1,"explanation":"Series motor: no load → speed runaway (dangerous)"},
     {"q":"DC shunt motor এ speed N ∝ ?","options":["φ","1/φ","Ia","V×φ"],"answer":1,"explanation":"N = (V-IaRa)/(kφ) ∝ 1/φ (shunt motor: φ ≈ const)"},
     {"q":"DC motor এ mechanical power Pm = ?","options":["V×Ia","Eb×Ia","Ia²Ra","V×I"],"answer":1,"explanation":"Pm = Eb×Ia (developed mechanical power)"},
   ],
   "math":{"q":"220V DC shunt motor: Ra=0.5Ω, Rf=110Ω, IL=21A, N=1000rpm। Back EMF, torque ও efficiency বের করো (friction loss নেই)।",
           "solution":"If = V/Rf = 220/110 = 2A\nIa = IL - If = 21-2 = 19A\nEb = V-IaRa = 220-19×0.5 = 220-9.5 = 210.5V\nPm = Eb×Ia = 210.5×19 = 3999.5W ≈ 4kW\nT = Pm/ω = 4000/(2π×1000/60) = 4000/104.7 = 38.2 N·m\nPin = V×IL = 220×21 = 4620W\nη = Pm/Pin = 4000/4620 = 86.6%"}},

  {"topic": "Induction Motor — slip, torque",
   "mcq": [
     {"q":"Synchronous speed Ns = ?","options":["120f/P","60f/P","240f/P","Pf/120"],"answer":0,"explanation":"Ns = 120f/P (rpm)"},
     {"q":"Slip s = ?","options":["(N-Ns)/Ns","(Ns-N)/Ns","Ns/N","N/Ns"],"answer":1,"explanation":"s = (Ns-N)/Ns"},
     {"q":"Rotor frequency fr = ?","options":["f","sf","f/s","s/f"],"answer":1,"explanation":"fr = sf (rotor frequency)"},
     {"q":"Full load slip সাধারণত কত?","options":["0%","1-5%","10-20%","50%"],"answer":1,"explanation":"Induction motor full load slip ≈ 1-5%"},
     {"q":"Induction motor starting এ slip = ?","options":["0","0.5","1","∞"],"answer":2,"explanation":"Starting: N=0, s=(Ns-0)/Ns = 1"},
   ],
   "math":{"q":"6-pole, 50Hz induction motor, full load speed=960rpm। Synchronous speed, slip, rotor frequency ও % slip বের করো।",
           "solution":"Ns = 120f/P = 120×50/6 = 1000 rpm\ns = (Ns-N)/Ns = (1000-960)/1000 = 0.04\n% slip = 4%\nRotor frequency fr = s×f = 0.04×50 = 2Hz\nRotor speed = 960 rpm = 100.5 rad/s"}},

  {"topic": "Synchronous Generator — EMF, voltage regulation",
   "mcq": [
     {"q":"Synchronous generator এর EMF equation: Eph = ?","options":["4.44fNΦ","2.22fNΦ","4.44fNΦKw","fNΦ"],"answer":2,"explanation":"Eph = 4.44×Kw×f×N×Φ (Kw = winding factor)"},
     {"q":"Voltage regulation = ?","options":["(VNL-VFL)/VNL","(VNL-VFL)/VFL","(VFL-VNL)/VFL","VNL/VFL"],"answer":1,"explanation":"VR% = (VNL-VFL)/VFL × 100"},
     {"q":"Salient pole machine কোথায় ব্যবহার হয়?","options":["High speed turbine","Hydro/low speed generators","Aircraft","Small motors"],"answer":1,"explanation":"Salient pole: hydro generators (low speed, many poles)"},
     {"q":"Synchronous speed Ns (rpm) = ?","options":["120f/P","60f/P","Pf/120","f/P"],"answer":0,"explanation":"Ns = 120f/P"},
     {"q":"Alternator এ armature reaction effect কোন load এ demagnetizing?","options":["Resistive","Capacitive","Inductive","No load"],"answer":2,"explanation":"Inductive load: lagging current → demagnetizing armature reaction"},
   ],
   "math":{"q":"3-phase alternator: 4-pole, 50Hz, star connected, 500 turns/phase, Φ=0.05Wb, Kw=0.9। Phase EMF, line EMF ও speed বের করো।",
           "solution":"Ns = 120f/P = 120×50/4 = 1500 rpm\nEph = 4.44×Kw×f×N×Φ\n= 4.44×0.9×50×500×0.05\n= 4.44×0.9×50×25\n= 4995V ≈ 5kV\nEL = √3×Eph = √3×5000 = 8.66kV"}},
],

# ══════════════════════════════════════════════════════════
# DAY 5 — Electronics
# ══════════════════════════════════════════════════════════
"Part-4: Electronics": [

  {"topic": "BJT — CE config, biasing, h-parameter",
   "mcq": [
     {"q":"BJT CE config এ current gain β = ?","options":["IC/IB","IB/IC","IE/IB","IC/IE"],"answer":0,"explanation":"β = IC/IB (common emitter current gain)"},
     {"q":"α ও β এর সম্পর্ক?","options":["β=α/(1-α)","α=β/(1-β)","β=α(1-α)","α=β(1+β)"],"answer":0,"explanation":"β = α/(1-α), α = β/(1+β)"},
     {"q":"CE config এ voltage gain কেমন?","options":["< 1","≈ 1","> 1 with 180° phase inversion","> 1 without inversion"],"answer":2,"explanation":"CE: high voltage gain with 180° phase inversion"},
     {"q":"Voltage divider bias সবচেয়ে stable কারণ?","options":["Less components","β independent","High gain","Low cost"],"answer":1,"explanation":"Voltage divider bias: Q-point β independent (stable)"},
     {"q":"h-parameter এ hfe মানে কী?","options":["Input impedance","Output admittance","Forward current gain","Reverse voltage ratio"],"answer":2,"explanation":"hfe = forward current transfer ratio = β"},
   ],
   "math":{"q":"CE amplifier: VCC=12V, RC=3kΩ, RE=1kΩ, R1=30kΩ, R2=10kΩ, β=100, VBE=0.7V। Q-point (ICQ, VCEQ) বের করো।",
           "solution":"VB = VCC×R2/(R1+R2) = 12×10/40 = 3V\nVE = VB-VBE = 3-0.7 = 2.3V\nIE = VE/RE = 2.3/1000 = 2.3mA\nIC ≈ IE = 2.3mA (β large)\nIB = IC/β = 2.3mA/100 = 23μA\nVCE = VCC-IC(RC+RE) = 12-2.3m×4k = 12-9.2 = 2.8V\nQ-point: ICQ=2.3mA, VCEQ=2.8V"}},

  {"topic": "Operational Amplifier",
   "mcq": [
     {"q":"Ideal Op-Amp এর input impedance?","options":["0","50Ω","1MΩ","∞"],"answer":3,"explanation":"Ideal Op-Amp: Zin = ∞"},
     {"q":"Inverting amplifier gain = ?","options":["Rf/R1","-Rf/R1","1+Rf/R1","R1/Rf"],"answer":1,"explanation":"Inverting: Av = -Rf/R1"},
     {"q":"Non-inverting amplifier gain = ?","options":["Rf/R1","-Rf/R1","1+Rf/R1","R1/Rf"],"answer":2,"explanation":"Non-inverting: Av = 1 + Rf/R1"},
     {"q":"CMRR = ?","options":["Differential gain/Common mode gain","Common mode gain/Differential gain","Av×Bandwidth","Gain×Phase"],"answer":0,"explanation":"CMRR = Ad/Acm (dB = 20log(Ad/Acm))"},
     {"q":"Slew rate মানে কী?","options":["Maximum frequency","Maximum output voltage rate of change","Input impedance","Bandwidth"],"answer":1,"explanation":"Slew rate = dVout/dt maximum (V/μs)"},
   ],
   "math":{"q":"Summing amplifier: Rf=100kΩ, R1=10kΩ (V1=1V), R2=20kΩ (V2=2V), R3=50kΩ (V3=3V)। Output voltage বের করো।",
           "solution":"Vout = -Rf×(V1/R1 + V2/R2 + V3/R3)\n= -100k×(1/10k + 2/20k + 3/50k)\n= -100k×(0.1m + 0.1m + 0.06m)\n= -100k×0.26mA\n= -26V"}},

  {"topic": "Diode & Rectifier",
   "mcq": [
     {"q":"Silicon diode forward voltage drop?","options":["0V","0.3V","0.7V","1.4V"],"answer":2,"explanation":"Silicon: Vf ≈ 0.7V, Germanium: 0.3V"},
     {"q":"Full-wave bridge rectifier Vdc = ?","options":["Vm/π","2Vm/π","Vm/2","0.636Vm"],"answer":1,"explanation":"Vdc = 2Vm/π ≈ 0.636Vm"},
     {"q":"Full-wave rectifier ripple factor?","options":["1.21","0.48","0.812","2.0"],"answer":1,"explanation":"Full-wave ripple factor γ = 0.48"},
     {"q":"Half-wave rectifier efficiency?","options":["81.2%","40.6%","50%","100%"],"answer":1,"explanation":"Half-wave efficiency = 40.6%"},
     {"q":"Zener diode কোন region এ কাজ করে?","options":["Forward active","Forward saturation","Reverse breakdown","Cut-off"],"answer":2,"explanation":"Zener: reverse breakdown region এ voltage regulation"},
   ],
   "math":{"q":"Full-wave bridge rectifier: Vrms=230V, RL=1kΩ, প্রতি diode Vf=0.7V। Vm, Vdc, Idc, ripple factor ও efficiency বের করো।",
           "solution":"Vm = 230×√2 = 325.3V\nVdc = 2Vm/π - 2Vf = 207.2-1.4 = 205.8V\nIdc = Vdc/RL = 205.8mA\nVrms_out = Vm/√2 = 230V (approx)\nRipple factor γ = 0.48\nPdc = 205.8×0.2058 = 42.4W\nPin ≈ 230×0.2058 = 47.3W... η=81.2%"}},

  {"topic": "Digital Electronics — K-map, gates",
   "mcq": [
     {"q":"(1010)₂ = ?₁₀","options":["8","10","12","16"],"answer":1,"explanation":"1×8+0×4+1×2+0×1 = 10"},
     {"q":"De Morgan: (AB)' = ?","options":["A'B'","A'+B'","AB","A+B"],"answer":1,"explanation":"De Morgan: (AB)' = A'+B'"},
     {"q":"NAND gate কে বলা হয়?","options":["Basic gate","Universal gate","Special gate","Compound gate"],"answer":1,"explanation":"NAND (ও NOR) universal gate — এ দিয়ে সব gate বানানো যায়"},
     {"q":"K-map এ adjacent cell differ করে কতটি variable?","options":["2","1","3","সব"],"answer":1,"explanation":"K-map: Gray code, adjacent cells differ by 1 variable"},
     {"q":"JK FF এ J=K=1 হলে output?","options":["Q=1","Q=0","Q unchanged","Q toggles"],"answer":3,"explanation":"JK: J=K=1 → toggle (complement of previous Q)"},
   ],
   "math":{"q":"F(A,B,C,D) = Σm(0,1,4,5,8,9,12,13) — K-map দিয়ে simplify করো।",
           "solution":"4-variable K-map:\n    CD\nAB | 00 01 11 10\n00 |  1  1  0  0\n01 |  1  1  0  0\n11 |  1  1  0  0\n10 |  1  1  0  0\n\nGroup: all cells where D=0 (8 cells)\nF = B'D' + BD' = ... \nActually: minterms 0,1,4,5,8,9,12,13 — all have C=0\nF = C' (simplified!)"}},
],

# ══════════════════════════════════════════════════════════
# DAY 6 — Communication & Signals
# ══════════════════════════════════════════════════════════
"Part-5: Communication & Signals": [

  {"topic": "AM Modulation — index, power, bandwidth",
   "mcq": [
     {"q":"AM modulation index m = ?","options":["Ac/Am","Am/Ac","Am×Ac","fc/fm"],"answer":1,"explanation":"m = Am/Ac (0 ≤ m ≤ 1 for no distortion)"},
     {"q":"AM bandwidth BW = ?","options":["fm","2fm","fc","fc±fm"],"answer":1,"explanation":"AM BW = 2fm (USB + LSB)"},
     {"q":"AM total power Pt = ?","options":["Pc(1+m)","Pc(1+m²/2)","Pc×m²","Pc+Pm"],"answer":1,"explanation":"Pt = Pc(1 + m²/2)"},
     {"q":"m > 1 হলে AM এ কী হয়?","options":["Better quality","Overmodulation/distortion","Less power","Wider bandwidth"],"answer":1,"explanation":"m > 1: overmodulation → waveform distortion"},
     {"q":"AM এ useful information কোথায় থাকে?","options":["Carrier","Upper sideband only","Lower sideband only","Both sidebands"],"answer":3,"explanation":"Information in both sidebands (carrier has no info)"},
   ],
   "math":{"q":"AM: carrier Pc=1kW, m=0.8, fm=5kHz। Total power, sideband power, USB ও LSB frequency (fc=1MHz) বের করো।",
           "solution":"Pt = Pc(1+m²/2) = 1000×(1+0.32) = 1320W\nSideband power = Pt-Pc = 320W\nEach sideband = 160W\nUSB = fc+fm = 1000+5 = 1005kHz\nLSB = fc-fm = 1000-5 = 995kHz\nEfficiency = 320/1320 = 24.2%"}},

  {"topic": "PCM — sampling, quantization",
   "mcq": [
     {"q":"Nyquist sampling rate = ?","options":["fm","2fm","fm/2","4fm"],"answer":1,"explanation":"fs ≥ 2fm (Nyquist criterion)"},
     {"q":"PCM এ quantization levels = ?","options":["2n","n²","2^n","n×2"],"answer":2,"explanation":"n-bit PCM: L = 2^n quantization levels"},
     {"q":"8-bit PCM এ quantization levels কত?","options":["8","64","128","256"],"answer":3,"explanation":"2^8 = 256 levels"},
     {"q":"Aliasing ঘটে কখন?","options":["fs > 2fm","fs = 2fm","fs < 2fm","fs = fm"],"answer":2,"explanation":"Aliasing: undersampling (fs < 2fm)"},
     {"q":"PCM bit rate = ?","options":["fs","fs×n","fs/n","n/fs"],"answer":1,"explanation":"Bit rate = fs × n (sampling rate × bits per sample)"},
   ],
   "math":{"q":"Audio signal: fm=4kHz, 8-bit PCM। (a) Minimum sampling rate? (b) Quantization levels? (c) Bit rate? (d) SNR (dB)?",
           "solution":"(a) fs = 2fm = 2×4 = 8kHz (Nyquist rate)\n(b) L = 2^n = 2^8 = 256 levels\n(c) Bit rate = fs×n = 8000×8 = 64kbps\n(d) SNR = 6.02n + 1.76 = 6.02×8 + 1.76 = 49.92 dB ≈ 50dB"}},

  {"topic": "SNR & Channel Capacity",
   "mcq": [
     {"q":"Shannon's channel capacity C = ?","options":["B×log2(1+S/N)","B×log10(SNR)","2B×log2(M)","B/SNR"],"answer":0,"explanation":"C = B×log2(1+SNR) bits/second"},
     {"q":"SNR দ্বিগুণ হলে channel capacity কতটুকু বাড়ে?","options":["দ্বিগুণ","এক bit/Hz বাড়ে","চারগুণ","অপরিবর্তিত"],"answer":1,"explanation":"C = Blog2(1+SNR), SNR double → C বাড়ে log2(2)=1 bit/Hz/s"},
     {"q":"Noise figure F = ?","options":["SNRin/SNRout","SNRout/SNRin","SNRin×SNRout","SNRin+SNRout"],"answer":0,"explanation":"F = SNRin/SNRout (F ≥ 1, perfect amplifier F=1)"},
     {"q":"Thermal noise power N = ?","options":["kTB","kT/B","kB/T","T/kB"],"answer":0,"explanation":"N = kTB (k=Boltzmann, T=temperature, B=bandwidth)"},
     {"q":"B=3kHz, SNR=31 হলে channel capacity কত?","options":["15kbps","30kbps","45kbps","60kbps"],"answer":0,"explanation":"C = 3000×log2(32) = 3000×5 = 15000bps = 15kbps"},
   ],
   "math":{"q":"Telephone channel: B=3.4kHz, SNR=30dB। Maximum channel capacity বের করো।",
           "solution":"SNR(linear) = 10^(30/10) = 1000\nC = B×log2(1+SNR) = 3400×log2(1001)\n= 3400×9.967\n= 33888 bps ≈ 33.9 kbps\n\nPractical telephone: 56kbps modem uses compression tricks"}},

  {"topic": "Angle Modulation — FM, Carson's rule",
   "mcq": [
     {"q":"FM modulation index β = ?","options":["Δf/fm","fm/Δf","Δf×fm","fc/fm"],"answer":0,"explanation":"β = Δf/fm (frequency deviation/message frequency)"},
     {"q":"Carson's rule: FM bandwidth BW ≈ ?","options":["2Δf","2fm","2(Δf+fm)","Δf+fm"],"answer":2,"explanation":"BW = 2(Δf+fm) = 2fm(1+β)"},
     {"q":"FM এ noise performance AM এর চেয়ে কেমন?","options":["খারাপ","একই","ভালো","β এর উপর নির্ভর করে"],"answer":2,"explanation":"FM: better noise performance, especially wideband FM"},
     {"q":"Wideband FM এ β = ?","options":["β < 1","β = 1","β >> 1","β = 0"],"answer":2,"explanation":"WBFM: β >> 1 (large frequency deviation)"},
     {"q":"FM transmitter এ pre-emphasis করা হয় কেন?","options":["Power বাড়াতে","High frequency noise কমাতে","Bandwidth কমাতে","Carrier suppress করতে"],"answer":1,"explanation":"Pre-emphasis: high frequency boost → better SNR at receiver"},
   ],
   "math":{"q":"FM: fc=100MHz, fm=5kHz, Δf=25kHz। (a) Modulation index β? (b) Carson's rule BW? (c) Narrowband নাকি Wideband?",
           "solution":"(a) β = Δf/fm = 25kHz/5kHz = 5\n(b) BW = 2(Δf+fm) = 2(25+5) = 60kHz\n(c) β = 5 > 1 → Wideband FM\n\nFor NBFM: BW ≈ 2fm = 10kHz (β << 1 case)\nWBFM uses 6× more bandwidth than NBFM"}},
],

# ══════════════════════════════════════════════════════════
# DAY 7 — Revision Day
# ══════════════════════════════════════════════════════════
"Revision Day — Mixed Topics": [

  {"topic": "DC Circuit — Theorem Practice",
   "mcq": [
     {"q":"Thevenin ও Norton equivalent এ কোনটি সবসময় same থাকে?","options":["Voltage","Current","Resistance","Power"],"answer":2,"explanation":"Rth = Rn (same resistance, different source type)"},
     {"q":"KCL based?","options":["Mesh analysis","Nodal analysis","Superposition","Thevenin"],"answer":1,"explanation":"Nodal analysis uses KCL at each node"},
     {"q":"KVL based?","options":["Nodal analysis","Mesh analysis","Norton","Source transformation"],"answer":1,"explanation":"Mesh analysis uses KVL around each mesh"},
     {"q":"Source transformation valid for?","options":["Only DC","Only AC","Both DC & AC","Neither"],"answer":2,"explanation":"Source transformation valid for both DC and AC circuits"},
     {"q":"Maximum power = Vth²/4Rth এ efficiency কত?","options":["25%","50%","75%","100%"],"answer":1,"explanation":"At maximum power transfer, efficiency = 50%"},
   ],
   "math":{"q":"Previous BPSC Question: একটি circuit এ V=20V, R1=4Ω, R2=4Ω, R3=8Ω। R1 ও V series, R2 parallel with R3। Thevenin equivalent at R3 এর terminals বের করো।",
           "solution":"Remove R3:\nVth = V × R2/(R1+R2) = 20×4/(4+4) = 10V\nRth = R1||R2 = (4×4)/(4+4) = 2Ω\n\nWith R3=8Ω:\nIR3 = 10/(2+8) = 1A\nPR3 = 1²×8 = 8W\nMax power (RL=Rth=2Ω): Pmax = 10²/(4×2) = 12.5W"}},

  {"topic": "Power System — Mixed Practice",
   "mcq": [
     {"q":"Load factor = ?","options":["Average load/Peak load","Peak load/Average load","Total energy/Peak load","Average load×hours"],"answer":0,"explanation":"Load factor = Average load/Maximum demand"},
     {"q":"Diversity factor = ?","options":["Sum of individual max demands/System max demand","System max/Individual max","Average/Peak","Peak/Average"],"answer":0,"explanation":"Diversity factor = ΣMax demands / System maximum demand"},
     {"q":"Transmission line এ corona loss কমাতে?","options":["Voltage বাড়াও","Conductor diameter বাড়াও","Length কমাও","Frequency বাড়াও"],"answer":1,"explanation":"Larger conductor diameter → less electric field → less corona"},
     {"q":"Buchholz relay কোথায় ব্যবহার হয়?","options":["Motor protection","Transformer protection","Generator protection","Line protection"],"answer":1,"explanation":"Buchholz relay: oil-immersed transformer protection"},
     {"q":"Distance relay কী পরিমাপ করে?","options":["Current","Voltage","Impedance","Power"],"answer":2,"explanation":"Distance relay measures impedance to fault location"},
   ],
   "math":{"q":"BREB MCQ style: 33/11kV transformer, 10MVA, Zpu=0.1pu (own base)। 3-phase fault at 11kV side। Fault current বের করো।",
           "solution":"Base current (11kV side) = S/(√3×V) = 10×10⁶/(√3×11000)\n= 524.9A\nFault current = Base current/Zpu = 524.9/0.1 = 5249A\nFault MVA = S/Zpu = 10/0.1 = 100 MVA"}},
],
}

# ══════════════════════════════════════════════════════════
# NON-DEPT MCQ
# ══════════════════════════════════════════════════════════
NON_DEPT_QUESTIONS = {
"বাংলা ভাষা ও সাহিত্য": [
  {"topic": "সন্ধি ও ব্যাকরণ", "mcq": [
    {"q":"'বিদ্যালয়' এর সন্ধি বিচ্ছেদ?","options":["বিদ্যা+আলয়","বিদ্যা+লয়","বিদ্+আলয়","বিদ্যাল+য়"],"answer":0,"explanation":"বিদ্যা+আলয় = বিদ্যালয় (আ+আ=আ)"},
    {"q":"'মনোযোগ' এর সন্ধি বিচ্ছেদ?","options":["মনো+যোগ","মন+যোগ","মনঃ+যোগ","মন+অযোগ"],"answer":2,"explanation":"মনঃ+যোগ = মনোযোগ (বিসর্গ সন্ধি)"},
    {"q":"রবীন্দ্রনাথ নোবেল পান কত সালে?","options":["1911","1913","1915","1921"],"answer":1,"explanation":"১৯১৩ — গীতাঞ্জলির জন্য"},
    {"q":"কাজী নজরুলের প্রথম কাব্যগ্রন্থ?","options":["অগ্নিবীণা","বিষের বাঁশী","সঞ্চিতা","ছায়ানট"],"answer":0,"explanation":"অগ্নিবীণা (১৯২২)"},
    {"q":"'আমার সোনার বাংলা' কার রচনা?","options":["নজরুল","রবীন্দ্রনাথ","জীবনানন্দ","মাইকেল"],"answer":1,"explanation":"রবীন্দ্রনাথ — বাংলাদেশের জাতীয় সংগীত"},
  ]},
],
"English Language & Literature": [
  {"topic": "Grammar & Vocabulary", "mcq": [
    {"q":"Passive of 'They built the bridge':","options":["The bridge built by them","The bridge was built by them","The bridge is built by them","The bridge were built by them"],"answer":1,"explanation":"Simple past passive: was/were + past participle"},
    {"q":"Synonym of 'Benevolent':","options":["Cruel","Kind","Angry","Lazy"],"answer":1,"explanation":"Benevolent = Kind, charitable"},
    {"q":"Antonym of 'Verbose':","options":["Talkative","Wordy","Concise","Eloquent"],"answer":2,"explanation":"Verbose = too many words; Antonym = Concise"},
    {"q":"'I wish I ___ rich.' correct form:","options":["am","was","were","will be"],"answer":2,"explanation":"Subjunctive with 'wish': were (all persons)"},
    {"q":"One word for 'one who walks in sleep':","options":["Insomniac","Somniloquist","Somnambulist","Narcissist"],"answer":2,"explanation":"Somnambulist = sleepwalker"},
  ]},
],
"বাংলাদেশ বিষয়াবলি": [
  {"topic": "মুক্তিযুদ্ধ ও সংবিধান", "mcq": [
    {"q":"বাংলাদেশের স্বাধীনতা ঘোষণা কোন তারিখে?","options":["২৫ মার্চ","২৬ মার্চ","১৬ ডিসেম্বর","৭ মার্চ"],"answer":1,"explanation":"২৬ মার্চ ১৯৭১ — স্বাধীনতা দিবস"},
    {"q":"মুক্তিযুদ্ধে কতটি সেক্টর ছিল?","options":["৯","১০","১১","১২"],"answer":2,"explanation":"১১টি সেক্টর"},
    {"q":"বাংলাদেশের সংবিধানের মূলনীতি কতটি?","options":["৩","৪","৫","৬"],"answer":1,"explanation":"৪টি: জাতীয়তাবাদ, সমাজতন্ত্র, গণতন্ত্র, ধর্মনিরপেক্ষতা"},
    {"q":"বাংলাদেশ সংবিধান কার্যকর হয়?","options":["১৬ ডিসেম্বর ১৯৭১","৪ নভেম্বর ১৯৭২","১৬ ডিসেম্বর ১৯৭২","২৬ মার্চ ১৯৭৩"],"answer":2,"explanation":"১৬ ডিসেম্বর ১৯৭২"},
    {"q":"বাংলাদেশের প্রথম রাষ্ট্রপতি?","options":["তাজউদ্দীন","সৈয়দ নজরুল","শেখ মুজিব","জিয়াউর রহমান"],"answer":2,"explanation":"বঙ্গবন্ধু শেখ মুজিবুর রহমান"},
  ]},
],
"আন্তর্জাতিক বিষয়াবলি": [
  {"topic": "জাতিসংঘ ও সংগঠন", "mcq": [
    {"q":"জাতিসংঘ প্রতিষ্ঠিত হয়?","options":["1944","1945","1946","1950"],"answer":1,"explanation":"২৪ অক্টোবর ১৯৪৫"},
    {"q":"UN Security Council এর স্থায়ী সদস্য কতটি?","options":["3","5","10","15"],"answer":1,"explanation":"P5: USA, UK, France, Russia, China"},
    {"q":"IMF সদর দপ্তর?","options":["New York","Geneva","Washington D.C.","London"],"answer":2,"explanation":"IMF HQ: Washington D.C."},
    {"q":"SAARC সদস্য দেশ কতটি?","options":["6","7","8","9"],"answer":2,"explanation":"৮ সদস্য"},
    {"q":"UNESCO সদর দপ্তর?","options":["New York","Paris","Geneva","Vienna"],"answer":1,"explanation":"UNESCO HQ: Paris, France"},
  ]},
],
"সাধারণ বিজ্ঞান": [
  {"topic": "পদার্থ ও জীববিজ্ঞান", "mcq": [
    {"q":"আলোর গতি?","options":["3×10⁶ m/s","3×10⁸ m/s","3×10¹⁰ m/s","3×10⁴ m/s"],"answer":1,"explanation":"c = 3×10⁸ m/s"},
    {"q":"মানবদেহের স্বাভাবিক তাপমাত্রা?","options":["36°C","37°C","38°C","35°C"],"answer":1,"explanation":"37°C = 98.6°F"},
    {"q":"DNA এর পূর্ণ রূপ?","options":["Deoxyribonucleic Acid","Deoxyribonitric Acid","Diribonucleic Acid","Dioxyribose Acid"],"answer":0,"explanation":"Deoxyribonucleic Acid"},
    {"q":"সালোকসংশ্লেষণে কোন গ্যাস ব্যবহার হয়?","options":["O₂","N₂","CO₂","H₂"],"answer":2,"explanation":"6CO₂+6H₂O → C₆H₁₂O₆+6O₂"},
    {"q":"বিদ্যুৎ পরিবাহিতার একক?","options":["Ohm","Ampere","Siemens","Volt"],"answer":2,"explanation":"Conductance unit = Siemens (S)"},
  ]},
],
"কম্পিউটার ও তথ্যপ্রযুক্তি": [
  {"topic": "নেটওয়ার্ক ও হার্ডওয়্যার", "mcq": [
    {"q":"OSI model এ কতটি layer?","options":["5","6","7","4"],"answer":2,"explanation":"7 layers"},
    {"q":"1 GB = কত MB?","options":["100","1000","1024","512"],"answer":2,"explanation":"1 GB = 1024 MB"},
    {"q":"HTTP port number?","options":["21","23","80","443"],"answer":2,"explanation":"HTTP=80, HTTPS=443"},
    {"q":"RAM এর পূর্ণ রূপ?","options":["Read Access Memory","Random Access Memory","Read Actual Memory","Rapid Access Memory"],"answer":1,"explanation":"Random Access Memory (volatile)"},
    {"q":"Binary তে (255)₁₀ = ?","options":["11111110","11111111","11110000","10101010"],"answer":1,"explanation":"255 = 2⁸-1 = 11111111"},
  ]},
],
"গাণিতিক যুক্তি": [
  {"topic": "পাটিগণিত ও বীজগণিত", "mcq": [
    {"q":"১২ ও ১৮ এর ল.সা.গু?","options":["6","36","72","24"],"answer":1,"explanation":"LCM(12,18) = 36"},
    {"q":"একটি সংখ্যার ৪০% = ৮০। সংখ্যাটি?","options":["160","200","180","220"],"answer":1,"explanation":"x = 80×100/40 = 200"},
    {"q":"x²-5x+6=0 এর সমাধান?","options":["x=2,3","x=1,6","x=-2,-3","x=2,-3"],"answer":0,"explanation":"(x-2)(x-3)=0"},
    {"q":"একটি বর্গের ক্ষেত্রফল ৬৪ বর্গমিটার। পরিসীমা?","options":["16m","32m","8m","64m"],"answer":1,"explanation":"a=8m, পরিসীমা=4×8=32m"},
    {"q":"৫ জন ৫ দিনে ৫টি কাজ। ১০ জন ১০ দিনে কতটি?","options":["10","20","50","100"],"answer":1,"explanation":"Rate=1/5 per person per day. 10×10×(1/5)=20"},
  ]},
],
}

# ══════════════════════════════════════════════════════════
# MISSING TOPICS — Added based on Rony Parvej syllabus
# ══════════════════════════════════════════════════════════

# Add to DC Circuit
EEE_QUESTIONS["Part-1: DC Circuit"] += [
  {"topic": "Mesh Analysis",
   "mcq": [
     {"q":"Mesh Analysis এ mesh current কোন দিকে ধরা হয়?","options":["শুধু clockwise","শুধু anticlockwise","যেকোনো দিকে","বাইরে"],"answer":2,"explanation":"যেকোনো দিক, তবে সাধারণত clockwise"},
     {"q":"Supermesh তৈরি হয় কখন?","options":["V source দুই mesh এ","I source দুই mesh এর মাঝে","R দুই mesh এ","কোনো source নেই"],"answer":1,"explanation":"Current source দুই mesh এর shared branch এ → supermesh"},
     {"q":"2 mesh circuit এ mesh analysis এ কতটি equation?","options":["1","2","3","4"],"answer":1,"explanation":"Mesh সংখ্যা = equation সংখ্যা"},
     {"q":"Mesh analysis কোন ধরনের circuit এ প্রযোজ্য?","options":["Non-planar","Planar","3D","যেকোনো"],"answer":1,"explanation":"Mesh analysis শুধু planar circuit এ"},
     {"q":"Mesh resistance matrix কেমন?","options":["Asymmetric","Symmetric","Zero","Identity"],"answer":1,"explanation":"Mesh R matrix সবসময় symmetric"},
   ],
   "math":{"q":"Mesh 1: 10V, R1=2Ω, R3=4Ω (shared). Mesh 2: 6V, R2=3Ω, R3=4Ω (shared)। I1, I2 ও R3 এর current বের করো।",
           "solution":"Mesh 1: (2+4)I1 - 4I2 = 10 → 6I1-4I2=10 ...(1)\nMesh 2: (3+4)I2 - 4I1 = 6 → -4I1+7I2=6 ...(2)\n(1)×7+( 2)×4: 42I1-28I2+(-16I1+28I2)=70+24\n26I1=94 → I1=3.62A\nI2=(6×3.62-10)/4=2.92A\nI_R3=I1-I2=0.7A"}},

  {"topic": "Nodal Analysis",
   "mcq": [
     {"q":"Nodal analysis এ reference node এর voltage?","options":["Vmax","Vmin","0","অজানা"],"answer":2,"explanation":"Reference (ground) node: V=0"},
     {"q":"Supernode তৈরি হয় কখন?","options":["R দুই node এ","V source দুই non-reference node এ","I source দুই node এ","R দুই branch এ"],"answer":1,"explanation":"Voltage source between two non-reference nodes → supernode"},
     {"q":"n node থাকলে independent KCL equation কতটি?","options":["n","n+1","n-1","2n"],"answer":2,"explanation":"n-1 (reference বাদ দিয়ে)"},
     {"q":"Nodal analysis এ প্রতিটি node এ কোন law apply?","options":["KVL","KCL","Ohm's","Faraday's"],"answer":1,"explanation":"KCL at each node"},
     {"q":"Nodal analysis এ অজানা রাশি কী?","options":["Branch current","Node voltage","Mesh current","Power"],"answer":1,"explanation":"Node voltage বের করা হয়"},
   ],
   "math":{"q":"Node V1: 5A current প্রবেশ করছে, V1→ground=2Ω, V1→V2=4Ω। Node V2: V2→ground=6Ω। V1 ও V2 বের করো।",
           "solution":"Node V1 KCL: 5 = V1/2 + (V1-V2)/4\n20 = 2V1 + V1-V2 → 3V1-V2=20 ...(1)\nNode V2 KCL: (V1-V2)/4 = V2/6\n3(V1-V2)=2V2 → 3V1=5V2 → V1=5V2/3 ...(2)\n(2)→(1): 5V2-V2=20 → V2=5V, V1=8.33V"}},
]

# Add to AC Circuit
EEE_QUESTIONS["Part-1: AC Circuit"] += [
  {"topic": "Wattmeter — Two Wattmeter Method",
   "mcq": [
     {"q":"Two wattmeter method এ total power P = ?","options":["W1-W2","W1+W2","W1×W2","(W1+W2)/2"],"answer":1,"explanation":"P = W1 + W2"},
     {"q":"Power factor = 0 হলে two wattmeter এ?","options":["W1=W2","W1=-W2","W1=0","W2=0"],"answer":1,"explanation":"PF=0: W1=-W2, P=0"},
     {"q":"Unity PF এ two wattmeter এ?","options":["W1=0","W2=0","W1=W2","W1=-W2"],"answer":2,"explanation":"PF=1: W1=W2, Q=0"},
     {"q":"tan φ = √3×(W1-W2)/(W1+W2) এ W1>W2 মানে?","options":["Capacitive load","Inductive load","Unity PF","Zero PF"],"answer":1,"explanation":"W1>W2 → lagging PF (inductive)"},
     {"q":"3-phase 3-wire system এ কতটি wattmeter দরকার?","options":["1","2","3","4"],"answer":1,"explanation":"Two wattmeter method: শুধু 2টি দিয়ে 3-phase power মাপা যায়"},
   ],
   "math":{"q":"Two wattmeter: W1=3kW, W2=1kW। Total power, power factor ও reactive power বের করো।",
           "solution":"P = W1+W2 = 3+1 = 4kW\ntanφ = √3×(W1-W2)/(W1+W2) = √3×2/4 = 0.866\nφ = 40.9°\nPF = cos(40.9°) = 0.755 lagging\nQ = P×tanφ = 4×0.866 = 3.46 kVAR\nS = P/PF = 4/0.755 = 5.3 kVA"}},

  {"topic": "Filters & Frequency Response",
   "mcq": [
     {"q":"Low pass filter এ cutoff frequency fc তে gain কত?","options":["Maximum","0","1/√2 × Amax","-3dB = 0.707×Amax"],"answer":3,"explanation":"fc তে gain = 0.707×Amax = -3dB"},
     {"q":"RC Low pass filter এর cutoff frequency fc = ?","options":["RC","1/RC","1/(2πRC)","2πRC"],"answer":2,"explanation":"fc = 1/(2πRC)"},
     {"q":"High pass filter pass করে?","options":["Low frequency","High frequency","All frequency","No frequency"],"answer":1,"explanation":"HPF: fc এর উপরে signal pass করে"},
     {"q":"Bode plot এ gain এর unit?","options":["Watt","dB","Volt","Ohm"],"answer":1,"explanation":"Bode plot gain: dB = 20log10(Vout/Vin)"},
     {"q":"Butterworth filter এর বৈশিষ্ট্য?","options":["Ripple in passband","Maximally flat response","Steep rolloff","Ripple in stopband"],"answer":1,"explanation":"Butterworth: maximally flat (no ripple) in passband"},
   ],
   "math":{"q":"RC HPF: R=1kΩ, C=0.1μF। fc বের করো। f=fc তে gain কত dB? f=10fc তে gain কত?",
           "solution":"fc = 1/(2πRC) = 1/(2π×1000×0.1×10⁻⁶) = 1592Hz\nAt f=fc: gain = 1/√2 = 0.707 = -3dB\nAt f=10fc: gain = 10/√(1+100) ≈ 10/10.05 = 0.995 ≈ 0dB (passband)"}},
]

# Add to Power System
EEE_QUESTIONS["Part-2: Power System"] += [
  {"topic": "Variable Load on Power Station",
   "mcq": [
     {"q":"Load factor = ?","options":["Peak load/Average load","Average load/Peak load","Total energy/Peak","Average×hours"],"answer":1,"explanation":"Load factor = Average load/Maximum demand (0 to 1)"},
     {"q":"Diversity factor = ?","options":["System max/Sum of individual max","Sum of individual max/System max","Average/Peak","Peak/Average"],"answer":1,"explanation":"Diversity factor = ΣMax demands / System max demand (≥1)"},
     {"q":"Demand factor = ?","options":["Max demand/Connected load","Connected load/Max demand","Average/Max","Max/Average"],"answer":0,"explanation":"Demand factor = Max demand/Total connected load (≤1)"},
     {"q":"Plant capacity factor = ?","options":["Average load/Plant capacity","Peak load/Plant capacity","Energy/Capacity","Capacity/Energy"],"answer":0,"explanation":"Plant capacity factor = Average load/Installed capacity"},
     {"q":"High load factor মানে?","options":["Equipment কম ব্যবহার","Equipment বেশি ব্যবহার","Fixed cost বেশি","Variable cost কম"],"answer":1,"explanation":"High load factor: plant বেশি সময় পূর্ণ লোডে চলে → ভালো"},
   ],
   "math":{"q":"Power station: Max demand=50MW, Load factor=0.6, Plant capacity=80MW। Units generated/day, plant capacity factor ও reserve capacity বের করো।",
           "solution":"Average load = Max demand × Load factor = 50×0.6 = 30MW\nUnits/day = 30×24 = 720 MWh\nPlant capacity factor = Average load/Plant capacity = 30/80 = 0.375 = 37.5%\nReserve capacity = Plant capacity - Max demand = 80-50 = 30MW"}},

  {"topic": "Unsymmetrical Fault",
   "mcq": [
     {"q":"Single Line to Ground (SLG) fault এ কোন sequence current আছে?","options":["Positive only","Positive & negative","Positive, negative & zero"],"answer":2,"explanation":"SLG: Ia1=Ia2=Ia0 (all three sequences equal)"},
     {"q":"Line to Line (LL) fault এ zero sequence current?","options":["Maximum","Same as positive","Zero","Infinite"],"answer":2,"explanation":"LL fault: Ia0=0 (no ground path)"},
     {"q":"Symmetrical components কে প্রবর্তন করেন?","options":["Tesla","Fortescue","Steinmetz","Edison"],"answer":1,"explanation":"C.L. Fortescue (1918) — symmetrical components theory"},
     {"q":"Positive sequence component মানে?","options":["ABC phase order","ACB phase order","All same phase","No rotation"],"answer":0,"explanation":"Positive sequence: ABC (normal rotation)"},
     {"q":"SLG fault এ fault current Ia = ?","options":["Ia1","3Ia1","Ia1/3","2Ia1"],"answer":1,"explanation":"SLG: Ia = 3Ia1 = 3Ia2 = 3Ia0"},
   ],
   "math":{"q":"SLG fault: Z1=j0.2, Z2=j0.2, Z0=j0.4 pu। Prefault voltage=1pu। Fault current (pu) বের করো।",
           "solution":"Ia1 = Vf/(Z1+Z2+Z0) = 1/(j0.2+j0.2+j0.4) = 1/j0.8 = -j1.25 pu\nIa = 3Ia1 = 3×(-j1.25) = -j3.75 pu\n|Ia| = 3.75 pu\nIf base current = 524A: Fault current = 3.75×524 = 1965A"}},

  {"topic": "Switchgear, Protection & Substation",
   "mcq": [
     {"q":"Buchholz relay কোন equipment protect করে?","options":["Motor","Oil-immersed transformer","Generator","Busbar"],"answer":1,"explanation":"Buchholz relay: oil transformer protection (gas/oil surge)"},
     {"q":"Distance relay কী measure করে?","options":["Current","Voltage","Impedance to fault","Power"],"answer":2,"explanation":"Distance relay: impedance দেখে fault location নির্ধারণ করে"},
     {"q":"Differential relay কাজ করে কখন?","options":["I_in = I_out","I_in ≠ I_out","V_in = V_out","Overvoltage"],"answer":1,"explanation":"Differential relay: I_in ≠ I_out → internal fault"},
     {"q":"SF6 circuit breaker এর সুবিধা?","options":["কম দামি","High dielectric strength, arc quenching","Mechanical সহজ","কম maintenance"],"answer":1,"explanation":"SF6: excellent arc quenching, high dielectric, compact"},
     {"q":"Lightning arrester কোথায় লাগানো হয়?","options":["Generator terminal","Substation incoming feeder","Transformer secondary","Motor terminal"],"answer":1,"explanation":"Lightning arrester: substation এ surge protection"},
   ],
   "math":{"q":"Overcurrent relay: CT ratio=100/5, relay pickup=2A, TMS=0.5। Primary fault current=600A হলে relay operate করবে? Operating time বের করো (IDMT: t=0.14/(I^0.02-1) × TMS)।",
           "solution":"CT secondary current = 600×(5/100) = 30A\nPlug setting multiplier PSM = 30/2 = 15\nt = 0.14/(PSM^0.02 - 1) × TMS\n= 0.14/(15^0.02 - 1) × 0.5\n15^0.02 = e^(0.02×ln15) = e^(0.054) = 1.0556\nt = 0.14/(0.0556) × 0.5 = 1.258s"}},

  {"topic": "Power Station & Thermodynamics",
   "mcq": [
     {"q":"Thermal efficiency of power plant = ?","options":["Output power/Heat input","Heat input/Output","Output/Fuel cost","Fuel/Output"],"answer":0,"explanation":"η = Output (kWh) / Heat input (kCal or BTU)"},
     {"q":"Heat rate = ?","options":["Output/Input","Input heat/Output kWh","Output/Fuel","Fuel cost/kWh"],"answer":1,"explanation":"Heat rate = kCal (or BTU) per kWh output (lower = better)"},
     {"q":"Nuclear power plant এ moderator এর কাজ?","options":["Neutron slow করা","Neutron fast করা","Heat produce করা","Coolant হিসেবে"],"answer":0,"explanation":"Moderator: fast neutrons কে slow (thermal) করে fission sustain রাখে"},
     {"q":"Rankine cycle কোন power plant এ ব্যবহার হয়?","options":["Nuclear","Hydro","Thermal steam","Gas turbine"],"answer":2,"explanation":"Rankine cycle: steam power plant (thermal)"},
     {"q":"Cooling tower কী করে?","options":["Steam produce করে","Used cooling water ঠান্ডা করে","Fuel burn করে","Electricity generate করে"],"answer":1,"explanation":"Cooling tower: condenser থেকে গরম water ঠান্ডা করে recirculate"},
   ],
   "math":{"q":"Thermal power plant: Fuel consumed=100 tonnes/day, Calorific value=6000 kCal/kg, Output=20MW। Thermal efficiency ও heat rate বের করো।",
           "solution":"Heat input/day = 100×1000×6000 = 6×10⁸ kCal\nHeat input/hour = 6×10⁸/24 = 2.5×10⁷ kCal/hr\nOutput = 20MW = 20000 kW\nOutput/hr = 20000 kWh\n1kWh = 860 kCal\nη = 20000×860/(2.5×10⁷) = 17.2×10⁶/25×10⁶ = 0.688 = 68.8%\nHeat rate = 2.5×10⁷/20000 = 1250 kCal/kWh"}},
]

# Add to Electrical Machine
EEE_QUESTIONS["Part-3: Electrical Machine"] += [
  {"topic": "DC Generator — EMF, types",
   "mcq": [
     {"q":"DC Generator EMF equation: E = ?","options":["φZNP/60A","φZN/60","ZNP/60φ","φZNA/60P"],"answer":0,"explanation":"E = φZNP/(60A), Z=conductors, P=poles, A=parallel paths"},
     {"q":"Lap winding এ A (parallel paths) = ?","options":["2","P","P/2","1"],"answer":1,"explanation":"Lap winding: A = P (poles সংখ্যার সমান)"},
     {"q":"Wave winding এ A = ?","options":["P","2","P/2","4"],"answer":1,"explanation":"Wave winding: A = 2 (সবসময়)"},
     {"q":"Separately excited generator এ field current কোথা থেকে?","options":["Armature থেকে","External DC source থেকে","AC supply থেকে","Self-generated"],"answer":1,"explanation":"Separately excited: external DC source থেকে field current"},
     {"q":"Compound generator এ series ও shunt field কীভাবে থাকে?","options":["শুধু series","শুধু shunt","উভয়","কোনোটাই না"],"answer":2,"explanation":"Compound generator: both series and shunt field winding"},
   ],
   "math":{"q":"4-pole DC generator: lap winding, Z=400, φ=0.02Wb, N=1500rpm। EMF ও terminal voltage বের করো যদি Ia=50A, Ra=0.2Ω।",
           "solution":"Lap winding: A = P = 4\nE = φZNP/(60A) = 0.02×400×1500×4/(60×4)\n= 0.02×400×1500/60 = 200V\nVt = E - IaRa = 200 - 50×0.2 = 200-10 = 190V"}},

  {"topic": "Synchronous Motor",
   "mcq": [
     {"q":"Synchronous motor কোন speed এ চলে?","options":["Variable","Less than Ns","Synchronous speed Ns","More than Ns"],"answer":2,"explanation":"Synchronous motor: exactly Ns (no slip)"},
     {"q":"Synchronous motor self-starting নয় কারণ?","options":["কম torque","Rotating field ও rotor sync হওয়ার আগেই slip হয়","High cost","কম power"],"answer":1,"explanation":"Rotating field খুব দ্রুত — rotor জড়তার কারণে sync করতে পারে না"},
     {"q":"Over-excited synchronous motor কী supply করে?","options":["Lagging VAR","Leading VAR","Active power only","Nothing"],"answer":1,"explanation":"Over-excited: leading current → supplies leading VAR (capacitive)"},
     {"q":"V-curve এ minimum armature current কখন?","options":["Under-excitation","Over-excitation","Unity PF","No load"],"answer":2,"explanation":"V-curve minimum Ia at unity PF"},
     {"q":"Hunting এ synchronous motor কী করে?","options":["Speed বাড়ে","Speed কমে","Speed oscillates","Motor বন্ধ হয়"],"answer":2,"explanation":"Hunting: speed oscillates around synchronous speed (load change)"},
   ],
   "math":{"q":"3-phase synchronous motor: 400V (line), 10kW, PF=0.8 leading। Line current ও reactive power বের করো।",
           "solution":"P = √3×VL×IL×cosφ\n10000 = √3×400×IL×0.8\nIL = 10000/(√3×400×0.8) = 10000/554 = 18.05A\nS = P/PF = 10000/0.8 = 12500 VA\nQ = S×sinφ = 12500×0.6 = 7500 VAR (leading/capacitive)"}},

  {"topic": "Control System — Transfer function, stability",
   "mcq": [
     {"q":"Closed loop TF = ?","options":["G(s)","G(s)/[1+G(s)H(s)]","G(s)H(s)","1/G(s)"],"answer":1,"explanation":"T(s) = G(s)/[1+G(s)H(s)] (negative feedback)"},
     {"q":"Routh-Hurwitz criterion দিয়ে কী জানা যায়?","options":["Frequency response","Stability","Transient response","Steady state error"],"answer":1,"explanation":"Routh-Hurwitz: poles left half plane এ আছে কিনা"},
     {"q":"First column এ sign change না থাকলে system?","options":["Unstable","Marginally stable","Stable","Oscillatory"],"answer":2,"explanation":"No sign change → all poles LHP → stable"},
     {"q":"Type 1 system এ unit ramp এর steady-state error?","options":["0","1/Kv","∞","1/(1+Kp)"],"answer":1,"explanation":"Type 1, ramp input: ess = 1/Kv"},
     {"q":"PID controller এ D term এর কাজ?","options":["Steady state error কমায়","Overshoot কমায়, speed বাড়ায়","Oscillation বাড়ায়","Gain বাড়ায়"],"answer":1,"explanation":"Derivative: anticipatory action, reduces overshoot"},
   ],
   "math":{"q":"G(s) = K/[s(s+2)(s+4)], H(s)=1। Routh-Hurwitz দিয়ে stability এর জন্য K এর range বের করো।",
           "solution":"CE: s(s+2)(s+4) + K = 0\ns³+6s²+8s+K = 0\nRouth array:\ns³ | 1    8\ns² | 6    K\ns¹ | (48-K)/6\ns⁰ | K\nFor stability: K>0 AND (48-K)/6>0 → K<48\n∴ 0 < K < 48"}},
]

# Add to Electronics
EEE_QUESTIONS["Part-4: Electronics"] += [
  {"topic": "MOSFET — characteristics, regions",
   "mcq": [
     {"q":"Enhancement MOSFET এ channel তৈরি হয় কখন?","options":["VGS=0","VGS < Vth","VGS > Vth","VGS < 0"],"answer":2,"explanation":"Enhancement MOSFET: VGS > Vth হলে channel invert হয়"},
     {"q":"MOSFET এর তিনটি terminal?","options":["E,B,C","A,K,G","G,D,S","G,S,B"],"answer":2,"explanation":"MOSFET: Gate (G), Drain (D), Source (S)"},
     {"q":"Saturation region এ MOSFET current ID ∝ ?","options":["VDS","VGS","(VGS-Vth)²","VGS×VDS"],"answer":2,"explanation":"ID = (k/2)(VGS-Vth)² in saturation"},
     {"q":"Depletion MOSFET ও Enhancement MOSFET এর পার্থক্য?","options":["Terminal সংখ্যা","Depletion: VGS=0 তেও channel আছে","Gate material","Substrate"],"answer":1,"explanation":"Depletion: built-in channel, VGS=0 তেও ON"},
     {"q":"JFET এ channel control হয় কীভাবে?","options":["Gate voltage দিয়ে depletion region","Gate current দিয়ে","Drain voltage দিয়ে","Source voltage দিয়ে"],"answer":0,"explanation":"JFET: reverse bias gate → depletion region → channel width control"},
   ],
   "math":{"q":"N-channel MOSFET: Vth=2V, k=1mA/V², VGS=5V। (a) Saturation এ ID কত? (b) VDS_sat কত? (c) VDS=3V হলে কোন region?",
           "solution":"(a) ID(sat) = (k/2)(VGS-Vth)² = (1m/2)(5-2)² = 0.5m×9 = 4.5mA\n(b) VDS_sat = VGS-Vth = 5-2 = 3V\n(c) VDS=3V = VDS_sat → boundary of saturation/triode\n(VDS ≥ VGS-Vth → saturation region)"}},

  {"topic": "Power Electronics — SCR, chopper, inverter",
   "mcq": [
     {"q":"SCR turn-on এর জন্য কী দরকার?","options":["শুধু forward voltage","Gate pulse + forward bias","Reverse voltage","কোনো signal ছাড়া"],"answer":1,"explanation":"SCR: forward biased + gate trigger pulse"},
     {"q":"Buck (step-down) chopper এ Vout = ?","options":["Vin/D","D×Vin","Vin/(1-D)","(1-D)×Vin"],"answer":1,"explanation":"Buck: Vout = D×Vin (D = duty cycle)"},
     {"q":"Boost (step-up) chopper এ Vout = ?","options":["D×Vin","Vin/(1-D)","(1-D)×Vin","Vin×(1+D)"],"answer":1,"explanation":"Boost: Vout = Vin/(1-D)"},
     {"q":"PWM inverter এ output frequency নির্ধারণ করে?","options":["DC input voltage","Switching frequency","Modulation index","Load resistance"],"answer":1,"explanation":"Output frequency = reference signal frequency"},
     {"q":"Single phase full bridge inverter এ কতটি switch?","options":["2","4","6","8"],"answer":1,"explanation":"Full bridge: 4 switches (IGBT/MOSFET)"},
   ],
   "math":{"q":"Boost converter: Vin=12V, D=0.6, RL=20Ω। (a) Output voltage? (b) Output current? (c) Inductor current (average)?",
           "solution":"(a) Vout = Vin/(1-D) = 12/(1-0.6) = 12/0.4 = 30V\n(b) Iout = Vout/RL = 30/20 = 1.5A\n(c) Inductor avg current = Iout/(1-D) = 1.5/0.4 = 3.75A\n(Assuming 100% efficiency: Pin=Pout: Iin=Iout×Vout/Vin=3.75A ✓)"}},
]

# Add Communication topics
EEE_QUESTIONS["Part-5: Communication & Signals"] += [
  {"topic": "Fourier Transform & Spectral Analysis",
   "mcq": [
     {"q":"Fourier Transform এ time domain pulse এর frequency spectrum কেমন?","options":["Pulse","Sinc function","Gaussian","Delta function"],"answer":1,"explanation":"Rect pulse → Sinc function in frequency domain"},
     {"q":"Fourier Transform linearity: F{ax(t)+by(t)} = ?","options":["F{x}×F{y}","aF{x}+bF{y}","F{x+y}","a+b×F{x}"],"answer":1,"explanation":"Linearity: F{ax+by} = aX(f)+bY(f)"},
     {"q":"Time shifting property: F{x(t-t0)} = ?","options":["X(f)","e^(j2πft0)X(f)","e^(-j2πft0)X(f)","X(f-f0)"],"answer":2,"explanation":"Time shift: e^(-j2πft0)X(f)"},
     {"q":"Parseval's theorem মানে কী?","options":["Energy in time = Energy in frequency","Phase conservation","Amplitude conservation","Power equality"],"answer":0,"explanation":"Parseval's: ∫|x(t)|²dt = ∫|X(f)|²df (energy conservation)"},
     {"q":"Delta function δ(t) এর Fourier Transform?","options":["0","1","δ(f)","2πδ(ω)"],"answer":1,"explanation":"F{δ(t)} = 1 (all frequencies equally)"},
   ],
   "math":{"q":"x(t) = e^(-at)u(t), a>0। Fourier Transform ও magnitude spectrum বের করো।",
           "solution":"X(f) = ∫₀^∞ e^(-at)e^(-j2πft)dt\n= ∫₀^∞ e^(-(a+j2πf)t)dt\n= 1/(a+j2πf)\n\n|X(f)| = 1/√(a²+(2πf)²)\nAt f=0: |X(0)| = 1/a (maximum)\nHalf power frequency: f = a/2π"}},

  {"topic": "Discrete-Time Signals & Z-Transform",
   "mcq": [
     {"q":"Z-transform এ unit step u[n] এর Z-transform?","options":["z/(z-1)","1/(z-1)","z","1/z"],"answer":0,"explanation":"Z{u[n]} = z/(z-1), ROC: |z|>1"},
     {"q":"Z-transform delay: Z{x[n-k]} = ?","options":["z^k X(z)","z^(-k) X(z)","kX(z)","X(z)/k"],"answer":1,"explanation":"Z{x[n-k]} = z⁻ᵏ X(z)"},
     {"q":"DFT এ N-point transform এর complexity?","options":["O(N)","O(N²)","O(NlogN)","O(logN)"],"answer":1,"explanation":"DFT: O(N²), FFT reduces to O(NlogN)"},
     {"q":"Sampling theorem: fs ≥ ?","options":["fm","2fm","fm/2","4fm"],"answer":1,"explanation":"Nyquist: fs ≥ 2fm"},
     {"q":"Aliasing এ কী হয়?","options":["Better quality","High frequency signals appear as low frequency","Signal disappears","Bandwidth increases"],"answer":1,"explanation":"Aliasing: high freq signals fold back as low freq (undersampling)"},
   ],
   "math":{"q":"x[n] = (0.5)^n u[n]। Z-transform ও ROC বের করো। এবং inverse Z-transform confirm করো।",
           "solution":"X(z) = Σ(0.5)^n z^(-n) for n=0 to ∞\n= Σ(0.5z⁻¹)^n = 1/(1-0.5z⁻¹) = z/(z-0.5)\nROC: |z| > 0.5\n\nInverse: X(z) = z/(z-0.5)\nUsing table: (a)^n u[n] ↔ z/(z-a)\n∴ x[n] = (0.5)^n u[n] ✓"}},

  {"topic": "Digital Modulation",
   "mcq": [
     {"q":"BPSK এ কতটি phase state?","options":["1","2","4","8"],"answer":1,"explanation":"BPSK: Binary PSK, 2 phase states (0° ও 180°)"},
     {"q":"QPSK এ প্রতি symbol কতটি bit?","options":["1","2","3","4"],"answer":1,"explanation":"QPSK: 4 phase states → 2 bits/symbol"},
     {"q":"QAM এর সুবিধা?","options":["Simple","High spectral efficiency","Less power","No noise"],"answer":1,"explanation":"QAM: amplitude + phase modulation → high bits/symbol"},
     {"q":"BER কমাতে কী করতে হয়?","options":["SNR বাড়াও","Frequency কমাও","Bandwidth কমাও","Power কমাও"],"answer":0,"explanation":"Higher SNR → lower BER (better signal quality)"},
     {"q":"FSK এ কীভাবে data represent হয়?","options":["Amplitude পরিবর্তন","Phase পরিবর্তন","Frequency পরিবর্তন","Both A & P"],"answer":2,"explanation":"FSK: Frequency Shift Keying — different frequencies for 0 and 1"},
   ],
   "math":{"q":"QPSK system: bit rate=1Mbps। (a) Symbol rate? (b) Bandwidth (BW=symbol rate)? (c) 16-QAM হলে same bandwidth এ bit rate কত?",
           "solution":"(a) QPSK: 2 bits/symbol\nSymbol rate = Bit rate/2 = 1M/2 = 500k symbols/sec\n(b) BW = Symbol rate = 500kHz\n(c) 16-QAM: 4 bits/symbol\nBit rate = Symbol rate × 4 = 500k × 4 = 2Mbps\n(Double the bit rate with same bandwidth!)"}},

  {"topic": "Signal & System — Laplace, convolution",
   "mcq": [
     {"q":"LTI system এর output y(t) = ?","options":["x(t)+h(t)","x(t)×h(t)","x(t)*h(t) (convolution)","x(t)/h(t)"],"answer":2,"explanation":"y(t) = x(t)*h(t) (convolution of input and impulse response)"},
     {"q":"Causality condition: h(t) = 0 for?","options":["t > 0","t < 0","t = 0","All t"],"answer":1,"explanation":"Causal system: h(t)=0 for t<0"},
     {"q":"BIBO stability condition?","options":["∫|h(t)|dt = ∞","∫|h(t)|dt < ∞","h(t) = 0","h(t) = 1"],"answer":1,"explanation":"BIBO stable: ∫|h(t)|dt < ∞ (absolutely integrable)"},
     {"q":"Convolution এ Laplace domain এ?","options":["Addition","Subtraction","Multiplication","Division"],"answer":2,"explanation":"Convolution in time = Multiplication in Laplace (frequency) domain"},
     {"q":"Transfer function H(s) = ?","options":["Y(s)+X(s)","Y(s)/X(s)","X(s)/Y(s)","Y(s)-X(s)"],"answer":1,"explanation":"H(s) = Y(s)/X(s) = output/input in s-domain"},
   ],
   "math":{"q":"H(s) = 10/(s²+3s+2)। Poles, stability check ও unit step response steady-state value বের করো।",
           "solution":"Poles: s²+3s+2=0 → (s+1)(s+2)=0\nPoles: s=-1, s=-2 (both LHP → stable)\n\nUnit step: X(s) = 1/s\nY(s) = H(s)/s = 10/[s(s+1)(s+2)]\nFinal Value Theorem:\ny(∞) = lim(s→0) sY(s) = 10/[(0+1)(0+2)] = 10/2 = 5"}},

  {"topic": "Optical Fiber Communication",
   "mcq": [
     {"q":"Optical fiber এ total internal reflection হয় কখন?","options":["θ < θc","θ > θc","θ = 0","θ = 90°"],"answer":1,"explanation":"TIR: incident angle > critical angle θc"},
     {"q":"Single mode fiber ও multimode fiber এর পার্থক্য?","options":["Core size","Cladding","Coating","Length"],"answer":0,"explanation":"Single mode: small core (8-10μm), Multimode: large core (50-62.5μm)"},
     {"q":"Numerical Aperture (NA) = ?","options":["sin(θmax)","cos(θmax)","tan(θmax)","√(n1²-n2²)"],"answer":3,"explanation":"NA = √(n1²-n2²) = sin(θmax) — acceptance angle"},
     {"q":"Modal dispersion কোন fiber এ বেশি?","options":["Single mode","Graded index multimode","Step index multimode","All same"],"answer":2,"explanation":"Step index multimode: highest modal dispersion"},
     {"q":"Optical fiber এর wavelength window (telecom)?","options":["850nm","1310nm & 1550nm","500nm","2000nm"],"answer":1,"explanation":"Telecom: 1310nm & 1550nm (low loss windows)"},
   ],
   "math":{"q":"Optical fiber: n1(core)=1.48, n2(cladding)=1.46। Critical angle, NA ও acceptance angle বের করো।",
           "solution":"Critical angle: sinθc = n2/n1 = 1.46/1.48 = 0.9865\nθc = sin⁻¹(0.9865) = 80.6°\n\nNA = √(n1²-n2²) = √(1.48²-1.46²)\n= √(2.1904-2.1316) = √0.0588 = 0.2425\n\nAcceptance angle θmax = sin⁻¹(NA) = sin⁻¹(0.2425) = 14.03°"}},

  {"topic": "Networking & Computing",
   "mcq": [
     {"q":"OSI model এ কতটি layer?","options":["5","6","7","4"],"answer":2,"explanation":"7 layers: Physical, Data Link, Network, Transport, Session, Presentation, Application"},
     {"q":"TCP/IP model এ কতটি layer?","options":["4","5","7","3"],"answer":0,"explanation":"TCP/IP: 4 layers (Network Access, Internet, Transport, Application)"},
     {"q":"IP address (IPv4) কত bit?","options":["16","32","64","128"],"answer":1,"explanation":"IPv4: 32-bit address"},
     {"q":"Router কোন layer এ কাজ করে?","options":["Physical","Data Link","Network","Transport"],"answer":2,"explanation":"Router: Network layer (Layer 3), IP routing"},
     {"q":"DNS এর কাজ?","options":["Email send করা","Domain name → IP address","IP → MAC address","Data encrypt করা"],"answer":1,"explanation":"DNS: Domain Name System, hostname to IP resolution"},
   ],
   "math":{"q":"IP address: 192.168.1.0/24 network। (a) Subnet mask? (b) Host range? (c) কতটি usable host? (d) Broadcast address?",
           "solution":"(a) /24 → Subnet mask: 255.255.255.0\n(b) Host range: 192.168.1.1 to 192.168.1.254\n(c) Usable hosts: 2^8 - 2 = 254 (network ও broadcast বাদ)\n(d) Broadcast: 192.168.1.255"}},
]
