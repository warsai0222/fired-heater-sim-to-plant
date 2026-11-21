---
doc_id: env_stack_emissions
doc_type: safety
equipment: [flue_gas_analyzers, stack, id_fan, air_preheater, bypass_dampers, burners, fuel_gas_system, radiant_section, heater_h101]
tags: [AT-1325, AT-1326, AT-1327, AT-1322, AIC-1321, TT-1301A, TT-1301B, AT-1203, FT-1201, TT-1303, TIC-1345, TT-1343, ZT-1361, ZT-1362, XS-1341, XS-1351]
title: Environmental Procedure — Stack Emissions Monitoring (CO, NOx)
revision: 1.4
date: 2026-11-20
---

# Environmental Procedure — Stack Emissions Monitoring (CO, NOx)

**Document No.:** H101-ENV-001
**Revision:** 1.4 | **Date:** 2026-11-20
**Applicability:** Unit 100 — H-101 Crude Charge Heater, stack S-101
**Owner:** Environmental Department / Unit 100 Operations
**P&ID reference:** U100-PID-102 (arch analyzers), U100-PID-103 (APH, ID fan, bypass damper, stack and CEMS)

**Revision note:** Rev 1.4 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).

> **NOTE:** Emission limits in this procedure are those of the site air permit as applied to H-101. Exceedances are reportable. When combustion safety and emissions conflict (e.g. high CO at low O2), combustion safety comes first: correct the combustion, then report.

---

## 1. Monitoring Instruments and Sample Point

Since Rev B the flue gas path is: firebox → convection section → regenerative air preheater E-102 → ID fan K-102 → stack S-101. The D-101 bypass damper (XV-1361) joins the convection outlet directly to S-101 for natural-draft operation. The stack CEMS probe is located on S-101 **above the point where the bypass duct joins** (design assumption), so it measures the gas actually emitted in both balanced-draft and natural-draft modes.

| Tag | Measurement | Location | Basis / normal | Use |
|---|---|---|---|---|
| AT-1325 | NOx (CEMS) | Stack S-101, after ID fan | mg/Nm³ corrected to 3% O2 dry; ≈ 80 | Permit compliance, Hi alarm 150 |
| AT-1326 | O2 (CEMS) | Stack S-101, same probe | vol% dry, ≈ 4.4% | O2 correction of AT-1325 |
| AT-1327 | O2 | Convection outlet / APH gas inlet | vol% dry, ≈ 3.2% | Diagnostic only |
| AIC-1321 | O2 | Arch (radiant exit) | vol% dry, setpoint 3.0% | Excess-air control; not used for emissions correction |
| AT-1322 | CO | Arch (radiant exit) | ppm, ≈ 30 | Combustion control and CO compliance surrogate; Hi 200, HH 1000 |

Instrument details and calibration are in Instrument Datasheet — Flue Gas O2, CO and Stack CEMS Analyzers, Rev 1.6 and Maintenance Procedure — O2 and CO Analyzer Calibration and Validation, Rev 2.2.

---

## 2. Emission Limits, Averaging and O2 Correction

| Pollutant | Limit | Averaging | Reference O2 |
|---|---|---|---|
| NOx (as NO2) | 150 mg/Nm³ | Rolling 24 h; hourly alarm at 150 | 3% O2 dry |
| CO | 200 ppm | Hourly average of AT-1322 | As measured at arch |

Correction to reference O2: **C_ref = C_meas × (20.9 − 3.0) / (20.9 − O2_meas)**, with O2_meas from the stack CEMS AT-1326 at the same probe as the NOx sample.

**Worked example:** raw NOx 60 mg/Nm³ dry at AT-1326 = 4.4% → 60 × 17.9 / 16.5 ≈ 65 mg/Nm³ @ 3% O2.

Never correct stack NOx with AIC-1321 or AT-1327. Between the arch and the CEMS the gas picks up air in two places, both of which dilute NOx and both of which the AT-1326 correction removes:

- **Convection-section ingress:** AT-1327 − AIC-1321, normal ≈ 0.2 points; investigate above ≈ 0.8.
- **APH seal leakage** (air-side to gas-side across the rotor seals): AT-1326 − AT-1327, normal ≈ 1.2 points (≈ 6% of FD air); investigate above ≈ 2.0.

Using the arch O2 (3.0%) instead of 4.4% in the example above would understate NOx by about 8%. Growing O2 differences are an efficiency and fan-capacity issue, covered in Troubleshooting Guide — High O2 Reading / Suspected Air Ingress, Rev 1.6 and Troubleshooting Guide — Air Preheater Leakage, Fouling and Low Cold-End Temperature, Rev 1.0.

---

## 3. What Drives NOx on H-101

H-101 has eight forced-draft low-NOx gas burners (B-101A–H) supplied with combustion air preheated to ≈ 300 °C (TT-1343) by E-102. Hot combustion air raises adiabatic flame temperature, so thermal NOx per unit heat is higher than it was with ambient air in the Rev A natural-draft design; the permit margin is correspondingly smaller. Expected effects:

- **Hot-air temperature (TT-1343):** higher air temperature raises NOx; APH fouling lowers TT-1343 and slightly lowers NOx while costing efficiency.
- **Higher excess O2 (AIC-1321 setpoint):** NOx rises moderately; stack loss and fan power also rise.
- **Higher firing (FT-1201 × AT-1203) and bridgewall (TT-1301A/B, ≈ 845 °C normal):** NOx rises with firebox temperature; firing near the 46 MW LHV limit or bridgewall above 900 °C brings NOx toward the limit.
- **Fuel gas composition:** higher hydrogen raises flame temperature and NOx; watch AT-1203.
- **Burner air distribution:** uneven registers or damaged tiles create hot, oxygen-rich zones (Maintenance Procedure — Burner Inspection, Cleaning and Tuning, Rev 2.0).
- **Tramp air below the arch** does not pass through the flames and affects NOx much less than burner air.

---

## 4. Emissions During Natural-Draft Operation

On an FD fan, ID fan or APH rotor stop (XS-1341, XS-1351 or XS-1349 = 0) BMS-101 opens the D-101 bypass damper XV-1361 and D-102 emergency air doors XV-1362 and runs the heater back to ≤ 60% firing (SOP — FD / ID Fan Trip Response and Natural-Draft Operation, Rev 1.0). During this mode:

- Combustion air is ambient, not preheated, so NOx per unit heat typically **falls**, but excess air is less controllable and O2 at the arch and stack is usually higher.
- Flue gas bypasses E-102 and the ID fan; stack temperature rises to ≈ 400 °C. The CEMS still measures it (sample point above the bypass junction).
- CO risk rises during the transition, when air supply changes abruptly. Watch AT-1322.
- Log the period (ZT-1361 / ZT-1362 open) with the CEMS data so that any exceedance can be attributed.

---

## 5. What Drives CO

CO at the arch (AT-1322, normal ≈ 30 ppm) is a sign of incomplete combustion. It rises sharply when burner-level O2 falls below about 1.5%, when flames are quenched, or when fuel and air mix poorly. On H-101, CO can appear at a "normal" AIC-1321 reading if tramp air enters below the arch or if the analyzer reads high, because the burners are then actually short of air. Diagnosis is in Troubleshooting Guide — Low Excess O2 / High CO, Rev 2.5.

---

## 6. Operator Response to Emissions Alarms

**AT-1325 NOx ≥ 150 mg/Nm³ (hourly):**
1. Check AT-1326 is reading validly (the corrected value depends on it).
2. If AIC-1321 is above its 3.0% design setpoint, reduce toward 3.0% while watching AT-1322.
3. Check bridgewall TT-1301A/B, hot-air TT-1343 and firing; reduce firing if above normal and production allows. A firing or COT reduction lowers flash-zone vaporization in C-101 and shifts distillate into residue; coordinate with the C-101 / unit operator.
4. Check AT-1203 for a fuel gas composition change. Inform the Environmental Department.

**AT-1322 CO ≥ 200 ppm (hourly):**
1. Correct the combustion first per Troubleshooting Guide — Low Excess O2 / High CO, Rev 2.5.
2. Above 1000 ppm (HH), treat as a combustion safety event (combustibles in the firebox), not an emissions issue.

---

## 7. Data Quality, Records and Reporting

- CEMS AT-1325/AT-1326: daily automatic zero and span drift check; quarterly cylinder gas audit; annual relative accuracy test against a reference stack method. Minimum data availability 95% per quarter.
- Periods of analyzer maintenance or failed calibration are flagged invalid and replaced by the permit substitute-data method; they are not "zero emission" periods.
- Any hourly exceedance is logged with cause and corrective action. Exceedances lasting more than 1 hour, or any 24 h rolling average above the limit, are reported to the regulator by the Environmental Department within 24 hours.
- Archived with the CEMS data: APH gas outlet temperature TIC-1345 (≈ 150 °C), convection outlet TT-1303 (≈ 390 °C), firing, and bypass/air-door positions ZT-1361/ZT-1362, so that exceedances can be related to operating mode and conditions.
