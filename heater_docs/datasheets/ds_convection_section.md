---
doc_id: ds_convection_section
doc_type: datasheet
equipment: [convection_section, soot_blowers, heater_h101, air_preheater, bypass_dampers]
tags: [TT-1131, TT-1132, TT-1133, TT-1134, TT-1301A, TT-1301B, TT-1302, TT-1303, PIC-1311, PT-1313, AIC-1321, AT-1327, AT-1326, AT-1322, TIC-1345, HS-1501]
title: Equipment Datasheet — H-101 Convection Section
revision: 1.5
date: 2026-11-20
---

# Equipment Datasheet — H-101 Convection Section

**Document No.:** H101-DS-003
**Revision:** 1.5 | **Date:** 2026-11-20
**Applicability:** Unit 100 — H-101 Crude Charge Heater
**Owner:** Fixed Equipment (Mechanical Integrity) Engineer
**P&ID Reference:** U100-PID-101 (process coil), U100-PID-103 (air preheater, FD/ID fans, ducts, dampers, stack)
**Revision note:** Rev 1.5 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).

---

## 1. Description

The H-101 convection section sits directly above the radiant arch. Flue gas leaves the radiant
section at the bridgewall (TT-1301A/B, ≈ 845 °C), passes up through two rows of bare **shield
tubes**, then six rows of **studded tubes**, and leaves the convection outlet at ≈ 390 °C (TT-1303).
From the convection outlet the flue gas is ducted to the gas inlet (hot end) of the regenerative air
preheater E-102; the convection section is no longer the last heat-recovery stage. In natural-draft
fallback the D-101 bypass damper (XV-1361) opens and the gas goes straight from the convection
outlet to the stack S-101.

Crude from the inlet header enters the top (coldest) studded row of each pass and flows downward,
counter-current to the flue gas, leaving from the shield rows through external crossover piping to
the radiant coil (TT-1131..1134, ≈ 292 °C). The section recovers about 26% (≈ 9 MW) of the absorbed
duty. There is no steam generation coil.

## 2. Tube Bank Data

| Parameter | Shield rows | Studded rows |
|-----------|-------------|--------------|
| Number of rows | 2 | 6 |
| Tubes per row | 8 (2 per pass) | 8 (2 per pass) |
| Tubes per pass | 4 | 12 |
| Tube size | 6" Sch 40, OD 168.3 mm, wall 7.11 mm | 6" Sch 40, OD 168.3 mm, wall 7.11 mm |
| Tube material | ASTM A335 P9 | ASTM A335 P5 |
| Effective length | 18.3 m | 18.3 m |
| Extended surface | None (bare; sees radiant heat from firebox) | Studs 12.7 mm dia × 25.4 mm high, 11–13Cr (Type 410S) |
| Tube pitch | 254 mm triangular | 254 mm triangular |
| Surface area | ≈ 155 m² (bare) | ≈ 1,250 m² (studs + bare) |
| Tube supports | Intermediate tube sheets, 25Cr-20Ni cast | Intermediate tube sheets, 25Cr-12Ni cast |

The convection coil uses the same 6" bore and long-radius (1.5D) return bends as the radiant coil
so that the whole pass, convection plus radiant, can be mechanically pigged in one run and there is
no velocity step at the crossover. The tube bank is unchanged from Rev A; only the flue-gas
conditions changed.

## 3. Design Performance (ANS, 50,000 bbl/d, clean)

| Parameter | Value | Tag |
|-----------|-------|-----|
| Convection duty | ≈ 9 MW (≈ 26% of absorbed) | — |
| Crude in / out | 250 °C / ≈ 292 °C | TT-1100 / TT-1131..1134 |
| Crossover temperature Hi alarm | 310 °C | TT-1131..1134 |
| Flue gas at bridgewall | ≈ 845 °C | TT-1301A/B |
| Flue gas between shield and studded rows | ≈ 740 °C (Hi alarm 800 °C) | TT-1302 |
| Flue gas at convection outlet / APH gas inlet | ≈ 390 °C (Hi alarm 440 °C) | TT-1303 |
| Flue gas mass flow | 57,230 kg/h (≈ 6% less than Rev A, less fuel fired) | — |
| Draft, arch (bottom of section) | −2.5 mmH₂O | PIC-1311 |
| Draft, convection outlet / APH gas inlet | ≈ −20 mmH₂O | PT-1313 |
| O2 at convection outlet / APH gas inlet | ≈ 3.2% dry (≈ 0.2 above arch, as commissioned) | AT-1327 |

The cold-end approach (flue gas ≈ 390 °C leaving against crude 250 °C entering) is ≈ 140 °C. The
convection bank is intentionally not extended to a closer approach: the remaining heat between
≈ 390 °C and ≈ 160 °C is recovered more cheaply into combustion air in E-102, which also returns it
to the firebox and shifts duty into the radiant section.

## 4. Casing, Refractory and Tramp-Air Openings

| Item | Value |
|------|-------|
| Casing | 6 mm carbon steel plate, seal-welded |
| Lining | 125 mm dual-layer castable (insulating backup + 1,200 °C hot face) |
| Header boxes | Both ends, bolted access doors with gaskets; return bends inside |
| Tube-sheet penetrations | Sleeved, with ceramic fibre packing and seal plates |
| Soot-blower wall boxes | 6, one per soot blower SB-101A–F |
| Access / inspection doors | 4 (2 per long side), gasketed |
| Design casing temperature | ≤ 82 °C at 27 °C ambient, still air |

The convection section runs between −2.5 mmH₂O (arch) and ≈ −20 mmH₂O (outlet), so every opening
(header-box doors, tube-sheet sleeves, soot-blower wall boxes, inspection doors, cracked casing) is
a potential tramp-air path even with balanced draft. Leak flow ≈ leak area × √(local draft); the
draft profile is now set by the ID fan through the arch draft setpoint, not by the stack. Leaks near
the outlet, where suction is strongest, admit the most air per unit area. Air entering here bypasses
the burners: it does not affect arch O2 AIC-1321 but raises **AT-1327 above AIC-1321**, cools the
flue gas, lowers the APH inlet temperature and adds stack loss and ID-fan load. As commissioned,
AT-1327 − AIC-1321 ≈ 0.2 percentage point; investigate above ≈ 0.8 (Maintenance Procedure — Tramp
Air Survey and Casing Sealing, Rev 1.5). APH seal leakage, by contrast, shows in AT-1326 − AT-1327.

## 5. Soot Blowers

| Parameter | Value |
|-----------|-------|
| Tags | SB-101A–F (6 blowers) |
| Type | Long retractable, single-nozzle-pair lance, travels parallel to tubes |
| Arrangement | 3 lanes (above shield rows, between studded rows 2/3, between studded rows 4/5), 2 lances per lane from opposite end walls |
| Lance travel | ≈ 9.3 m each (half the tube length) |
| Blowing medium | LP steam, 3.5 barg, 150 °C |
| Steam consumption | ≈ 2 t/h per blower while blowing |
| Sequence | HS-1501, one blower at a time, SB-101A→F then APH blowers SB-102A/B, typically daily |
| Blow time | ≈ 4 min per blower, ≈ 35 min for SB-101A–F including drains |

Fuel-gas firing deposits little soot; fouling here is mainly corrosion product, sulfate/salt
deposits from fuel-gas contaminants, and refractory dust lodged between studs. Convection blowing
runs **before** the APH blowers so that dislodged deposit carried downstream is then removed from the
APH elements. Blowing steam adds water vapour and a brief draft disturbance; the ID-fan draft loop
PIC-1311 absorbs it, and a short transient in AIC-1321 and AT-1327 is normal. Procedure:
Maintenance Procedure — Convection Section Soot Blowing, Rev 1.9.

## 6. Convection Fouling Signature

Convection fouling reduces heat recovery in the convection section. With the APH downstream the
signature extends past the convection outlet:

- TT-1303 (convection outlet / APH gas inlet) rises at constant charge, crude and COT (Hi 440 °C).
- Crossover temperatures TT-1131..1134 fall: the crude picks up less heat before the radiant.
- The radiant section must absorb more duty for the same COT, so firing (FT-1201) and bridgewall
  TT-1301A/B rise.
- The hotter APH inlet raises the APH gas outlet TIC-1345 and hot-air temperature somewhat; the APH
  recovers part of the lost convection duty, so the efficiency penalty is smaller than in Rev A, but
  not zero.
- Radiant coil indicators (TMT TI-1121A..1124B, coil ΔP PDI-1101..1104) stay essentially normal;
  AT-1327 − AIC-1321 and AT-1326 − AT-1327 are unchanged.

Distinguish from convection air ingress (AT-1327 − AIC-1321 grows; TT-1303 flat or lower by
dilution) and from afterburning (TT-1302/TT-1303 up with high arch CO AT-1322). See Troubleshooting
Guide — High Stack Temperature, Rev 1.7.
