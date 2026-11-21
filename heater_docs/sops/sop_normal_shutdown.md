---
doc_id: sop_normal_shutdown
doc_type: sop
equipment: [heater_h101, radiant_coil, burners, fuel_gas_system, pilot_gas_system, air_preheater, fd_fan, id_fan, bypass_dampers, flue_gas_analyzers, pass_flow_control, soot_blowers, transfer_line, atmospheric_column]
tags: [TIC-1110, FY-1100, FIC-1101, FIC-1102, FIC-1103, FIC-1104, FT-1151, FT-1152, FT-1153, FT-1154, PIC-1202, PT-1206, FT-1201, PT-1208, PIC-1311, AIC-1321, AT-1322, AT-1326, AT-1327, FIC-1341, XS-1341, XS-1351, XS-1349, TIC-1345, TT-1303, TT-1343, PDT-1347, ZT-1361, ZT-1362, TI-1121A, TI-1122A, TI-1123A, TI-1124A, TT-1301A, TT-1301B, PDI-1101, PDI-1102, PDI-1103, PDI-1104, HS-1501]
title: SOP — H-101 Normal Shutdown
revision: 2.4
date: 2026-11-20
---

# SOP — H-101 Normal Shutdown

**Document No.:** H101-SOP-002
**Revision:** 2.4 | **Date:** 2026-11-20
**Revision note:** Rev 2.4 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).
**Applicability:** Unit 100 — H-101 Crude Charge Heater
**Owner:** Unit 100 Operations (Shift Superintendent)
**P&ID Reference:** U100-PID-101 (process coil), U100-PID-102 (combustion, fuel gas, burners, BMS), U100-PID-103 (air preheater, fans, dampers, stack)

---

## 1. Scope and Purpose

This procedure covers a planned shutdown of H-101 from normal operation (COT 360 °C on TIC-1110, charge 286 t/h on FY-1100) to a de-fired, cooled and fuel-isolated condition, with the fans and air preheater E-102 stopped last. It applies to planned outages, crude unit shutdowns and the run-down ahead of a decoke. Trips are covered in SOP — H-101 Emergency Shutdown and Trip Response, Rev 2.6.

Two guiding principles: **fire comes out before flow comes out** (crude flow through every pass is kept until all burners and pilots are out and the coil has cooled), and **the APH rotor keeps turning until its gas inlet has cooled** (a stopped hot rotor distorts and any deposits on it can ignite).

## 2. Pre-Shutdown Preparation

1. Agree the plan and timing with the crude unit console, the C-101 column operator and the shift superintendent. The column operator plans the draw and pumparound reductions that follow the falling COT and charge.
2. Record end-of-run readings: TI-1121A..1124B, PDI-1101..1104 at current charge, FT-1201, AIC-1321, TT-1301A/B, and the APH set — AT-1327, AT-1326, TT-1303, TT-1343, TIC-1345, PDT-1347. These are the end-of-run references for the next decoke and APH maintenance decisions.
3. If the shutdown precedes a decoke or APH work, notify maintenance (Per Maintenance Procedure — Mechanical Pigging Decoke of H-101 Coil, Rev 2.7; Maintenance Procedure — Air Preheater Seal Inspection, Soot Blowing and Water Washing, Rev 1.0).
4. Run one full HS-1501 soot-blow sequence (SB-101A..F then SB-102A/B) while still at normal firing, so the APH is not left with loose deposits that absorb moisture during the outage. Then suspend HS-1501.

## 3. Reduce Firing and Charge

| Parameter | Shutdown rate / limit | Tag |
|---|---|---|
| COT ramp-down | ≤ 50 °C/h | TIC-1110 |
| Pass flow while any burner is lit | ≥ 55 t/h per pass (LL trip 43 t/h) | FIC-1101..1104, FT-1151..1154 |
| Fuel gas pressure | ≥ 0.5 barg while burners lit (LL trip 0.25 barg) | PIC-1202, PT-1206 |
| Arch draft | −2.5 mmH2O, never positive | PIC-1311 |
| CO | < 200 ppm | AT-1322 |
| Combustion air | ≥ 25% of design (≥ 14,500 kg/h) | FIC-1341 |

1. Lower the TIC-1110 setpoint in steps of no more than 10 °C every 12 minutes; the COT cascade reduces PIC-1202. Each step reduces flash-zone vaporization in C-101 — announce each step to the column operator.
2. Reduce charge with the column operator in steps to about 220 t/h (55 t/h per pass). The FY-1100 Lo alarm (250 t/h) will stand.
3. Keep AIC-1321 in AUTO at 3.0% O2 cascaded to FIC-1341. When FIC-1341 reaches its 25% floor, the O2 rises above setpoint — this is normal at low firing.
4. As firing falls TIC-1345 falls; TV-1345 opens to hold 145 °C. When it can no longer hold, note the time; minimize firing time with TIC-1345 below 140 °C.

## 4. Take Burners Out of Service

1. When PIC-1202 approaches 0.5 barg, take burners out in the reverse of the light-off pattern: **B-101H, B-101A, B-101F, B-101C, B-101G, B-101B** — leaving B-101D and B-101E.
2. Close each burner gas cock, de-select it at the BMS (so it is not counted toward the 3-of-8 flame-failure trip) and close its air register to stop hot air bypassing the remaining flames.
3. Re-adjust PIC-1202 after each burner is removed to keep manifold pressure above 0.5 barg.
4. With two burners left and COT at about 250 °C, close the last two cocks and trip main fuel from the BMS: XV-1201/1202 close and XV-1203 opens. Confirm on the BMS mimic.
5. Close XV-1209 to extinguish the pilots. Confirm PT-1208 falls and no flame on BS-1211..1218.

## 5. Cool-Down With Fans and APH Running

1. Keep ID fan K-102 in AUTO on PIC-1311 and FD fan K-101 at FIC-1341 ≥ 25% (AIC-1321 in MANUAL). The air sweeps the firebox and cools the refractory, tubes and APH evenly.
2. **Keep the APH rotor turning (XS-1349 = 1)** until TT-1303 (APH gas inlet) is below 150 °C. Watch TT-1303 and TT-1343 for any unexpected rise — a sign of a deposit fire in the APH; if seen, keep the rotor turning, stop the FD fan, and call the fire team per Emergency Response — Tube Rupture and Firebox Fire, Rev 2.3.
3. Continue crude circulation through all four passes until COT and TI-1121A..1124B are below 150 °C, then follow the crude unit procedure to stop charge.
4. If the outage is longer than 48 hours or precedes a decoke, displace the coil with flushing oil (gas oil) before stopping flow.
5. When TT-1303 is below 150 °C, stop FD fan K-101 first (reverse of the start order). The BMS fan-stop logic then opens bypass damper XV-1361 and emergency air doors XV-1362 and stops ID fan K-102 — confirm XS-1351 = 0 and ZT-1361 / ZT-1362 open. Then stop the APH rotor drive. Leave the dampers open for natural ventilation during the outage.

## 6. Isolation for Maintenance

1. Close the manual fuel gas isolation upstream of V-101 and install the spectacle blind; close the pilot gas isolation. Drain V-101 to closed drain.
2. For coil work, close XV-1105A..D and XV-1106A..D and swing the spectacle blinds per the isolation register.
3. For fan or APH work, LOTO the K-101 / K-102 motors and the E-102 rotor drive; consider the rotor's free rotation (stack draft can turn an unlocked rotor) and lock it mechanically per the vendor manual.
4. Before any firebox, APH or duct entry, apply Safety Procedure — Firebox and Header Box Entry (Confined Space), Rev 1.7.

## 7. Records

Log: time charge reduction started, time of each burner out, main fuel trip time, pilot out time, time TIC-1345 fell below 140 °C, fan and rotor stop times and TT-1303 at rotor stop, time flow stopped, and the end-of-run readings from Section 2.
