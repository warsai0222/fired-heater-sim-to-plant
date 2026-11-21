---
doc_id: ds_h101_crude_charge_heater
doc_type: datasheet
equipment: [heater_h101, radiant_section, radiant_coil, convection_section, burners, air_preheater, fd_fan, id_fan, bypass_dampers, stack, pass_flow_control, transfer_line, crude_charge_pumps, atmospheric_column]
tags: [FY-1100, TT-1100, PT-1100, TIC-1110, PT-1110, FT-1201, AT-1203, TT-1301A, TT-1301B, TT-1303, TIC-1345, TT-1343, PIC-1311, AIC-1321, AT-1322, AT-1327, AT-1326, FIC-1341, SI-1341, SI-1351, JI-1341, JI-1351, XS-1341, XS-1351, XS-1349, PDT-1347, TT-1001]
title: Equipment Datasheet — H-101 Crude Charge Heater (Overall)
revision: 2.2
date: 2026-11-20
---

# Equipment Datasheet — H-101 Crude Charge Heater (Overall)

**Document No.:** H101-DS-001
**Revision:** 2.2 | **Date:** 2026-11-20
**Applicability:** Unit 100 — H-101 Crude Charge Heater
**Owner:** Unit 100 Process Engineer
**P&ID Reference:** U100-PID-101 (process coil), U100-PID-102 (combustion, fuel gas, burners, BMS), U100-PID-103 (air preheater, FD/ID fans, ducts, dampers, stack); PFD U100-PFD-001
**Revision note:** Rev 2.2 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).

> Top-level datasheet for H-101. Component details are in the radiant coil, convection section,
> burner, fuel gas, air preheater, fan, stack/bypass damper and analyzer datasheets. Alarm and trip
> values quoted here are for information only; the controlling source is the
> Alarm and Trip Setpoint Register — H-101 Crude Charge Heater, Rev 3.1.

---

## 1. Service and General Description

H-101 heats the full crude charge of Unit 100 from the preheat-train outlet to the atmospheric column
(C-101) flash-zone feed temperature. It is a horizontal-tube **cabin heater**, **balanced draft**,
**floor-fired** by eight forced-draft low-NOx gas burners (B-101A–H) in one row on the firebox
centreline. The process coil is **4 passes**, each flowing first through the convection section
(counter-current to flue gas) and then, via external crossover piping, through the radiant section.

Combustion air is delivered by the forced draft fan **K-101** through the air side of the
regenerative (Ljungström) air preheater **E-102**, where it is heated to ≈ 300 °C (TT-1343), and on to
a common hot-air windbox under the burners. Flue gas leaving the convection section (≈ 390 °C,
TT-1303) passes through the gas side of E-102, is cooled to ≈ 150 °C (TIC-1345) and is drawn by the
induced draft fan **K-102** into the stack **S-101**. If either fan or the APH rotor stops, the heater
falls back to natural draft through the flue-gas bypass damper **D-101** (XV-1361) and the emergency
air doors **D-102** (XV-1362), limited to ≤ 60% firing (Section 8).

| Item | Value |
|------|-------|
| Equipment tag | H-101 |
| Heater type | Cabin, horizontal tubes, balanced draft, floor-fired |
| Number of passes | 4 (A, B, C, D) |
| Burners | 8 × forced-draft low-NOx gas burners, B-101A–H, common hot-air windbox |
| Fuel | Refinery fuel gas (main), regulated pilot gas (continuous pilots) |
| Draft | Balanced: FD fan K-101 (VFD SC-1341) + ID fan K-102 (VFD SC-1351); arch draft set by ID fan speed |
| Air preheat | Regenerative APH E-102, air ≈ 30 → 300 °C, duty ≈ 4.3 MW |
| Natural-draft fallback | D-101 bypass damper + D-102 emergency air doors, both fail open; ≤ 60% firing |
| Design code basis | API 560 (heater, APH and fans), API 530 (tube thickness) |
| Downstream / upstream | TL-101 to C-101 flash zone / preheat train fed by P-101A/B (boundary) |

## 2. Design Case — Process Conditions (Alaska North Slope, 50,000 bbl/d, clean, as-new)

| Parameter | Value | Tag |
|-----------|-------|-----|
| Design crude | Alaska North Slope (API 32.3) | — |
| Throughput | 50,000 bbl/d (≈ 7,950 m³/d) = 286 t/h | FY-1100 |
| Pass flow | 71.5 t/h per pass | FIC-1101..1104 |
| Heater inlet temperature / pressure | 250 °C / 11.0 barg | TT-1100 / PT-1100 |
| Coil inlet pressure (downstream of FV) | 8.5 barg | PT-1101..1104 |
| Crossover temperature | ≈ 292 °C | TT-1131..1134 |
| Coil outlet temperature (COT) | 360 °C (production target, given) | TIC-1110 |
| Coil outlet pressure | 2.5 barg | PT-1110 |
| Coil pressure drop, clean (per pass) | ≈ 6.0 bar | PDI-1101..1104 |
| Outlet phase | Two-phase (≈ 40–55 wt% vaporized, model computed) | — |

## 3. Design Case — Thermal Performance

| Parameter | Value | Tag / note |
|-----------|-------|------------|
| Absorbed duty | 35.0 MW | Sensible + latent |
| Radiant / convection duty | ≈ 26 / 9 MW (≈ 74 / 26%) | Hot air raises firebox temperature |
| APH duty | ≈ 4.3 MW, returned to the firebox as hot air | E-102 |
| Fired duty (LHV) | 38.5 MW | 35.0 / 0.91 |
| Thermal efficiency (LHV) | **≈ 91%** | Stack loss ≈ 6% + wall/duct loss ≈ 2.5% |
| Fuel gas flow / LHV | 2,860 kg/h (≈ 3,800 Nm³/h) / 48.5 MJ/kg | FT-1201 / AT-1203 |
| FD air (incl. APH leakage) | 57,850 kg/h | FIC-1341 |
| Air to burners | 54,370 kg/h at ≈ 300 °C (15% excess air) | TT-1343 |
| Flue gas firebox → APH / after APH | 57,230 / 60,700 kg/h | Difference = APH leak air (≈ 6% of FD air) |
| O2 chain (dry) | Arch 3.0% → APH inlet ≈ 3.2% → stack ≈ 4.4% | AIC-1321 → AT-1327 → AT-1326 |
| Bridgewall | ≈ 845 °C (envelope 760–900 °C) | TT-1301A/B |
| Convection outlet / APH gas inlet | ≈ 390 °C | TT-1303 |
| APH gas outlet / stack | ≈ 150 °C / ≈ 155 °C after ID fan | TIC-1345 |
| Arch draft | −2.5 mmH₂O | PIC-1311 |
| Average radiant flux / clean SOR hottest TMT | ≈ 34 kW/m² / ≈ 430 °C | Peak ≈ 1.8 × average |
| Fan speeds / motor power (normal) | FD 70% / ID 72%; ≈ 32 / 42 kW | SI-1341, SI-1351, JI-1341, JI-1351 |
| Maximum firing | ≤ 46 MW LHV (120% of normal) | FT-1201 × AT-1203 |
| Design ambient | 25 °C | TT-1001 |

**Efficiency basis.** Without the APH (Rev A) the flue gas could not leave much below ≈ 320 °C because
the coldest process stream in the convection section is crude at 250 °C; efficiency was ≈ 84%. The
APH transfers ≈ 4.3 MW from the flue gas to the combustion air, saving ≈ 3.2 MW of fuel (≈ 235 kg/h)
for ≈ 75 kW of fan power. The APH gas outlet temperature (≈ 160 °C before, ≈ 150 °C after leak-air
dilution) is now bounded by the cold-end acid-dew-point limit (TIC-1345 ≥ 140 °C), not by the crude.

## 4. Crude Slate and Coking Tendency

Volumetric charge is the operating target, so mass flow, duty and coking tendency change with the crude.

| Crude | API | Sulfur, wt% | TAN, mg KOH/g | MCR, wt% | C7 asphaltenes, wt% | 370 °C+ residue, wt% | Mass rate at 50,000 bbl/d |
|-------|-----|-------------|---------------|----------|---------------------|----------------------|---------------------------|
| WTI Light | 47.4 | 0.07 | 0.05 | 0.1 | 0.0 | 22.4 | ≈ 262 t/h |
| Alaska North Slope (design) | 32.3 | 1.04 | 0.41 | 4.7 | 1.9 | 43.5 | 286 t/h |
| Kearl (heavy) | 19.8 | 3.83 | 2.08 | 9.7 | 5.7 | 67.1 | ≈ 310 t/h |

A heavier crude does **not** automatically need more duty: more mass per barrel needs more sensible
heat, but less of it vaporizes at 360 °C, so less latent heat is needed. The net duty change must be
confirmed with the physics model for each crude. Coking rate rises with MCR and asphaltenes, with
tube film temperature and with residence time, so Kearl cokes faster than ANS at the same COT; its
high TAN also raises naphthenic-acid corrosion concern in the hot end and transfer line. Crude changes
follow SOP — Crude Switch / Crude Blend Change at H-101, Rev 1.8.

## 5. Mechanical Arrangement

| Item | Value |
|------|-------|
| Radiant box (inside refractory) | ≈ 7.0 m wide × 19.0 m long × 9.0 m floor-to-arch |
| Radiant tubes | 80 (20 per pass), 6" Sch 40, A335 P9, 18.3 m; area ≈ 766 m² |
| Convection section | 2 bare shield rows + 6 studded rows, 8 tubes per row (2 per pass) |
| Return bends | Welded long-radius (1.5D) 180° bends, suitable for mechanical pigging |
| Air preheater | E-102, rotary regenerative, vertical shaft, at grade beside the heater |
| Fans | K-101 FD and K-102 ID, centrifugal, VFD driven, at grade |
| Bypass damper / air doors | D-101 (convection outlet → stack, XV-1361), D-102 (windbox, XV-1362), both fail open |
| Stack | S-101, self-supporting steel, top ≈ 45 m above grade |
| Soot blowers | SB-101A–F (convection), SB-102A/B (APH), LP steam 3.5 barg |
| Snuffing steam / pass isolation | XV-1401, HV-1402 / XV-1105A–D, XV-1106A–D with spectacle blinds |

## 6. Operating Envelope (Optimizer and Operator Limits)

None of these is a trip; they are enforced by operator alarms (Alarm and Trip Setpoint Register —
H-101 Crude Charge Heater, Rev 3.1; Integrity Operating Windows (IOW) — H-101 Radiant Coil, Rev 2.1).

| Limit | Value | Tag(s) |
|-------|-------|--------|
| Hottest-tube TMT | ≤ 600 °C | TI-1121A..1124B |
| Coil ΔP per pass | ≤ 8.4 bar (≈ 40% above clean) | PDI-1101..1104 |
| Arch CO | ≤ 200 ppm | AT-1322 |
| Burner-level (true) O2 | ≥ 1.5% dry | AIC-1321 corrected for analyzer error and tramp air |
| Bridgewall | 760–900 °C | TT-1301A/B |
| Firing | ≤ 46 MW LHV | FT-1201 × AT-1203 |
| Draft | Arch negative (< 0) | PIC-1311 |
| APH gas outlet | ≥ 140 °C (acid dew point margin) | TIC-1345 |
| FD / ID fan speed | ≤ 95% | SI-1341 / SI-1351 |
| COT | 360 ± 2 °C (given target) | TIC-1110 |

The optimizer objective is fuel cost **plus fan electrical power** (JI-1341 + JI-1351) plus amortized
decoke cost. Any change of COT or firing also changes C-101 flash-zone vaporization and cut yields;
COT is not an optimizer decision and changes are coordinated with the C-101 operator.

## 7. Principal Degradation Mechanisms and Their Signatures

| Mechanism | Primary signature | What stays normal |
|-----------|-------------------|-------------------|
| Radiant tube coking | Skin TMT **and** coil ΔP of the same pass rise together over weeks; the coked pass runs a slightly **cooler** outlet while TIC-1110 fires harder | TT-1303, APH indicators |
| Convection fouling | TT-1303 rises, crossover TT-1131..1134 falls, more radiant firing for the same COT; hotter APH inlet also raises TIC-1345 | TMT/coil ΔP; O2 differences |
| Tramp air (firebox, convection) | Fuel per absorbed duty up; AT-1327 − AIC-1321 above ≈ 0.2 (convection leaks); CO rising at "normal" AIC-1321 (leaks below the arch) | Coil ΔP; AT-1326 − AT-1327 |
| APH seal leakage growth | AT-1326 − AT-1327 above ≈ 1.2; ID fan speed/power up; TIC-1345 lower by dilution; less hot air to burners for the same FIC-1341 | AT-1327 − AIC-1321 |
| APH fouling | PDT-1347 up; TT-1343 hot air down; TIC-1345 up; efficiency down; ID fan load up | O2 differences |
| O2 analyzer error | AIC-1321 inconsistent with AT-1327, AT-1326, fuel/air balance and a portable analyzer | Process-side readings |

See Troubleshooting Guide — High Tube Metal Temperature, Rev 2.4; Troubleshooting Guide — High Stack
Temperature, Rev 1.7; Troubleshooting Guide — High Fuel Consumption / Low Efficiency, Rev 2.1; and
Troubleshooting Guide — Air Preheater Leakage, Fouling and Low Cold-End Temperature, Rev 1.0.

## 8. Natural-Draft Fallback Capability

On FD fan stop (XS-1341), ID fan stop (XS-1351) or APH rotor stop (XS-1349) the BMS performs a
**natural-draft runback**, not a fuel trip: XV-1361 opens D-101 so flue gas goes from the convection
outlet straight to S-101, XV-1362 opens D-102 so the burners draw ambient air, the other fan is
stopped and firing is clamped to ≤ 60% of normal (≈ 23 MW). Without air preheat and with ≈ 350–400 °C
gas to the stack, efficiency falls to roughly 80–83%, so absorbed duty is only ≈ 50–55% of design:
charge must be cut or COT will fall. Either way C-101 flash-zone vaporization drops and distillate
shifts into residue — coordinate with the C-101 operator. Response: SOP — FD / ID Fan Trip Response
and Natural-Draft Operation, Rev 1.0. Equipment: Equipment Datasheet — S-101 Stack, D-101 Bypass
Damper and D-102 Emergency Air Doors, Rev 1.3.
