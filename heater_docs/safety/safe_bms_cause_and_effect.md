---
doc_id: safe_bms_cause_and_effect
doc_type: safety
equipment: [bms_sis, fuel_gas_system, fuel_gas_ko_drum, pilot_gas_system, burners, pass_flow_control, fd_fan, id_fan, air_preheater, bypass_dampers, heater_h101]
tags: [FT-1151, FT-1152, FT-1153, FT-1154, FIC-1101, FIC-1102, FIC-1103, FIC-1104, PT-1206, PT-1207, LT-1205, PT-1208, BS-1211, BS-1212, BS-1213, BS-1214, BS-1215, BS-1216, BS-1217, BS-1218, HS-1290, PT-1314, PIC-1311, XS-1341, XS-1351, XS-1349, ZT-1361, ZT-1362, FIC-1341, PIC-1202, TIC-1110, TIC-1345, SI-1341, SI-1351]
title: BMS / SIS Cause and Effect — H-101
revision: 3.3
date: 2026-11-20
---

# BMS / SIS Cause and Effect — H-101

**Document No.:** H101-SAF-001
**Revision:** 3.3 | **Date:** 2026-11-20
**Applicability:** Unit 100 — H-101 Crude Charge Heater
**Owner:** Process Safety Engineering / Instrument & Controls Engineering
**P&ID reference:** U100-PID-101 (process coil, pass flow SIS transmitters), U100-PID-102 (fuel gas, pilot gas, burners, firebox pressure, BMS-101), U100-PID-103 (FD/ID fans, APH, bypass damper, emergency air doors)

**Revision note:** Rev 3.3 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).

> **SAFETY NOTE:** The H-101 Burner Management System / Safety Instrumented System (BMS-101) is a SIL-rated system. No initiator listed in this document may be bypassed without an approved bypass permit, compensating measures and shift supervisor authorisation. Alarm setpoints and operator responses are listed separately in Alarm and Trip Setpoint Register — H-101 Crude Charge Heater, Rev 3.1.

---

## 1. Purpose and Scope

This document defines every automatic safety action taken by BMS-101 on H-101: which initiator acts on which final element, with what setpoint and delay. It also lists the light-off permissives and the conditions that are deliberately **not** trips. It covers the main fuel gas system (V-101, PV-1202, XV-1201/XV-1202 double block, XV-1203 bleed), the pilot gas system (XV-1209), burners B-101A–H with flame scanners BS-1211..BS-1218, the pass-flow SIS transmitters FT-1151..FT-1154, the firebox pressure transmitter PT-1314, and the balanced-draft system: FD fan K-101, ID fan K-102, regenerative air preheater E-102, D-101 bypass damper (XV-1361) and D-102 emergency air doors (XV-1362). Operator trip response is in SOP — H-101 Emergency Shutdown and Trip Response, Rev 2.6; fan and APH-rotor stops in SOP — FD / ID Fan Trip Response and Natural-Draft Operation, Rev 1.0.

Three automatic action levels exist on H-101:

- **Main fuel trip (MFT):** close XV-1201 and XV-1202, open the bleed XV-1203. Pilots stay lit (XV-1209 remains open).
- **Total trip:** MFT plus close XV-1209. All flame is extinguished; a full purge is required before relight.
- **Natural-draft runback:** not a fuel trip. On loss of a fan or the APH rotor, BMS-101 opens the natural-draft path (XV-1361, XV-1362), stops the remaining fan and clamps firing to ≤ 60% of normal (≈ 23 MW LHV) so the heater stays lit on natural draft.

---

## 2. Final Elements and Fail Positions

| Final element | Service | Action | Fail position (loss of air/power/signal) |
|---|---|---|---|
| XV-1201 / XV-1202 | Main fuel gas double block | Close on MFT / total trip | Fail closed |
| XV-1203 | Main fuel gas bleed vent to safe location | Open on MFT / total trip | Fail open |
| XV-1209 | Pilot gas shutoff | Close on total trip only | Fail closed |
| XV-1361 (D-101) | Flue-gas bypass damper, convection outlet → S-101, bypassing E-102 and K-102 | Open on runback | **Fail open** (natural-draft path) |
| XV-1362 (D-102) | Emergency air doors on the burner windbox | Open on runback | **Fail open** (natural-draft air) |
| SC-1341 | FD fan K-101 VFD | Stopped by BMS on ID fan or APH rotor stop | Holds last speed on signal loss |
| SC-1351 | ID fan K-102 VFD | Stopped by BMS on FD fan stop | Holds last speed on signal loss |
| PIC-1202 setpoint | Fuel gas pressure (COT cascade slave) | Clamped by BMS to the 60% firing limit during runback | — |

Not SIS final elements but safety-relevant fail positions: PV-1202 fail closed; FV-1101..FV-1104 fail open (a control failure never starves the coil of crude); TV-1345 APH cold-air bypass fail closed. After any trip the operator keeps crude flowing through all four passes to cool the coil unless a tube rupture is suspected (Emergency Response — Tube Rupture and Firebox Fire, Rev 2.3). An MFT or total trip does **not** stop the fans: K-101 and K-102 stay on their controllers so the firebox continues to be swept and held negative.

---

## 3. Cause and Effect Matrix — Fuel Trips

| No. | Initiator | Tag(s) | Setpoint | Voting / delay | XV-1201/1202 | XV-1203 | XV-1209 | Result |
|---|---|---|---|---|---|---|---|---|
| C1 | Low-low pass flow, any pass | FT-1151..FT-1154 | < 43 t/h (60% of 71.5) | 1oo1 per pass, any pass; 2 s | Close | Open | No action | MFT |
| C2 | Low-low fuel gas pressure | PT-1206 | < 0.25 barg | 1 s | Close | Open | No action | MFT |
| C3 | High-high fuel gas pressure | PT-1207 | > 2.5 barg | 1 s | Close | Open | No action | MFT |
| C4 | High-high V-101 level | LT-1205 / LSHH-1205 | > 80% | 2 s | Close | Open | No action | MFT |
| C5 | Low-low pilot gas pressure | PT-1208 | < 0.25 barg | 1 s | Close | Open | Close | Total trip |
| C6 | Flame loss on ≥ 3 of 8 burners | BS-1211..BS-1218 | Flame OFF | 3oo8; flame failure response ≤ 4 s | Close | Open | No action | MFT |
| C7 | Manual ESD push-button | HS-1290 | Pressed | None | Close | Open | Close | Total trip |
| C8 | Firebox pressure high-high (new in Rev B) | PT-1314 | > +10 mmH2O | 5 s | Close | Open | No action | MFT |

Notes: cause numbers C1–C7 are unchanged from Rev 3.2; the Rev 3.2 purge row C8 is now Section 6 and C8 is the new PT-1314 trip. (1) Each FT-1151..FT-1154 is independent of the FIC-1101..FIC-1104 control transmitter; a deviation alarm between them warns of a transmitter fault. (2) PT-1206 is suppressed only during each burner's timed trial-for-ignition. (3) PT-1314 is a dedicated SIS transmitter, independent of the PIC-1311 draft control transmitter; it protects the casing, peephole doors and personnel against sustained positive firebox pressure (e.g. ID fan unable to hold draft, APH gas-side plugging, afterburning). (4) Delays shown are site design values.

---

## 4. Cause and Effect Matrix — Natural-Draft Runback (Not a Fuel Trip)

| No. | Initiator | Tag | XV-1361 bypass | XV-1362 air doors | FD fan K-101 | ID fan K-102 | Firing | Additional |
|---|---|---|---|---|---|---|---|---|
| R1 | FD fan stopped | XS-1341 = 0 | Open | Open | (stopped) | Stop | Clamp ≤ 60% of normal | — |
| R2 | ID fan stopped | XS-1351 = 0 | Open | Open | Stop | (stopped) | Clamp ≤ 60% of normal | — |
| R3 | APH rotor stopped | XS-1349 = 0 | Open | Open | Stop | Stop | Clamp ≤ 60% of normal | APH fire watch alarm |

In all three cases the heater ends in natural draft: both fans stopped, flue gas to S-101 through D-101, ambient air through D-102. Natural-draft capability is ≈ 60% of normal firing. BMS-101 clamps the PIC-1202 setpoint; TIC-1110 will not be able to hold COT at full charge, so the operator reduces charge (FY-1100) to keep COT and TMT in range. A runback lowers flash-zone vaporization in C-101 and shifts distillate into residue; inform the C-101 / unit operator immediately. If combustion becomes unstable during the transition, the fuel trips in Section 3 (C6 flame loss, C8 firebox pressure) still act.

For R3, a stopped rotor leaves one sector of the hot element in the gas stream with no cooling air: deposits can ignite. The field operator checks E-102 casing and TT-1343/TIC-1345 for an abnormal rise; response is in Troubleshooting Guide — Air Preheater Leakage, Fouling and Low Cold-End Temperature, Rev 1.0. Return to balanced draft is a manual, operator-initiated sequence per SOP — FD / ID Fan Trip Response and Natural-Draft Operation, Rev 1.0.

---

## 5. Individual Burner Flame Supervision

Each burner B-101A–H has its own scanner (B-101A = BS-1211 through B-101H = BS-1218). Loss of flame on **one or two** burners closes only that burner's gas supply and alarms; PIC-1202 / TIC-1110 raise fuel pressure to the remaining burners to hold COT. Loss of flame on **three or more** burners is cause C6 (MFT): the remaining five cannot carry duty within their 120% design release, and unburned gas could accumulate. A burner that went out on flame failure is not relit until the cause is understood, and only from its own pilot, never from hot refractory.

---

## 6. Light-off Permissives (Purge)

BMS-101 will not allow XV-1201/XV-1202 to open until **all** of the following are true:

1. **Purge complete:** at least 5 firebox and convection volume changes credited by the purge timer, with
   - a proven purge path: **both fans running** (XS-1341 = 1 and XS-1351 = 1) **or** the natural-draft path open (XV-1361 and XV-1362 open, proven by ZT-1361 / ZT-1362), and
   - **air flow ≥ 25%** of design (FIC-1341 ≥ ≈ 14,500 kg/h).
   The timer restarts if any purge condition is lost during the purge. The balanced-draft path is the normal purge; how the air-flow condition is met on the natural-draft path is defined in SOP — H-101 Cold Start-up, Purge and Burner Light-off, Rev 3.2.
2. **All pass flows above low-low:** FT-1151..FT-1154 > 43 t/h (start-up practice ≥ 60 t/h per pass).
3. **KO drum level normal:** LT-1205 below 50% and LSHH-1205 not active.
4. **Pilots proven:** PT-1208 above 0.4 barg, XV-1209 open, pilot flame proven on every burner to be lit.
5. **Main fuel valves proven:** XV-1201/XV-1202 closed and XV-1203 open at sequence start; all burner gas valves closed.
6. **No trip active:** HS-1290 reset, no cause C1–C8 present, and PT-1314 below its trip setpoint.

Each burner light-off has a 10 s trial-for-ignition; on failure the burner valve closes and a 1 minute wait applies.

---

## 7. Conditions That Are Alarms, Not Trips

BMS-101 takes no automatic action on the following; they require operator action and are the constraints the heater optimizer must respect:

| Condition | Tag(s) | Alarm | Operator response document |
|---|---|---|---|
| High tube metal temperature | TI-1121A..TI-1124B | Hi 585 °C, HH 600 °C | Troubleshooting Guide — High Tube Metal Temperature, Rev 2.4 |
| High COT | TIC-1110 | Hi 368 °C, HH 375 °C | Control Narrative — Coil Outlet Temperature / Fuel Gas Pressure Cascade, Rev 2.3 |
| Low / high excess O2 | AIC-1321 | Lo 1.5%, LL 1.0%, Hi 5.0% | Troubleshooting Guide — Low Excess O2 / High CO, Rev 2.5 |
| High CO | AT-1322 | Hi 200 ppm, HH 1000 ppm | Troubleshooting Guide — Low Excess O2 / High CO, Rev 2.5 |
| High coil ΔP | PDI-1101..PDI-1104 | Hi 7.8 bar, HH 8.4 bar | Troubleshooting Guide — Rising Coil Pressure Drop, Rev 1.9 |
| Positive arch draft | PIC-1311 | Hi −0.5, HH 0.0 mmH2O (the trip is PT-1314, C8) | Troubleshooting Guide — Positive Draft and Afterburning, Rev 1.8 |
| Low APH gas outlet temperature | TIC-1345 | Lo 145 °C, LL 140 °C | Troubleshooting Guide — Air Preheater Leakage, Fouling and Low Cold-End Temperature, Rev 1.0 |
| High fan speed (capacity) | SI-1341, SI-1351 | Hi 95% | Troubleshooting Guide — Positive Draft and Afterburning, Rev 1.8 |

Operators must not treat the absence of a trip as permission to run outside these limits (Integrity Operating Windows (IOW) — H-101 Radiant Coil, Rev 2.1).

---

## 8. Bypass, Testing and Reset

- **Reset:** manual reset from the control room once the initiating cause has cleared. After an MFT with all pilots proven, main burners may be relit without repurge. After a total trip, or an MFT where any pilot was lost, the full purge in Section 6 is mandatory. A runback (R1–R3) is reset only when the stopped equipment is proven running again.
- **Bypasses:** maintenance bypasses on FT-1151..FT-1154, PT-1206, PT-1207, LT-1205, PT-1208 and PT-1314 are key-switch, time-limited (maximum one shift), logged and require a compensating measure (dedicated operator watching the redundant control transmitter; for PT-1314, PIC-1311).
- **Proof testing:** each SIF at the SIL-verification interval (typically each turnaround), with partial-stroke testing of XV-1201/XV-1202 every 6 months and a stroke test of XV-1361/XV-1362 at each turnaround.
