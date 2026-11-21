---
doc_id: ctrl_excess_o2_and_draft
doc_type: controls
equipment: [flue_gas_analyzers, burners, fd_fan, id_fan, air_preheater, bypass_dampers, radiant_section, convection_section, heater_h101]
tags: [AIC-1321, AT-1322, AT-1327, AT-1326, AT-1325, FIC-1341, SI-1341, JI-1341, PIC-1311, PT-1312, PT-1313, PT-1314, PT-1352, SI-1351, JI-1351, TIC-1345, TT-1343, TT-1303, TT-1301A, TT-1301B, FT-1201, AT-1203, PT-1342, XS-1341, XS-1351, XS-1349, HS-1501, TT-1001]
title: Control Philosophy — Excess O2 and Arch Draft Control
revision: 2.5
date: 2026-11-20
---

# Control Philosophy — Excess O2 and Arch Draft Control

**Document No.:** H101-CTRL-004
**Revision:** 2.5 | **Date:** 2026-11-20
**Applicability:** Unit 100 — H-101 Crude Charge Heater
**Owner:** Process Control Engineer; Combustion / Heater Specialist Engineer
**P&ID Reference:** U100-PID-102 (combustion, fuel gas, burners, BMS), U100-PID-103 (air preheater, FD/ID fans, ducts, dampers, stack)
**Revision note:** Rev 2.5 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).

---

## 1. Loops and Final Elements

| Loop | Measured | Setpoint | Output / final element | Notes |
|------|----------|----------|------------------------|-------|
| Excess O2 (master) | AIC-1321 arch O2, dry | 3.0% design; decision 2–4% | Setpoint of FIC-1341 (as an air/fuel ratio trim) | Closed loop ≈ 3–5 min |
| Combustion air (slave) | FIC-1341, FD discharge (incl. APH leakage) | From AIC-1321 and cross-limits | FD fan VFD SC-1341 (SI-1341) | Closed loop ≈ 10–20 s |
| Arch draft | PIC-1311 | −2.5 mmH₂O (stretch decision) | ID fan VFD SC-1351 (SI-1351) | Closed loop ≈ 10–20 s, FD feedforward |
| APH cold end | TIC-1345 APH gas outlet | Minimum-temperature setpoint 148 °C (Lo alarm 145, limit 140) | Cold-air bypass damper TV-1345 (fail closed) | Normally closed at design |

The Rev A burner-plenum louvre and stack damper no longer exist. O2, air flow and draft
loops have **no trip**: AIC-1321 Lo 1.5 / LL 1.0%, AT-1322 Hi 200 / HH 1000 ppm, PIC-1311 Hi −0.5 / HH
0.0 mmH₂O and TIC-1345 Lo 145 / LL 140 °C are operator alarms. The only draft trip is the SIS firebox
pressure PT-1314 (+10 mmH₂O for 5 s → main fuel trip); fan or APH-rotor stops cause a natural-draft
runback (Section 11).

## 2. The O2 Setpoint Is an Optimization Decision

The AIC-1321 setpoint is a decision variable chosen within 2–4% dry. Lowering it:

| Effect | Direction |
|--------|-----------|
| Stack loss (less excess air leaving at ≈ 150 °C) | Better — ≈ 0.3–0.4% of fuel per percentage point of O2 (≈ 10 kg/h, ≈ 0.13 MW at design) |
| Fan power (≈ 5% less air and flue gas per point) | Better — ≈ 18 kW less FD + ID power per point (JI-1341 + JI-1351) |
| Flame temperature, radiant heat transfer, NOx (AT-1325) | Slightly higher flame temperature; NOx usually lower (less O2) |
| CO (AT-1322) | Flat down to the burner minimum O2, then rises steeply |
| Margin to sub-stoichiometric firing on a firing increase | Smaller |

With the APH, the fuel value of each point of O2 is about half the Rev A value (the flue gas now
leaves at ≈ 150 °C, not ≈ 320 °C), but the fan-power saving now adds to it. The optimum is the lowest
setpoint at which **burner-level** O2 stays above the burner minimum (≈ 1.5% dry) with margin for
firing transients and analyzer uncertainty, and CO stays below 200 ppm. On a sealed heater with a
validated analyzer this is typically 2.0–2.5%; with tramp air or analyzer doubt it is higher. Steps
≤ 0.3% with ≥ 15 minutes between steps, watching AT-1322.

## 3. Fuel vs CO Trade-off (the "CO Knee")

| Burner-level O2 (dry) | Arch CO AT-1322 | Fuel vs 3.0% O2 | Fan power vs 3.0% |
|-----------------------|-----------------|-----------------|-------------------|
| 4.0% | < 30 ppm | ≈ +0.35% | ≈ +18 kW |
| 3.0% | ≈ 30 ppm | Base | Base |
| 2.0% | 30–80 ppm | ≈ −0.35% | ≈ −17 kW |
| 1.5% | 100–200 ppm (approaching limit) | ≈ −0.5% | ≈ −25 kW |
| < 1.2% | Several hundred to > 1,000 ppm | Savings lost to unburned fuel; afterburning and APH deposit/fire risk | — |

The economic optimum sits just above the knee; its position depends on burner condition (plugged
tips, damaged tiles, uneven registers or windbox distribution move it to higher O2). High CO is a
safety hazard: combustibles can afterburn in the convection section and deposit on APH elements.

## 4. Objective Terms: Fuel, Fan Power and C-101

The optimizer objective is fuel cost + fan electrical power cost (JI-1341 + JI-1351) + amortized
decoke cost. Fan power (≈ 75 kW) is small against 38.5 MW fired, but electricity costs several times
more per MWh than fuel gas, so it enters three decisions: the O2 setpoint (Section 2), the draft
setpoint (Section 9) and the value of restoring APH seals or cleaning (leakage and fouling raise both
fan loads). COT is a given production target, not an optimizer decision; any firing or COT change
also moves C-101 flash-zone vaporization and cut yields and is coordinated with the C-101 operator.

## 5. Why Arch O2 Differs from True Burner O2

AIC-1321 samples at the arch, after all air that has entered the firebox has mixed in. Air leaking
in **below the arch** — peepholes, burner-tile gaps, floor and wall penetrations, header boxes — is
drawn in because the firebox is below atmospheric pressure, and it bypasses the burners:

> O2,arch ≈ (1 − f) × O2,burner + f × 20.9, where f = leak-air fraction of dry flue gas at the arch.

With f = 5% and burners at 2.0%, the arch reads ≈ 3.0%. Lowering the setpoint to 2.0% on the strength
of the arch reading takes the burners to ≈ 1.0% and CO rises — the signature is **CO rising while
AIC-1321 looks acceptable**. The optimizer constraint is therefore on burner-level O2 (≥ 1.5%), estimated
as AIC-1321 corrected for tramp air and analyzer error. Tramp air also costs fuel and ID-fan power: it
is heated and pulled through the APH and ID fan without contributing to combustion.

## 6. The O2 Measurement Chain (AT-1327, AT-1326)

| Difference | Normal | Investigate | Indicates |
|------------|--------|-------------|-----------|
| AT-1327 − AIC-1321 | ≈ 0.2 point | > ≈ 0.8 | Convection-section air ingress (above the arch) |
| AT-1326 − AT-1327 | ≈ 1.2 point (≈ 6% APH leakage) | > ≈ 2.0 | APH seal leakage, or leaks in the APH-to-ID-fan duct |

Neither difference sees leaks **below** the arch; those show only as CO and in the step test. A
negative AT-1327 − AIC-1321 is impossible without afterburning, so it indicates analyzer error (or
afterburning, if CO is high). An arch analyzer reading low also widens AT-1327 − AIC-1321 and can be
mistaken for convection ingress. If AIC-1321 reads high, the loop cuts FD air and runs the burners
short; if it reads low, the heater wastes fuel and fan power. Do not lower the O2 setpoint while the
analyzer is in doubt. Details: Instrument Datasheet — Flue Gas O2, CO and Stack CEMS Analyzers, Rev
1.6; SOP — Excess O2 Step Test (Analyzer / Air-Ingress Check), Rev 1.3; Maintenance Procedure — O2 and
CO Analyzer Calibration and Validation, Rev 2.2.

## 7. Air Flow Slave and Air/Fuel Cross-Limiting

The fired-duty demand from the COT cascade (TIC-1110 → PIC-1202) is converted to an air requirement
(stoichiometric air × fired duty FT-1201 × AT-1203), multiplied by the AIC-1321 trim (limited to
0.85–1.25) to give the FIC-1341 setpoint. Cross-limiting keeps the heater air-rich in transients:

- **Air leads on increase:** the FIC-1341 setpoint is the higher of the O2-trimmed demand and the
  air needed for the *demanded* firing; firing (the PIC-1202 setpoint) is limited to what the
  *measured* air flow supports.
- **Fuel leads on decrease:** firing falls first; air follows only when measured fuel has fallen.

FIC-1341 is measured at the FD discharge and **includes APH leakage**. The cross-limit subtracts the
design leakage (≈ 6%); if leakage has grown, the cross-limit overestimates the air reaching the
burners and is less conservative than intended. A rising AT-1326 − AT-1327 must therefore be followed
up even though the O2 loop hides it in steady state by raising FD flow.

## 8. Arch Draft Control by ID Fan Speed

PIC-1311 holds the arch — the point of least suction in the firebox — at −2.5 mmH₂O by trimming ID fan
speed (SC-1351). The floor (PT-1312) is ≈ −10, the convection outlet (PT-1313) ≈ −20 and the ID fan
inlet (PT-1352) ≈ −120 mmH₂O. The FD speed demand is fed forward to SC-1351 so that an air-flow change
does not first push the arch toward positive pressure. The fast VFD draft loop decouples the O2 loop
(minutes) from the draft loop (seconds). Manual practice: **set draft with the ID fan first, then O2
with the FD fan.** High O2 with excessive draft (arch more negative than −4 mmH₂O) is corrected by
lowering ID speed first, not by cutting FD air. Soot blowing (HS-1501) and burner light-offs cause
short draft transients that the loop rides through.

## 9. The Draft Setpoint as a Stretch Decision

Leak flow through any casing opening ≈ leak area × √(local draft). Raising the arch setpoint from
−2.5 toward zero reduces every leak in the firebox and convection section and slightly reduces ID fan
power. The gain is largest for leaks near the arch: −2.5 → −1.5 mmH₂O cuts arch-level leak flow by
≈ 23%, floor-level leak flow by ≈ 5%, and barely changes leaks at the convection outlet or APH ducts,
whose suction is set mainly by friction. The cost is **less margin to positive pressure**: a draft
disturbance (FD step, burner flame-out and relight, soot blowing, VFD transient) that was harmless at
−2.5 can take the arch to the PIC-1311 HH alarm (0.0 mmH₂O) — hot gas and CO out of peepholes — and,
if sustained, to the PT-1314 trip at +10 mmH₂O for 5 s. Do not stretch beyond −1.5 mmH₂O without a
recorded disturbance test showing the draft excursions; never operate at or above −1.0 mmH₂O. Do not
run deeper than −2.5 "for safety" without reason — it only adds tramp air and fan power.

## 10. APH Cold-End Control (TIC-1345 / TV-1345)

TIC-1345 is a minimum-temperature controller on the APH gas outlet. When the gas outlet falls toward
its setpoint it opens TV-1345, bypassing part of the cold air around E-102 so less heat is removed
and the gas leaves hotter. The 140 °C limit (LL alarm, optimizer constraint) protects the cold-end
elements and the stack from sulfuric-acid condensation. Lower air temperature (cold weather TT-1001),
low firing and a higher O2 setpoint (more air through the APH) all lower TIC-1345. Opening TV-1345
costs efficiency because bypassed air reaches the burners cold (TT-1343 lower). Caution: APH leak air
also lowers the measured TIC-1345 by dilution; check AT-1326 − AT-1327 before opening TV-1345 to
"correct" a low reading.

## 11. Natural-Draft Runback and Mode Handling

On FD stop (XS-1341), ID stop (XS-1351) or APH rotor stop (XS-1349) the BMS opens D-101 (XV-1361) and
D-102 (XV-1362), stops the other fan and clamps firing to ≤ 60%. AIC-1321, FIC-1341 and PIC-1311 go to
manual/track; arch draft is then set by the stack and firebox buoyancy, and O2 only by firing rate and
burner registers. Watch AT-1322 and keep the arch negative by limiting firing. Response and return to
balanced draft: SOP — FD / ID Fan Trip Response and Natural-Draft Operation, Rev 1.0; positive draft:
Troubleshooting Guide — Positive Draft and Afterburning, Rev 1.8.
