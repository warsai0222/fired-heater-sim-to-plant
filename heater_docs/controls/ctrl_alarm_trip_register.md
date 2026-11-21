---
doc_id: ctrl_alarm_trip_register
doc_type: controls
equipment: [heater_h101, radiant_section, radiant_coil, convection_section, burners, fuel_gas_system, fuel_gas_ko_drum, pilot_gas_system, air_preheater, fd_fan, id_fan, bypass_dampers, stack, flue_gas_analyzers, pass_flow_control, transfer_line, snuffing_steam, soot_blowers, bms_sis]
tags: [TT-1001, FY-1100, TT-1100, PT-1100, FIC-1101, FIC-1102, FIC-1103, FIC-1104, FT-1151, FT-1152, FT-1153, FT-1154, PT-1101, PT-1102, PT-1103, PT-1104, PDI-1101, PDI-1102, PDI-1103, PDI-1104, TT-1131, TT-1132, TT-1133, TT-1134, TT-1111, TT-1112, TT-1113, TT-1114, TIC-1110, PT-1110, TI-1121A, TI-1121B, TI-1122A, TI-1122B, TI-1123A, TI-1123B, TI-1124A, TI-1124B, FT-1201, PIC-1202, PT-1206, PT-1207, AT-1203, TT-1204, LT-1205, PT-1208, BS-1211, BS-1212, BS-1213, BS-1214, BS-1215, BS-1216, BS-1217, BS-1218, TT-1301A, TT-1301B, TT-1302, TT-1303, PIC-1311, PT-1312, PT-1313, AIC-1321, AT-1322, AT-1326, AT-1325, PI-1403, HS-1501, HS-1290, FIC-1341, PT-1342, TT-1343, TIC-1345, AT-1327, PDT-1347, PDT-1348, XS-1349, PT-1314, PT-1352, SI-1341, SI-1351, JI-1341, JI-1351, XS-1341, XS-1351, ZT-1361, ZT-1362]
title: Alarm and Trip Setpoint Register — H-101 Crude Charge Heater
revision: 3.1
date: 2026-11-20
---

# Alarm and Trip Setpoint Register — H-101 Crude Charge Heater

**Document No.:** H101-CTRL-001
**Revision:** 3.1 | **Date:** 2026-11-20
**Applicability:** Unit 100 — H-101 Crude Charge Heater
**Owner:** Instrument & Controls Engineer (custodian); Unit 100 Process Engineer (setpoint basis)
**P&ID Reference:** U100-PID-101 (process coil), U100-PID-102 (combustion, fuel gas, burners, BMS), U100-PID-103 (air preheater, FD/ID fans, ducts, dampers, stack)
**Revision note:** Rev 3.1 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).

> This register is the single authoritative source for H-101 alarm and trip setpoints. The DCS, the
> SIS/BMS configuration and all datasheets must agree with it. Any change requires a Management of
> Change (MOC) signed by the Process Engineer and the I&C Engineer; changes to SIS trip or runback
> setpoints also require the SIS owner and a review against BMS / SIS Cause and Effect — H-101, Rev 3.3.
> Rev 3.1 lists all 86 registered tags, grouped by service. The Rev A stack-damper and
> plenum-louvre position tags and final elements are deleted with that equipment.

---

## 1. Conventions — Alarms, Trips and Natural-Draft Runbacks

| Column / mark | Meaning |
|---------------|---------|
| Normal | Design-case value (ANS, 50,000 bbl/d, clean, balanced draft) |
| L / H | Operator alarm, low / high (DCS) |
| LL / HH **(trip)** | **SIS/BMS trip** — automatic fuel shutdown, independent SIS transmitter |
| LL **(runback)** | **Natural-draft runback** — automatic, not a fuel trip: D-101 (XV-1361) and D-102 (XV-1362) open, the other fan stops, firing clamped to ≤ 60% |
| LL / HH (alarm) | **Operator alarm only** — nothing trips automatically |
| — | No setpoint configured on that side |

**Fuel trips** (automatic shutdown): pass low-low flow FT-1151..1154; fuel gas pressure low-low PT-1206
and high-high PT-1207; KO drum level high-high LT-1205 / LSHH-1205; pilot gas low-low PT-1208 (total
trip); flame loss on ≥ 3 of 8 burners BS-1211..1218; firebox pressure high-high PT-1314; manual ESD
HS-1290 (total trip). **Runbacks:** FD fan stop XS-1341, ID fan stop XS-1351, APH rotor stop XS-1349.
**Operator alarms only:** high TMT, high COT, low/low-low O2, high CO, high coil ΔP, high bridgewall,
arch draft at 0.0 mmH₂O, low APH gas outlet temperature, high fan speed. These are the limits the
operator and the optimizer must respect; exceeding them is a limit violation, not a trip.

Priority: SIS trip and runback pre-alarms and integrity limits (TMT HH, coil ΔP HH, O2 LL, CO HH, draft
HH, TIC-1345 LL, D-101/D-102 open in balanced draft) = **High**; other H/L alarms = **Medium**;
equipment-status alarms = **Low**.

## 2. Process — Charge, Pass Flow and Coil Pressure (U100-PID-101)

| Tag | Description | Units | Normal | LL | L | H | HH | Type / response |
|-----|-------------|-------|--------|----|---|---|----|-----------------|
| FY-1100 | Total crude charge (sum of 4 pass flows) | t/h | 286 | — | 250 | — | — | Alarm — check P-101A/B and preheat train; charge changes agreed with C-101 |
| TT-1100 | Heater inlet crude temperature | °C | 250 | — | 235 | 265 | — | Alarm — preheat-train upset; firing follows with lag |
| PT-1100 | Heater inlet header pressure | barg | 11.0 | — | 9.0 | — | — | Alarm — loss of charge-pump head; FV-1101..1104 losing control margin |
| FIC-1101 | Pass A flow control | t/h | 71.5 | — | 60 | 80 | — | Alarm — restore pass flow before SIS LL 43 t/h (FT-1151) |
| FIC-1102 | Pass B flow control | t/h | 71.5 | — | 60 | 80 | — | Alarm — as FIC-1101 (FT-1152) |
| FIC-1103 | Pass C flow control | t/h | 71.5 | — | 60 | 80 | — | Alarm — as FIC-1101 (FT-1153) |
| FIC-1104 | Pass D flow control | t/h | 71.5 | — | 60 | 80 | — | Alarm — as FIC-1101 (FT-1154) |
| PT-1101 | Pass A coil inlet pressure (downstream of FV) | barg | 8.5 | — | — | — | — | Indication (PDI-1101 input) |
| PT-1102 | Pass B coil inlet pressure | barg | 8.5 | — | — | — | — | Indication (PDI-1102 input) |
| PT-1103 | Pass C coil inlet pressure | barg | 8.5 | — | — | — | — | Indication (PDI-1103 input) |
| PT-1104 | Pass D coil inlet pressure | barg | 8.5 | — | — | — | — | Indication (PDI-1104 input) |
| PDI-1101 | Pass A coil pressure drop (PT-1101 minus PT-1110) | bar | 6.0 | — | — | 7.8 | 8.4 (alarm) | Alarm only — coke indicator; HH = hydraulic end-of-run limit |
| PDI-1102 | Pass B coil pressure drop | bar | 6.0 | — | — | 7.8 | 8.4 (alarm) | Alarm only — as PDI-1101 |
| PDI-1103 | Pass C coil pressure drop | bar | 6.0 | — | — | 7.8 | 8.4 (alarm) | Alarm only — as PDI-1101 |
| PDI-1104 | Pass D coil pressure drop | bar | 6.0 | — | — | 7.8 | 8.4 (alarm) | Alarm only — as PDI-1101 |
| PT-1110 | Coil outlet pressure | barg | 2.5 | — | — | 3.2 | — | Alarm — transfer-line / C-101 backpressure; raises coil ΔP reference |

PDI-1101..1104 HH 8.4 bar is ≈ 40% above the clean 6.0 bar: an end-of-run criterion, not a trip.
Response: Troubleshooting Guide — Rising Coil Pressure Drop, Rev 1.9. Pass flow practice: Control
Narrative — Pass Flow Control and Pass Balancing, Rev 2.1.

## 3. Process — Crossover, Pass Outlet and Coil Outlet Temperatures (U100-PID-101)

| Tag | Description | Units | Normal | LL | L | H | HH | Type / response |
|-----|-------------|-------|--------|----|---|---|----|-----------------|
| TT-1131 | Pass A crossover temperature (convection outlet) | °C | 292 | — | — | 310 | — | Alarm — convection-side heat pickup |
| TT-1132 | Pass B crossover temperature | °C | 292 | — | — | 310 | — | Alarm — as TT-1131 |
| TT-1133 | Pass C crossover temperature | °C | 292 | — | — | 310 | — | Alarm — as TT-1131 |
| TT-1134 | Pass D crossover temperature | °C | 292 | — | — | 310 | — | Alarm — as TT-1131 |
| TT-1111 | Pass A outlet temperature | °C | 360 | — | 352 | 368 | — | Alarm; also TDA-1111 deviation (±6 °C) |
| TT-1112 | Pass B outlet temperature | °C | 360 | — | 352 | 368 | — | Alarm; also TDA-1112 deviation |
| TT-1113 | Pass C outlet temperature | °C | 360 | — | 352 | 368 | — | Alarm; also TDA-1113 deviation |
| TT-1114 | Pass D outlet temperature | °C | 360 | — | 352 | 368 | — | Alarm; also TDA-1114 deviation |
| TIC-1110 | Combined coil outlet temperature (COT) control | °C | 360 | — | 352 | 368 | 375 (alarm) | Alarm only — HH is not a trip; reduce firing; tell C-101 operator |

COT target is 360 ± 2 °C, a given production target. A COT change or a COT that cannot be held (e.g.
during a natural-draft runback) changes C-101 flash-zone vaporization and cut yields; inform the C-101
operator. A coked pass runs a slightly cooler outlet while TIC-1110 fires harder. Response:
Troubleshooting Guide — Pass Outlet Temperature Imbalance, Rev 2.0.

## 4. Process — Tube Skin Temperatures (TMT) (U100-PID-101)

| Tag | Description | Units | Normal | LL | L | H | HH | Type / response |
|-----|-------------|-------|--------|----|---|---|----|-----------------|
| TI-1121A | Pass A tube skin temperature (hot zone upper) | °C | 430 | — | — | 585 | 600 (alarm) | Alarm only — HH = P9 TMT operating limit (EOR) |
| TI-1121B | Pass A tube skin temperature (hot zone lower) | °C | 430 | — | — | 585 | 600 (alarm) | Alarm only — HH = P9 TMT operating limit (EOR) |
| TI-1122A | Pass B tube skin temperature (hot zone upper) | °C | 430 | — | — | 585 | 600 (alarm) | Alarm only — HH = P9 TMT operating limit (EOR) |
| TI-1122B | Pass B tube skin temperature (hot zone lower) | °C | 430 | — | — | 585 | 600 (alarm) | Alarm only — HH = P9 TMT operating limit (EOR) |
| TI-1123A | Pass C tube skin temperature (hot zone upper) | °C | 430 | — | — | 585 | 600 (alarm) | Alarm only — HH = P9 TMT operating limit (EOR) |
| TI-1123B | Pass C tube skin temperature (hot zone lower) | °C | 430 | — | — | 585 | 600 (alarm) | Alarm only — HH = P9 TMT operating limit (EOR) |
| TI-1124A | Pass D tube skin temperature (hot zone upper) | °C | 430 | — | — | 585 | 600 (alarm) | Alarm only — HH = P9 TMT operating limit (EOR) |
| TI-1124B | Pass D tube skin temperature (hot zone lower) | °C | 430 | — | — | 585 | 600 (alarm) | Alarm only — HH = P9 TMT operating limit (EOR) |

Clean SOR hottest TMT ≈ 430 °C. 600 °C is the ASTM A335 P9 operating limit (end-of-run criterion),
configured as an HH **alarm**, not a trip: a skin-thermocouple trip would cause spurious shutdowns and
thermal cycling. Limits and time allowed above the alarm: Integrity Operating Windows (IOW) — H-101
Radiant Coil, Rev 2.1; response: Troubleshooting Guide — High Tube Metal Temperature, Rev 2.4. Check
TMT against the coil ΔP of the same pass before acting on a single thermocouple.

## 5. Fuel Gas and Pilot Gas (U100-PID-102)

| Tag | Description | Units | Normal | LL | L | H | HH | Type / response |
|-----|-------------|-------|--------|----|---|---|----|-----------------|
| FT-1201 | Fuel gas mass flow to burners | kg/h | 2,860 | — | — | 3,430 | — | Alarm — ≈ 120% heat release (≈ 46 MW LHV) firing limit |
| PIC-1202 | Fuel gas pressure to burner manifold (COT cascade slave) | barg | 1.2 | — | 0.35 | 2.2 | — | Alarm — pre-alarm to PT-1206 / PT-1207 trips |
| AT-1203 | Fuel gas lower heating value (calorimeter) | MJ/kg | 48.5 | — | 44 | 52 | — | Alarm — fuel composition upset |
| TT-1204 | Fuel gas temperature | °C | 40 | — | — | — | — | Indication |
| LT-1205 | Fuel gas KO drum level | % | 10 | — | — | 50 | **80 (trip)** | H = drain V-101; **HH (LSHH-1205) = SIS main fuel trip** |
| PT-1208 | Pilot gas pressure | barg | 0.7 | **0.25 (trip)** | 0.4 | — | — | L = alarm; **LL = SIS total trip** (main fuel + XV-1209) |

During a natural-draft runback the BMS clamps the PIC-1202 setpoint at ≈ 0.43 barg (≤ 60% firing) and
lowers its normal low clamp to 0.40 barg; PIC-1202 Lo alarm (0.35 barg) and the PT-1206 trip (0.25
barg) are unchanged. Fuel system data: Equipment Datasheet — Fuel Gas and Pilot Gas System (incl.
V-101), Rev 1.4.

## 6. Combustion Air — FD Fan, APH Air Side and Air Doors (U100-PID-103)

| Tag | Description | Units | Normal | LL | L | H | HH | Type / response |
|-----|-------------|-------|--------|----|---|---|----|-----------------|
| FIC-1341 | Combustion air flow (FD discharge; includes APH leakage) | kg/h | 57,850 | — | 45,000 | — | — | Alarm — low air for firing; check FD fan K-101 / SC-1341; cross-limit restricts firing |
| PT-1342 | Burner windbox (hot air) pressure | mmH₂O | 60 | — | 20 | — | — | Alarm — low burner air driving pressure; check FD fan, D-102 doors, APH air side |
| TT-1343 | Hot air temperature (APH air outlet) | °C | 300 | — | 250 | 340 | — | Alarm — L: APH fouling / rotor fault / TV-1345 open; H: abnormal, check for APH fire |
| PDT-1348 | APH air-side pressure drop | mmH₂O | 50 | — | — | 75 | — | Alarm — APH air-side fouling |
| SI-1341 | FD fan speed (VFD) | % | 70 | — | — | 95 | — | Alarm — FD fan at capacity limit (optimizer constraint); do not raise firing |
| JI-1341 | FD fan motor power | kW | 32 | — | — | 60 | — | Indication with Hi alarm — motor loading (75 kW motor) |
| ZT-1362 | Emergency air doors D-102 position (XV-1362) | % open | 0 | — | — | 5 | — | Alarm (High priority) — D-102 not closed in balanced draft: hot air escaping, burn hazard |

FIC-1341 is measured at the FD discharge and includes APH seal leakage, so for the same reading less
air reaches the burners as leakage grows. The 95% speed limits (with motor power alarms as a backstop) are capacity
limits, not trips. Fan data: Equipment Datasheet — K-101 Forced Draft Fan and K-102 Induced Draft Fan,
Rev 1.0; APH data: Equipment Datasheet — E-102 Regenerative Air Preheater, Rev 1.0.

## 7. Flue Gas — Temperatures, Draft, ID Fan and APH Gas Side (U100-PID-102 / U100-PID-103)

| Tag | Description | Units | Normal | LL | L | H | HH | Type / response |
|-----|-------------|-------|--------|----|---|---|----|-----------------|
| TT-1301A | Bridgewall temperature A (radiant exit) | °C | 845 | — | 760 | 900 | 930 (alarm) | Alarm only — envelope 760–900 °C |
| TT-1301B | Bridgewall temperature B (radiant exit) | °C | 845 | — | 760 | 900 | 930 (alarm) | Alarm only — envelope 760–900 °C |
| TT-1302 | Flue gas temperature between shield and studded rows | °C | 740 | — | — | 800 | — | Alarm — overfiring or afterburning |
| TT-1303 | Convection outlet / APH gas inlet temperature | °C | 390 | — | — | 440 | — | Alarm — convection fouling / afterburning; APH inlet |
| PIC-1311 | Arch draft control | mmH₂O | −2.5 | — | −6.0 | −0.5 | 0.0 (alarm) | Alarm only — HH = positive arch pressure; reduce firing, check ID fan; trip is PT-1314 |
| PT-1312 | Floor (burner level) draft | mmH₂O | −10.0 | — | — | −6.0 | — | Alarm — low floor draft |
| PT-1313 | Draft at convection outlet / APH gas inlet | mmH₂O | −20.0 | — | — | — | — | Indication |
| TIC-1345 | APH gas outlet temperature (cold-end control) | °C | 150 | 140 (alarm) | 145 | — | — | Alarm only — L: cold end near limit, check TV-1345; LL = acid dew point margin (optimizer limit) |
| PDT-1347 | APH gas-side pressure drop | mmH₂O | 80 | — | — | 120 | — | Alarm — APH gas-side fouling; soot blow SB-102A/B |
| PT-1352 | ID fan inlet pressure | mmH₂O | −120 | — | — | — | — | Indication — ID fan suction; rises in magnitude with APH fouling |
| SI-1351 | ID fan speed (VFD) | % | 72 | — | — | 95 | — | Alarm — ID fan at capacity limit (optimizer constraint); do not raise firing |
| JI-1351 | ID fan motor power | kW | 42 | — | — | 75 | — | Indication with Hi alarm — motor loading |
| ZT-1361 | Flue-gas bypass damper D-101 position (XV-1361) | % open | 0 | — | — | 5 | — | Alarm — D-101 not closed in balanced draft: gas short-circuit, lost recovery |

Arch draft at 0.0 mmH₂O (PIC-1311 HH) is an alarm; the trip is the independent SIS transmitter PT-1314
at +10 mmH₂O for 5 s (Section 9). TIC-1345 LL 140 °C is the acid-dew-point margin and an optimizer
limit, not a trip. Responses: Troubleshooting Guide — Positive Draft and Afterburning, Rev 1.8;
Troubleshooting Guide — Air Preheater Leakage, Fouling and Low Cold-End Temperature, Rev 1.0;
Troubleshooting Guide — High Stack Temperature, Rev 1.7.

## 8. Flue Gas — Analyzers (U100-PID-102 / U100-PID-103)

| Tag | Description | Units | Normal | LL | L | H | HH | Type / response |
|-----|-------------|-------|--------|----|---|---|----|-----------------|
| AIC-1321 | Arch excess O2 control (dry basis) | vol% dry | 3.0 | 1.0 (alarm) | 1.5 | 5.0 | — | Alarm only — LL requires immediate operator action, no trip |
| AT-1322 | Arch CO | ppm | 30 | — | — | 200 | 1,000 (alarm) | Alarm only — H = optimizer CO limit; HH = combustibles, sub-stoichiometric firing |
| AT-1326 | Stack O2 (CEMS) | vol% dry | 4.4 | — | — | — | — | Indication — AT-1326 − AT-1327 ≈ 1.2 normal (APH leakage check) |
| AT-1325 | Stack NOx (CEMS) | mg/Nm³ @ 3% O2 | 80 | — | — | 150 | — | Alarm — permit limit 150 mg/Nm³ |
| AT-1327 | O2 at convection outlet / APH gas inlet | vol% dry | 3.2 | — | — | — | — | Indication — AT-1327 − AIC-1321 ≈ 0.2 normal (convection ingress check) |

The O2 LL 1.0% and CO HH 1000 ppm are operator alarms. Air leaking in below the arch makes AIC-1321
read above burner-level O2, so AT-1322 CO is the more direct indicator of incomplete combustion.
Normal differences: AT-1327 − AIC-1321 ≈ 0.2 (investigate > ≈ 0.8, convection ingress); AT-1326 −
AT-1327 ≈ 1.2 (investigate > ≈ 2.0, APH seal leakage). Response: Troubleshooting Guide — Low Excess O2
/ High CO, Rev 2.5; Troubleshooting Guide — High O2 Reading / Suspected Air Ingress, Rev 1.6.

## 9. SIS / BMS Initiators

| Tag | Description | Units | Normal | LL | L | H | HH | Type / response |
|-----|-------------|-------|--------|----|---|---|----|-----------------|
| FT-1151 | Pass A flow (SIS transmitter) | t/h | 71.5 | **43 (trip)** | — | — | — | **Main fuel trip**, 2 s delay; pilots stay lit |
| FT-1152 | Pass B flow (SIS transmitter) | t/h | 71.5 | **43 (trip)** | — | — | — | **Main fuel trip**, 2 s delay |
| FT-1153 | Pass C flow (SIS transmitter) | t/h | 71.5 | **43 (trip)** | — | — | — | **Main fuel trip**, 2 s delay |
| FT-1154 | Pass D flow (SIS transmitter) | t/h | 71.5 | **43 (trip)** | — | — | — | **Main fuel trip**, 2 s delay |
| PT-1206 | Fuel gas burner pressure low-low (SIS) | barg | 1.2 | **0.25 (trip)** | — | — | — | **Main fuel trip** (flame stability) |
| PT-1207 | Fuel gas burner pressure high-high (SIS) | barg | 1.2 | — | — | — | **2.5 (trip)** | **Main fuel trip** (lift-off / burner capacity) |
| BS-1211 | Burner B-101A flame scanner | on/off | 1 | **0 (trip)** | — | — | — | Burner isolated; ≥ 3 of 8 lost = **main fuel trip** |
| BS-1212 | Burner B-101B flame scanner | on/off | 1 | **0 (trip)** | — | — | — | As BS-1211 |
| BS-1213 | Burner B-101C flame scanner | on/off | 1 | **0 (trip)** | — | — | — | As BS-1211 |
| BS-1214 | Burner B-101D flame scanner | on/off | 1 | **0 (trip)** | — | — | — | As BS-1211 |
| BS-1215 | Burner B-101E flame scanner | on/off | 1 | **0 (trip)** | — | — | — | As BS-1211 |
| BS-1216 | Burner B-101F flame scanner | on/off | 1 | **0 (trip)** | — | — | — | As BS-1211 |
| BS-1217 | Burner B-101G flame scanner | on/off | 1 | **0 (trip)** | — | — | — | As BS-1211 |
| BS-1218 | Burner B-101H flame scanner | on/off | 1 | **0 (trip)** | — | — | — | As BS-1211 |
| HS-1290 | Manual emergency shutdown push-button (control room and field) | on/off | 0 | — | — | — | **1 (trip)** | **Total trip** (main fuel + pilots) |
| XS-1349 | APH rotor rotation monitor | on/off | 1 | **0 (runback)** | — | — | — | **Natural-draft runback** (as ID fan stop) + APH fire watch |
| PT-1314 | Firebox pressure high-high (SIS) | mmH₂O | −2.5 | — | — | — | **10 (trip)** | **Main fuel trip** at +10 mmH₂O for 5 s |
| XS-1341 | FD fan running status | on/off | 1 | **0 (runback)** | — | — | — | **Natural-draft runback** (not a fuel trip): open XV-1361/XV-1362, stop ID fan, firing ≤ 60% |
| XS-1351 | ID fan running status | on/off | 1 | **0 (runback)** | — | — | — | **Natural-draft runback**: open XV-1361/XV-1362, stop FD fan, firing ≤ 60% |

Main fuel trip = close XV-1201 and XV-1202, open bleed XV-1203; pilots stay lit. Total trip = main fuel
trip plus close pilot shutoff XV-1209. Natural-draft runback = open XV-1361 (D-101) and XV-1362
(D-102), confirmed by ZT-1361 / ZT-1362; stop the other fan; clamp firing to ≤ 60%; AIC-1321,
FIC-1341 and PIC-1311 to manual/track. If D-101 fails to open on an ID fan stop, firebox pressure rises
and PT-1314 trips main fuel. The DCS also alarms a > 5% deviation between FT-1151..1154 and
FIC-1101..1104. Full logic: BMS / SIS Cause and Effect — H-101, Rev 3.3; response: SOP — H-101
Emergency Shutdown and Trip Response, Rev 2.6, and SOP — FD / ID Fan Trip Response and Natural-Draft
Operation, Rev 1.0.

## 10. Utilities and Ambient

| Tag | Description | Units | Normal | LL | L | H | HH | Type / response |
|-----|-------------|-------|--------|----|---|---|----|-----------------|
| TT-1001 | Ambient air temperature | °C | 25 | — | — | — | — | Indication — affects FD air density and natural-draft capacity |
| PI-1403 | Snuffing steam header pressure | barg | 3.5 | — | 2.5 | — | — | Alarm — snuffing steam (XV-1401, HV-1402) not at full pressure |
| HS-1501 | Soot blower sequence status | step | 0 | — | — | — | — | Event log only (SB-101A–F, SB-102A/B) |

## 11. Calculated Alarms and Permissives

| Item | Basis | Setting | Type |
|------|-------|---------|------|
| TDA-1111..1114 | Each pass outlet TT-1111..1114 minus average of the four | ±6 °C | Operator alarm |
| LSHH-1205 | LT-1205 high-high switch function | 80% | SIS main fuel trip |
| FT-115x vs FIC-110x deviation | Per pass | 5% of reading | Operator alarm |
| Fired duty | FT-1201 × AT-1203 | Limit 46 MW LHV | Operator display; FT-1201 H alarm |
| Convection ingress | AT-1327 − AIC-1321 | > 0.8 point | Operator advisory |
| APH leakage | AT-1326 − AT-1327 | > 2.0 point | Operator advisory |
| Purge permissive | 5 firebox volume changes; both fans running (or D-101 / D-102 open); air flow ≥ 25% | — | Light-off permissive (blocks pilot/main light-off) |
