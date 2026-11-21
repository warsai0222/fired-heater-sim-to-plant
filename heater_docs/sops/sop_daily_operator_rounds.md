---
doc_id: sop_daily_operator_rounds
doc_type: sop
equipment: [heater_h101, radiant_section, radiant_coil, convection_section, burners, fuel_gas_system, fuel_gas_ko_drum, pilot_gas_system, stack, air_preheater, fd_fan, id_fan, bypass_dampers, flue_gas_analyzers, snuffing_steam, soot_blowers]
tags: [TIC-1110, TT-1111, TT-1112, TT-1113, TT-1114, TI-1121A, TI-1121B, TI-1122A, TI-1122B, TI-1123A, TI-1123B, TI-1124A, TI-1124B, PDI-1101, PDI-1102, PDI-1103, PDI-1104, FT-1201, PIC-1202, LT-1205, PT-1208, TT-1301A, TT-1301B, TT-1303, PIC-1311, PT-1312, AIC-1321, AT-1322, AT-1327, AT-1326, FIC-1341, PT-1342, TT-1343, TIC-1345, PDT-1347, PDT-1348, XS-1349, SI-1341, SI-1351, JI-1341, JI-1351, ZT-1361, ZT-1362, PI-1403, HS-1501]
title: SOP — H-101 Daily Operator Rounds and Firebox Inspection
revision: 2.1
date: 2026-11-20
---

# SOP — H-101 Daily Operator Rounds and Firebox Inspection

**Document No.:** H101-SOP-005
**Revision:** 2.1 | **Date:** 2026-11-20
**Revision note:** Rev 2.1 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).
**Applicability:** Unit 100 — H-101 Crude Charge Heater
**Owner:** Unit 100 Operations (Area Field Operator)
**P&ID Reference:** U100-PID-101 (process coil), U100-PID-102 (combustion, fuel gas, burners, BMS), U100-PID-103 (air preheater, fans, dampers, stack)

---

## 1. Scope and Frequency

The H-101 field operator completes these rounds **once per 12-hour shift**, and in addition after any trip, natural-draft runback, crude switch, burner or APH work, or abnormal alarm. The rounds combine a console readings check, a field equipment check (now including fans K-101/K-102, air preheater E-102 and dampers D-101/D-102) and a visual firebox inspection. Many slow problems — flame impingement, hot spots, tramp air, burner fouling, APH seal wear — are seen in the field or in the trends long before an alarm.

PPE for firebox viewing: face shield with shade 5 lens, FR clothing, gloves. Stand to the side when opening a peephole. The burner windbox is under **positive** hot-air pressure (≈ +60 mmH2O, ≈ 300 °C): never open a burner sight port or windbox door without the burner's register closed.

## 2. Console Readings Check — Process and Firebox

Record on the round sheet; report anything in the "action" column to the console operator immediately.

| Tag | Service | Normal | Action if |
|---|---|---|---|
| TIC-1110 | Combined COT | 360 °C | outside 352–368 °C |
| TT-1111..1114 | Pass outlet temps | 360 °C | any pass > ±6 °C from average |
| TI-1121A..1124B | Tube skin temps | ≈ 430 °C (clean, SOR) | > 585 °C Hi, or > 15 °C rise since last shift |
| PDI-1101..1104 | Pass coil ΔP | 6.0 bar (clean) | > 7.8 bar Hi, or one pass ≥ 0.5 bar above the others |
| TT-1301A/B | Bridgewall | ≈ 845 °C | outside 760–900 °C |
| TT-1303 | Convection outlet / APH gas inlet | ≈ 390 °C | > 440 °C Hi, or > 15 °C above post-soot-blow baseline |
| AIC-1321 | Arch O2 (dry) | 3.0% | < 1.5% Lo or > 5.0% Hi |
| AT-1322 | Arch CO | ≈ 30 ppm | > 200 ppm Hi |
| PIC-1311 | Arch draft | −2.5 mmH2O | above −0.5 (Hi) or below −6.0 (Lo) |
| FT-1201 | Fuel gas flow | 2,860 kg/h | > 3,430 kg/h Hi |

## 3. Console Readings Check — Air Preheater, Fans and O2 Chain

| Tag | Service | Normal | Action if |
|---|---|---|---|
| AT-1327 − AIC-1321 | Convection-section air ingress | ≈ 0.2% | > 0.8% sustained |
| AT-1326 − AT-1327 | APH seal leakage | ≈ 1.2% | > 2.0% sustained |
| TIC-1345 | APH gas outlet (cold end) | ≈ 150 °C | < 145 °C Lo, < 140 °C LL |
| TT-1343 | Hot air to burners | ≈ 300 °C | < 250 °C or > 340 °C |
| PDT-1347 / PDT-1348 | APH gas / air ΔP | 80 / 50 mmH2O | > 120 / > 75 mmH2O Hi |
| FIC-1341 | Combustion air flow | 57,850 kg/h | < 45,000 kg/h Lo |
| PT-1342 | Windbox pressure | +60 mmH2O | < 20 mmH2O Lo |
| SI-1341 / SI-1351 | FD / ID fan speed | 70% / 72% | > 95% Hi, or > 5 points above last week at same firing |
| JI-1341 / JI-1351 | FD / ID motor power | 32 / 42 kW | > 60 / > 75 kW |
| ZT-1361 / ZT-1362 | Bypass damper / air doors | 0% | > 5% open |
| XS-1349 | APH rotor rotation | 1 (turning) | 0 — runback; see Section 6 |

A slow rise in AT-1326 − AT-1327 together with rising SI-1351 points to APH seal leakage; a rise in PDT-1347 with falling TT-1343 points to APH fouling (Per Troubleshooting Guide — Air Preheater Leakage, Fouling and Low Cold-End Temperature, Rev 1.0).

## 4. Field Equipment Check

1. **V-101:** gauge glass vs LT-1205 (≈ 10%); drain if above normal and report liquids — they foul burner tips and cause flame-outs.
2. **Fuel and pilot gas:** manifold gauge agrees with PIC-1202 within 0.1 barg; pilot gauge agrees with PT-1208 (0.7 barg); portable detector at burner-front flanges.
3. **Snuffing steam:** PI-1403 ≥ 2.5 barg; traps on the XV-1401 and HV-1402 lines working.
4. **FD fan K-101 and ID fan K-102:** listen for rubbing or change in noise; check bearing housings by hand-held vibration pen and IR gun against the posted baseline; oil level and colour; no leaks at the ID fan shaft seal (hot flue gas). Note VFD panel alarms.
5. **Air preheater E-102:** rotor turning (local indicator agrees with XS-1349); drive motor and gearbox not overheating, no oil leaks at the support and guide bearings; no unusual seal rubbing noise; casing and expansion joints free of hot spots or flue-gas leaks.
6. **Dampers:** D-101 bypass damper and D-102 emergency air doors closed, local indicators agree with ZT-1361 / ZT-1362; actuators healthy (they must fail open on demand). Cold-air bypass TV-1345 position consistent with TIC-1345 (normally closed).
7. **Casing and header boxes:** IR gun for hot or cool spots (cool spots on a negative-pressure casing are air in-leaks); header box doors latched. Note casing above 90 °C.
8. **Soot blowers SB-101A..F and SB-102A/B:** all lances retracted, no steam leaking at the wall boxes; last HS-1501 sequence completed normally.

## 5. Firebox Inspection Through Peepholes

Inspect from all peepholes on both side walls at burner level and mid-height, and the arch-level ports.

1. **Flames (B-101A..H):** each flame stable, compact and vertical, similar height to its neighbours. Report flames leaning toward or touching tubes; long, lazy, yellow or smoky flames; flames lifting or pulsing; a burner short or out of pattern. Hot combustion air shortens and brightens flames compared with ambient-air firing (as seen during a natural-draft runback) — compare with neighbours, not with memory.
2. **Radiant tubes:** uniform dull colour. Report any bright spot, streak, scale flaking, bowing or hanger out of position. Compare with the nearest skin TC (TI-1121A..1124B) — a visual hot spot with a normal TC reading is still reported.
3. **Refractory and tiles:** no fallen refractory, cracked tiles or glowing casing behind the lining.
4. **Convection entry:** no visible flame entering the shield tubes (afterburning).
5. **Close every peephole door after viewing.** An open peephole is a tramp-air leak (Per Maintenance Procedure — Tramp Air Survey and Casing Sealing, Rev 1.5).

## 6. Reporting and Escalation

| Finding | Action |
|---|---|
| Flame impingement on tubes | Inform console; Per Maintenance Procedure — Burner Inspection, Cleaning and Tuning, Rev 2.0 |
| Visual tube hot spot | Inform console and shift superintendent; Per Troubleshooting Guide — High Tube Metal Temperature, Rev 2.4 |
| Smoke, afterburning or positive draft | Inform console immediately; Per Troubleshooting Guide — Positive Draft and Afterburning, Rev 1.8 |
| Fan vibration/noise change, APH rotor stopped, damper open | Inform console immediately; Per SOP — FD / ID Fan Trip Response and Natural-Draft Operation, Rev 1.0 |
| Gas smell / leak at burner front | Clear the area, inform console, consider HS-1290 |

Sign and file the round sheet; transcribe exceptions into the shift log.
