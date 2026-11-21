---
doc_id: ctrl_cot_fuel_gas_cascade
doc_type: controls
equipment: [transfer_line, fuel_gas_system, burners, radiant_coil, heater_h101, fd_fan, bms_sis, atmospheric_column]
tags: [TIC-1110, PIC-1202, FT-1201, AT-1203, PT-1206, PT-1207, TT-1111, TT-1112, TT-1113, TT-1114, TT-1100, FY-1100, TI-1121A, TI-1121B, TI-1122A, TI-1122B, TI-1123A, TI-1123B, TI-1124A, TI-1124B, AIC-1321, FIC-1341, SI-1341, SI-1351, XS-1341, XS-1351, XS-1349, TT-1301A, TT-1301B]
title: Control Narrative — Coil Outlet Temperature / Fuel Gas Pressure Cascade
revision: 2.3
date: 2026-11-20
---

# Control Narrative — Coil Outlet Temperature / Fuel Gas Pressure Cascade

**Document No.:** H101-CTRL-002
**Revision:** 2.3 | **Date:** 2026-11-20
**Applicability:** Unit 100 — H-101 Crude Charge Heater
**Owner:** Process Control Engineer
**P&ID Reference:** U100-PID-101 (process coil), U100-PID-102 (combustion, fuel gas, burners, BMS)
**Revision note:** Rev 2.3 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).

---

## 1. Purpose and Structure

The heater's firing is set by a two-level cascade:

| Level | Controller | Measured variable | Output |
|-------|------------|-------------------|--------|
| Master | TIC-1110 | Combined coil outlet temperature (COT), 360 °C | Setpoint of PIC-1202 |
| Slave | PIC-1202 | Fuel gas pressure at burner manifold, 1.2 barg | Fuel gas pressure control valve PV-1202 (fail closed) |

TIC-1110 measures the mixed temperature in the outlet header / transfer line to C-101. It adjusts
the fuel gas manifold pressure setpoint; PIC-1202 moves PV-1202 to hold that pressure. Burner heat
release on B-101A–H follows manifold pressure (approximately ∝ √pressure for fixed fuel
composition), so a pressure slave rejects fuel-header pressure disturbances in seconds, before
they reach the COT.

## 2. Why Pressure, Not Flow, Is the Slave

A fuel-gas pressure slave is standard for heaters with multiple fixed-orifice gas burners:

- The quantity that sets burner stability is tip pressure. Using it as the slave lets the slave
  setpoint be clamped directly inside the burner-pressure trip limits (PT-1206 LL 0.25 barg,
  PT-1207 HH 2.5 barg).
- A refinery fuel-header pressure swing is corrected by PIC-1202 within seconds.
- FT-1201 (Coriolis mass flow) is used for monitoring, fired-duty calculation (FT-1201 × AT-1203),
  the air/fuel cross-limit (Section 6) and the 3,430 kg/h firing-limit alarm, not as the slave PV.

The cost is that the slave does not compensate for fuel composition: at the same manifold pressure,
a change in fuel density and heating value changes heat release. The COT master corrects this
more slowly.

## 3. Setpoint Clamps and Limits

| Item | Value | Basis |
|------|-------|-------|
| TIC-1110 setpoint | 360 °C (production target ± 2 °C) | Atmospheric column feed |
| TIC-1110 setpoint operator range | 350–365 °C | Changes outside require shift supervisor approval; any change is agreed with the C-101 operator |
| PIC-1202 setpoint low clamp | 0.45 barg | Above Lo alarm 0.35 and LL trip 0.25 barg |
| PIC-1202 setpoint high clamp | 2.1 barg | Below Hi alarm 2.2 and HH trip 2.5 barg |
| PIC-1202 normal | 1.2 barg | 100% heat release |
| Firing limit | 46 MW LHV (FT-1201 ≈ 3,430 kg/h at 48.5 MJ/kg) | 120% of normal heat release |
| Air cross-limit | PIC-1202 setpoint limited to the firing that measured air FIC-1341 supports | Air/fuel cross-limiting (Section 6) |
| Natural-draft runback clamp | PIC-1202 setpoint high clamp ≈ 0.43 barg (≤ 60% firing); low clamp lowered to 0.40 barg | BMS, on FD, ID or APH-rotor stop |

The clamps keep the cascade from driving the burners into a fuel-pressure trip. When PIC-1202's
setpoint is held at a clamp, TIC-1110 is flagged "output limited" on the DCS faceplate and its
integral action is frozen (anti-windup). A COT that cannot be held with PIC-1202 at the high clamp
means the heater is at a firing limit (fuel pressure, air cross-limit, or fan capacity): reduce charge
rate (FY-1100) rather than overriding the clamp. COT is a given production target, not an optimizer
decision; when it cannot be held, C-101 flash-zone vaporization falls and distillate shifts into residue,
so the C-101 operator must be told at once.

## 4. Tuning and Dynamics

| Controller | Action | Typical tuning | Comment |
|------------|--------|----------------|---------|
| PIC-1202 | Reverse (pressure up → valve closes) | Kc 0.5, Ti 0.3 min, no derivative | Fast; closed-loop response ≈ 10–20 s |
| TIC-1110 | Reverse (COT up → pressure SP down) | Kc 1.0 %/%, Ti 4 min, Td 0.5 min | Dominated by firebox and coil lag ≈ 3–6 min |

Tuning values are recorded in the DCS configuration database; these are the commissioning values.
The COT loop has a long dead time (fluid residence in ≈ 362 m of tube per pass plus firebox
thermal lag), so aggressive master tuning causes cycling that also shows on TMT and O2.

## 5. Mode Handling

| PIC-1202 mode | TIC-1110 behaviour |
|---------------|--------------------|
| Cascade (normal) | TIC-1110 in Auto, writes PIC-1202 setpoint |
| Auto (local setpoint) | TIC-1110 tracks (setpoint follows PV, output follows PIC-1202 SP) for bumpless return |
| Manual | TIC-1110 tracks; PV-1202 positioned by operator |

On a main fuel trip the BMS forces PIC-1202 to Manual with output 0% and TIC-1110 to track. On a
natural-draft runback (fan or APH-rotor stop) PIC-1202 stays in cascade but its setpoint is clamped
(Section 3), so TIC-1110 runs output-limited with integral action frozen; the operator cuts charge
(FY-1100) to restore COT or accepts a lower COT, in agreement with the C-101 operator. Re-lighting and
return to cascade follow SOP — H-101 Emergency Shutdown and Trip Response, Rev 2.6, SOP — H-101 Cold
Start-up, Purge and Burner Light-off, Rev 3.2, and SOP — FD / ID Fan Trip Response and Natural-Draft
Operation, Rev 1.0.

## 6. Interaction with Excess O2, Air Flow and Draft

H-101 is balanced draft with a measured combustion-air flow (FIC-1341, FD fan K-101), so firing and
air are **cross-limited**: on a firing increase the air flow setpoint rises first and the PIC-1202
setpoint is limited to the firing the *measured* air supports; on a decrease fuel falls first and air
follows. A fast COT increase therefore no longer dips O2 the way it did on the Rev A natural-draft
heater, but it is rate-limited by the FD fan response, and the ID fan must follow to hold arch draft.
Practice:

- Change the COT setpoint in steps of ≤ 2 °C with at least 5 minutes between steps; each step also
  changes C-101 flash-zone vaporization, so tell the C-101 operator.
- For charge-rate (FY-1100) increases of more than 5%, check that FD and ID fan speeds (SI-1341,
  SI-1351) have room below the 95% limit before the change.
- On rate cuts, reduce charge first and let the COT loop cut fuel; O2 rises transiently, which is safe.

The cross-limit uses FIC-1341 corrected for the design APH leakage; if leakage has grown, less air
reaches the burners than the cross-limit assumes. See Control Philosophy — Excess O2 and Arch Draft
Control, Rev 2.5.

## 7. Constraints Not Handled Automatically

The cascade controls the **mixed** COT. It does not protect the tubes:

- **TMT:** TI-1121A..1124B have no override on the cascade. As coke builds, the same COT needs a
  higher tube wall temperature; the operator must watch the 585 °C High and 600 °C HH alarms
  and reduce COT or charge (Troubleshooting Guide — High Tube Metal Temperature, Rev 2.4).
- **Pass imbalance:** a cold pass hidden in the average makes TIC-1110 over-fire the other passes.
  Pass outlets TT-1111..1114 and deviation alarms TDA-1111..1114 must be watched (Control
  Narrative — Pass Flow Control and Pass Balancing, Rev 2.1).
- **Bridgewall:** TT-1301A/B 900 °C High alarm indicates firing near the radiant limit.
- **Fan capacity:** FD and ID fan speed ≤ 95% (SI-1341 / SI-1351) is not enforced by the cascade; a
  fan at its limit means O2 or draft can no longer be held as firing rises.
- **Inlet temperature:** a preheat-train upset (TT-1100 Lo 235 °C) raises required firing with no
  feedforward; the COT loop recovers it with a lag of several minutes.

## 8. Fuel Composition Disturbances

At a fixed tip pressure, burner heat release follows the fuel's Wobbe index. A rise in H2
content lowers fuel density, volumetric heating value and Wobbe index, so at the same PIC-1202
pressure the heat release falls slightly and the flame shortens; a rise in C3+ does the opposite.
Note that the mass-basis LHV on AT-1203 (normal 48.5 MJ/kg, alarms 44 / 52 MJ/kg) moves the other
way for H2 (H2 has a high heating value per kg), so FT-1201 in kg/h falls while fired duty barely
changes. The COT loop corrects within a
few minutes. Efficiency and fuel-per-duty calculations must use the measured AT-1203 LHV, otherwise
a fuel-quality change is mistaken for an efficiency loss (or vice versa) — see Troubleshooting
Guide — High Fuel Consumption / Low Efficiency, Rev 2.1.
