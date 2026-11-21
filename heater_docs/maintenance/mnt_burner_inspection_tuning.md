---
doc_id: mnt_burner_inspection_tuning
doc_type: maintenance
equipment: [burners, radiant_section, fuel_gas_system, fuel_gas_ko_drum, pilot_gas_system, fd_fan, air_preheater, bypass_dampers, flue_gas_analyzers, bms_sis]
tags: [BS-1211, BS-1212, BS-1213, BS-1214, BS-1215, BS-1216, BS-1217, BS-1218, PIC-1202, PT-1206, PT-1207, PT-1208, LT-1205, FT-1201, AT-1203, AIC-1321, AT-1322, AT-1325, FIC-1341, PT-1342, TT-1343, ZT-1362, PIC-1311, PT-1312, TT-1301A, TT-1301B, TI-1121A, TI-1122A, TI-1123A, TI-1124A]
title: Maintenance Procedure — Burner Inspection, Cleaning and Tuning
revision: 2.0
date: 2026-11-20
---

# Maintenance Procedure — Burner Inspection, Cleaning and Tuning

**Document No.:** H101-MNT-006
**Revision:** 2.0 | **Date:** 2026-11-20
**Revision note:** Rev 2.0 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).
**Applicability:** Unit 100 — H-101 Crude Charge Heater, burners B-101A..H and pilots
**Owner:** Fired Heater Maintenance / Process Engineering
**P&ID Reference:** U100-PID-102 (combustion, fuel gas, burners, BMS)
**Frequency:** Inspection monthly (on-line); tip cleaning on condition; full tuning after cleaning and annually

---

## 1. Scope and Purpose

H-101 has eight forced-draft low-NOx gas burners, B-101A..H, floor-mounted in one row in a common hot-air windbox. Combustion air comes from FD fan K-101 through air preheater E-102 at ≈ 300 °C (TT-1343) and ≈ +60 mmH2O windbox pressure (PT-1342); total air is set by FIC-1341 under the O2 controller AIC-1321, and each burner's share by its air register, which is set at tuning. Normal heat release is 4.8 MW per burner, design 5.8 MW (120%), at 1.2 barg fuel gas on PIC-1202. Equipment data: Equipment Datasheet — B-101A–H Process Burners, Rev 1.7.

Burner condition decides flame shape: a fouled tip or mis-set register gives long, leaning flames that impinge on the radiant tubes, raising local flux and tube metal temperature, and raises CO and NOx. Hot combustion air raises flame temperature, so NOx (AT-1325) is more sensitive to register and O2 settings than with ambient air.

## 2. On-Line Inspection (monthly)

1. Through the burner sight ports and side-wall peepholes, record for each burner: flame height and colour, lean direction, impingement, lift-off, tile condition and pilot flame. **The windbox is under positive pressure with ≈ 300 °C air** — open sight ports only with the face shield down and stand to the side.
2. Read flame scanner signal strength for BS-1211..1218 at the BMS. A signal falling over weeks points to a dirty sight tube or weakening flame.
3. Record burner-front fuel pressure (local gauge) for each burner. With clean tips, pressures agree within 0.05 bar; a burner reading higher than its neighbours has partially plugged tips.
4. Record AIC-1321, AT-1322 CO, AT-1325 NOx, FIC-1341, PT-1342, TT-1343, PIC-1311 and PT-1312 floor draft (≈ −10 mmH2O).

| Observation | Probable cause |
|---|---|
| Long, lazy, yellow flame | Low air at that burner (register closed, tramp air making AIC-1321 read rich in air), or plugged tips |
| Flame leaning toward tubes | Plugged or eroded tip ports, damaged tile, uneven register or windbox air distribution |
| Flame lifting / pulsing | Fuel pressure too high, windbox pressure too high, high H2 or changing LHV (AT-1203) |
| Burner pressure high, flame short | Partially plugged tips |
| Liquid flicker, sparking, smoky flame | Liquid carryover — check V-101 level LT-1205 and drains |
| All flames shorter and NOx up after APH cleaning | Hotter air (TT-1343 up) — expected; re-check NOx against permit |

## 3. On-Line Tip Cleaning (one burner at a time)

1. Obtain permit; inform the console. Confirm margins: TI-1121A..1124B below 570 °C, COT steady, AT-1322 below 50 ppm.
2. **Only one burner out of service at a time.** With one burner out, the other seven carry ≈ 5.5 MW each at normal firing (38.5 MW), inside the 5.8 MW design rating. Reduce charge if firing is above normal.
3. De-select the burner at the BMS so its flame loss is not counted toward the 3-of-8 flame-failure trip. Close the gas cock; leave the pilot lit.
4. **Close that burner's air register fully before removing the gun.** With the register open, hot air (≈ 300 °C) blows out of the gun port — a burn hazard — and air through the idle burner bypasses the flames while AIC-1321 still counts it.
5. Remove the gas gun; inspect for coke, scale and erosion. Clean tip ports with the correct drill gauge by hand — **never enlarge a port**. Replace eroded or out-of-gauge tips. Check gaskets and tip orientation.
6. Reinstall the gun aligned to the tile; open the register to its tuned position; open the gas cock and confirm flame proven within the 10 s trial-for-ignition. Re-select at the BMS.
7. Watch the flame for 15 minutes before moving on.

## 4. Tuning (after cleaning)

1. Heater steady at reference charge, COT 360 °C, PIC-1311 at −2.5 mmH2O, AIC-1321 in AUTO at 3.0% cascaded to FIC-1341.
2. Set individual registers so all eight flames are of similar height and vertical; one notch at a time, 10 minutes between moves. Total air is held by FIC-1341, so a register move redistributes air between burners and changes windbox pressure PT-1342 slightly.
3. Confirm burner fuel pressures within 0.05 bar of each other.
4. Confirm AT-1322 CO below 50 ppm and AT-1325 NOx below 150 mg/Nm³ @ 3% O2 (permit).
5. Check CO stays below 200 ppm at AIC-1321 = 2.5%. If CO rises earlier, the burners are short of air (registers, tramp air) or the analyzer is suspect (Per SOP — Excess O2 Step Test (Analyzer / Air-Ingress Check), Rev 1.3).
6. Confirm TT-1301A/B within 760–900 °C and within 30 °C of each other.
7. Lock the registers and record their positions. Registers also govern burner air on natural draft (through D-102); any change in tuned positions must be reviewed by process engineering for natural-draft capability (Per SOP — FD / ID Fan Trip Response and Natural-Draft Operation, Rev 1.0).

## 5. Outage Work

During outages (e.g. a decoke): remove all guns for shop cleaning and gauging; inspect tiles and repair with castable; clean scanner sight tubes; check pilots and igniters; verify register movement over full travel; inspect the windbox interior for insulation damage and debris; stroke-test the D-102 emergency air doors XV-1362 and confirm ZT-1362 indication and the door seals (a leaking door lets hot air escape, so FD air is wasted).

## 6. Records

Record per burner: findings, burner pressure, scanner signal, tips cleaned or replaced, register positions as-found / as-left, and the heater O2, CO, NOx, FIC-1341, PT-1342 and TT-1343 after tuning. Report any burner needing cleaning more often than monthly — and any liquid in tips — to process engineering (fuel gas quality or V-101 drainage).
