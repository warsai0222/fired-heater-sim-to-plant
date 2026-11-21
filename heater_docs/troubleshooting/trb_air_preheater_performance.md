---
doc_id: trb_air_preheater_performance
doc_type: troubleshooting
equipment: [air_preheater, fd_fan, id_fan, bypass_dampers, soot_blowers, flue_gas_analyzers, burners, bms_sis, stack, heater_h101]
tags: [TIC-1345, TT-1343, TT-1303, PDT-1347, PDT-1348, XS-1349, AT-1326, AT-1327, AIC-1321, FIC-1341, SI-1341, SI-1351, JI-1341, JI-1351, PT-1342, PT-1352, PIC-1311, XS-1341, XS-1351, ZT-1361, ZT-1362, HS-1501, FT-1201, AT-1203, TT-1001, AT-1322, HS-1290]
title: Troubleshooting Guide — Air Preheater Leakage, Fouling and Low Cold-End Temperature
revision: 1.0
date: 2026-11-20
---

# Troubleshooting Guide — Air Preheater Leakage, Fouling and Low Cold-End Temperature

**Document No.:** H101-TRB-010
**Symptom:** AT-1326 − AT-1327 above ≈ 2.0 percentage points (normal ≈ 1.2); APH gas-side ΔP PDT-1347 above 90 mmH2O (Hi) or air-side PDT-1348 above 75 mmH2O; hot air TT-1343 below 250 °C (Lo); APH gas outlet TIC-1345 below 145 °C (Lo) or 140 °C (LL); APH rotor stopped (XS-1349 = 0); or an unexplained rapid rise of TIC-1345 / TT-1343 (possible APH fire)
**Revision:** 1.0 | **Date:** 2026-11-20
**Applicability:** Unit 100 — H-101 Crude Charge Heater — E-102 regenerative air preheater
**Owner:** Fired Equipment Engineering / Unit 100 Operations
**P&ID reference:** U100-PID-103 (air preheater, FD/ID fans, ducts, dampers, stack)

> **NOTE:** E-102 is a rotary regenerative (Ljungström) air preheater: heated element baskets rotate between the flue gas (≈ 390 → 160 °C) and the combustion air (≈ 30 → 300 °C), recovering ≈ 4.3 MW. Some air always leaks to the gas side across the radial, axial and circumferential seals — ≈ 6% of FD air as new. Seal leakage and fouling are slow (Type B) degradations; rotor stop and APH fire are emergencies. Equipment data are in Equipment Datasheet — E-102 Regenerative Air Preheater, Rev 1.0.

---

## 1. Immediate Actions

**Rotor stopped (XS-1349 = 0):** BMS-101 initiates the natural-draft runback — XV-1361 bypass damper and XV-1362 emergency air doors open, FD fan K-101 and ID fan K-102 stopped, firing clamped to ≤ 60% (BMS / SIS Cause and Effect — H-101, Rev 3.3). Confirm ZT-1361 and ZT-1362 open, start an **APH fire watch** (TIC-1345, TT-1343, casing), and follow SOP — FD / ID Fan Trip Response and Natural-Draft Operation, Rev 1.0. COT cannot be held at full charge: reduce charge in coordination with the C-101 operator (reduced throughput and any COT shortfall change flash-zone vaporization and yields).

**Suspected APH fire** (TIC-1345 or TT-1343 rising fast with no firing change, TIC-1345 approaching or exceeding TT-1303, smoke or sparks at S-101, hot casing): trip with HS-1290, call the fire brigade, follow Section 2.5.

**Slow degradation alarms (leakage, ΔP, temperatures):** confirm with trends normalised to firing, then diagnose per Section 2. Check fan margins first: SI-1341 and SI-1351 must stay below 95%; if either is at the limit, reduce firing (Troubleshooting Guide — Positive Draft and Afterburning, Rev 1.8).

---

## 2. Probable Causes

### 2.1 Seal Leakage Growth

**Description:** Radial, axial and circumferential seals wear, and the rotor "turndown" distortion at the hot end opens gaps. More air passes straight from the high-pressure air side (FD discharge ≈ +130 mmH2O) to the low-pressure gas side (ID suction). The leak air does no useful work: the FD fan must move it, the ID fan must remove it, and it dilutes and cools the gas leaving E-102.

**Diagnosis:** AT-1326 − AT-1327 rises above ≈ 2.0 (normal ≈ 1.2). Leakage can be estimated (ASME PTC 4.3 form) as **leakage % of gas-inlet mass ≈ 90 × (AT-1326 − AT-1327) / (20.9 − AT-1326)** — ≈ 6.5% at design (3.2 → 4.4%), ≈ 11–12% at a 2.0-point difference. Supporting signature: SI-1351 and JI-1351 up; FIC-1341 and SI-1341 up for the same burner air (AIC-1321 holds arch O2, so the FD fan makes up the air lost to leakage); TIC-1345 **lower** by dilution — this looks like better heat recovery but is not; hot air TT-1343 roughly unchanged.

**Action:** Check that the stack CEMS AT-1326 and AT-1327 are both valid (Section 2.6). Trend leakage weekly. Plan seal inspection and adjustment per Maintenance Procedure — Air Preheater Seal Inspection, Soot Blowing and Water Washing, Rev 1.0. Until then, the penalty is fan power (JI-1341 + JI-1351) and fan capacity, which limits maximum firing.

### 2.2 Fouling / Plugging of the Element Baskets

**Description:** Soot from poor combustion, deposits carried from the convection section, and sticky acid-wetted deposits at the cold end plug the element passages. Heat transfer falls and gas-side and air-side resistance rise.

**Diagnosis:** PDT-1347 above its ≈ 80 mmH2O normal (Hi 120), often with PDT-1348 rising; hot air TT-1343 **down**; APH gas outlet TIC-1345 **up**; efficiency down (≈ 1 point per ≈ 20 °C rise in final gas temperature) and fuel per unit duty up; ID fan load SI-1351 / JI-1351 up and PT-1352 more negative. TT-1303 (APH gas inlet) stays normal — that separates APH fouling from convection fouling, where TT-1303 rises.

**Action:** Run the APH soot blowers SB-102A/B (HS-1501 sequence) and watch PDT-1347 and TIC-1345 over the next hours. If ΔP does not recover, plan an off-line water wash per Maintenance Procedure — Air Preheater Seal Inspection, Soot Blowing and Water Washing, Rev 1.0. Correct poor combustion upstream (Troubleshooting Guide — Low Excess O2 / High CO, Rev 2.5).

### 2.3 Low Cold-End Temperature and Acid Dew Point Corrosion

**Description:** Sulfur in the refinery fuel gas (mainly H2S, higher after an amine-treating upset) burns to SO2 with a small fraction of SO3, which forms sulfuric acid that condenses on surfaces below the acid dew point. The cold-end element metal runs colder than the gas outlet (between the gas-outlet and cold-air-inlet temperatures), so TIC-1345 is held ≥ 145 °C by the cold-air bypass TV-1345, with an alarm and optimizer limit at 140 °C. Cold ambient (low TT-1001), low firing and a failed-closed TV-1345 lower the cold end; leak-air dilution lowers the TIC-1345 reading itself.

**Diagnosis:** TIC-1345 below 145 °C with TV-1345 already fully open (control capacity exhausted), or TIC-1345 low with the controller not responding (TV-1345 fails closed on signal or air loss). Corrosion consequences develop over months: rising PDT-1347 from corrosion products and accelerating seal leakage.

**Action:** Confirm TV-1345 strokes. At low load or cold weather accept a hotter stack to hold ≥ 140 °C; do not run below it to gain efficiency. Ask the laboratory for a fuel gas H2S check if the dew point may have risen. Inspect the cold-end baskets at the next opportunity.

### 2.4 Rotor Stop

**Description:** Drive motor, coupling or gearbox failure, a seized support bearing, or seal rubbing heavy enough to stall the rotor. A stationary rotor leaves one sector permanently in hot gas (distortion, seal damage, deposit ignition) and stops air preheat.

**Diagnosis:** XS-1349 = 0 and natural-draft runback in progress; TT-1343 falling; TIC-1345 rising toward TT-1303. Confirm locally — a rotation-monitor fault can mimic a stop.

**Action:** Restart on the standby (auxiliary) drive if available and the cause is known; otherwise remain on natural draft. Return to balanced draft only per SOP — FD / ID Fan Trip Response and Natural-Draft Operation, Rev 1.0, after an APH fire has been ruled out.

### 2.5 APH Fire

**Description:** Combustible deposits (soot, unburned fuel or oil from fuel-rich firing, afterburning, a tube leak or repeated failed light-offs) ignite on the element baskets. Low load and start-up are the high-risk periods. A fire can melt baskets and spread to the rotor and seals.

**Diagnosis:** TIC-1345 and/or TT-1343 rising rapidly with no firing change; TIC-1345 equal to or above TT-1303 (the APH is then a heat source, not a heat sink); local casing hot spots, smoke or sparks at S-101; rotor drive struggling or XS-1349 = 0. Recent history of high CO (AT-1322) supports the diagnosis.

**Action:** Trip with HS-1290. Stopping K-101 initiates the natural-draft runback (XV-1361 and XV-1362 open, K-102 stopped), sending flue gas through the D-101 bypass to S-101 around E-102. Keep the rotor turning if it can be done safely. Apply APH fire-fighting / washing water per Maintenance Procedure — Air Preheater Seal Inspection, Soot Blowing and Water Washing, Rev 1.0 under fire brigade direction. Do not open APH access doors. No restart until E-102 has been inspected.

### 2.6 Analyzer Error in the O2 Chain

**Description:** AT-1326 reading high, or AT-1327 reading low, inflates AT-1326 − AT-1327 and imitates seal leakage.

**Diagnosis:** Difference up but SI-1351, JI-1351, FIC-1341 and TIC-1345 unchanged. A portable analyzer at the stack and APH inlet test points disagrees.

**Action:** Validate per Maintenance Procedure — O2 and CO Analyzer Calibration and Validation, Rev 2.2.

---

## 3. Distinguishing Cause from Symptom

| What you see | What it means | How to confirm |
|---|---|---|
| AT-1326 − AT-1327 > ≈ 2.0, SI-1351 / JI-1351 up, FIC-1341 up, TIC-1345 lower | Seal leakage growth | Leakage estimate trend; fan powers |
| PDT-1347 up, TT-1343 down, TIC-1345 up, TT-1303 normal | APH fouling | SB-102A/B soot-blow response |
| TT-1303 up, TIC-1345 up less, PDT-1347 normal | Convection fouling, not APH | Troubleshooting Guide — High Stack Temperature, Rev 1.7 |
| TIC-1345 < 145 °C with TV-1345 open, cold TT-1001 or low load | Cold-end limit, acid dew point risk | TV-1345 position, ambient, firing |
| XS-1349 = 0, runback, TT-1343 falling | Rotor stop | Local check; fire watch |
| TIC-1345 / TT-1343 rising fast, TIC-1345 ≥ TT-1303 | APH fire | Visual from safe position, casing temperature |
| O2 difference up, fans and temperatures unchanged | Analyzer error | Portable analyzer |

Lower TIC-1345 is **not** automatically good: it may be leak-air dilution (seal leakage) rather than better heat recovery. Higher SI-1351 is a **symptom** shared by leakage, fouling and convection ingress; the O2 chain and PDT-1347 separate them.

---

## 4. Prevention / Follow-up

- Run SB-102A/B daily (HS-1501) and more often at low load or after any high-CO episode; log PDT-1347 before and after.
- Trend weekly: APH leakage estimate, PDT-1347 and PDT-1348 normalised to flow, TT-1343, TIC-1345, SI-1341 / SI-1351 and JI-1341 + JI-1351.
- Hold TIC-1345 ≥ 140 °C at all times; keep TV-1345 in AUTO.
- Inspect seals and cold-end baskets at every turnaround; water-wash when the soot-blown PDT-1347 baseline keeps rising.
- Avoid fuel-rich firing and repeated failed light-offs, which load E-102 with combustibles.
