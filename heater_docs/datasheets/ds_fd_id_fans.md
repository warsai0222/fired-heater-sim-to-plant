---
doc_id: ds_fd_id_fans
doc_type: datasheet
equipment: [fd_fan, id_fan, air_preheater, bypass_dampers, burners, bms_sis]
tags: [FIC-1341, SI-1341, JI-1341, XS-1341, PIC-1311, PT-1352, SI-1351, JI-1351, XS-1351, PT-1314, PT-1342, XS-1349, ZT-1361, ZT-1362, AIC-1321, AT-1326, AT-1327, PDT-1347, TT-1001]
title: Equipment Datasheet — K-101 Forced Draft Fan and K-102 Induced Draft Fan
revision: 1.0
date: 2026-11-20
---

# Equipment Datasheet — K-101 Forced Draft Fan and K-102 Induced Draft Fan

**Document No.:** H101-DS-009
**Revision:** 1.0 | **Date:** 2026-11-20
**Applicability:** Unit 100 — H-101 Crude Charge Heater
**Owner:** Rotating Equipment Engineer; Instrument & Controls Engineer (VFDs SC-1341 / SC-1351)
**P&ID Reference:** U100-PID-103 (air preheater, FD/ID fans, ducts, dampers, stack)

> New for the Rev B balanced-draft design (MOC-H101-2026-07). Values are preliminary design figures
> pending vendor fan curves and the physics model.

---

## 1. Duties

| Fan | Duty | Manipulated by | Final element |
|-----|------|----------------|---------------|
| K-101 FD fan | Delivers all combustion air: ambient → E-102 air side → burner windbox | Combustion-air flow controller FIC-1341 (slave of arch O2 AIC-1321) | VFD SC-1341 |
| K-102 ID fan | Draws all flue gas: convection outlet → E-102 gas side → stack S-101; sets firebox draft | Arch draft controller PIC-1311 | VFD SC-1351 |

The FD fan sets **how much air** enters; the ID fan sets **where the zero-pressure point sits**. Both
must run for balanced-draft operation. Neither fan has inlet vanes or a control damper; flow is set
by speed only. Both VFDs hold last speed on signal loss.

## 2. Fan Data (design case)

| Parameter | K-101 FD fan | K-102 ID fan |
|-----------|--------------|--------------|
| Type | Centrifugal, backward-curved, single inlet | Centrifugal, backward-inclined, single inlet, wear liners |
| Gas | Ambient air, 25 °C in | Flue gas incl. APH leak air, ≈ 150 °C in |
| Mass flow | 57,850 kg/h (FIC-1341) | 60,700 kg/h |
| Volume flow | ≈ 13.6 m³/s | ≈ 20 m³/s |
| Pressure rise | ≈ 1.5 kPa (≈ 155 mmH₂O: inlet filter/silencer −25, APH air side 50, ducts 20, windbox +60) | ≈ 1.3 kPa (≈ 135 mmH₂O: ≈ −120 mmH₂O inlet PT-1352 to ≈ +15 mmH₂O discharge) |
| Efficiency (fan) | ≈ 0.75 | ≈ 0.72 |
| Absorbed power, design | ≈ 30 kW | ≈ 40 kW |
| Electrical power at normal (incl. motor/VFD losses) | ≈ 32 kW (JI-1341) | ≈ 42 kW (JI-1351) |
| Motor rating | 75 kW, 4-pole | 90 kW, 6-pole |
| Normal speed (% of maximum) | ≈ 70% (SI-1341) | ≈ 72% (SI-1351) |
| Speed capacity limit | 95% (SI-1341 Hi alarm) | 95% (SI-1351 Hi alarm) |
| Motor power Hi alarm | 60 kW (JI-1341) | 75 kW (JI-1351) |
| Running status (to BMS) | XS-1341 | XS-1351 |
| Design temperature | 60 °C | 450 °C (bypass upset cases) |

The ID fan handles a larger and hotter volume than the FD fan even though the mass flows are similar,
which is why it has the larger motor. Fan bearings carry local vibration and temperature monitoring
with machine protection in the motor control centre.

## 3. Variable-Speed Drives SC-1341 / SC-1351

| Parameter | Value |
|-----------|-------|
| Type | Low-voltage PWM VFD, one per fan |
| Speed range in operation | ≈ 30–95% of maximum |
| Ramp limits | ≈ 10% of speed per second (protects against draft pulses) |
| On DCS signal loss | Hold last speed |
| Speed / power feedback | SI-1341, SI-1351 / JI-1341, JI-1351 |
| Feedforward | FD speed demand feeds forward to the ID draft loop, so an air-flow change does not first pressurize the firebox |

Draft control by VFD is fast and smooth (closed-loop ≈ 10–20 s), which is what allows a tighter arch
draft setpoint than the Rev A natural-draft damper could hold. See Control Philosophy — Excess O2 and
Arch Draft Control, Rev 2.5.

## 4. Fan Laws and Power Cost

At a fixed system resistance, flow ∝ speed, pressure ∝ speed², power ∝ speed³:

| Change | FD fan | ID fan |
|--------|--------|--------|
| +5% air (≈ +1 point O2 setpoint) | ≈ +16% power (≈ +5 kW) | ≈ +14% power (≈ +6 kW) |
| Deeper arch draft setpoint | Negligible | Small direct power increase, plus more tramp air to move |
| APH leakage 6% → 12% of air | ≈ +6% air → ≈ +20% power | ≈ +6% gas → ≈ +20% power, speed toward limit |
| Firing at 46 MW (≈ 120% air) | Speed ≈ 84%; power ≈ 30 × 1.2³ ≈ 52 kW | Speed ≈ 86%; power ≈ 40 × 1.2³ ≈ 69 kW |

Fan electrical power (JI-1341 + JI-1351, ≈ 75 kW at design) is a term in the optimizer objective. It
is small against fired duty (≈ 0.3%) but electricity costs several times more per MWh than fuel
gas, so it matters in the O2, draft and APH-maintenance decisions. The last row shows that at the
46 MW firing limit both fans stay within their motor ratings (75 / 90 kW) and below the 95% speed
limit, so the speed limit — not motor power — is the capacity constraint; the JI Hi alarms (60 / 75 kW)
are a backstop. Margin shrinks as APH leakage or fouling grows. Confirm against vendor fan curves.

## 5. Capacity Limit (95% Speed)

95% speed is treated as the capacity limit for each fan (optimizer constraint and Hi alarm on SI-1341
/ SI-1351): it leaves control margin for disturbances and keeps the VFD and motor within rating. What
drives each fan toward it:

- **ID fan K-102:** APH seal leakage growth (more gas), APH fouling (PDT-1347 up, more pressure rise
  needed), tramp air in the firebox and convection, higher firing, a deeper draft setpoint.
- **FD fan K-101:** higher firing, higher O2 setpoint, APH leakage (part of FD air never reaches the
  burners), APH air-side fouling (PDT-1348), hot ambient TT-1001 (lower air density).

When the ID fan reaches its limit the arch draft PIC-1311 drifts toward zero and positive pressure
(PIC-1311 HH 0.0 alarm, PT-1314 trip at +10 mmH₂O): firing must not be increased further. When the
FD fan reaches its limit, O2 can no longer be held as firing rises; reduce firing. Both conditions
reduce the heater's achievable charge or COT, with knock-on effects on C-101 — coordinate with the
C-101 operator.

## 6. Fan Trips and the Natural-Draft Runback

A fan stop is **not** a fuel trip. On XS-1341 = 0 (FD stop) or XS-1351 = 0 (ID stop) the BMS:

1. Opens D-101 bypass damper XV-1361 (flue path to stack) and D-102 emergency air doors XV-1362
   (ambient air to windbox); confirmed by ZT-1361 / ZT-1362.
2. Stops the other fan. With only the FD fan running the firebox would pressurize; with only the ID
   fan running it would pull uncontrolled suction and cold air through the open air doors.
3. Clamps firing to ≤ 60% of normal (PIC-1202 high clamp) and puts AIC-1321, FIC-1341 and PIC-1311 in
   manual/tracking.

An ID fan stop is the most time-critical: firebox pressure starts to rise within seconds, so D-101
must open quickly and PT-1314 (+10 mmH₂O, 5 s → main fuel trip) is the backstop if it does not. An
APH rotor stop (XS-1349) triggers the same runback. Restart of the fans and return to balanced draft
follow SOP — FD / ID Fan Trip Response and Natural-Draft Operation, Rev 1.0; trip logic is in BMS /
SIS Cause and Effect — H-101, Rev 3.3.

## 7. Instruments

| Tag | Service | Normal | Alarms / action |
|-----|---------|--------|-----------------|
| FIC-1341 | Combustion air flow (FD discharge, incl. APH leakage) | 57,850 kg/h | Lo 45,000 kg/h |
| PT-1342 | Burner windbox pressure | +60 mmH₂O | Lo 20 mmH₂O |
| SI-1341 / SI-1351 | FD / ID fan speed | 70% / 72% | Hi 95% |
| JI-1341 / JI-1351 | FD / ID motor power | 32 / 42 kW | Hi 60 / 75 kW |
| PT-1352 | ID fan inlet pressure | −120 mmH₂O | — |
| XS-1341 / XS-1351 | FD / ID running status | 1 | 0 → natural-draft runback |
