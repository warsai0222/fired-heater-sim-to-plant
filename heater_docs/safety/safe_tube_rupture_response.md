---
doc_id: safe_tube_rupture_response
doc_type: safety
equipment: [radiant_coil, radiant_section, convection_section, snuffing_steam, bms_sis, pass_flow_control, fd_fan, id_fan, air_preheater, bypass_dampers, stack, burners, crude_charge_pumps, atmospheric_column, heater_h101]
tags: [HS-1290, FIC-1101, FIC-1102, FIC-1103, FIC-1104, PT-1101, PT-1102, PT-1103, PT-1104, TT-1111, TT-1112, TT-1113, TT-1114, TT-1301A, TT-1301B, TT-1302, TT-1303, AIC-1321, AT-1322, PIC-1311, PT-1312, PT-1314, FIC-1341, SI-1341, SI-1351, XS-1341, XS-1351, XS-1349, ZT-1361, ZT-1362, TT-1343, TIC-1345, PI-1403, FT-1201]
title: Emergency Response — Tube Rupture and Firebox Fire
revision: 2.3
date: 2026-11-20
---

# Emergency Response — Tube Rupture and Firebox Fire

**Document No.:** H101-SAF-003
**Revision:** 2.3 | **Date:** 2026-11-20
**Applicability:** Unit 100 — H-101 Crude Charge Heater — all operations and emergency response personnel
**Owner:** Process Safety Engineering / Unit 100 Operations
**P&ID reference:** U100-PID-101 (process coil, pass isolation), U100-PID-102 (fuel gas, snuffing steam, firebox pressure), U100-PID-103 (fans, APH, bypass damper, emergency air doors)

**Revision note:** Rev 2.3 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).

> **SAFETY WARNING:** Crude leaving H-101 is at about 360 °C, well above its auto-ignition temperature. A radiant or convection tube failure feeds hot crude straight into an ≈ 845 °C firebox. Expect heavy black smoke, flame out of peepholes and casing openings, positive firebox pressure and possible secondary fires at grade. Unburned hydrocarbon can be carried into the air preheater E-102 and ignite deposits there. **Do not approach the heater casing, peephole doors, header boxes, APH or flue ducts.**

---

## 1. Recognising a Tube Leak or Rupture

A rupture is usually obvious; a small leak is not. Both show the same direction of change, in different sizes:

| Indication | Tag(s) | Small leak | Rupture |
|---|---|---|---|
| Arch O2 falls with no change in fuel gas | AIC-1321, FT-1201 | Slow drift down; O2 controller raises air: FIC-1341 and FD speed SI-1341 rise | Collapse toward 0%, AIC-1321 LL 1.0%; FD fan to maximum |
| CO rises | AT-1322 | Above 200 ppm Hi | Above 1000 ppm HH, off-scale |
| Firebox and convection flue temperatures rise | TT-1301A/B, TT-1302, TT-1303 | Unexplained rise at constant firing | Rapid rise, TT-1301A/B above 900–930 °C |
| Draft lost | PIC-1311, PT-1312, SI-1351, PT-1314 | Draft less negative, ID fan speed SI-1351 rising to hold setpoint | ID fan at 95%, PIC-1311 HH 0.0 mmH2O, PT-1314 > +10 mmH2O → MFT |
| Affected pass hydraulics | FIC-110x, PT-110x, TT-111x | Small rise in pass flow at the same FV-110x opening | Pass flow jumps, PT-110x falls, TT-111x falls |
| Visual | Field | Smoky flame or flame "licking" at one tube | Black smoke from S-101, fire out of openings |

A sudden fall in arch O2 with **rising** bridgewall temperature, **rising** air demand and **no** increase in fuel gas flow is a tube leak until proven otherwise. Do not first assume an O2 analyzer fault.

---

## 2. Immediate Actions — Confirmed or Strongly Suspected Rupture

1. **Press HS-1290.** Total trip: XV-1201/XV-1202 close, XV-1203 opens, XV-1209 closes, per BMS / SIS Cause and Effect — H-101, Rev 3.3.
2. **Sound the unit alarm and call the fire brigade.** Clear all personnel from the heater, APH, fan and S-101 areas; muster at the Unit 100 assembly point.
3. **Open firebox snuffing steam XV-1401** from the control room; confirm PI-1403 stays above 2.5 barg (normal 3.5). Open header-box snuffing HV-1402 if a header box fire is seen. Snuffing steam is the primary extinguishing medium.
4. **Stop hydrocarbon feed to the coil.** Drive FV-1101..FV-1104 closed from the DCS (they fail open, so they must be driven closed); stop the crude charge pumps P-101A/B in coordination with the crude unit board; isolate the heater inlet upstream.
5. **Prevent back-flow from C-101.** Coordinate with the column operator to apply the atmospheric column fire-case procedure so column liquid cannot drain back through the transfer line. Loss of heater effluent upsets C-101 flash-zone vaporization and all draws.
6. **Restrict forced air to the fire:** put FIC-1341 in MANUAL and drive the FD fan K-101 to minimum speed via SC-1341. Do not stop K-101 at this step unless the decision in step 7 is to go to natural draft.
7. **Keep the ID fan K-102 running** on PIC-1311 to hold the firebox negative and carry smoke and combustion products to S-101, **unless** fire spreads into the convection section, E-102 or the flue ducts, or the ID fan is endangered. In that case, go deliberately to natural draft: stop K-101 (XS-1341 = 0). BMS-101 then performs the natural-draft runback — opens the D-102 emergency air doors XV-1362 and D-101 bypass damper XV-1361 and stops K-102 — so the box vents through D-101 to S-101 by natural draft (confirm on ZT-1361 / ZT-1362). Be aware that opening XV-1362 admits ambient air; continue full snuffing steam.
8. **Protect the air preheater.** Hydrocarbon carried into E-102 is an APH fire risk. Keep the rotor turning if possible (a stopped rotor leaves one hot sector in the gas stream). Watch TT-1343 and TIC-1345: a rapid, unexplained rise in either indicates an APH fire; follow Troubleshooting Guide — Air Preheater Leakage, Fouling and Low Cold-End Temperature, Rev 1.0, Section on APH fire. An APH rotor stop (XS-1349 = 0) also triggers the natural-draft runback.
9. Keep snuffing steam on until the firebox is cool and hydrocarbons have burned out or been displaced. Do not open peephole or access doors.

---

## 3. Small Tube Leak — Controlled Response

If the evidence points to a small leak (Section 1, middle column) and there is no fire outside the casing:

1. Inform the shift superintendent; be ready to execute Section 2 at once if indications worsen.
2. Do not raise excess air to "clean up" the CO — the O2 controller will already be adding air via FIC-1341; extra air feeds the leak. Put AIC-1321 / FIC-1341 in MANUAL at the pre-leak air flow and reduce firing instead.
3. Identify the pass: pass-flow increase at the same FV-110x opening and lower PT-110x than the other passes.
4. Watch ID fan speed SI-1351 and PIC-1311; if the ID fan approaches 95%, reduce firing further to keep the box negative.
5. Execute a controlled shutdown per SOP — H-101 Normal Shutdown, Rev 2.4 with steam-out of the coil. A firing or charge reduction lowers C-101 flash-zone vaporization; coordinate with the C-101 / unit operator. A leaking tube is never left in service to the next turnaround.

---

## 4. Firebox Fire Without Tube Failure

Fires can start from fuel gas leaks at the burner manifold, liquid carry-over from V-101 (LT-1205 high), oil-soaked refractory, or deposits in the hot-air windbox or E-102. Indications are flame outside a burner throat, fire in the windbox, burning drips, or a rapid rise in TT-1343 / TIC-1345. Response:

1. Trip main fuel (HS-1290 if fire is outside the firebox or growing).
2. Open snuffing steam XV-1401 (firebox) or HV-1402 (header boxes) as appropriate.
3. Fan actions as Section 2 steps 6–8: FD to minimum, ID running unless the fire is in the convection/APH/duct path.
4. If V-101 carry-over is the cause, confirm LT-1205 and drain V-101 to closed drain before any relight.

---

## 5. Recovery and Restart Conditions

No relight after a tube rupture or firebox fire until:

- The fire brigade has declared the area safe and the firebox has cooled below 60 °C for entry (Safety Procedure — Firebox and Header Box Entry (Confined Space), Rev 1.7).
- The failed tube has been located, the failure investigated (sample retained for metallurgy), and the tube replaced and pressure tested.
- Inspection has assessed neighbouring tubes, supports, refractory, header boxes, and the E-102 baskets, seals and ducts for fire or hydrocarbon damage (Maintenance Procedure — Air Preheater Seal Inspection, Soot Blowing and Water Washing, Rev 1.0).
- Fired Equipment Engineering has reviewed the TMT and IOW history (Integrity Operating Windows (IOW) — H-101 Radiant Coil, Rev 2.1), because most crude-heater tube ruptures follow sustained high TMT from internal coke or flame impingement.
- Restart follows SOP — H-101 Cold Start-up, Purge and Burner Light-off, Rev 3.2 with a full purge.

---

## 6. Common Root Causes to Investigate After a Failure

| Root cause | Evidence to look for in the historian |
|---|---|
| Creep from long-term coke build-up | TI-112xA/B rising together with PDI-110x in the failed pass over weeks; that pass's outlet slightly cooler while TIC-1110 fired harder |
| Flame impingement | Local high TMT on one TC; inspection notes of long or leaning flames |
| Low pass flow | FIC-110x near or below 60 t/h for extended periods |
| Hidden hot tube (failed skin TC) | Flat, unresponsive TI-112x while paired TC and PDI-110x rose |
| Corrosion / thinning | Wall-thickness history; high-sulfur or high-TAN crude runs such as Kearl |

The investigation must separate the **trigger** (the tube failed) from the **cause** (why that tube was hotter or thinner than the others).
