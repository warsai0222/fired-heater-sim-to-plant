---
doc_id: sop_o2_step_test
doc_type: sop
equipment: [heater_h101, radiant_section, convection_section, burners, flue_gas_analyzers, fuel_gas_system, air_preheater, fd_fan, id_fan]
tags: [AIC-1321, AT-1322, AT-1327, AT-1326, FIC-1341, FT-1201, AT-1203, TT-1303, TT-1343, TIC-1345, PIC-1311, SI-1341, SI-1351, JI-1341, JI-1351, PT-1342, TIC-1110, FY-1100, TT-1100, TT-1301A, TT-1301B, TI-1121A, TI-1122A, TI-1123A, TI-1124A, HS-1501]
title: SOP — Excess O2 Step Test (Analyzer / Air-Ingress Check)
revision: 1.3
date: 2026-11-20
---

# SOP — Excess O2 Step Test (Analyzer / Air-Ingress Check)

**Document No.:** H101-SOP-006
**Revision:** 1.3 | **Date:** 2026-11-20
**Revision note:** Rev 1.3 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).
**Applicability:** Unit 100 — H-101 Crude Charge Heater
**Owner:** Process Engineering (Fired Heaters) with Unit 100 Operations
**P&ID Reference:** U100-PID-102 (combustion, fuel gas, burners, BMS), U100-PID-103 (air preheater, fans)

---

## 1. Purpose — Why This Test Exists

AIC-1321 holds arch O2 at 3.0% dry by resetting the combustion air flow setpoint FIC-1341, which moves the FD fan speed SC-1341. When AIC-1321 is steady at 3.0%, the console cannot tell apart four different problems:

- **Arch analyzer bias.** If AIC-1321 reads high, the burners really get less air than shown (CO and flame risk); if it reads low, the heater burns with too much air and wastes fuel.
- **Tramp air below the arch.** Cold air through peepholes, burner fronts or tube penetrations is counted by AIC-1321 but never went through the burners, so the burners run leaner in air than 3.0% suggests.
- **Convection-section ingress.** Air leaking in above the arch analyzer raises AT-1327 (APH gas inlet O2) above AIC-1321.
- **APH seal leakage.** FD air leaking across the rotor seals to the gas side raises AT-1326 (stack O2) above AT-1327, loads the ID fan and reduces hot air to the burners for the same FD flow.

The test moves the O2 setpoint up and down on purpose and watches **air flow**, **fuel**, **CO**, the **O2 chain** (AIC-1321 → AT-1327 → AT-1326) and an **independent portable analyzer**. Use it when Troubleshooting Guide — High O2 Reading / Suspected Air Ingress, Rev 1.6, Troubleshooting Guide — High Fuel Consumption / Low Efficiency, Rev 2.1 or Troubleshooting Guide — Air Preheater Leakage, Fouling and Low Cold-End Temperature, Rev 1.0 points here.

## 2. Preconditions (H-101 must be steady)

| Condition | Requirement |
|---|---|
| Charge FY-1100 | Constant ± 1% for 2 h before and during the test |
| COT TIC-1110 | In CASCADE, 360 ± 1 °C |
| Inlet temperature TT-1100 | Constant ± 2 °C |
| Fuel heating value AT-1203 | No step > 0.5 MJ/kg in the last 2 h |
| Crude | No crude switch in the last 12 h (Per SOP — Crude Switch / Crude Blend Change at H-101, Rev 1.8) |
| Soot blowing | No HS-1501 sequence (convection or APH) during or 2 h before the test |
| Draft | PIC-1311 in AUTO at −2.5 mmH2O and **not changed** during the test (leakage ∝ √draft) |
| Fans | SI-1341 and SI-1351 ≤ 88% at base, so the step up has headroom to 95% |
| Cold end | TIC-1345 ≥ 148 °C with TV-1345 closed |
| Margins | TI-1121A..1124B < 570 °C; TT-1301A/B 760–900 °C; AT-1322 < 50 ppm |

Obtain shift superintendent agreement and inform the C-101 column operator (COT is held, so no column effect is expected). The test takes about 7 hours.

## 3. Test Sequence

1. **Base (1 h):** AIC-1321 in AUTO, cascaded to FIC-1341, setpoint at the current base (normally 3.0%). Record all Section 4 tags.
2. **Portable check at base** at the arch sample point and at the APH gas inlet sample point (Section 5).
3. **Step up:** raise the AIC-1321 setpoint by **+0.5%** (e.g. 3.0 → 3.5%). AIC-1321 raises FIC-1341 and the FD fan speeds up; the ID fan follows on PIC-1311. Hold **2 hours**.
4. **Portable check** in the last 30 minutes of the step-up hold.
5. **Return to base;** hold 1 hour.
6. **Step down:** lower the setpoint by **−0.5%** (e.g. 3.0 → 2.5%). Hold **2 hours**. The setpoint must **never be below 2.0%**.
7. **Portable check** in the last 30 minutes of the step-down hold.
8. **Return to base** and log the end time.

**Abort the step-down and return to base immediately if:** AT-1322 exceeds 200 ppm, or exceeds 100 ppm and is still climbing; AIC-1321 reads below 1.8%; flames become long, lazy or smoky; PIC-1311 rises above −1.0 mmH2O; or a fan speed reaches 95%. **An early CO rise is itself a result** — record the O2 at which it began.

## 4. Data to Record

Use 1-minute historian averages; evaluate each hold on its **last 60 minutes**.

| Tag | What it tells us |
|---|---|
| AIC-1321 (PV, SP) and FIC-1341 (PV, SP) | Arch O2 reported, and the FD air the loop delivers for it |
| AT-1327 | O2 at APH gas inlet; AT-1327 − AIC-1321 = convection ingress (≈ 0.2% normal) |
| AT-1326 | Stack O2 after APH; AT-1326 − AT-1327 = APH seal leakage (≈ 1.2% normal) |
| AT-1322 | Arch CO — how close the burners are to air shortage |
| FT-1201 × AT-1203 | Fuel heat input (MW) |
| SI-1341, JI-1341 / SI-1351, JI-1351 | FD / ID fan speed and power |
| TT-1303, TT-1343, TIC-1345 | APH gas inlet, hot air, APH gas outlet |
| PT-1342, PIC-1311 | Windbox pressure; arch draft |

## 5. Portable Analyzer Checks

1. Use a calibrated portable flue gas analyzer (O2/CO, dry basis via its conditioning unit), bump-tested that day with 4.0% O2 / 500 ppm CO.
2. Insert the probe at the arch sample point beside the AIC-1321 probe at the same depth; allow 5 minutes to stabilise; record the average of 5 readings 1 minute apart with the simultaneous AIC-1321 PV.
3. Repeat at the APH gas inlet sample point beside the AT-1327 probe.
4. Agreement within **±0.3% O2** is acceptable for each analyzer.

## 6. Interpretation — Reading the Result

**Expected response:** each +0.5% O2 adds about 3 points of excess air, ≈ 1,400 kg/h (≈ 2.5%) more FIC-1341 flow, a 1–2 point rise in SI-1341 and SI-1351. Because the APH recovers most of the heat in the extra air, the fuel penalty is small: about **0.15–0.25% of fired duty (≈ 0.06–0.1 MW, ≈ 4–7 kg/h fuel)** per 0.5% step, roughly half of what the same heater would show without an air preheater. The fuel signal is therefore weak; give more weight to the air-flow, O2-chain and CO evidence. "Expected" values come from the heater performance model at the current charge, crude and COT. The leak differences (AT-1327 − AIC-1321, AT-1326 − AT-1327) should stay almost constant through the steps, because leakage is set by draft and opening area, not by the O2 setpoint.

| What you see | Plain meaning | Conclusion / next step |
|---|---|---|
| Portables agree (±0.3%) at all holds; FIC-1341 and fuel close to expected; responses as above; CO low on step down; chain differences ≈ 0.2 and ≈ 1.2 | Analyzers true, no abnormal air ingress | Look elsewhere for any efficiency loss |
| Portable reads **lower** than AIC-1321 by a similar offset at all holds; AT-1327 − AIC-1321 smaller than normal or negative while the AT-1327 portable agrees; FIC-1341 below expected for the indicated O2; CO rises early on step down | Arch analyzer biased **high**: burners have less air than shown | Calibrate AIC-1321 (Per Maintenance Procedure — O2 and CO Analyzer Calibration and Validation, Rev 2.2); until fixed, raise the setpoint by the observed offset |
| Portable reads **higher** than AIC-1321; AT-1327 − AIC-1321 larger than normal while the AT-1327 portable agrees; FIC-1341 and fuel above expected | Arch analyzer biased **low**: heater wastes air and fuel | Calibrate; re-check fuel |
| Arch portable **agrees**; FIC-1341 **below** expected for the indicated O2; CO rises early on step down; chain differences normal | Part of the arch O2 is tramp air below the arch — burners short of air | Tramp air below the arch; survey per Maintenance Procedure — Tramp Air Survey and Casing Sealing, Rev 1.5 |
| AT-1327 − AIC-1321 > 0.8% with both portables agreeing; CO normal; FIC-1341 as expected; SI-1351 / JI-1351 up; fuel slightly above expected | Air entering the convection section | Convection ingress; survey header boxes, wall boxes, casing |
| AT-1326 − AT-1327 > 2.0%; FIC-1341 **above** expected for the indicated O2; SI-1351 / JI-1351 up; TIC-1345 lower (leak-air dilution) and PT-1342 lower than baseline for the same FD flow | FD air short-circuits across the APH seals | APH seal leakage; confirm per Maintenance Procedure — Air Preheater Seal Inspection, Soot Blowing and Water Washing, Rev 1.0, Section 4 (also rules out duct in-leakage after the APH) |
| AIC-1321 moves but FIC-1341 or fuel barely responds, or the O2 reading settles slowly (> 3 min) or is noisy | Reading not following the real air | Sample-system fault; call analyzer maintenance |

One step test is evidence, not proof. If two rows partly fit, record both and lower confidence; repeat the portable checks before any recalibration.

## 7. Records

Enter in the shift log and DCS event log: start and end of each hold, setpoints, portable readings with simultaneous AIC-1321 and AT-1327 values, the chain differences at each hold, CO peak on the step down, and any abort. Process engineering files the evaluated result against the heater model.
