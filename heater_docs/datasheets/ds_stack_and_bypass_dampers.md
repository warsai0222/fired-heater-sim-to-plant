---
doc_id: ds_stack_and_bypass_dampers
doc_type: datasheet
equipment: [stack, bypass_dampers, id_fan, fd_fan, air_preheater, convection_section, radiant_section, burners]
tags: [PIC-1311, PT-1312, PT-1313, PT-1314, PT-1352, PT-1342, ZT-1361, ZT-1362, XS-1341, XS-1351, XS-1349, TT-1303, TIC-1345, AT-1326, AT-1325, TT-1001]
title: Equipment Datasheet — S-101 Stack, D-101 Bypass Damper and D-102 Emergency Air Doors
revision: 1.3
date: 2026-11-20
---

# Equipment Datasheet — S-101 Stack, D-101 Bypass Damper and D-102 Emergency Air Doors

**Document No.:** H101-DS-006
**Revision:** 1.3 | **Date:** 2026-11-20
**Applicability:** Unit 100 — H-101 Crude Charge Heater
**Owner:** Fixed Equipment (Mechanical Integrity) Engineer; Instrument & Controls Engineer (XV-1361 / XV-1362 actuators)
**P&ID Reference:** U100-PID-103 (air preheater, FD/ID fans, ducts, dampers, stack)
**Revision note:** Rev 1.3 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).

> Supersedes the Rev A datasheet for the S-101 stack and D-101 stack damper (doc_id
> ds_stack_and_damper, last issued at revision 1.2), which is withdrawn: the stack damper no longer exists and the
> equipment tag D-101 is reused for the flue-gas bypass damper.

---

## 1. Description and What Changed

H-101 is a **balanced-draft** heater. Draft is produced by the ID fan K-102, whose speed (VFD
SC-1351) is manipulated by the arch draft controller PIC-1311; the stack S-101 only discharges the ID
fan exhaust to atmosphere. The Rev A natural-draft stack damper, its position transmitter and its
minimum-open stop no longer exist. Two on/off natural-draft fallback devices replace it:

- **D-101 flue-gas bypass damper (XV-1361, position ZT-1361):** a damper from the convection outlet
  duct direct to the stack base, bypassing the air preheater E-102 and the ID fan. Closed in
  balanced-draft operation; **fails open**.
- **D-102 emergency air doors (XV-1362, position ZT-1362):** doors on the burner windbox that admit
  ambient air when the FD fan is not running. Closed in balanced-draft operation; **fail open**.

Both open automatically on FD fan stop (XS-1341), ID fan stop (XS-1351) or APH rotor stop (XS-1349),
as part of the natural-draft runback to ≤ 60% firing. Neither is a modulating control element.

## 2. S-101 Stack Data

| Parameter | Value |
|-----------|-------|
| Tag | S-101 |
| Type | Self-supporting, refractory-lined carbon steel, at grade after ID fan |
| Top elevation | ≈ 45 m above grade |
| Inside diameter (inside lining) | 2.3 m |
| Shell / lining | SA-283 Gr C, 10 mm tapering to 8 mm / 50 mm insulating castable, anchored |
| Normal flue gas | 60,700 kg/h at ≈ 155 °C (ID fan discharge, incl. APH leak air) |
| Normal velocity | ≈ 5 m/s |
| Bypass (natural-draft) flue gas | ≈ 30,000–35,000 kg/h at ≈ 350–400 °C (≤ 60% firing) |
| Stack draft at bypass conditions | ≈ 0.65 mmH₂O per metre of hot stack (flue ≈ 380 °C, ambient 25 °C) |
| CEMS platform | ≈ 30 m above grade, ≥ 8 diameters downstream of the ID fan / bypass entries |
| Sampling ports | 2 × 4" flanged at 90° (CEMS AT-1325/AT-1326 and test port) |

The lining is retained because the stack must accept ≈ 400 °C gas on bypass. In normal operation the
flue gas is only ≈ 155 °C and the lining keeps the shell warm; shell temperatures below the acid dew
point would corrode it, which is one reason the APH cold end is held at TIC-1345 ≥ 140 °C.

## 3. D-101 Flue-Gas Bypass Damper (XV-1361)

| Parameter | Value |
|-----------|-------|
| Tag / final element / position | D-101 / XV-1361 / ZT-1361 |
| Service | Convection outlet → stack base, bypassing E-102 and K-102 |
| Type | Multi-louvre, opposed-blade, refractory-lined frame, low-leakage blade seals |
| Design temperature | 450 °C |
| Actuator | Pneumatic, spring return |
| Fail position | **Open** |
| Stroke time to open | ≤ 15 s |
| Normal position | Closed (ZT-1361 = 0%); open alarm at 5% |
| Purpose of fail-open | Gives a natural-draft flue path if the ID fan stops or the APH must be bypassed |

A partly open or leaking D-101 in balanced draft short-circuits gas between the stack base and the
convection outlet duct: it wastes ID fan power, lowers APH heat recovery and can disturb AT-1327 and
TT-1303. Any ZT-1361 reading above 5% with both fans running is investigated.

## 4. D-102 Emergency Air Doors (XV-1362)

| Parameter | Value |
|-----------|-------|
| Tag / final element / position | D-102 / XV-1362 / ZT-1362 |
| Location | Burner windbox (hot-air side, downstream of E-102) |
| Type | Hinged doors with counterweights, held closed by pneumatic cylinders |
| Fail position | **Open** (counterweight opens on loss of air or BMS signal) |
| Normal position | Closed (ZT-1362 = 0%) against windbox pressure ≈ +60 mmH₂O (PT-1342); open alarm 5% |
| Natural-draft air capacity (with D-101 open) | ≈ 60% of design firing |

With the FD fan running the windbox is above atmospheric pressure, so an open or leaking door blows
≈ 300 °C air outward: a burn hazard at the door, a loss of windbox pressure and of burner air, and a
fall in AIC-1321 that the O2 loop answers with more FD flow. Keep personnel clear of the doors.

## 5. Draft and Pressure Profile (design, balanced draft)

| Location | Pressure, mmH₂O | Tag |
|----------|-----------------|-----|
| FD fan discharge / APH air inlet | ≈ +200 | — |
| Burner windbox (hot air) | ≈ +60 | PT-1342 |
| Firebox floor / burner level | −10.0 | PT-1312 |
| Arch (top of radiant) | −2.5 (controlled by ID fan speed) | PIC-1311, PT-1314 (SIS) |
| Convection outlet / APH gas inlet | ≈ −20 | PT-1313 |
| ID fan inlet (after APH) | ≈ −120 | PT-1352 |
| ID fan discharge / stack base | ≈ +10 | — |

The arch is the point of least suction in the firebox: floor draft is ≈ 7.5 mmH₂O stronger because of
the ≈ 9 m column of ≈ 845 °C gas. Everything from the firebox to the ID fan inlet is below
atmospheric pressure and can draw in tramp air; leaks in the APH gas-outlet duct and ID fan inlet
box, at up to −120 mmH₂O, admit far more air per unit area than firebox leaks and appear in
AT-1326 together with APH seal leakage. PT-1314 trips main fuel at +10 mmH₂O for 5 s.

## 6. Ambient Effects

In balanced draft, ambient temperature TT-1001 affects draft mainly through the fans: hot air is less
dense, so the FD fan needs more speed for the same mass flow. In natural-draft fallback, available
stack and firebox draft fall on hot days (≈ −9% at 40 °C vs 25 °C) and rise on cold days
(≈ +18% at 0 °C), so the achievable firing on bypass is lower in summer than the nominal 60%.

## 7. Instruments

| Tag | Service | Normal | Alarms / trips |
|-----|---------|--------|----------------|
| PIC-1311 | Arch draft control → ID fan VFD SC-1351 | −2.5 mmH₂O | Lo −6.0, Hi −0.5, HH 0.0 (alarm) |
| PT-1314 | Firebox pressure high-high (SIS) | −2.5 mmH₂O | **HH +10 mmH₂O, 5 s = main fuel trip** |
| PT-1312 / PT-1313 / PT-1352 | Floor draft / convection outlet / ID fan inlet | −10 / −20 / −120 mmH₂O | PT-1312 Hi −6.0 |
| ZT-1361 / ZT-1362 | D-101 / D-102 position | 0% | Hi (open) 5% |
| TIC-1345 | APH gas outlet temperature | 150 °C | Lo 145, LL 140 °C (alarm) |
| AT-1326 / AT-1325 | Stack O2 / NOx (CEMS) | 4.4% dry / 80 mg/Nm³ | NOx Hi 150 |

Draft transmitters are low-range differential units referenced to atmosphere at the same elevation,
with purged impulse lines; a plugged or water-logged line shows as a flat, unresponsive signal.

## 8. Inspection Points

- Stroke-test XV-1361 and XV-1362 to the open position at each planned shutdown and confirm ZT-1361 /
  ZT-1362 against the local indicator; a slipped linkage gives a "closed" reading on an open device.
- D-101 blade seals and D-102 door gaskets for leakage; hot spots by infrared survey.
- Stack shell hot spots (lining loss) and, in the low-temperature normal mode, signs of acid
  corrosion at the shell and at the CEMS ports.
- Breeching and duct flanges between E-102 and K-102 (highest suction in the system).
