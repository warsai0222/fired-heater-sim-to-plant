---
doc_id: trb_low_o2_high_co
doc_type: troubleshooting
equipment: [flue_gas_analyzers, burners, radiant_section, fuel_gas_system, fd_fan, id_fan, air_preheater, bypass_dampers, heater_h101]
tags: [AIC-1321, AT-1322, AT-1327, AT-1326, FIC-1341, SI-1341, PT-1342, PDT-1348, TT-1343, PIC-1311, PT-1312, SI-1351, FT-1201, AT-1203, PIC-1202, TIC-1110, TT-1301A, TT-1301B, TT-1302, TT-1303, XS-1341, ZT-1362, BS-1211, BS-1218, HS-1290]
title: Troubleshooting Guide — Low Excess O2 / High CO
revision: 2.5
date: 2026-11-20
---

# Troubleshooting Guide — Low Excess O2 / High CO

**Document No.:** H101-TRB-005
**Symptom:** Arch O2 AIC-1321 below 1.5% dry (Lo alarm) or 1.0% (LL alarm), and/or arch CO AT-1322 above 200 ppm (Hi) or 1000 ppm (HH)
**Revision:** 2.5 | **Date:** 2026-11-20
**Applicability:** Unit 100 — H-101 Crude Charge Heater
**Owner:** Unit 100 Operations / Fired Equipment Engineering
**P&ID reference:** U100-PID-102 (fuel gas, burners, analyzers), U100-PID-103 (FD/ID fans, air preheater, dampers)

**Revision note:** Rev 2.5 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).

> **SAFETY WARNING:** Low O2 and high CO are operator alarms, not SIS trips. High CO means unburned fuel is present in the firebox. **If the firebox is fuel-rich, do not add air quickly** — a sudden air increase can ignite accumulated combustibles (explosion / afterburning). Always cut fuel first, then restore air slowly.

---

## 1. Immediate Actions

**AIC-1321 < 1.5% with AT-1322 below 200 ppm:**
1. Check AIC-1321 is in AUTO and that FIC-1341 is following its setpoint. If FIC-1341 cannot reach setpoint with the FD fan SI-1341 near 95%, air supply is fan-limited.
2. Reduce firing slightly (lower TIC-1110 setpoint, or PIC-1202 in manual) until O2 recovers to the 3.0% design. COT below target reduces C-101 flash-zone vaporization; inform the C-101 / unit operator.

**AT-1322 > 1000 ppm, or AIC-1321 < 1.0%, or visible smoke / pulsation:**
1. **Reduce fuel first:** PIC-1202 in MANUAL, reduce fuel gas pressure in steps, staying above 0.35 barg (Lo alarm; PT-1206 trips main fuel below 0.25 barg). Air/fuel cross-limiting keeps air ahead of fuel on the way down.
2. Then raise FIC-1341 slowly in steps, watching AT-1322 fall and AIC-1321 rise.
3. Keep personnel away from peepholes and the burner floor. If draft goes positive or the box pulses, go to Troubleshooting Guide — Positive Draft and Afterburning, Rev 1.8.
4. If combustion cannot be stabilised, trip with HS-1290 per SOP — H-101 Emergency Shutdown and Trip Response, Rev 2.6.

---

## 2. Probable Causes

### 2.1 True Air Shortage (FD Fan, Air Path or Natural-Draft Operation)

**Description:** Not enough air reaches the burners: FD fan K-101 at its speed limit, the air side of E-102 restricted, a fan or APH-rotor trip with the heater on natural draft, or firing above what the air system can supply.
**Diagnosis:** FIC-1341 below its setpoint with SI-1341 near 95%; windbox PT-1342 below its ≈ +60 mmH₂O normal (Lo 20); PDT-1348 above ≈ 50 mmH₂O if the APH air side is plugged; AIC-1321, AT-1327 and AT-1326 all fall together (analyzers agree). On natural draft (XS-1341 = 0, ZT-1362 open) air capacity supports only ≈ 60% firing and the BMS runback clamps firing.
**Action:** Reduce firing to within air capacity; investigate the fan or APH per Equipment Datasheet — K-101 Forced Draft Fan and K-102 Induced Draft Fan, Rev 1.0 and SOP — FD / ID Fan Trip Response and Natural-Draft Operation, Rev 1.0.

### 2.2 Fuel Gas Composition Change (Higher Air Demand)

**Description:** Heavier or hydrogen-rich refinery fuel gas changes the air needed per kg of fuel. A rich gas swing outruns the O2 controller.
**Diagnosis:** AT-1203 moves (normal 48.5 MJ/kg, alarms 44 / 52); the O2 dip coincides with the change and the PIC-1202 response; AIC-1321, AT-1327 and AT-1326 drop together.
**Action:** Let AIC-1321 recover; if swings are frequent, raise the O2 setpoint temporarily within 2–4% and inform the fuel gas system operator.

### 2.3 Tramp Air Below the Arch (Burners Starved at "Normal" O2)

**Description:** Air leaking into the firebox after the burners is seen by AIC-1321 but does not reach the flames. The controller trims FIC-1341 down to hold setpoint, so true burner-level O2 is lower than indicated.
**Diagnosis:** **CO rises while AIC-1321 reads normal** (e.g. 3%); air/fuel ratio FIC-1341 / FT-1201 below its ≈ 20.2 kg/kg baseline; fuel per unit duty up; leakage increases when PIC-1311 runs more negative.
**Action:** Do not lower the O2 setpoint. Raise it temporarily to bring CO below 200 ppm, then arrange a leak survey per Maintenance Procedure — Tramp Air Survey and Casing Sealing, Rev 1.5.

### 2.4 O2 Analyzer Reading High (Bias)

**Description:** If AIC-1321 reads higher than true, the controller under-supplies air. The screen shows setpoint; the burners are short of air.
**Diagnosis:** CO rises at a "normal" AIC-1321 — **the same signature as 2.3**. Differences: a portable analyzer at the arch test port reads lower; the fuel/air balance (FT-1201, AT-1203, FIC-1341 less estimated APH leakage) gives a lower burner O2 than AIC-1321; AT-1327 − AIC-1321 shrinks below its ≈ 0.2 normal or goes negative; fuel per unit duty does **not** rise.
**Action:** Validate per Maintenance Procedure — O2 and CO Analyzer Calibration and Validation, Rev 2.2. At constant O2 setpoint, bias and air ingress are hard to tell apart; an O2 step test separates them, per SOP — Excess O2 Step Test (Analyzer / Air-Ingress Check), Rev 1.3.

### 2.5 Burner Fault (Poor Mixing)

**Description:** Plugged or eroded tips, damaged tiles or a misset air register on one of B-101A–H produce CO even at adequate overall O2.
**Diagnosis:** CO high, O2 normal or high, visibly long, smoky or detached flames on one or two burners; a flame scanner BS-1211..BS-1218 flickering.
**Action:** Correct per Maintenance Procedure — Burner Inspection, Cleaning and Tuning, Rev 2.0.

### 2.6 Analyzer Reading Low / CO Analyzer Fault

**Diagnosis:** AIC-1321 low but CO normal, flames normal, AT-1327 and AT-1326 normal, FIC-1341 rising without effect — the analyzer is reading low (AT-1327 − AIC-1321 widens). A CO spike with no change in O2, flames or temperatures suggests an AT-1322 fault.
**Action:** Validate the analyzer; place AIC-1321 in manual with FIC-1341 at the flow established before the fault.

---

## 3. Distinguishing Cause from Symptom

| What you see | What it means | How to confirm |
|---|---|---|
| All three O2 readings low, FIC-1341 below setpoint, SI-1341 high | True air shortage | SI-1341, PT-1342, PDT-1348, firing |
| O2 dip with AT-1203 change | Fuel composition swing | AT-1203 trend |
| CO up at normal AIC-1321, FIC-1341 / FT-1201 low, fuel per duty up | Tramp air below arch | O2 step test; leak survey |
| CO up at normal AIC-1321, portable O2 lower, AT-1327 − AIC-1321 shrunk | Analyzer reading high | Portable analyzer; fuel/air balance |
| CO up, O2 normal, one burner flame poor | Burner fault | Visual inspection |
| Low AIC-1321, normal CO, flames and AT-1327 | Analyzer reading low | Portable analyzer |

Low O2 and high CO are **symptoms**. The cause is whatever is making the burners short of air or mixing poorly. An analyzer reading high does not raise fuel per duty; tramp air does.

---

## 4. Prevention / Follow-up

- Never run the AIC-1321 setpoint below 2.0% while tramp air or analyzer bias is unresolved.
- Validate AIC-1321 monthly against a portable analyzer; trend AT-1327 − AIC-1321 and FIC-1341 / FT-1201 continuously.
- Treat any CO at a normal O2 reading as a prompt for an O2 step test.
- Keep FD fan speed margin below 95% at maximum firing; investigate rising SI-1341 at constant firing.
- CO compliance is covered in Environmental Procedure — Stack Emissions Monitoring (CO, NOx), Rev 1.4.
