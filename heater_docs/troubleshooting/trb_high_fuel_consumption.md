---
doc_id: trb_high_fuel_consumption
doc_type: troubleshooting
equipment: [heater_h101, fuel_gas_system, convection_section, radiant_section, radiant_coil, flue_gas_analyzers, burners, air_preheater, fd_fan, id_fan, bypass_dampers, stack]
tags: [FT-1201, AT-1203, TT-1204, FY-1100, TT-1100, TIC-1110, TT-1303, TIC-1345, TT-1343, AIC-1321, AT-1322, AT-1327, AT-1326, FIC-1341, PIC-1311, PDT-1347, SI-1351, JI-1341, JI-1351, ZT-1361, TT-1301A, TT-1301B, HS-1501, PDI-1101, TI-1121A]
title: Troubleshooting Guide — High Fuel Consumption / Low Efficiency
revision: 2.1
date: 2026-11-20
---

# Troubleshooting Guide — High Fuel Consumption / Low Efficiency

**Document No.:** H101-TRB-004
**Symptom:** Fuel per unit duty more than 3% above the clean baseline for the current crude, calculated efficiency below about 89% LHV, or fuel gas flow FT-1201 approaching its 3,430 kg/h Hi alarm (≈ 120% of normal heat release, ≈ 46 MW LHV)
**Revision:** 2.1 | **Date:** 2026-11-20
**Applicability:** Unit 100 — H-101 Crude Charge Heater
**Owner:** Fired Equipment Engineering / Energy Coordinator, Unit 100
**P&ID reference:** U100-PID-102 (fuel gas, burners, analyzers), U100-PID-103 (air preheater, FD/ID fans, dampers, stack)

**Revision note:** Rev 2.1 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).

> **NOTE:** Rising fuel flow is a **symptom**, not a diagnosis. Fuel rises when the heater needs more duty (more charge, a different crude, colder inlet) and when the heater wastes more heat (convection or air preheater fouling, excess air, air ingress, a passing bypass damper, coke). Only the second group is an efficiency loss. Always normalise before diagnosing. Fan power (JI-1341 + JI-1351) is part of the energy cost of H-101 and should be tracked alongside fuel.

---

## 1. Immediate Actions

1. **Compute fuel per unit duty, not fuel flow.** Fired duty = FT-1201 × AT-1203 (kg/h × MJ/kg ÷ 3,600 = MW). Absorbed duty is calculated from FY-1100 and the enthalpy rise from TT-1100 to TIC-1110 for the current crude. Efficiency = absorbed ÷ fired; design ≈ 91% LHV (38.5 MW fired, 2,860 kg/h, for 35.0 MW absorbed on ANS at 286 t/h).
2. **Check firing limits:** fired duty ≤ 46 MW LHV (120% of normal), skin TMTs below the 585 °C Hi alarm, bridgewall TT-1301A/B 760–900 °C, FD and ID fan speeds below 95%.
3. **Check the draft mode.** If the bypass damper D-101 position ZT-1361 or the emergency air doors ZT-1362 show more than 5% open, the heater is partly or fully on the natural-draft path and low efficiency is expected; see SOP — FD / ID Fan Trip Response and Natural-Draft Operation, Rev 1.0.
4. **Rule out a demand change:** FY-1100 up, TT-1100 down, a crude switch or a COT setpoint change all raise fuel without any loss of efficiency. A heavier crude does not automatically need more duty — confirm with the model for the new assay. COT is a given production target; any firing reduction that pulls COT below target reduces flash-zone vaporization in C-101 and shifts distillate into residue, so coordinate with the C-101 / unit operator.
5. If efficiency really has fallen, work through Section 2. Do not lower the AIC-1321 O2 setpoint to "save fuel" until tramp air and analyzer bias have been ruled out — doing so can starve the burners.

---

## 2. Probable Causes

### 2.1 Convection Fouling

**Description:** Soot on the studded convection tubes reduces heat recovery into the crude; hotter gas reaches the air preheater E-102.
**Diagnosis:** TT-1303 (convection outlet / APH gas inlet) above its ≈ 390 °C baseline and **drops after soot blowing** (HS-1501). TMTs normal. The APH recovers part of the extra heat, so TIC-1345 rises by less than TT-1303. Roughly 1 efficiency point per 20 °C rise of the final stack temperature.
**Action:** Soot blow per Maintenance Procedure — Convection Section Soot Blowing, Rev 1.9. See Troubleshooting Guide — High Stack Temperature, Rev 1.7.

### 2.2 Air Preheater Fouling or Seal Leakage

**Description:** Fouled APH baskets recover less heat; worn seals short-circuit cold air to the gas side, which costs fan power and dilutes the outlet gas.
**Diagnosis:** *Fouling:* PDT-1347 above its ≈ 80 mmH₂O baseline, hot air TT-1343 below ≈ 300 °C, TIC-1345 up, SI-1351 / JI-1351 up. *Seal leakage:* AT-1326 − AT-1327 above ≈ 2.0 points (≈ 1.2 normal), FIC-1341 up for the same firing, SI-1341 and SI-1351 up, TIC-1345 **lower** by dilution — the fuel penalty is small but the fan power penalty is real.
**Action:** Per Troubleshooting Guide — Air Preheater Leakage, Fouling and Low Cold-End Temperature, Rev 1.0.

### 2.3 Tramp Air Below the Arch (Firebox Air Ingress)

**Description:** Air leaking through peephole doors, burner windbox joints, tube penetrations or casing cracks enters the firebox after the burners. It leaves heated (a pure loss), but AIC-1321 at the arch counts it as excess O2. The controller then trims FIC-1341 down to hold setpoint, so the burners get **less** air than AIC-1321 indicates.
**Diagnosis:** Fuel per unit duty up; AIC-1321 at setpoint while the air/fuel ratio FIC-1341 / FT-1201 falls below its ≈ 20.2 kg/kg baseline; CO (AT-1322) may appear at a "normal" O2 reading; flames longer or lazier. Leakage rises with draft (∝ √draft), so it is larger when PIC-1311 runs more negative.
**Action:** Tramp air survey and sealing per Maintenance Procedure — Tramp Air Survey and Casing Sealing, Rev 1.5. Keep arch draft at −2.5 mmH₂O. Confirm with SOP — Excess O2 Step Test (Analyzer / Air-Ingress Check), Rev 1.3.

### 2.4 Air Ingress in the Convection Section

**Description:** Leaks at header boxes, soot blower wall boxes or access doors admit air above the radiant section and ahead of the APH.
**Diagnosis:** AT-1327 − AIC-1321 above ≈ 0.8 points (≈ 0.2 normal); TT-1303 **lower** than expected (dilution can mask fouling); ID fan SI-1351 higher for the same firing. Fuel penalty is smaller than for firebox ingress.
**Action:** Locate and seal leaks (same procedure as 2.3).

### 2.5 Bypass Damper D-101 Passing

**Description:** If XV-1361 is partly open or its blade seals leak, ≈ 390 °C gas goes straight to S-101, bypassing E-102.
**Diagnosis:** ZT-1361 above 5% (or reading closed with a known seal defect); TT-1343 lower and fuel per duty up; TIC-1345 may look normal or even low because less gas passes through the APH — a normal TIC-1345 is not proof of a normal stack loss.
**Action:** Confirm the damper closed from the field; repair seals at the next opportunity.

### 2.6 Excess O2 Too High or Analyzer Reading Low

**Description:** AIC-1321 left above the 3.0% design, or an analyzer reading **lower** than true, makes the controller add air.
**Diagnosis:** Setpoint check; FIC-1341 / FT-1201 above baseline; portable analyzer at the arch reads higher than AIC-1321; the fuel/air balance (FT-1201, AT-1203, FIC-1341 less estimated APH leakage) gives a higher burner O2 than AIC-1321. A low-reading AIC-1321 also widens AT-1327 − AIC-1321, mimicking convection ingress, but TT-1303 is not lower.
**Action:** Restore setpoint to 3.0%. Validate per Maintenance Procedure — O2 and CO Analyzer Calibration and Validation, Rev 2.2.

### 2.7 Coke in the Radiant Coil

**Description:** Coke adds resistance in a pass; that pass absorbs a little less and TIC-1110 fires harder to hold COT.
**Diagnosis:** Slow rise in fuel per duty with TMTs **and** PDI-1101..PDI-1104 rising in the same pass; that pass outlet slightly cooler than the others.
**Action:** Decoke planning per Troubleshooting Guide — High Tube Metal Temperature, Rev 2.4.

### 2.8 Fuel Measurement or Heating Value Error

**Diagnosis:** Apparent efficiency steps with a fuel gas header change; TT-1301A/B, TT-1303 and AIC-1321 unchanged; AT-1203 outside 44–52 MJ/kg or flat-lined; TT-1204 changed (density compensation).
**Action:** Check AT-1203 calibration and FT-1201 compensation; take a lab sample.

---

## 3. Distinguishing Cause from Symptom

| What you see | What it means | How to confirm |
|---|---|---|
| Fuel up, fuel per duty unchanged | Higher demand, not a loss | FY-1100, TT-1100, crude, COT |
| TT-1303 up, recovers on soot blow, TMTs normal | Convection fouling | HS-1501 vs TT-1303 |
| PDT-1347 up, TT-1343 down, TIC-1345 up | APH fouling | APH guide, soot blow SB-102A/B response |
| AT-1326 − AT-1327 > 2.0, FIC-1341 and SI-1351 up, TIC-1345 down | APH seal leakage | APH guide |
| AIC-1321 normal, FIC-1341 / FT-1201 low, CO at normal O2, fuel per duty up | Tramp air below arch | O2 step test; leak survey |
| AT-1327 − AIC-1321 > 0.8, TT-1303 low | Convection air ingress | Leak survey |
| ZT-1361 open or TT-1343 low with TIC-1345 not high | Bypass damper passing | Field check of D-101 |
| Fuel per duty up, FIC-1341 high, portable O2 above AIC-1321 | Analyzer low / excess air | Analyzer validation |
| Fuel per duty up slowly with TMT and ΔP up in one pass | Coke | TMT vs PDI per pass |

An analyzer reading **high** on its own lowers total air and does not raise fuel per duty; rising fuel per duty at a "normal" O2 favours tramp air. At a constant O2 setpoint the two still look similar; an O2 step test (± 0.5% for about 2 h each) separates them, per SOP — Excess O2 Step Test (Analyzer / Air-Ingress Check), Rev 1.3.

---

## 4. Prevention / Follow-up

- Calculate efficiency, fuel per unit duty and fan power (JI-1341 + JI-1351) every shift; trend against the clean baseline for each crude.
- Trend the two O2 differences (AT-1327 − AIC-1321, AT-1326 − AT-1327), PDT-1347 and the air/fuel ratio FIC-1341 / FT-1201.
- Daily convection and APH soot blowing; quarterly tramp air survey; monthly analyzer validation against a portable instrument.
- Keep peephole doors closed, draft at −2.5 mmH₂O, and D-101 / D-102 proven closed in balanced-draft operation.
