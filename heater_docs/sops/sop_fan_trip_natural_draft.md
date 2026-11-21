---
doc_id: sop_fan_trip_natural_draft
doc_type: sop
equipment: [heater_h101, fd_fan, id_fan, air_preheater, bypass_dampers, stack, burners, radiant_coil, fuel_gas_system, flue_gas_analyzers, pass_flow_control, transfer_line, atmospheric_column, bms_sis]
tags: [XS-1341, XS-1351, XS-1349, ZT-1361, ZT-1362, SI-1341, SI-1351, JI-1341, JI-1351, FIC-1341, PT-1342, PIC-1311, PT-1312, PT-1314, PT-1352, AIC-1321, AT-1322, AT-1327, AT-1326, TT-1303, TT-1343, TIC-1345, PDT-1347, FT-1201, AT-1203, PIC-1202, TIC-1110, FY-1100, FIC-1101, FIC-1102, FIC-1103, FIC-1104, TT-1111, TT-1112, TT-1113, TT-1114, TI-1121A, TI-1121B, TI-1122A, TI-1122B, TI-1123A, TI-1123B, TI-1124A, TI-1124B, TT-1301A, TT-1301B, HS-1290]
title: SOP — FD / ID Fan Trip Response and Natural-Draft Operation
revision: 1.0
date: 2026-11-20
---

# SOP — FD / ID Fan Trip Response and Natural-Draft Operation

**Document No.:** H101-SOP-007
**Revision:** 1.0 | **Date:** 2026-11-20
**Applicability:** Unit 100 — H-101 Crude Charge Heater, FD fan K-101, ID fan K-102, air preheater E-102, bypass damper D-101, emergency air doors D-102
**Owner:** Unit 100 Operations (Shift Superintendent)
**P&ID Reference:** U100-PID-102 (combustion, fuel gas, burners, BMS), U100-PID-103 (air preheater, fans, ducts, dampers, stack)

---

## 1. Scope and Purpose

H-101 normally runs in balanced draft: FD fan K-101 (VFD SC-1341) supplies combustion air through the regenerative air preheater E-102, and ID fan K-102 (VFD SC-1351) draws flue gas through E-102 and holds arch draft on PIC-1311. If either fan or the APH rotor stops, the heater cannot continue in balanced draft. Rather than trip the fuel, the BMS performs a **natural-draft runback**: the flue gas goes straight from the convection outlet to stack S-101 through bypass damper D-101, ambient air enters the windbox through emergency air doors D-102, and firing is limited to what natural draft can support, **≤ 60% of normal**.

This SOP covers the automatic actions, the operator response to each event (FD trip, ID trip, APH rotor stop, loss of both fans), operation on natural draft, and the return to balanced draft. Logic and setpoints: BMS / SIS Cause and Effect — H-101, Rev 3.3 and Alarm and Trip Setpoint Register — H-101 Crude Charge Heater, Rev 3.1. Equipment data: Equipment Datasheet — K-101 Forced Draft Fan and K-102 Induced Draft Fan, Rev 1.0; Equipment Datasheet — S-101 Stack, D-101 Bypass Damper and D-102 Emergency Air Doors, Rev 1.3.

## 2. Automatic Actions (BMS-101)

| Initiator | Automatic action |
|---|---|
| FD fan stopped (XS-1341 = 0) | Open XV-1362 emergency air doors and XV-1361 bypass damper; stop ID fan; clamp firing to ≤ 60% of normal |
| ID fan stopped (XS-1351 = 0) | Open XV-1361 bypass damper and XV-1362; stop FD fan; clamp firing to ≤ 60% |
| APH rotor stopped (XS-1349 = 0) | Natural-draft runback as for ID fan stop, plus APH fire-watch alarm |
| Both fans lost (e.g. power dip) | Both XS-1341 / XS-1351 = 0: runback as above; XV-1361 / XV-1362 fail open |
| Firebox pressure PT-1314 > +10 mmH2O for 5 s | Main fuel trip (may follow an ID fan trip if the bypass opens late) |

The runback is **not** a fuel trip: burners and pilots stay lit. The firing clamp acts on the PIC-1202 fuel-gas pressure setpoint (≈ 60% of normal heat release ≈ 23 MW LHV, ≈ 1,720 kg/h on FT-1201 at 48.5 MJ/kg). If the runback fails (a damper does not open, or PT-1314 trips), follow SOP — H-101 Emergency Shutdown and Trip Response, Rev 2.6.

## 3. Immediate Operator Actions — Any Runback (first 5 minutes)

1. **Confirm the runback on the BMS mimic:** both fans stopped (XS-1341, XS-1351 = 0), ZT-1361 and ZT-1362 > 90% open, fuel clamp active. If either damper has not opened within 30 s and the draft is going positive, press HS-1290.
2. **Confirm draft is negative:** PIC-1311 below 0 mmH2O and PT-1314 well below +10 mmH2O. PIC-1311 has no final element in natural draft; it is indication only.
3. **Put loops in a safe mode:** AIC-1321 and FIC-1341 to MANUAL (the FD fan is stopped; air now comes through D-102 by natural draft). Put TIC-1110 in MANUAL or lower its setpoint to an achievable value so it does not wind up against the firing clamp.
4. **Keep crude flowing on all four passes** at ≥ 55 t/h per pass (LL trip 43 t/h).
5. **Inform the C-101 operator immediately:** heater duty has dropped to roughly half of normal, COT will fall, flash-zone vaporization drops, distillate draws fall and residue rises. Agree a charge reduction plan with the crude unit console.
6. **Look into the firebox:** flames will be longer and lazier on cold ambient air; check for impingement, smoke or flame-out.
7. Record the time and first-out on the BMS sequence-of-events.

## 4. Event-Specific Response

| Event | Verify | Follow-up |
|---|---|---|
| FD fan trip | SC-1341 VFD fault, motor protection, high vibration, low lube oil (local panel) | Electrical/rotating equipment to investigate; check JI-1341 history for overload; do not restart until cause found |
| ID fan trip | SC-1351 fault, high vibration, bearing temperature, PT-1352 trend (inlet blockage, damper malfunction) | Check PT-1314 peak (a positive excursion means the bypass opened late — report it); inspect ID fan |
| Both fans lost | Electrical supply; also check the APH rotor drive and XS-1349 (usually on the same supply) | Treat as APH rotor stop as well if XS-1349 = 0 (Section 5) |
| Fan trip on high load | SI-1341 or SI-1351 near 95% before the trip | Suspect APH leakage or fouling raising fan load; see Troubleshooting Guide — Air Preheater Leakage, Fouling and Low Cold-End Temperature, Rev 1.0 |

## 5. APH Rotor Stop — Fire Watch

A rotor that stops while hot is heated on the gas side only. It distorts (seals rub or jam on restart) and any combustible deposits on the elements can ignite.

1. Confirm the stop locally (rotor not turning, drive motor or coupling failed). XS-1349 = 0 has already opened the bypass and stopped both fans, so little flue gas reaches E-102.
2. **Try to keep the rotor turning** with the vendor's auxiliary drive or by hand-barring, if this can be done safely.
3. **Fire watch:** trend TT-1303, TT-1343 and TIC-1345 every 5 minutes. With no gas or air flow these should fall slowly. A rise in TT-1343 or TIC-1345, smoke or a hot spot on the APH casing is an **APH fire**: call the fire team and follow Emergency Response — Tube Rupture and Firebox Fire, Rev 2.3. Do not start the fans into a suspected APH fire.
4. Do not restart the rotor drive after a hot stop until maintenance has checked seal clearance and drive torque (Per Maintenance Procedure — Air Preheater Seal Inspection, Soot Blowing and Water Washing, Rev 1.0).

## 6. Operating on Natural Draft (≤ 60% Firing)

| Parameter | Limit / watch | Tag |
|---|---|---|
| Firing | ≤ 60% of normal (BMS clamp) | FT-1201 × AT-1203 |
| Arch draft | Negative; reduce firing if it weakens toward −0.5 mmH2O | PIC-1311, PT-1312, PT-1314 |
| O2 | ≥ 2.0% dry at the arch; no automatic O2 control | AIC-1321 |
| CO | < 200 ppm; reduce firing if rising | AT-1322 |
| TMT | < 585 °C; pass spread ±6 °C (TDA-1111..1114) | TI-1121A..1124B, TT-1111..1114 |
| Bridgewall | 760–900 °C (may run low) | TT-1301A/B |
| Pass flow | ≥ 55 t/h per pass | FIC-1101..1104 |

1. Air is now set by natural draft through D-102 and the burner registers. If O2 falls below 2.0% or CO rises, **reduce firing** — do not move burner registers unless directed by process engineering.
2. Without the APH the flue gas leaves at convection-outlet temperature (TT-1303 region, ≈ 400 °C on the bypass); efficiency is well below the balanced-draft ≈ 91%, so absorbed duty is roughly half of normal.
3. **COT cannot be held at 360 °C at full charge.** The unit supervisor decides with the C-101 operator between reducing charge (not below 55 t/h per pass) and running a lower COT. Either choice changes column cut points and yields; the column operator adjusts draws, pumparounds and stripping steam. Keep the COT change rate ≤ 50 °C/h.
4. Watch TMT: pass flows at minimum make the coil more sensitive to pass imbalance. Re-balance per Control Narrative — Pass Flow Control and Pass Balancing, Rev 2.1.
5. Do not run soot blowers while on natural draft.

## 7. Restoring Balanced Draft

1. Cause found and fixed; the shift superintendent authorizes the restart. Heater steady on natural draft.
2. **APH rotor turning first:** start the rotor drive; confirm XS-1349 = 1 and normal drive current.
3. Put PIC-1311 in MANUAL. Start ID fan K-102 at minimum speed (XS-1351 = 1) and close bypass damper XV-1361 (ZT-1361 < 5%) while matching ID speed so the arch stays between −1 and −5 mmH2O. Then put PIC-1311 in AUTO at −2.5 mmH2O. Watch PT-1314.
4. Start FD fan K-101 at minimum speed (XS-1341 = 1); with FIC-1341 in MANUAL, raise air flow while closing emergency air doors XV-1362 (ZT-1362 < 5%), keeping AIC-1321 ≥ 2.5% and AT-1322 < 200 ppm.
5. Put FIC-1341 in AUTO, then AIC-1321 in AUTO (cascade) at 3.0%. Put TIC-1345 in AUTO at 145 °C; the APH has cooled, so TV-1345 will open until the cold end warms (Per SOP — H-101 Cold Start-up, Purge and Burner Light-off, Rev 3.2, Section 7).
6. Reset the runback at the BMS to release the firing clamp. Raise firing at ≤ 5% of FT-1201 per 10 minutes, watching TT-1343 rise and SI-1341 / SI-1351 below 95%.
7. Restore charge and the 360 °C COT target in steps agreed with the C-101 operator, then return TIC-1110 to CASCADE.

## 8. Records

Log: event time, first-out, damper opening times, PT-1314 peak, minimum COT and charge reached, duration on natural draft, fan restart and clamp release times. Record JI-1341, JI-1351, SI-1341, SI-1351, PDT-1347 and AT-1326 − AT-1327 after return to balanced draft and compare with the previous baseline. File a report with process engineering within 24 hours.
