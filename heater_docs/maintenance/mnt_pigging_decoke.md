---
doc_id: mnt_pigging_decoke
doc_type: maintenance
equipment: [heater_h101, radiant_coil, convection_section, air_preheater, fd_fan, id_fan, pass_flow_control, transfer_line, atmospheric_column]
tags: [TI-1121A, TI-1121B, TI-1122A, TI-1122B, TI-1123A, TI-1123B, TI-1124A, TI-1124B, PDI-1101, PDI-1102, PDI-1103, PDI-1104, PT-1101, PT-1102, PT-1103, PT-1104, PT-1110, FIC-1101, FIC-1102, FIC-1103, FIC-1104, FY-1100, TIC-1110, TT-1111, TT-1112, TT-1113, TT-1114, FT-1201, AT-1203, AIC-1321, FIC-1341, XS-1349, TT-1303, PDT-1347, TT-1343, AT-1326, AT-1327]
title: Maintenance Procedure — Mechanical Pigging Decoke of H-101 Coil
revision: 2.7
date: 2026-11-20
---

# Maintenance Procedure — Mechanical Pigging Decoke of H-101 Coil

**Document No.:** H101-MNT-001
**Revision:** 2.7 | **Date:** 2026-11-20
**Revision note:** Rev 2.7 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).
**Applicability:** Unit 100 — H-101 Crude Charge Heater, process coil (4 passes, convection + radiant)
**Owner:** Fixed Equipment Engineering / Turnaround Planning
**P&ID Reference:** U100-PID-101 (process coil)
**Estimated Downtime:** ≈ 4 days (heater off-line to heater back at COT)

---

## 1. Scope and Purpose

Coke deposits inside the H-101 radiant tubes insulate the tube wall, so tube metal temperatures (TI-1121A..1124B) rise for the same duty, and they narrow the bore, so coil pressure drop (PDI-1101..1104) rises. This procedure removes coke from all four passes by mechanical pigging: abrasive urethane pigs, propelled by water, are pumped through each pass from inlet to outlet, cutting the coke from the tube wall. Pigging avoids the thermal cycling of steam-air decoking. The radiant coil is ASTM A335 P9, 6" Sch 40 (ID 154.1 mm), 20 radiant tubes per pass plus the convection rows and crossover.

## 2. Decoke Triggers (H-101)

A decoke is planned when any of the following applies:

| Trigger | Value | Tag |
|---|---|---|
| Tube metal temperature approaching limit | Hottest skin TC sustained at or above 585 °C (Hi alarm), with the 600 °C TMT limit forecast within 30 days | TI-1121A..1124B |
| Coil ΔP approaching hydraulic limit | Any pass sustained at or above 7.8 bar (Hi) at reference charge, forecast to reach 8.4 bar (HH) within 30 days | PDI-1101..1104 |
| Economic optimum | The fuel penalty and lost-throughput cost of running on exceed the cost of a decoke (≈ 4 days lost production + contractor cost) | FT-1201 × AT-1203 trend vs model |

Readings are compared at the **reference condition**: charge 286 t/h on FY-1100, COT 360 °C on TIC-1110, on the same crude where possible. Before declaring a TMT trigger, rule out a faulty thermocouple (Per Troubleshooting Guide — Suspect Tube Skin Thermocouple Reading, Rev 1.4).

## 3. Shutdown, Cool-Down and Isolation (Day 1)

1. Shut down H-101 per SOP — H-101 Normal Shutdown, Rev 2.4, including displacement of the coil with flushing oil (gas oil) before charge is stopped.
2. Continue forced cooling with ID fan K-102 on draft control and FD fan K-101 at ≥ 25% air flow (FIC-1341) until TI-1121A..1124B read below 60 °C. Keep the APH rotor turning (XS-1349 = 1) at least until TT-1303 is below 150 °C. Then stop the fans and rotor per SOP — H-101 Normal Shutdown, Rev 2.4, Section 5, and LOTO them before any entry.
3. Drain the flushing oil to the slop system; steam out each pass at low rate to free residual oil, then water-flush until the drain runs clear.
4. Close pass inlet valves XV-1105A..D and outlet valves XV-1106A..D; swing the spectacle blinds to the BLIND position at all eight locations. Verify by the isolation register.
5. Isolate and blind the fuel gas supply at V-101 and the pilot gas supply; apply LOTO to FV-1101..1104 actuators, the K-101 / K-102 motors and the E-102 rotor drive.
6. Remove the flanged spools at the pass inlet and pass outlet and fit the contractor's pig launcher (inlet) and pig receiver (outlet) to each pass.

## 4. Pigging Sequence (Days 2–3)

Water is the propellant, supplied by the contractor's pumping unit with a pressure relief set below the coil hydrotest pressure. Typical pig speed is 0.5–1.5 m/s; the run pressure is monitored continuously.

| Run | Pig | Nominal OD | Purpose |
|---|---|---|---|
| 1 | Soft foam swab | 125 mm | Prove the pass is open; locate restrictions |
| 2 | Bare urethane, light studs | 135 mm | Remove loose and soft coke |
| 3 | Studded urethane | 145 mm | Main coke cutting |
| 4 | Studded urethane, carbide studs | 155 mm (≈ 1 mm over ID) | Cut hard coke to bare metal |
| 5 | Full-bore studded (repeat as needed) | 158 mm | Polishing passes until clean |
| 6 | Gauging pig with aluminium plate | 150 mm plate | Confirm no deformation or residual restriction |

1. Start each pass with the smallest pig. Never step up a pig size until the previous size runs freely at a steady pressure.
2. If a pig sticks (pressure rises to the relief setting), reverse flow to back it out; do not exceed the contractor's maximum differential.
3. Collect the returned water and coke at the receiver; record coke fines volume per run.
4. Pig the passes one at a time; record the run log for each pass separately.

## 5. End-Point Criteria (per pass)

| Criterion | Acceptance |
|---|---|
| Return water | Clear after two consecutive full-bore runs; no coke fines |
| Run pressure | Steady, matching the contractor's clean-tube reference at the same water rate |
| Gauging pig | Plate undamaged; no dents or scoring |
| Pig wear | Final full-bore pig studs show uniform wear (no metal pickup) |

Record a pass as complete only when all four criteria are met.

## 6. Inspection Window

While the coil is open: UT thickness readings at the marked TML locations on the radiant tubes; visual inspection of tubes, hangers and refractory from the firebox (Per Safety Procedure — Firebox and Header Box Entry (Confined Space), Rev 1.7); skin thermocouple checks (Per Maintenance Procedure — Tube Skin Thermocouple Inspection and Replacement, Rev 1.6); burner cleaning if planned (Per Maintenance Procedure — Burner Inspection, Cleaning and Tuning, Rev 2.0). The decoke outage is also the normal window for air preheater seal inspection, basket inspection and off-line water washing (Per Maintenance Procedure — Air Preheater Seal Inspection, Soot Blowing and Water Washing, Rev 1.0) — plan it with the pigging contractor so the APH work does not extend the outage.

## 7. Reinstatement and Restart (Day 4)

1. Remove launchers and receivers; reinstate spools with new gaskets.
2. Hydrostatic leak test each pass at the coil test pressure agreed by fixed equipment engineering; check all disturbed flanges.
3. Drain water fully; blow through with plant air or nitrogen to remove standing water (water left in the coil flashes to steam on start-up and upsets pass flows).
4. Swing spectacle blinds to OPEN, open XV-1105A..D / XV-1106A..D, remove LOTO.
5. Restart per SOP — H-101 Cold Start-up, Purge and Burner Light-off, Rev 3.2. Inform the C-101 operator of the expected return-to-COT time: the column restarts on the heater's schedule.

## 8. Record Post-Decoke Clean Baselines

Decoke recovery is never 100%: some hard coke and tube-wall oxide always remain, and the clean baseline creeps upward from one decoke to the next. **The run-length forecast and the heater model must use the new measured baseline, not the as-new design values (TMT ≈ 430 °C, ΔP ≈ 6.0 bar).**

Within 72 hours of reaching steady operation, at the reference condition (286 t/h, COT 360 °C, O2 3.0%), log 4-hour averages of:

1. TI-1121A..1124B (each thermocouple).
2. PDI-1101..1104 and PT-1101..1104, PT-1110.
3. FIC-1101..1104, TT-1111..1114, FT-1201, AT-1203, AIC-1321 and FIC-1341.
4. Crude name / blend and assay ID.
5. If APH work was done in the same outage, the APH baselines (AT-1326 − AT-1327, PDT-1347, TT-1343, TT-1303) per Maintenance Procedure — Air Preheater Seal Inspection, Soot Blowing and Water Washing, Rev 1.0, Section 9. Firing at a given COT depends on APH condition as well as coil condition, so the two baselines must be filed together.

File the baseline, the decoke date, coke volume per pass and the pigging run log with process engineering. Compare against the previous post-decoke baseline; a step increase of more than 15 °C TMT or 0.4 bar ΔP versus the last clean baseline is reported to fixed equipment engineering.
