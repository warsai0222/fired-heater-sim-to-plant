---
doc_id: mnt_aph_inspection_washing
doc_type: maintenance
equipment: [air_preheater, fd_fan, id_fan, bypass_dampers, soot_blowers, flue_gas_analyzers, heater_h101]
tags: [AT-1327, AT-1326, AIC-1321, PDT-1347, PDT-1348, TT-1343, TT-1303, TIC-1345, XS-1349, FIC-1341, PT-1342, SI-1341, SI-1351, JI-1341, JI-1351, PT-1352, HS-1501, FT-1201, AT-1203, TIC-1110, FY-1100]
title: Maintenance Procedure — Air Preheater Seal Inspection, Soot Blowing and Water Washing
revision: 1.0
date: 2026-11-20
---

# Maintenance Procedure — Air Preheater Seal Inspection, Soot Blowing and Water Washing

**Document No.:** H101-MNT-007
**Revision:** 1.0 | **Date:** 2026-11-20
**Applicability:** Unit 100 — H-101 Crude Charge Heater, regenerative air preheater E-102 and soot blowers SB-102A/B
**Owner:** Fired Heater Maintenance / Rotating Equipment / Process Engineering
**P&ID Reference:** U100-PID-103 (air preheater, FD/ID fans, ducts, dampers, stack)
**Frequency:** Performance review monthly; leakage test quarterly and on trigger; seal and basket inspection at every major outage (decoke)

---

## 1. Scope and Purpose

E-102 is a vertical-shaft rotary regenerative (Ljungström) air preheater. Heating elements packed in baskets on a slowly turning rotor pass alternately through the flue gas (≈ 390 → 160 °C) and the combustion air (≈ 30 → 300 °C), recovering ≈ 4.3 MW and raising heater efficiency from ≈ 84% to ≈ 91%. Equipment data: Equipment Datasheet — E-102 Regenerative Air Preheater, Rev 1.0.

Two slow degradations matter, and both cost fuel and fan power:
- **Seal leakage.** Radial, axial and circumferential seals separate the high-pressure air side from the low-pressure gas side. As new, ≈ 6% of FD air leaks to the gas side. Seals wear and clearances open; leakage grows: stack O2 AT-1326 rises above AT-1327, ID fan speed and power rise, TIC-1345 falls by dilution, and less hot air reaches the burners for the same FD flow.
- **Fouling and cold-end corrosion.** Deposits build up on the elements, worst at the cold end where metal can fall below the acid dew point. Gas ΔP PDT-1347 rises, TT-1343 falls, TIC-1345 rises, efficiency falls and ID fan load rises.

This procedure covers monitoring, on-line soot blowing, the on-line leakage test, off-line seal and basket inspection, water washing, rotor drive and bearing checks, and post-maintenance baselines.

## 2. Performance Monitoring and Triggers

Compare monthly at the reference condition (286 t/h on FY-1100, COT 360 °C on TIC-1110, AIC-1321 3.0%) with the last post-maintenance baseline (Section 9).

| Signal | Clean / as-new | Trigger | Points to |
|---|---|---|---|
| AT-1326 − AT-1327 | ≈ 1.2% | > 2.0% sustained | Seal leakage (or duct in-leakage — Section 4) |
| PDT-1347 gas ΔP | ≈ 80 mmH2O | > 120 mmH2O Hi, or +15 above baseline | Fouling / plugging |
| PDT-1348 air ΔP | ≈ 50 mmH2O | > 75 mmH2O Hi | Air-side plugging |
| TT-1343 hot air | ≈ 300 °C | < 250 °C Lo, or −15 °C vs baseline | Fouling or rotor fault |
| TIC-1345 gas outlet | ≈ 150 °C | +15 °C vs baseline at same TT-1303 | Fouling |
| SI-1351 / JI-1351 | ≈ 72% / 70 kW | +5 points / +10 kW vs baseline | Leakage or fouling |

## 3. On-Line Soot Blowing (SB-102A/B)

1. SB-102A/B run daily at the end of the HS-1501 sequence, after the convection blowers (Per Maintenance Procedure — Convection Section Soot Blowing, Rev 1.9).
2. Preconditions: rotor turning (XS-1349 = 1), TIC-1345 ≥ 145 °C, steam supply drained to dry steam, ID fan SI-1351 ≤ 90%.
3. Each blower traverses the rotor face so the whole matrix passes under the jet; allow at least one rotor revolution per traverse.
4. Check effectiveness by PDT-1347 and TT-1343 30–60 minutes after blowing. If PDT-1347 does not recover after three days of twice-daily blowing, plan an off-line water wash (Section 7).

## 4. On-Line Leakage Test Using the O2 Chain

1. Heater steady at the reference condition; no soot blowing for 2 hours; PIC-1311 at −2.5 mmH2O.
2. Validate AT-1327 and AT-1326 with a portable analyzer at the APH gas inlet and APH gas outlet sample points (±0.3% O2) — an analyzer error looks exactly like a leakage change (Per Maintenance Procedure — O2 and CO Analyzer Calibration and Validation, Rev 2.2).
3. Calculate leakage as a percentage of the gas entering the APH (ASME PTC 4.3 form):
   **Leakage % ≈ 90 × (O2 out − O2 in) / (20.9 − O2 out)**, with O2 in = AT-1327 and O2 out = APH outlet O2.
   As new: 90 × (4.4 − 3.2) / (20.9 − 4.4) ≈ 6.5%. At the 2.0% trigger difference it is ≈ 11%.
4. **Separate seal leakage from duct in-leakage:** if the portable O2 at the APH gas outlet is close to AT-1326, the gain is across the APH; if it is close to AT-1327 plus the normal gain and AT-1326 is much higher, the air is entering in the ducts or ID fan (Per Maintenance Procedure — Tramp Air Survey and Casing Sealing, Rev 1.5).
5. Cross-check: seal leakage moves FD air to the gas side, so FIC-1341 runs **above** the air the heater model expects for the indicated O2 and fuel (FT-1201 × AT-1203), while windbox pressure PT-1342 falls slightly for the same FD flow. Duct in-leakage does not change FIC-1341.
6. Record the result with SI-1341, SI-1351, JI-1341 and JI-1351.

## 5. Off-Line Seal Clearance Inspection and Adjustment (outage)

1. Heater shut down per SOP — H-101 Normal Shutdown, Rev 2.4; fans and rotor stopped only after TT-1303 is below 150 °C; K-101, K-102 and the rotor drive under LOTO; rotor mechanically locked against draft-driven rotation.
2. Ventilate, gas test and enter under Safety Procedure — Firebox and Header Box Entry (Confined Space), Rev 1.7 (its confined-space requirements apply to the APH housing and ducts).
3. Inspect radial seals (hot and cold end), axial seals and circumferential (bypass) seals for wear, erosion, missing strips and loose bolts; inspect sector plates for warping and scoring.
4. Measure clearances with feeler gauges at marked points while turning the rotor by hand. Set to the vendor's **cold settings**, which allow for the hot end growing more than the cold end in service (rotor "turndown"). Do not set to zero cold clearance — the seals will rub and wear quickly when hot.
5. Replace worn seal strips as a set per sector; record as-found and as-left clearances on the rotor map.

## 6. Basket Inspection — Cold-End Corrosion and Plugging (outage)

1. Inspect the cold-end and hot-end faces with a lamp: count plugged passages, note deposit type (soft soot, hard scale, wet acidic paste).
2. Remove at least two sample cold-end baskets; inspect for thinning, perforation and corrosion of element sheets; weigh against the nominal clean weight.
3. Replace cold-end baskets with significant metal loss or perforation; hot-end baskets showing erosion at the leading edge are replaced or reversed per vendor guidance.
4. Corrosion concentrated at the cold end points to operation below the acid dew point — review TIC-1345 history (time below 145 °C and 140 °C), start-ups and TV-1345 operation with process engineering.

## 7. Off-Line Water Wash

1. Wash only with the heater shut down and E-102 isolated from fire; agree with process engineering when soot blowing no longer recovers PDT-1347.
2. Turn the rotor slowly with its drive during washing so all sectors are washed; use the vendor's wash lances or fixed nozzles from the hot end down.
3. Wash with service water, adding a mild alkaline agent (e.g. soda ash) if the drain pH is acidic; collect the wash water to the oily-water/neutralization system.
4. Continue until the drain runs clear and drain pH is neutral (≈ 6–8); then rinse with clean water.
5. **Dry completely before restart:** run the rotor and fans with warm air, or bring the heater on line promptly with TV-1345 open and minimum time below 145 °C (Per SOP — H-101 Cold Start-up, Purge and Burner Light-off, Rev 3.2, Section 7). Wet elements left standing corrode rapidly.

## 8. Rotor Drive and Support Bearing Checks

1. **On-line (monthly):** rotor turning and steady (XS-1349 and local indication); drive motor current steady (a rising or cyclic current means seal rub or a distorted rotor); gearbox oil level and temperature; support (bottom) and guide (top) bearing oil level, temperature and vibration against baseline; no oil leaks.
2. **Outage:** change gearbox and bearing oils per vendor schedule; inspect drive pinion and rotor pin rack wear; check the auxiliary drive or hand-barring arrangement works; verify the XS-1349 rotation monitor by proof test per BMS / SIS Cause and Effect — H-101, Rev 3.3 (it initiates a natural-draft runback, so test only under the BMS proof-test procedure).
3. After any hot rotor stop, check seal clearances and drive torque before restart (Per SOP — FD / ID Fan Trip Response and Natural-Draft Operation, Rev 1.0, Section 5).

## 9. Post-Maintenance Baselines

Within 72 hours of steady operation after any seal work, wash or basket change, at the reference condition and 30–60 minutes after a soot-blow sequence, log 4-hour averages of:

1. **AT-1326 − AT-1327** (and the calculated leakage %), with the portable check of both analyzers.
2. **PDT-1347** and PDT-1348.
3. **TT-1343**, TT-1303 and TIC-1345 (note TV-1345 position: closed).
4. FIC-1341, PT-1342, SI-1341, SI-1351, JI-1341, JI-1351, PT-1352, FT-1201 × AT-1203.

These replace the previous baseline for the triggers in Section 2 and for the heater model calibration. Seal clearances never return fully to as-new, so compare against the last post-maintenance baseline, not the design values.

## 10. Records

File with process engineering: as-found / as-left seal clearance map, seal strips replaced, basket inspection results and photos, wash dates and drain pH log, oil and bearing readings, and the Section 9 baseline set.
