---
doc_id: trb_high_o2_reading
doc_type: troubleshooting
equipment: [flue_gas_analyzers, convection_section, radiant_section, burners, air_preheater, fd_fan, id_fan, bypass_dampers, heater_h101]
tags: [AIC-1321, AT-1327, AT-1326, AT-1322, FIC-1341, SI-1341, SI-1351, JI-1351, PIC-1311, PT-1312, PT-1313, TT-1303, TT-1302, TIC-1345, ZT-1362, FT-1201, AT-1203, BS-1211, BS-1218]
title: Troubleshooting Guide — High O2 Reading / Suspected Air Ingress
revision: 1.6
date: 2026-11-20
---

# Troubleshooting Guide — High O2 Reading / Suspected Air Ingress

**Document No.:** H101-TRB-006
**Symptom:** Arch O2 AIC-1321 above 5.0% dry (Hi alarm) or unable to come down to setpoint with FIC-1341 at its minimum; or AT-1327 − AIC-1321 above ≈ 0.8 points (normal ≈ 0.2); or AT-1326 − AT-1327 above ≈ 2.0 points (normal ≈ 1.2)
**Revision:** 1.6 | **Date:** 2026-11-20
**Applicability:** Unit 100 — H-101 Crude Charge Heater
**Owner:** Fired Equipment Engineering / Unit 100 Operations
**P&ID reference:** U100-PID-102 (burners, analyzers), U100-PID-103 (air preheater, FD/ID fans, dampers)

**Revision note:** Rev 1.6 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).

> **NOTE:** A high O2 reading is usually an efficiency problem, not an immediate hazard. The exception is a burner flame-out: an extinguished burner still passes air, so O2 rises. Check BS-1211..BS-1218 before anything else. H-101 has three O2 measurements in series — arch AIC-1321 (≈ 3.0%), APH gas inlet AT-1327 (≈ 3.2%), stack AT-1326 (≈ 4.4%) — and the step between each pair locates where air is entering.

---

## 1. Immediate Actions

1. **Check all eight flame scanners BS-1211..BS-1218.** One or two burners out raises O2. Do not relight from the hot firebox; follow BMS / SIS Cause and Effect — H-101, Rev 3.3.
2. **Check the air loop.** If AIC-1321 is in AUTO and FIC-1341 is at its minimum (Lo 45,000 kg/h) or held up by the air/fuel cross-limit while O2 stays high, the air is not coming through the burners — suspect leakage, low firing or an open D-102 emergency air door (ZT-1362 above 5%).
3. **Check the draft.** If PIC-1311 is more negative than its −2.5 mmH₂O setpoint (ID fan in manual or SC-1351 held high), restore setpoint; leakage rises with draft.
4. **Locate the step.** Compare AIC-1321, AT-1327 and AT-1326: a large AT-1327 − AIC-1321 points to the convection section; a large AT-1326 − AT-1327 points to the air preheater seals.
5. Keep peephole and access doors closed; check none was left open after rounds.

---

## 2. Probable Causes

### 2.1 Air Ingress in the Convection Section

**Description:** Leaks at header box covers, soot blower wall sleeves (SB-101A..F), access doors or casing seams admit cold air above the radiant section. AIC-1321 at the arch does not see it; AT-1327 at the APH gas inlet does.
**Diagnosis:** AT-1327 − AIC-1321 above ≈ 0.8 points and growing; TT-1303 **lower** than expected for the firing (dilution); ID fan SI-1351 / JI-1351 up to move the extra gas at the same arch draft. AIC-1321 and AT-1326 − AT-1327 normal.
**Action:** Locate leaks per Maintenance Procedure — Tramp Air Survey and Casing Sealing, Rev 1.5. Check soot blower sleeves after each sequence.

### 2.2 Air Preheater Seal Leakage

**Description:** Worn radial, axial or circumferential seals on E-102 let FD-fan air short-circuit to the gas side. It never reaches the burners.
**Diagnosis:** AT-1326 − AT-1327 above ≈ 2.0 points; FIC-1341 up for the same firing (ratio FIC-1341 / FT-1201 above ≈ 20.2 kg/kg); SI-1341 and SI-1351 up; TIC-1345 lower by dilution. AIC-1321 and AT-1327 normal.
**Action:** Per Troubleshooting Guide — Air Preheater Leakage, Fouling and Low Cold-End Temperature, Rev 1.0.

### 2.3 Tramp Air Below the Arch

**Description:** Air entering the firebox through peepholes, windbox joints, tube penetrations or floor seals. AIC-1321 sees it; the burners do not. Leakage rises roughly with the square root of draft.
**Diagnosis:** In AUTO, AIC-1321 is held at setpoint by trimming FIC-1341 down (air/fuel ratio falling over weeks at constant firing); fuel per unit duty rises; CO (AT-1322) can appear at a "normal" O2. Only when leakage exceeds what the air loop can take out does AIC-1321 read above setpoint. AT-1327 − AIC-1321 stays near normal.
**Action:** Leak survey and sealing. Do not lower the O2 setpoint to compensate; the burners already have less air than indicated.

### 2.4 O2 Analyzer Reading High, or Sample System Leak

**Description:** The arch analyzer is extractive. A leak in the probe, filter or sample line draws in ambient air; calibration drift does the same.
**Diagnosis:** AIC-1321 high or drifting while AT-1327 and AT-1326 do not move with it (AT-1327 − AIC-1321 shrinks or goes negative); portable analyzer at the arch test port reads lower; the fuel/air balance (FT-1201, AT-1203, FIC-1341 less estimated APH leakage) gives a lower burner O2 than displayed. Fuel per unit duty does not rise. In AUTO the controller **removes** air, so CO may rise.
**Action:** Validate per Maintenance Procedure — O2 and CO Analyzer Calibration and Validation, Rev 2.2. Leak-check the sample system.

### 2.5 Low Firing / Turndown

**Description:** At low firing the FD fan and air/fuel cross-limit hold a minimum air flow, and casing leakage becomes a larger share of the total.
**Diagnosis:** FT-1201 well below the 2,860 kg/h normal; FIC-1341 at its minimum; O2 falls back as firing rises.
**Action:** Accept higher O2 at turndown; raise PIC-1311 toward −1.5 mmH₂O only if the floor draft PT-1312 remains negative.

### 2.6 Excessive Draft or Emergency Air Door Open

**Description:** A draft more negative than design pulls in more leakage everywhere; an open D-102 door admits ambient air directly to the windbox.
**Diagnosis:** PIC-1311 below −2.5 mmH₂O, SI-1351 higher than usual, PT-1312 more negative than −10 mmH₂O; or ZT-1362 above 5%.
**Action:** Restore PIC-1311 to AUTO at −2.5 mmH₂O; confirm XV-1362 closed from the field.

---

## 3. Distinguishing Cause from Symptom

| What you see | What it means | How to confirm |
|---|---|---|
| O2 jump, one scanner BS-121x lost | Burner out | Scanner status, visual |
| AT-1327 − AIC-1321 > 0.8, TT-1303 low, SI-1351 up | Convection air ingress | Leak survey (smoke / IR camera) |
| AT-1326 − AT-1327 > 2.0, FIC-1341 up, TIC-1345 down | APH seal leakage | APH guide |
| FIC-1341 trimmed down over weeks, fuel per duty up, CO at normal O2 | Tramp air below arch | O2 step test, leak survey |
| AIC-1321 high, AT-1327 not following, portable O2 lower | Analyzer high / sample leak | Portable analyzer, calibration |
| High O2 only at low firing | Turndown | FT-1201 |
| Draft more negative than −2.5, or ZT-1362 open | Excessive draft / air door | PIC-1311, ZT-1362 |

An AIC-1321 that reads **low** widens AT-1327 − AIC-1321 and can mimic convection ingress; it is distinguished because TT-1303 is not lower and the portable analyzer and fuel/air balance disagree with AIC-1321. At constant O2 setpoint, analyzer bias and air ingress below the arch look very similar. The decisive test is an O2 step test (± 0.5% for about 2 h each), per SOP — Excess O2 Step Test (Analyzer / Air-Ingress Check), Rev 1.3: a bias appears as a constant offset against the portable analyzer and the fuel/air balance at every step, while tramp air appears as CO breaking through at a higher-than-expected AIC-1321 as burner air is reduced, and responds to a change in draft.

---

## 4. Prevention / Follow-up

- Trend AT-1327 − AIC-1321, AT-1326 − AT-1327 and FIC-1341 / FT-1201 at normalised firing; all three are early leakage indicators.
- Quarterly tramp air survey; reseal peephole doors and windbox joints after every burner job.
- Monthly portable-analyzer validation of AIC-1321 and AT-1327.
- Hold arch draft at −2.5 mmH₂O; more draft is not "safer", it pulls in more air and costs ID fan power.
