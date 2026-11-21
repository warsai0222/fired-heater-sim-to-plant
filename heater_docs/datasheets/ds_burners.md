---
doc_id: ds_burners
doc_type: datasheet
equipment: [burners, fuel_gas_system, pilot_gas_system, radiant_section, bms_sis, bypass_dampers]
tags: [BS-1211, BS-1212, BS-1213, BS-1214, BS-1215, BS-1216, BS-1217, BS-1218, PIC-1202, PT-1206, PT-1207, PT-1208, FT-1201, AT-1203, PT-1342, TT-1343, FIC-1341, AIC-1321, AT-1322, AT-1325, PT-1312, ZT-1362]
title: Equipment Datasheet — B-101A–H Process Burners
revision: 1.7
date: 2026-11-20
---

# Equipment Datasheet — B-101A–H Process Burners

**Document No.:** H101-DS-004
**Revision:** 1.7 | **Date:** 2026-11-20
**Applicability:** Unit 100 — H-101 Crude Charge Heater
**Owner:** Combustion / Heater Specialist Engineer
**P&ID Reference:** U100-PID-102 (combustion, fuel gas, burners, BMS), U100-PID-103 (air preheater, FD/ID fans, ducts, dampers, stack)
**Revision note:** Rev 1.7 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).

---

## 1. Description

H-101 is fired by eight identical **forced-draft**, staged-fuel, low-NOx gas burners, B-101A
through B-101H, mounted upward-firing in a single row on the firebox floor centreline between the
two radiant tube walls. All burners take hot combustion air (≈ 300 °C, TT-1343) from a **common
windbox** beneath the floor, supplied by FD fan K-101 through the air preheater E-102. Windbox
pressure PT-1342 is normally ≈ +60 mmH₂O. Total air is set by the combustion-air flow controller
FIC-1341 (FD fan speed), trimmed by the arch O2 controller AIC-1321. Individual burner air registers
are set at tuning and locked; they are not used for routine O2 control. Each burner has a continuous
pilot and a UV flame scanner (BS-1211..1218). The windbox carries the emergency air doors D-102
(XV-1362, ZT-1362) for natural-draft fallback (Section 7).

## 2. Burner Data

| Parameter | Value |
|-----------|-------|
| Burner tags | B-101A, B, C, D, E, F, G, H |
| Type | Forced-draft, staged-fuel, low-NOx, round flame, upfired, preheated-air rated |
| Heat release, normal | ≈ 4.8 MW LHV per burner (38.5 MW total) |
| Heat release, design (120%) | ≈ 5.8 MW LHV per burner (≈ 46 MW total) |
| Heat release, minimum stable | ≈ 1.6 MW LHV per burner (≈ 3:1 turndown) |
| Fuel gas pressure at normal release | 1.2 barg at burner manifold (PIC-1202) |
| Fuel gas pressure at design release | ≈ 1.75 barg (heat release ∝ √pressure, approx.) |
| Fuel tips | 1 primary (centre) + 6 staged tips per burner, drilled 310SS |
| Combustion air temperature | ≈ 300 °C design; rated for 25–340 °C (cold air on natural draft) |
| Air-side pressure drop at normal release | ≈ 70 mmH₂O (windbox +60 to floor −10 mmH₂O) |
| Design excess air | 15% (3.0% O2 dry at arch) |
| Minimum stable excess O2 (vendor) | ≈ 1.5% dry at burner level; CO rises sharply below this |
| Flame length at normal release | ≈ 4.0 m (≈ 45% of 9.0 m floor-to-arch height) |
| Burner-to-tube clearance / spacing | ≈ 3.2 m centreline to tube / ≈ 2.3 m burner to burner |
| Guaranteed NOx | ≤ 80 mg/Nm³ @ 3% O2 dry at normal release with 300 °C air (permit limit 150) |
| Guaranteed CO | ≤ 50 ppm at ≥ 2.0% O2 dry |
| Burner tile | 60% alumina castable, pre-fired |

Preheated air raises adiabatic flame temperature by roughly 200 °C, which raises thermal NOx; the
fuel staging is what holds the guarantee. NOx AT-1325 is therefore more sensitive to burner tip
condition and to O2 than it was with ambient air.

## 3. Pilots and Flame Supervision

| Parameter | Value |
|-----------|-------|
| Pilot type | Continuous, self-inspirating gas pilot, high-energy spark ignited |
| Pilot gas pressure | 0.7 barg (PT-1208; Lo alarm 0.4, LL trip 0.25 barg) |
| Pilot heat release | ≈ 40 kW each; ≈ 25 kg/h pilot gas total for 8 pilots |
| Flame scanners | BS-1211 (B-101A) … BS-1218 (B-101H), UV self-checking |
| Single flame loss | BMS closes that burner's fuel only; heater stays on line |
| Flame loss on ≥ 3 of 8 burners | Main fuel trip (XV-1201/1202 close, XV-1203 opens) |

Pilots stay lit through a main fuel trip unless the pilot gas pressure itself trips (PT-1208 LL) or
the manual ESD HS-1290 is operated, which close XV-1209 as well. Pilots are self-inspirating and stay
stable in natural-draft operation. Full logic: BMS / SIS Cause and Effect — H-101, Rev 3.3.

## 4. Fuel-Pressure Operating Range

Burner heat release follows the fuel gas manifold pressure, controlled by PIC-1202 (slave of the COT
cascade). The range is bounded by flame stability at the low end and lift-off at the high end.

| Point | Pressure, barg | Approx. heat release | Type |
|-------|----------------|----------------------|------|
| PT-1206 LL trip | 0.25 | ≈ 46% of normal | SIS trip (flame stability) |
| PIC-1202 Lo alarm | 0.35 | ≈ 54% | Operator alarm |
| Natural-draft runback clamp | ≈ 0.43 | ≈ 60% | BMS firing clamp (fan or APH-rotor stop) |
| Normal | 1.2 | 100% (≈ 4.8 MW per burner) | — |
| PIC-1202 Hi alarm | 2.2 | ≈ 135% | Operator alarm |
| PT-1207 HH trip | 2.5 | ≈ 144% | SIS trip (lift-off / burner capacity) |

Heat release at a given pressure also depends on fuel composition (Wobbe index). AT-1203 (fuel LHV,
normal 48.5 MJ/kg, alarms 44 / 52) should be checked whenever the pressure–firing relation shifts.

## 5. Combustion Performance and the O2 Trade-off

| Burner-level O2 (dry; equals arch O2 only in a sealed heater) | Excess air (approx.) | Expected CO | Fuel vs 3.0% |
|---------------|----------------------|-------------|---------|
| 4.0% | ≈ 21% | < 30 ppm | ≈ +0.35%, plus ≈ 15% more fan power |
| 3.0% | ≈ 15% | ≈ 30 ppm | Design |
| 2.0% | ≈ 9.5% | 30–80 ppm | ≈ −0.35%; requires tight, sealed heater |
| ≤ 1.5% | ≤ 7% | ≈ 100–200 ppm at 1.5%, then rising steeply (> 1,000 ppm below ≈ 1.2%) | Below burner minimum — AT-1322 Hi 200, HH 1000 ppm |

With the APH the flue gas leaves at ≈ 150 °C, so each percentage point of O2 removed saves only
≈ 0.3–0.4% of fuel (about half the Rev A value at a 320 °C stack); lower air flow also reduces FD and
ID fan power. Below the burner minimum O2, flame mixing becomes incomplete and CO rises sharply —
the "CO knee". These values refer to **burner-level** O2: air leaking into the firebox below the arch
makes AIC-1321 read higher than the O2 available at the burners, so CO can rise while AIC-1321 looks
acceptable. See Control Philosophy — Excess O2 and Arch Draft Control, Rev 2.5.

## 6. Flame Pattern and Tube Heat Flux

A correct flame is compact, blue-yellow with a defined envelope, vertical, and does not touch the
tubes. With hot air, flames are slightly shorter and more intense than on cold air.

| Observation | Likely cause | Effect on coil |
|-------------|--------------|----------------|
| Long, lazy, yellow flames | Low air (low O2), plugged staged tips, low windbox pressure PT-1342 | Higher flux at upper tubes, CO |
| Flames leaning toward one wall | Damaged tile, blocked air register, plugged tip, uneven windbox distribution | Local hot spots, high TMT on one side |
| Flame impingement on tubes | Tip orientation wrong, overfiring | Local coke and TMT rise |
| Pulsing / unstable flame | Low fuel pressure, very high air, wet fuel gas, draft swings | Flame-scanner (BS-1211..1218) losses |

Uneven firing changes the flux to individual tubes and can make one wall hotter. Check flames every
round per SOP — H-101 Daily Operator Rounds and Firebox Inspection, Rev 2.1. Cleaning and tuning:
Maintenance Procedure — Burner Inspection, Cleaning and Tuning, Rev 2.0.

## 7. Natural-Draft Capability

On an FD fan, ID fan or APH-rotor stop the emergency air doors D-102 open (ZT-1362) and the burners
draw **ambient** air through the windbox using only firebox draft (floor PT-1312 ≈ −10 to −12 mmH₂O).
Burner air flow scales roughly with √(ρ_air × ΔP): cold air is ≈ 1.9 times denser than 300 °C air,
but the available ΔP is only ≈ 1/6 of the forced-draft value, so air capacity is ≈ 55–60% of design.
This is the basis of the ≤ 60% firing clamp. On natural draft the burners run cold-air flames
(longer, lower NOx), O2 is set only by firing rate and register positions, and operators must watch
AT-1322 CO closely. See SOP — FD / ID Fan Trip Response and Natural-Draft Operation, Rev 1.0.
