---
doc_id: trb_high_stack_temperature
doc_type: troubleshooting
equipment: [convection_section, air_preheater, stack, soot_blowers, bypass_dampers, radiant_section, flue_gas_analyzers, heater_h101]
tags: [TT-1303, TIC-1345, TT-1343, PDT-1347, TT-1302, TT-1301A, TT-1301B, TT-1131, TT-1132, TT-1133, TT-1134, TT-1100, TT-1001, HS-1501, FT-1201, AT-1203, AIC-1321, AT-1322, AT-1327, AT-1326, PT-1313, PIC-1311, SI-1351, ZT-1361, XS-1349, TI-1121A, TI-1124B]
title: Troubleshooting Guide — High Stack Temperature
revision: 1.7
date: 2026-11-20
---

# Troubleshooting Guide — High Stack Temperature

**Document No.:** H101-TRB-003
**Symptom:** APH gas outlet TIC-1345 more than 20 °C above its ≈ 150 °C clean baseline at the same firing; or convection outlet / APH gas inlet TT-1303 above 440 °C (Hi alarm) or more than 20 °C above its ≈ 390 °C baseline
**Revision:** 1.7 | **Date:** 2026-11-20
**Applicability:** Unit 100 — H-101 Crude Charge Heater
**Owner:** Fired Equipment Engineering / Unit 100 Operations
**P&ID reference:** U100-PID-102 (flue gas path, soot blowers), U100-PID-103 (air preheater, ID fan, bypass damper, stack)

**Revision note:** Rev 1.7 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).

> **NOTE:** In balanced-draft operation flue gas leaves the convection section at ≈ 390 °C (TT-1303), is cooled to ≈ 150 °C in the air preheater E-102 (TIC-1345) and leaves S-101 at ≈ 150–155 °C after the ID fan; this corresponds to ≈ 91% LHV efficiency. Each 20 °C rise of the final stack temperature costs roughly 1 efficiency point. TT-1303 and TIC-1345 tell different stories: TT-1303 reflects the convection section, TIC-1345 the air preheater. On the natural-draft path (D-101 open) the stack runs at ≈ 400 °C by design. A sudden jump in TT-1302 / TT-1303 with high CO may be afterburning — a safety issue, not an efficiency issue.

---

## 1. Immediate Actions

1. **Check for afterburning first.** If TT-1302 or TT-1303 rose quickly (minutes) with AT-1322 above 200 ppm or AIC-1321 low, go to Troubleshooting Guide — Positive Draft and Afterburning, Rev 1.8.
2. **Check the draft mode.** If ZT-1361 shows D-101 more than 5% open, or the APH rotor monitor XS-1349 has dropped out, high stack temperature is expected; see SOP — FD / ID Fan Trip Response and Natural-Draft Operation, Rev 1.0.
3. **Check the cold-end control.** TV-1345 (cold-air bypass) opens deliberately in cold weather (low TT-1001) or at low load to hold TIC-1345 above 145 °C; a higher TIC-1345 in those conditions is not a fault.
4. **Check firing and charge.** If FT-1201 × AT-1203 and TT-1301A/B rose with TT-1303, flue temperatures are following firing (more duty demand).
5. **Check when soot blowing last ran** (HS-1501, convection SB-101A..F and APH SB-102A/B). If more than 24 h ago, run a sequence per Maintenance Procedure — Convection Section Soot Blowing, Rev 1.9 and watch TT-1303, PDT-1347 and TIC-1345 for 1–2 h.

---

## 2. Probable Causes

### 2.1 Convection Section Fouling

**Description:** Deposits on the studded convection tubes reduce heat recovery into the crude; hotter gas reaches the APH, and the radiant section must pick up the lost convection duty, so firing rises to hold COT.
**Diagnosis:** TT-1303 drifts up over days at constant firing and **drops after each convection soot-blow sequence**. TMTs TI-1121A..TI-1124B and coil ΔP normal. Crossover TT-1131..TT-1134 slightly **lower**. TIC-1345 rises by less than TT-1303 because the APH recovers part of it. PT-1313 more negative relative to PIC-1311 (higher convection draft loss) and SI-1351 up.
**Action:** Soot blow. If TT-1303 does not recover to within 10 °C of baseline after two sequences, check SB-101A..F for failed retraction or low steam pressure and plan a convection wash.

### 2.2 Air Preheater Fouling

**Description:** Deposits in the E-102 baskets (soot, or sticky acid-wetted deposits and corrosion products at the cold end) reduce heat transfer and raise gas-side resistance.
**Diagnosis:** TIC-1345 up while TT-1303 is normal; PDT-1347 above ≈ 80 mmH₂O (Hi 120); hot air TT-1343 below ≈ 300 °C; ID fan load SI-1351 up; partial recovery after APH soot blowing (SB-102A/B).
**Action:** Per Troubleshooting Guide — Air Preheater Leakage, Fouling and Low Cold-End Temperature, Rev 1.0.

### 2.3 Higher Firing / Higher Duty Demand

**Description:** More crude, a lower inlet temperature, or a crude needing more duty raises firing; all flue temperatures rise together.
**Diagnosis:** TT-1301A/B, TT-1302, TT-1303 and TIC-1345 all up in proportion with FT-1201; FY-1100 up, TT-1100 down or a crude switch. No lasting response to soot blowing. A heavier crude does not automatically need more duty — confirm with the model.
**Action:** No flue-side fault. If firing is high because of efficiency loss, see Troubleshooting Guide — High Fuel Consumption / Low Efficiency, Rev 2.1. If firing is reduced, COT may fall below target, reducing C-101 flash-zone vaporization and distillate yield — coordinate with the C-101 / unit operator.

### 2.4 Higher Crude Inlet Temperature

**Diagnosis:** TT-1100 above its 250 °C normal, FT-1201 **down**, TT-1303 and crossover TT-1131..TT-1134 up; TIC-1345 up only slightly.
**Action:** None; overall unit energy use has improved. Re-baseline TT-1303 for the new inlet temperature.

### 2.5 Bypass Damper D-101 Passing

**Description:** Gas leaking through XV-1361 reaches S-101 at ≈ 390 °C without passing E-102.
**Diagnosis:** ZT-1361 above 5%, or a stack temperature higher than TIC-1345 would explain; TT-1343 lower; TIC-1345 normal or low (less gas through the APH). A normal TIC-1345 is not proof of normal stack loss.
**Action:** Field-check D-101 closed; repair seals at the next opportunity.

### 2.6 Afterburning in the Convection Section

**Diagnosis:** Fast rise of TT-1302 / TT-1303 while TT-1301A/B rises less; AT-1322 high; AIC-1321 low or at setpoint; draft pulsation on PIC-1311.
**Action:** Cut fuel first, then restore air slowly, per Troubleshooting Guide — Positive Draft and Afterburning, Rev 1.8.

### 2.7 Thermocouple Fault or Flue Bypassing

**Diagnosis:** TT-1303 changes with no matching change in TT-1302, crossover temperatures, TIC-1345 or firing (TC fault); TT-1303 high and never responding to soot blowing after a turnaround (missing corbels / baffles).
**Action:** Check with a portable probe; bypassing needs inspection at shutdown.

---

## 3. Distinguishing Cause from Symptom

| What you see | What it means | How to confirm |
|---|---|---|
| TT-1303 up, falls after convection soot blow, TMTs normal | Convection fouling | HS-1501 log vs TT-1303 |
| TIC-1345 up, TT-1303 normal, PDT-1347 up, TT-1343 down | APH fouling | APH soot blow response |
| TIC-1345 **low**, AT-1326 − AT-1327 > 2.0 | APH seal leakage (dilution) masking performance | APH guide |
| All flue temperatures up with FT-1201 | Higher duty / firing | FY-1100, TT-1100, crude |
| TT-1303 up, FT-1201 down, TT-1100 up | Hotter crude from preheat | TT-1100 trend |
| TIC-1345 up in cold weather / low load | TV-1345 opening as designed | TT-1001, firing |
| Stack hot, TIC-1345 normal, ZT-1361 open | D-101 passing | Field check |
| TT-1303 jumps, CO high | Afterburning | AT-1322, AIC-1321, draft |
| TT-1303 lower than expected, AT-1327 − AIC-1321 > 0.8 | Convection air ingress masking fouling | O2 difference trend |

Dilution hides problems: convection air ingress cools TT-1303 and APH seal leakage cools TIC-1345, so a "normal" temperature with a widened O2 difference is not proof of clean surfaces.

---

## 4. Prevention / Follow-up

- Run convection and APH soot blowing daily (HS-1501) and log TT-1303, TIC-1345 and PDT-1347 before and 1 h after each sequence; a shrinking recovery means deposits are hardening.
- Track TT-1303 and TIC-1345 normalised to firing, TT-1100 and TT-1001; investigate a 20 °C rise from baseline.
- Monitor both O2 differences (AT-1327 − AIC-1321, AT-1326 − AT-1327) alongside the flue temperatures.
- Never lower TIC-1345 below 140 °C to gain efficiency; that is the acid dew point margin.
