---
doc_id: trb_positive_draft_afterburning
doc_type: troubleshooting
equipment: [id_fan, fd_fan, air_preheater, bypass_dampers, stack, radiant_section, convection_section, burners, flue_gas_analyzers, fuel_gas_system, bms_sis, heater_h101]
tags: [PIC-1311, PT-1312, PT-1313, PT-1314, PT-1352, SI-1351, JI-1351, XS-1351, SI-1341, XS-1341, FIC-1341, PT-1342, PDT-1347, ZT-1361, ZT-1362, XS-1349, AIC-1321, AT-1322, AT-1326, AT-1327, TT-1301A, TT-1301B, TT-1302, TT-1303, TIC-1345, FT-1201, AT-1203, PIC-1202, HS-1290]
title: Troubleshooting Guide — Positive Draft and Afterburning
revision: 1.8
date: 2026-11-20
---

# Troubleshooting Guide — Positive Draft and Afterburning

**Document No.:** H101-TRB-007
**Symptom:** Arch draft PIC-1311 above −0.5 mmH2O (Hi alarm) or at/above 0.0 mmH2O (HH alarm, positive pressure); firebox pressure approaching the PT-1314 trip (+10 mmH2O for 5 s); ID fan speed SI-1351 at its 95% capacity limit; or a sudden rise in TT-1302 / TT-1303 with high CO (afterburning)
**Revision:** 1.8 | **Date:** 2026-11-20
**Applicability:** Unit 100 — H-101 Crude Charge Heater
**Owner:** Unit 100 Operations / Fired Equipment Engineering
**P&ID reference:** U100-PID-102 (combustion, BMS), U100-PID-103 (ID/FD fans, air preheater, bypass damper, stack)

**Revision note:** Rev 1.8 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).

> **SAFETY WARNING:** H-101 is balanced draft: the FD fan K-101 pushes air in, the ID fan K-102 (PIC-1311 → SC-1351) pulls flue gas out and holds the arch at −2.5 mmH2O. Positive pressure pushes hot flue gas (≈ 845 °C, containing CO) out through peepholes, header boxes and casing gaps. PIC-1311 Hi/HH are operator alarms; **PT-1314 > +10 mmH2O for 5 s is a main fuel trip** per BMS / SIS Cause and Effect — H-101, Rev 3.3. Keep personnel away from the casing and peepholes while draft is positive. In a fuel-rich box, cut fuel before adding air.

---

## 1. Immediate Actions

1. **Clear personnel** from the burner floor, platforms and peephole doors.
2. **Check the ID fan.** XS-1351 running? SI-1351 following the PIC-1311 output, or at 95%? JI-1351 consistent with speed? If SI-1351 does not follow the controller output, suspect the SC-1351 VFD or its signal (it holds last speed on signal loss) — take PIC-1311 to MANUAL only if the drive responds locally, and call electrical.
3. **Check the bypass damper and air doors.** ZT-1361 (D-101) and ZT-1362 (D-102) must read closed (< 5%) in balanced draft.
4. **Check for afterburning:** AT-1322 CO above 1000 ppm, AIC-1321 falling, TT-1302 / TT-1303 rising quickly, draft pulsation. If present: **reduce fuel first** (PIC-1202 in MANUAL, reduce pressure, staying above the 0.35 barg Lo alarm), then raise air slowly via FIC-1341.
5. **If the ID fan is at 95% and draft is still positive, reduce firing** (lower TIC-1110 setpoint; the air/fuel cross-limit takes fuel down first and FD air follows, reducing gas volume). Inform the C-101 operator: a lower COT or charge reduces flash-zone vaporization and shifts yields. Act before PT-1314 trips.
6. If combustion is unstable or flames are seen outside the firebox, trip with HS-1290 per SOP — H-101 Emergency Shutdown and Trip Response, Rev 2.6.

---

## 2. Probable Causes

### 2.1 ID Fan at Capacity — Gas-Side Resistance or Volume Too High

**Description:** The ID fan must overcome firebox, convection, APH gas-side and duct losses (≈ −120 mmH2O at its inlet PT-1352) for the whole flue-gas plus leak-air volume. When resistance or volume grows, SI-1351 rises until it reaches the 95% limit, after which draft can no longer be held.

**Diagnosis:** SI-1351 and JI-1351 trending up over weeks at constant firing, then draft drifting positive at high firing. Identify which contributor grew:
- **APH fouling / plugging:** PDT-1347 above its ≈ 80 mmH2O normal (Hi 120), PT-1352 more negative, TIC-1345 up, hot air TT-1343 down.
- **APH seal leakage:** AT-1326 − AT-1327 above ≈ 2.0 (normal ≈ 1.2), TIC-1345 lower by dilution, FIC-1341 and SI-1341 up for the same burner air.
- **Convection air ingress:** AT-1327 − AIC-1321 above ≈ 0.8 (normal ≈ 0.2), TT-1303 lower.
- **Convection fouling:** PIC-1311 − PT-1313 difference growing; TT-1303 above ≈ 390 °C and dropping after soot blowing.
- **Firing / excess air:** FT-1201 × AT-1203 near 46 MW, or O2 setpoint raised (FIC-1341 and windbox PT-1342 high).

**Action:** Reduce firing to within ID capacity. Treat the contributor: Troubleshooting Guide — Air Preheater Leakage, Fouling and Low Cold-End Temperature, Rev 1.0; Maintenance Procedure — Convection Section Soot Blowing, Rev 1.9; Maintenance Procedure — Tramp Air Survey and Casing Sealing, Rev 1.5.

### 2.2 ID Fan Drive Fault or Trip

**Description:** SC-1351 holds last speed on signal loss, so after a signal fault the draft drifts as firing and air change. A VFD or motor trip stops the fan (XS-1351 = 0), which initiates the BMS natural-draft runback: XV-1361 bypass and XV-1362 air doors open, FD fan stopped, firing clamped to ≤ 60%. Until the bypass is open the box can puff positive.

**Diagnosis:** Signal fault: SI-1351 flat while the PIC-1311 output moves. Trip: XS-1351 = 0, JI-1351 to zero, PIC-1311 jumps toward positive, then recovers as ZT-1361 opens. If ZT-1361 does not open, pressure keeps rising and PT-1314 trips main fuel.

**Action:** Follow SOP — FD / ID Fan Trip Response and Natural-Draft Operation, Rev 1.0. Confirm ZT-1361 and ZT-1362 open and firing within the 60% clamp; COT cannot be held at full charge on natural draft, so charge is reduced in coordination with the C-101 operator.

### 2.3 Bypass Damper D-101 Mis-positioned

**Description:** In balanced draft XV-1361 must be closed. Partly open, it lets gas from the pressurized stack base (≈ +10 mmH2O after the ID fan) flow back to the convection outlet and round the APH/ID fan again, wasting ID capacity. On natural draft the reverse fault — damper failing to open — leaves the box with no outlet.

**Diagnosis:** ZT-1361 above 5% (open alarm) in balanced draft; SI-1351 and JI-1351 higher than normal for the firing with no change in PDT-1347 or the O2 differences. On natural draft: XS-1341 / XS-1351 = 0, ZT-1361 not open, PIC-1311 and PT-1314 rising.

**Action:** Field-check damper and actuator from a safe position; refer to Equipment Datasheet — S-101 Stack, D-101 Bypass Damper and D-102 Emergency Air Doors, Rev 1.3.

### 2.4 Afterburning (Combustibles Burning in the Convection Section)

**Description:** Fuel-rich firing (air shortage, fuel composition swing, burner fault) leaves CO and unburned fuel that ignite when they meet leaked air higher up, with draft swings and local overheating of convection tubes, supports and the APH hot end.

**Diagnosis:** AT-1322 CO very high; AIC-1321 low; TT-1302 and TT-1303 rise faster than bridgewall TT-1301A/B; draft pulsation; puffs at peepholes.

**Action:** Cut fuel, then restore air slowly. Diagnose per Troubleshooting Guide — Low Excess O2 / High CO, Rev 2.5. Combustibles reaching E-102 are an APH fire risk — watch TIC-1345 and TT-1343 for an unexplained rise.

### 2.5 Tube Leak

**Description:** Crude leaking into the firebox burns with extra flue volume and smoke.

**Diagnosis:** Draft toward positive with SI-1351 rising, O2 falling and CO rising while fuel gas flow is **unchanged**, bridgewall rising, black smoke at S-101.

**Action:** Emergency Response — Tube Rupture and Firebox Fire, Rev 2.3.

### 2.6 Draft Transmitter Fault

**Diagnosis:** PIC-1311 alone shows positive while PT-1312, PT-1313 and the independent SIS transmitter PT-1314 are normal, and SI-1351 has not changed. Check for plugged impulse lines (soot) before believing the reading. A PIC-1311 reading falsely **low** is worse: the ID fan slows and the true box goes positive — PT-1314 then disagrees with PIC-1311.

**Action:** Compare transmitters; blow down impulse lines; recalibrate.

---

## 3. Distinguishing Cause from Symptom

| What you see | What it means | How to confirm |
|---|---|---|
| SI-1351 at 95%, PDT-1347 up, TIC-1345 up, TT-1343 down | APH fouling limiting ID fan | Soot blow SB-102A/B response |
| SI-1351 up, AT-1326 − AT-1327 > ≈ 2.0, FIC-1341 up | APH seal leakage | O2 chain trend; fan powers |
| SI-1351 up, AT-1327 − AIC-1321 > ≈ 0.8, TT-1303 low | Convection ingress | Leak survey |
| PIC-1311 − PT-1313 growing, TT-1303 high, recovers on soot blow | Convection fouling | HS-1501 vs TT-1303 |
| SI-1351 flat while PIC-1311 output moves | SC-1351 signal / VFD fault | Local drive check |
| XS-1351 = 0, ZT-1361 opening | ID fan trip, runback | SOP — FD / ID Fan Trip Response and Natural-Draft Operation, Rev 1.0 |
| ZT-1361 > 5% in balanced draft, ID load high | Bypass damper passing | Field check |
| CO very high, TT-1302 / TT-1303 jumping, pulsation | Afterburning | AT-1322, AIC-1321 |
| Draft positive, O2 down, fuel unchanged, smoke | Tube leak | Visual from safe position |
| Only PIC-1311 abnormal | Transmitter / impulse line | PT-1312, PT-1313, PT-1314 |

Positive draft is a **symptom**; the causes are gas-side resistance, gas volume, ID fan capability, a damper fault or incomplete combustion.

---

## 4. Prevention / Follow-up

- Keep PIC-1311 in AUTO at −2.5 mmH2O. Trend SI-1351 and JI-1351 normalised to firing; a rising trend is the early warning of APH fouling, seal leakage or ingress.
- Trend PDT-1347, AT-1326 − AT-1327 and AT-1327 − AIC-1321 together with SI-1351.
- Run convection and APH soot blowing daily (HS-1501); stroke-check XV-1361 and XV-1362 each turnaround.
- Never correct a fuel-rich condition by adding air first.
