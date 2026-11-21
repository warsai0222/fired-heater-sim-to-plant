---
doc_id: sop_cold_startup_light_off
doc_type: sop
equipment: [heater_h101, radiant_section, radiant_coil, burners, fuel_gas_system, fuel_gas_ko_drum, pilot_gas_system, air_preheater, fd_fan, id_fan, bypass_dampers, flue_gas_analyzers, pass_flow_control, transfer_line, atmospheric_column, snuffing_steam, bms_sis]
tags: [FIC-1101, FIC-1102, FIC-1103, FIC-1104, FT-1151, FT-1152, FT-1153, FT-1154, FY-1100, TIC-1110, TT-1111, TT-1112, TT-1113, TT-1114, TI-1121A, TI-1122A, TI-1123A, TI-1124A, PIC-1202, PT-1206, PT-1207, PT-1208, LT-1205, BS-1211, BS-1212, BS-1213, BS-1214, BS-1215, BS-1216, BS-1217, BS-1218, PIC-1311, PT-1314, AIC-1321, AT-1322, AT-1327, FIC-1341, SI-1341, SI-1351, XS-1341, XS-1351, XS-1349, ZT-1361, ZT-1362, TIC-1345, TT-1343, TT-1303, TT-1301A, TT-1301B, PI-1403, HS-1290]
title: SOP — H-101 Cold Start-up, Purge and Burner Light-off
revision: 3.2
date: 2026-11-20
---

# SOP — H-101 Cold Start-up, Purge and Burner Light-off

**Document No.:** H101-SOP-001
**Revision:** 3.2 | **Date:** 2026-11-20
**Revision note:** Rev 3.2 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).
**Applicability:** Unit 100 — H-101 Crude Charge Heater
**Owner:** Unit 100 Operations (Shift Superintendent)
**P&ID Reference:** U100-PID-101 (process coil), U100-PID-102 (combustion, fuel gas, burners, BMS), U100-PID-103 (air preheater, FD/ID fans, ducts, dampers, stack)

---

## 1. Scope and Purpose

This procedure covers start-up of H-101 from a cold, de-fired condition (firebox at ambient, all burners and pilots out, fuel gas positively isolated, fans stopped) through air preheater and fan start, purge, pilot light-off, main burner light-off and heat-up to the coil outlet temperature (COT) target of 360 °C on TIC-1110. It applies after a normal shutdown, after a total trip, and after a decoke (Per Maintenance Procedure — Mechanical Pigging Decoke of H-101 Coil, Rev 2.7).

H-101 is a balanced-draft heater: FD fan K-101 (VFD SC-1341) pushes combustion air through the regenerative air preheater E-102 to the burner windbox, and ID fan K-102 (VFD SC-1351) draws flue gas from the convection section through E-102 to stack S-101. The BMS-101 light-off permissives and trips are listed in BMS / SIS Cause and Effect — H-101, Rev 3.3. This SOP never bypasses a permissive. Expected duration from purge start to COT 360 °C is 10–14 hours, governed by the column start-up and the heating-rate limits in Section 8.

## 2. Prerequisites and Pre-Start Checks (H-101)

1. All work permits closed; LOTO removed from the K-101/K-102 motors, the E-102 rotor drive and the fuel system; firebox, header boxes, APH and ducts confirmed clear of people and tools; all access doors bolted (Per Safety Procedure — Firebox and Header Box Entry (Confined Space), Rev 1.7).
2. Decoking spectacle blinds at XV-1105A..D / XV-1106A..D in the OPEN (flow) position and the valves open on all four passes.
3. Fuel gas blinds removed; XV-1201 / XV-1202 closed, XV-1203 bleed open, XV-1209 pilot shutoff closed, PV-1202 closed.
4. V-101 drained; LT-1205 below 50% (Hi alarm) and well below the 80% HH trip (LSHH-1205).
5. Snuffing steam header PI-1403 at or above 2.5 barg; XV-1401 and HV-1402 closed and drained.
6. Analyzers in service and validated within 30 days (Per Maintenance Procedure — O2 and CO Analyzer Calibration and Validation, Rev 2.2): AIC-1321 and AT-1327 read 20.0–20.9% O2 cold; AT-1322 below 10 ppm CO.
7. Flame scanners BS-1211..1218 healthy and reading "no flame". HS-1290 reset in the control room and field.
8. Fans and APH ready: lube oil levels correct, couplings guarded, VFDs SC-1341 / SC-1351 healthy; APH soot blowers SB-102A/B retracted (Per Maintenance Procedure — Air Preheater Seal Inspection, Soot Blowing and Water Washing, Rev 1.0).
9. With the fans de-energized, the fail-open bypass damper D-101 (XV-1361) and emergency air doors D-102 (XV-1362) are open; ZT-1361 / ZT-1362 confirm this. Cold-air bypass TV-1345 (fail closed) is closed.

## 3. Establish Crude Flow Through All Passes

Coil flow must be established on all four passes **before** any fire is put in the box. The SIS pass low-flow trip (FT-1151..1154 < 43 t/h for 2 s) stays active.

1. Line up P-101A/B and the start-up circulation route through the preheat train, H-101 and the transfer line to C-101 per the crude unit start-up procedure.
2. Put FIC-1101..1104 in MANUAL; open FV-1101..1104 gradually and establish flow.
3. Bring each pass to at least **55 t/h**, then transfer FIC-1101..1104 to AUTO. The 60 t/h Lo alarm may stand until Section 8 step 2.
4. Confirm FT-1151..1154 agree with FIC-1101..1104 within 3 t/h per pass; resolve any mismatch before light-off. Record FY-1100.

## 4. Start the Air Preheater and Fans (Balanced-Draft Line-up)

The APH rotor must be turning **before** any air or flue gas flows through it: a stationary rotor heats unevenly, distorts and wears its seals on restart.

1. Start the E-102 rotor drive; confirm XS-1349 = 1 (rotation proven) at the BMS and visually at the drive.
2. Put PIC-1311 in MANUAL. Start ID fan K-102 at minimum speed on SC-1351; confirm XS-1351 = 1. As the ID fan comes up, close bypass damper XV-1361 so the flue path is through E-102; confirm ZT-1361 < 5%.
3. Put PIC-1311 in AUTO at −2.5 mmH2O (manipulates SC-1351).
4. Start FD fan K-101 at minimum speed on SC-1341 (**ID first, then FD** — never pressurize the firebox); confirm XS-1341 = 1. Close the emergency air doors XV-1362; confirm ZT-1362 < 5%.
5. Put FIC-1341 in AUTO on a local setpoint at purge air flow, **≥ 25% of design air (≥ 14,500 kg/h)**; the FIC-1341 Lo alarm (45,000 kg/h) will stand. Confirm arch draft stays negative and PT-1314 is well below the +10 mmH2O trip.
6. Put TIC-1345 in AUTO at its 148 °C setpoint. During warm-up the APH gas outlet is far below setpoint, so TV-1345 opens fully and bypasses cold air around the APH, which warms the cold end faster.

If the fans are unavailable, the heater may be purged and lit on **natural draft** with XV-1361 and XV-1362 open (permitted by the BMS), limited to ≤ 60% firing, and converted to balanced draft later per SOP — FD / ID Fan Trip Response and Natural-Draft Operation, Rev 1.0, Section 7.

## 5. Firebox Purge

The purge must deliver **5 volume changes** of the firebox, convection section, APH and ducts. The BMS purge permissive requires both fans running with air flow ≥ 25% (or, for a natural-draft start, XV-1361 and XV-1362 open). The purge timer (set at commissioning for 5 volume changes at 25% air) runs only while all permissives are healthy.

1. Gas test the firebox through two peepholes and the arch sample point with a calibrated portable combustible-gas meter: result must be **0% LEL**.
2. Confirm permissives: XV-1201/1202 and XV-1209 closed; pass flows above LL; XS-1341, XS-1351 and XS-1349 = 1; FIC-1341 ≥ 25%; LT-1205 not HH; no flame on BS-1211..1218; HS-1290 reset.
3. Initiate purge from the BMS console. Loss of any permissive resets the timer — restart from the beginning.
4. On "PURGE COMPLETE", light-off is enabled for 10 minutes; if pilots are not lit in that window, re-purge.

## 6. Pilot and Main Burner Light-off

1. Reset the BMS; open XV-1209. Confirm PT-1208 at 0.7 barg (Lo 0.4, LL trip 0.25 barg).
2. Light pilots one at a time; confirm each visually. No more than two ignition tries on one pilot before investigating.
3. With pilots proven, PIC-1202 in MANUAL with PV-1202 closed; open XV-1201/1202 (XV-1203 closes) from the BMS.
4. Raise fuel gas pressure to about **0.5 barg** (above the PT-1206 LL trip 0.25 barg and the PIC-1202 Lo alarm 0.35 barg).
5. Open the first burner gas cock; the flame must be proven by its scanner within the 10 s trial-for-ignition, otherwise close the cock and investigate.
6. Light burners in the symmetrical pattern **B-101D, B-101E, B-101B, B-101G, B-101C, B-101F, B-101A, B-101H**, 2 minutes apart, watching PIC-1311, PT-1314 and AT-1322.
7. Keep FIC-1341 at purge air flow until at least four burners are lit and AT-1322 is below 200 ppm, then put FIC-1341 in CASCADE under AIC-1321 at 3.0% O2. Air/fuel cross-limiting is then active (air leads on load increase, fuel leads on decrease).

## 7. Bringing the Air Preheater Up to Temperature (Cold End)

Flue gas leaving a cold APH is below its acid dew point, so the cold-end elements are wetted with acid and collect sticky deposits. Keep this period short.

1. Keep TV-1345 open under TIC-1345 until the APH gas outlet exceeds 145 °C; TIC-1345 then controls and TV-1345 closes progressively as firing rises.
2. Watch TT-1303 (convection outlet / APH gas inlet) and TT-1343 (hot air) rise together. Hot air that stays flat while TT-1303 rises suggests the rotor has stopped — check XS-1349 locally.
3. Do **not** run APH soot blowers SB-102A/B until TIC-1345 is at or above 145 °C (wet deposits plug the cold end).
4. If the start was on natural draft, bring the APH on line and close the bypass per SOP — FD / ID Fan Trip Response and Natural-Draft Operation, Rev 1.0, Section 7, before firing above 60%.

## 8. Heat-up to Operating Temperature

| Parameter | Limit during heat-up | Tag |
|---|---|---|
| COT rate of rise | ≤ 40 °C/h | TIC-1110 |
| Tube skin temperature | < 585 °C Hi; expect < 450 °C | TI-1121A..1124B |
| Pass outlet spread | ±6 °C of average (TDA-1111..1114) | TT-1111..1114 |
| Bridgewall | ≤ 900 °C | TT-1301A/B |
| Arch draft | −2.5 mmH2O, never positive (trip +10 mmH2O, 5 s) | PIC-1311, PT-1314 |
| O2 / CO | 3.0% dry; CO < 200 ppm | AIC-1321, AT-1322 |
| Fan speed | ≤ 95% | SI-1341, SI-1351 |

1. Raise firing in steps by fuel gas pressure, keeping PIC-1202 between 0.5 and 2.2 barg (PT-1207 HH trip 2.5 barg).
2. At COT 340 °C and stable, raise pass flows to plan (71.5 t/h each) and put TIC-1110 in CASCADE to PIC-1202.
3. Balance passes per Control Narrative — Pass Flow Control and Pass Balancing, Rev 2.1.
4. Agree the rate of COT rise with the C-101 operator: flash-zone vaporization, the column temperature profile and product draws all come up with COT, so the column start-up sets the pace. The final COT is the given production target (360 °C); do not change it without the unit supervisor and the column operator.

## 9. Records

Log: rotor and fan start times, purge start/complete, gas test result, each burner light-off, the time TIC-1345 reached 145 °C and the time COT reached 360 °C. After a decoke or APH work, record the clean baselines per Maintenance Procedure — Mechanical Pigging Decoke of H-101 Coil, Rev 2.7, Section 8 and Maintenance Procedure — Air Preheater Seal Inspection, Soot Blowing and Water Washing, Rev 1.0, Section 9.
