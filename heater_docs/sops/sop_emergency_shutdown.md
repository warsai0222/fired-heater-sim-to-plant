---
doc_id: sop_emergency_shutdown
doc_type: sop
equipment: [heater_h101, radiant_coil, burners, fuel_gas_system, fuel_gas_ko_drum, pilot_gas_system, air_preheater, fd_fan, id_fan, bypass_dampers, pass_flow_control, transfer_line, atmospheric_column, snuffing_steam, bms_sis, crude_charge_pumps]
tags: [HS-1290, FT-1151, FT-1152, FT-1153, FT-1154, FIC-1101, FIC-1102, FIC-1103, FIC-1104, PT-1206, PT-1207, PIC-1202, LT-1205, PT-1208, BS-1211, BS-1212, BS-1213, BS-1214, BS-1215, BS-1216, BS-1217, BS-1218, TIC-1110, PIC-1311, PT-1314, AIC-1321, AT-1322, FIC-1341, XS-1341, XS-1351, XS-1349, TIC-1345, TT-1303, TI-1121A, TI-1122A, TI-1123A, TI-1124A, PI-1403]
title: SOP — H-101 Emergency Shutdown and Trip Response
revision: 2.6
date: 2026-11-20
---

# SOP — H-101 Emergency Shutdown and Trip Response

**Document No.:** H101-SOP-003
**Revision:** 2.6 | **Date:** 2026-11-20
**Revision note:** Rev 2.6 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).
**Applicability:** Unit 100 — H-101 Crude Charge Heater
**Owner:** Unit 100 Operations (Shift Superintendent)
**P&ID Reference:** U100-PID-101 (process coil), U100-PID-102 (combustion, fuel gas, burners, BMS), U100-PID-103 (air preheater, fans, dampers, stack)

---

## 1. Scope and Purpose

This procedure tells the H-101 console and field operators what the SIS does on each trip, what they must verify, and what they must do next. The full logic is in BMS / SIS Cause and Effect — H-101, Rev 3.3; setpoints are in Alarm and Trip Setpoint Register — H-101 Crude Charge Heater, Rev 3.1.

H-101 has two trip levels and one automatic runback:
- **Main fuel trip** — XV-1201 and XV-1202 close, XV-1203 bleed opens. **Pilots stay lit** (XV-1209 stays open).
- **Total trip** — main fuel trip **plus** XV-1209 closes; pilots go out. A full purge is required before relight.
- **Natural-draft runback** (not a fuel trip) — on FD fan, ID fan or APH rotor stop the BMS opens bypass damper XV-1361 and emergency air doors XV-1362, stops the other fan, and clamps firing to ≤ 60%. This is handled in SOP — FD / ID Fan Trip Response and Natural-Draft Operation, Rev 1.0.

High TMT, high COT, low or high O2, high CO, high coil ΔP, low APH outlet temperature and high fan speed are **alarms, not trips**; they are handled under the troubleshooting guides.

## 2. Trip Initiators and Automatic Actions (H-101 SIS)

| Initiator | Setpoint | Automatic action |
|---|---|---|
| Any pass flow FT-1151..1154 low-low | < 43 t/h for 2 s | Main fuel trip |
| Fuel gas pressure PT-1206 low-low | < 0.25 barg | Main fuel trip |
| Fuel gas pressure PT-1207 high-high | > 2.5 barg | Main fuel trip |
| V-101 level LT-1205 high-high (LSHH-1205) | > 80% | Main fuel trip |
| Flame loss on 3 or more burners BS-1211..1218 | 3 of 8 | Main fuel trip |
| Firebox pressure PT-1314 high-high | > +10 mmH2O for 5 s | Main fuel trip |
| Pilot gas pressure PT-1208 low-low | < 0.25 barg | Total trip |
| Manual ESD HS-1290 (control room or field) | — | Total trip |
| FD fan stop XS-1341, ID fan stop XS-1351, APH rotor stop XS-1349 | = 0 | Natural-draft runback (not a trip) |

Loss of flame on a single burner closes that burner only and is alarmed; it is not a heater trip.

## 3. Immediate Actions — Any Trip (first 5 minutes)

1. **Confirm the trip on the BMS mimic:** XV-1201/1202 closed, XV-1203 open; for a total trip also XV-1209 closed. If a valve has not moved, press HS-1290 and close the manual fuel isolation upstream of V-101 in the field.
2. **Keep crude flowing through all four passes** unless the trip is a tube rupture (Section 6). FV-1101..1104 fail open; confirm FIC-1101..1104 steady.
3. Put TIC-1110 and PIC-1202 in MANUAL with PV-1202 output at 0% so the COT controller does not wind up and slam fuel in on reset.
4. **Keep both fans and the APH rotor running.** Put AIC-1321 in MANUAL and FIC-1341 on a local setpoint at purge air flow (≥ 25% of design, ≥ 14,500 kg/h); the fans sweep the firebox and cool the APH evenly. Keep PIC-1311 in AUTO on the ID fan — draft goes more negative as the box cools and the ID fan slows.
5. Confirm XS-1349 = 1. A hot rotor must not stop: if it does, follow SOP — FD / ID Fan Trip Response and Natural-Draft Operation, Rev 1.0, Section 5.
6. Inform the C-101 column operator: COT will fall quickly, flash-zone vaporization drops, distillate draws fall and more material goes to the bottoms. The column operator acts on draws, pumparounds and stripping steam.
7. Look through peepholes: only pilots (main fuel trip) or no flames (total trip); no fire in header boxes; no smoke at the stack.
8. TIC-1345 will fall below 145 °C as the gas cools; TV-1345 opens automatically. This is expected after a trip.
9. Record trip time and first-out initiator from the BMS sequence-of-events.

## 4. Initiator-Specific Follow-up

| First-out initiator | Verify | Corrective action before reset |
|---|---|---|
| Pass flow LL (FT-1151..1154) | Real flow loss vs transmitter fault: FT-115x vs FIC-110x; P-101A/B; FV position | Restore all passes ≥ 55 t/h; check TI-1121A..1124B of that pass; inspect tubes for bowing or glowing spots |
| Fuel gas LL (PT-1206) | Header pressure, PV-1202 failed closed, blocked tips | Restore header; stroke PV-1202 |
| Fuel gas HH (PT-1207) | PV-1202 failed open, regulator, header surge | Repair; confirm PIC-1202 clamps |
| KO drum HH (LT-1205) | Liquids in fuel gas; V-101 gauge glass | Drain V-101 below 50%; check supplier carryover; inspect tips |
| Flame loss ≥ 3 burners | Fuel quality (AT-1203), liquid carryover, low pressure, air flow upset (FIC-1341) | Identify cause; Per Maintenance Procedure — Burner Inspection, Cleaning and Tuning, Rev 2.0 |
| Firebox pressure HH (PT-1314) | ID fan speed loss or VFD fault (SC-1351), FD overspeed, damper or duct blockage, afterburning, tube rupture | Find and fix the cause; Per Troubleshooting Guide — Positive Draft and Afterburning, Rev 1.8; gas test before relight |
| Pilot gas LL (PT-1208) | Pilot regulator, supply | Restore supply; full purge required |
| Manual ESD HS-1290 | Reason for activation | Event-specific; full purge required |

## 5. Restart After a Trip

1. **Main fuel trip with pilots proven continuously** (except a PT-1314 trip, see step 2): after the cause is cleared and the shift superintendent authorizes, reset the BMS and relight from the proven pilots per SOP — H-101 Cold Start-up, Purge and Burner Light-off, Rev 3.2, Section 6 steps 3–7. Re-purge is not required **only** if every pilot stayed proven and both fans stayed running.
2. **Total trip, PT-1314 trip, or any doubt that all pilots stayed lit:** a full 5-volume-change purge with both fans running and air flow ≥ 25% is mandatory, preceded by a 0% LEL gas test (SOP — H-101 Cold Start-up, Purge and Burner Light-off, Rev 3.2, Sections 4–6).
3. Never re-attempt light-off more than once on the same trip without identifying the first-out cause.
4. On relight, agree the COT recovery rate with the C-101 operator.

## 6. Tube Rupture or Firebox Fire

Signs: dense black smoke at the stack, sudden positive draft on PIC-1311 / PT-1314, flame at peepholes or header boxes, a pass flow that rises while its coil inlet pressure falls, bridgewall rising with fuel falling, TT-1303 rising sharply (burning oil carried into the convection and APH).

1. Press HS-1290 (total trip).
2. Open firebox snuffing steam XV-1401; confirm PI-1403 ≥ 2.5 barg. Use HV-1402 for header-box fires.
3. Follow Emergency Response — Tube Rupture and Firebox Fire, Rev 2.3 for pass isolation, charge reduction and fan handling. In this case **flow to the ruptured pass is stopped**, contrary to Section 3 step 2.
4. Keep the ID fan running on PIC-1311 to hold the firebox negative; reduce FD air to the minimum that procedure allows. Keep the APH rotor turning and watch TT-1303 and TIC-1345 for signs of fire in the APH.

## 7. Records

Within the shift log: trip time, first-out, operator actions and times, restart time, and any TMT, draft or APH temperature excursions. File a trip report with the process engineer within 24 hours.
