---
doc_id: ds_air_preheater
doc_type: datasheet
equipment: [air_preheater, soot_blowers, fd_fan, id_fan, bypass_dampers, flue_gas_analyzers, burners]
tags: [TT-1303, TT-1343, TIC-1345, PDT-1347, PDT-1348, XS-1349, AT-1327, AT-1326, AIC-1321, FIC-1341, SI-1341, SI-1351, JI-1351, PT-1313, PT-1352, HS-1501, TT-1001, AT-1322]
title: Equipment Datasheet — E-102 Regenerative Air Preheater
revision: 1.0
date: 2026-11-20
---

# Equipment Datasheet — E-102 Regenerative Air Preheater

**Document No.:** H101-DS-008
**Revision:** 1.0 | **Date:** 2026-11-20
**Applicability:** Unit 100 — H-101 Crude Charge Heater
**Owner:** Fixed Equipment (Mechanical Integrity) Engineer; Combustion / Heater Specialist Engineer
**P&ID Reference:** U100-PID-103 (air preheater, FD/ID fans, ducts, dampers, stack)

> New for the Rev B balanced-draft design (MOC-H101-2026-07). Values are preliminary design figures
> pending vendor data and the physics model.

---

## 1. Function and Arrangement

E-102 recovers heat from the flue gas leaving the convection section and returns it to the firebox
as hot combustion air. It is a **rotary regenerative (Ljungström)** preheater with a vertical shaft:
a slowly turning rotor packed with corrugated steel heating elements passes alternately through the
gas side, where the elements are heated, and the air side, where they release that heat. Flue gas
from the convection outlet (TT-1303, ≈ 390 °C) enters the hot end at the top and flows down; cold air
from FD fan K-101 enters the cold end at the bottom and flows up (counterflow). Hot air (TT-1343,
≈ 300 °C) goes to the burner windbox; cooled gas (TIC-1345, ≈ 150 °C) goes to ID fan K-102. A
cold-air bypass damper TV-1345 can route part of the FD air around E-102 to protect the cold end.

## 2. Design Data (ANS, 50,000 bbl/d, clean, as-new)

| Parameter | Value | Tag |
|-----------|-------|-----|
| Duty | ≈ 4.3 MW | — |
| Gas in / out (before leak-air dilution) | ≈ 390 °C / ≈ 160 °C | TT-1303 / — |
| Gas out, measured (after leak air mixes) | ≈ 150 °C | TIC-1345 |
| Air in / out | ≈ 30 °C (after FD fan) / ≈ 300 °C | — / TT-1343 |
| Gas flow in / out | 57,230 / 60,700 kg/h | — |
| FD air in / hot air to burners | 57,850 / 54,370 kg/h | FIC-1341 / — |
| Seal leakage, air to gas | ≈ 6% of FD air (≈ 3,470 kg/h), as new | AT-1326 − AT-1327 ≈ 1.2 point |
| Gas-side ΔP | ≈ 80 mmH₂O (Hi alarm 120) | PDT-1347 |
| Air-side ΔP | ≈ 50 mmH₂O (Hi alarm 75) | PDT-1348 |
| Rotor diameter / element depth | ≈ 4.3 m / ≈ 1.1 m (hot + intermediate + cold layers) | — |
| Rotor speed | ≈ 2 rpm, electric main drive with standby drive | XS-1349 (rotation) |
| Hot / intermediate elements | Carbon steel, 0.6 mm, notched-undulated profile | — |
| Cold-end elements | 0.3 m deep layer, porcelain-enamelled steel, open profile (easier cleaning) | — |
| Soot blowers | SB-102A (hot end), SB-102B (cold end), LP steam 3.5 barg | HS-1501 |

## 3. Rotor, Sector Plates and Seals

The rotor is divided into sectors by radial **diaphragms**. Stationary **sector plates** at the hot
and cold ends separate the gas and air streams; the rotor turns under them. Three seal systems limit
air-to-gas leakage:

| Seal | Location | Purpose |
|------|----------|---------|
| Radial seals | Flexible strips on the top and bottom edges of each diaphragm, sealing against the sector plates | Main barrier between air and gas sides across the rotor faces |
| Axial seals | Strips on the outside of the rotor shell at each diaphragm, sealing against axial seal plates | Stop leakage along the rotor periphery between the two sides |
| Circumferential (bypass) seals | Rings at the top and bottom of the rotor shell | Stop gas or air bypassing around the outside of the rotor without passing through the elements |

The hot-end sector plates are adjustable so their gap can be set for the hot, distorted rotor (Section
4). Seal clearances are set cold at overhaul with allowance for thermal movement and checked at every
planned shutdown per Maintenance Procedure — Air Preheater Seal Inspection, Soot Blowing and Water
Washing, Rev 1.0.

## 4. Leakage Mechanism and Why It Grows

The air side is at positive pressure (FD discharge ≈ +130 mmH₂O) and the gas side under suction
(≈ −20 mmH₂O at the hot end, falling further across the elements), so the pressure difference across
the seals is roughly 170 mmH₂O at the hot end and over 250 mmH₂O at the cold end. Leakage has two parts:

- **Direct (seal) leakage:** flow through seal gaps, ≈ gap area × √(ΔP). This is the part that grows.
- **Entrained (carry-over) leakage:** air trapped in the element voids carried into the gas side by
  rotation, ≈ 0.5–1% of air flow, roughly constant at fixed speed.

Direct leakage grows over a run because: seal strips wear and erode by rubbing and fly-ash/deposit
abrasion; the rotor "turns down" (the hot end expands more than the cold end, so the rotor dishes and
opens the outer hot-end radial gaps), more so at high firing; seals are bent by start-up and trip
transients; cold-end seals corrode if the cold end runs below the acid dew point; and fouling or a
higher FD discharge pressure raises the ΔP that drives the leak.

**Consequences of higher leakage:** FD fan must deliver more air for the same burner air; ID fan must
move more gas, so SI-1351 and JI-1351 rise toward the 95% speed limit; stack O2 AT-1326 rises relative
to AT-1327; the measured gas outlet TIC-1345 falls because cold leak air dilutes the gas (this is
**not** better heat recovery); and for the same FIC-1341 reading less hot air reaches the burners,
so AIC-1321 falls and the O2 loop raises the FD air setpoint. Leak air passes through no burner and
adds stack loss and fan power. A leak-corrected gas outlet temperature is estimated as
TIC-1345 + leak fraction × ≈ 0.93 × (TIC-1345 − air inlet temperature), ≈ 157–160 °C at design.

## 5. Cold End, Acid Dew Point and TV-1345

Each element alternately meets cold air and cooled gas, so the coldest metal is at the cold end and
sits roughly midway between the air inlet and gas outlet temperatures (cold-end average temperature,
CEAT ≈ ½ × (TIC-1345 + air inlet)). Refinery fuel gas contains some H2S, so the flue gas carries traces
of SO3; below the sulfuric-acid dew point (estimated ≈ 90–110 °C for amine-treated fuel gas, depending
on H2S) acid condenses on the elements, corrodes them and makes deposits sticky. The enamelled
cold-end layer tolerates brief excursions; sustained low temperatures do not.

The operating limit is **TIC-1345 ≥ 140 °C** (LL alarm and optimizer constraint, not a trip), with a Lo
alarm at 145 °C. TIC-1345 opens the cold-air bypass TV-1345 (fail closed) when the gas outlet falls
toward its minimum: less air through E-102 means less heat removed, so the gas leaves hotter. TV-1345
is normally closed at design and opens in cold weather (low TT-1001 lowers the air inlet and the
CEAT) and at low firing. Opening TV-1345 costs efficiency (bypassed air reaches the burners colder)
and must never be used to "cure" a low TIC-1345 caused by leak-air dilution — check AT-1326 − AT-1327
first. Response: Troubleshooting Guide — Air Preheater Leakage, Fouling and Low Cold-End Temperature, Rev 1.0.

## 6. Fouling

Gas-fired fouling is light but steady: refractory dust and convection deposits carried over, iron
sulfate and acid-bonded deposits at the cold end (worse after cold-end excursions), and soot after CO
excursions. Signature: gas-side ΔP PDT-1347 rises (and, more slowly, air-side PDT-1348); hot air
TT-1343 falls; gas outlet TIC-1345 rises; efficiency falls; and the ID fan needs more speed for the
same draft. Higher ΔP also slightly raises seal leakage. Distinguish from leakage: fouling raises
TIC-1345, leakage lowers it; leakage moves AT-1326 − AT-1327, fouling does not.

## 7. Soot Blowing and Water Washing

SB-102A (hot end) and SB-102B (cold end) are swivel-arm steam blowers that sweep the element face
radially while the rotor turns. They run in the HS-1501 sequence **after** convection blowers
SB-101A–F, ≈ 10 min each, typically daily, and additionally when PDT-1347 is rising. LP steam must be
thoroughly drained and dry before blowing: wet steam on the cold end makes deposits sticky and acidic.
When soot blowing no longer restores PDT-1347, the elements are **water washed** offline at a heater
shutdown, with the rotor turning, alkaline-neutralized wash water and complete drying with warm air
before return to service. Procedure: Maintenance Procedure — Air Preheater Seal Inspection, Soot
Blowing and Water Washing, Rev 1.0.

## 8. Rotor-Stop Protection and Fire Risk

The rotor must turn whenever hot gas is present. A stopped rotor stops heating the air (burners lose
hot air), heats one sector unevenly (rotor and seal distortion), and leaves a hot sector in the gas
stream where deposits can ignite. The rotation monitor **XS-1349** initiates a **natural-draft
runback** on rotor stop: as for an ID fan stop, D-101 (XV-1361) and D-102 (XV-1362) open, both fans
stop so no gas or air is forced through E-102, firing is clamped to ≤ 60%, and an APH fire watch is
posted. The standby drive is started locally to restore rotation as soon as it is safe.

**APH fires** start when combustible deposits (soot or unburned hydrocarbons after CO excursions or
fuel-gas liquid carry-over) accumulate on the elements, typically at low load or during start-up, and
ignite. Signs: TT-1343 and/or TIC-1345 rising quickly with no firing change, gas outlet hotter than
expected for the inlet, smoke or glow at casing doors. Response: go to natural-draft bypass (cuts air
supply), keep the rotor turning if possible, apply steam through SB-102A/B and fire water as directed,
per Emergency Response — Tube Rupture and Firebox Fire, Rev 2.3. Prevention: avoid prolonged high CO
(AT-1322) and keep soot blowing effective.
