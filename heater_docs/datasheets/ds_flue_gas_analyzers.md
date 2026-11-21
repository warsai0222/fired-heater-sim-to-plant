---
doc_id: ds_flue_gas_analyzers
doc_type: datasheet
equipment: [flue_gas_analyzers, radiant_section, convection_section, air_preheater, stack, burners]
tags: [AIC-1321, AT-1322, AT-1327, AT-1326, AT-1325, FIC-1341, SI-1341, SI-1351, FT-1201, AT-1203, TIC-1345]
title: Instrument Datasheet — Flue Gas O2, CO and Stack CEMS Analyzers
revision: 1.6
date: 2026-11-20
---

# Instrument Datasheet — Flue Gas O2, CO and Stack CEMS Analyzers

**Document No.:** H101-DS-007
**Revision:** 1.6 | **Date:** 2026-11-20
**Applicability:** Unit 100 — H-101 Crude Charge Heater
**Owner:** Analyzer / Instrument & Controls Engineer
**P&ID Reference:** U100-PID-102 (combustion, fuel gas, burners, BMS), U100-PID-103 (air preheater, FD/ID fans, ducts, dampers, stack)
**Revision note:** Rev 1.6 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).

---

## 1. Analyzer Overview (AN-101)

| Tag | Measurement | Location | Basis | Normal | Alarms | Use |
|-----|-------------|----------|-------|--------|--------|-----|
| AIC-1321 | Arch excess O2 | Radiant arch, below shield rows | vol% dry | 3.0% | Lo 1.5, LL 1.0 (alarm only), Hi 5.0 | Master of combustion-air flow FIC-1341 (FD fan) |
| AT-1322 | Arch CO | Same probe as AIC-1321 | ppm dry | 30 ppm | Hi 200, HH 1000 | Combustion completeness |
| AT-1327 | O2 at convection outlet / APH gas inlet | Duct between convection outlet and E-102 | vol% dry | ≈ 3.2% | — | Convection-ingress check (vs AIC-1321) |
| AT-1326 | Stack O2 (CEMS) | S-101 platform, after ID fan | vol% dry | ≈ 4.4% | — | Reporting; APH-leakage check (vs AT-1327) |
| AT-1325 | Stack NOx (CEMS) | S-101 platform | mg/Nm³ @ 3% O2 dry | 80 | Hi 150 (permit) | Environmental compliance |

No analyzer on H-101 initiates a trip. Low O2 and high CO are operator alarms requiring immediate
action per Troubleshooting Guide — Low Excess O2 / High CO, Rev 2.5.

## 2. Arch O2 / CO and APH-Inlet O2 Analyzers (AIC-1321, AT-1322, AT-1327)

| Parameter | Value |
|-----------|-------|
| Sampling | Extractive, single-point probe (arch: through side wall; AT-1327: through duct wall) |
| Probe | Inconel 600, 1.2 m insertion (arch) / 1.0 m (duct), sintered ceramic filter, instrument-air blow-back |
| Sample line | Heated, 180 °C, ≈ 15 m (arch) / ≈ 20 m (AT-1327) to the analyzer shelter |
| Conditioning | Peltier chiller, 4 °C outlet dew point (dry basis), coalescing filter |
| O2 principle / range | Paramagnetic / 0–10% vol dry |
| O2 accuracy / repeatability | ±0.1% O2 abs / ±0.05% O2 |
| CO principle / range (AT-1322 only) | NDIR, auto-ranging 0–1,000 / 0–5,000 ppm, ±2% of range |
| Response time T90 | ≤ 45 s including transport lag |
| Validation | Automatic zero/span check weekly; full calibration per maintenance procedure |

AT-1327 uses the same principle, basis and calibration gases as AIC-1321 so that their difference is
meaningful to ≈ ±0.15 percentage point. Dry-basis O2 is higher than wet-basis O2: at the design point
3.0% dry ≈ 2.5% wet (flue gas ≈ 16.6 mol% H2O). Correct portable in-situ zirconia (wet) readings
before comparing them with these analyzers.

## 3. Stack CEMS (AT-1326, AT-1325)

| Parameter | Value |
|-----------|-------|
| Sampling | Extractive, cold-dry, heated probe and line (180 °C), chiller to 4 °C |
| O2 principle | Paramagnetic, 0–25% vol dry |
| NOx principle | Chemiluminescence with NO2 converter, 0–300 mg/Nm³ |
| NOx reporting | mg/Nm³ at 3% O2 dry, normalized using AT-1326 |
| Daily drift check / relative accuracy test | Automatic zero and span / annual, against reference method |

AT-1326 is not used for control. Because it now sits after the APH and ID fan, stack O2 is ≈ 1.4
points above arch O2 at design and is **not** a direct check on the arch reading; use AT-1327 for that.

## 4. The O2 Measurement Chain

| Step | Normal difference | Investigate above | What a rise means |
|------|-------------------|-------------------|-------------------|
| AT-1327 − AIC-1321 | ≈ 0.2 point (as-commissioned convection casing leakage) | ≈ 0.8 | Air ingress into the convection section / header boxes (or arch analyzer reading low) |
| AT-1326 − AT-1327 | ≈ 1.2 point (≈ 6% APH seal leakage, as new) | ≈ 2.0 | APH seal leakage growth, or leaks in the APH-to-ID-fan duct (highest suction) |

Air entering between two analyzers dilutes the flue gas. An approximate leak estimate, as a fraction
of the gas flow at the upstream analyzer, is:

> Leak fraction ≈ 0.9 × (O2,down − O2,up) / (20.9 − O2,down)

At design, (4.4 − 3.2) / (20.9 − 4.4) × 0.9 ≈ 6.5% of APH inlet gas (≈ 6% of FD air), matching the
design APH leakage. The arch reading AIC-1321 includes any tramp air entering **below** the arch, so
the O2 the burners actually see (burner-level or true O2) is lower than AIC-1321 when the firebox
leaks:

> O2,arch ≈ (1 − f) × O2,burner + f × 20.9, f = leak-air fraction of dry flue gas at the arch.

For example, f = 5% with burners at 2.0% gives an arch reading of ≈ 3.0%; controlling AIC-1321 at
3.0% then leaves the burners at 2.0%. Firebox leakage below the arch is not visible in either
difference above; it shows as CO rising at a "normal" AIC-1321 and is confirmed by SOP — Excess O2
Step Test (Analyzer / Air-Ingress Check), Rev 1.3. A **negative** AT-1327 − AIC-1321 is not
physically possible without afterburning, so it points to an analyzer error, or to afterburning if
AT-1322 CO is also high.

## 5. Recognising Analyzer Error vs a Real O2 Change

| Check | Real O2 change at the burners | Analyzer / sample-system error on AIC-1321 |
|-------|-------------------------------|-------------------------------------------|
| AT-1327 and AT-1326 | Move with AIC-1321; both differences stay at baseline | Do not follow; AT-1327 − AIC-1321 shifts (and can go negative) while AT-1326 − AT-1327 is unchanged |
| Arch CO AT-1322 | Rises if O2 truly low | Unchanged despite "low" O2, or high CO despite "normal" O2 |
| Fuel / air balance | Consistent with FT-1201, AT-1203, FIC-1341 (minus APH leakage) | FIC-1341 and firing unchanged but reading shifts |
| Portable analyzer at arch test port | Agrees with AIC-1321 (after dry/wet correction) | Disagrees |
| O2 step test | Response of the expected size and dynamics | Too small, too large or sluggish |

Note the ambiguity in the first row: an arch analyzer reading **low** makes AT-1327 − AIC-1321 grow
exactly as convection air ingress would. Separate them with CO, the fuel/air balance and a portable
analyzer before any casing work. A sample-system air leak (cracked probe, loose fitting under suction)
reads **high**, so the O2 loop cuts FD air (FIC-1341, SI-1341) and runs the burners short of air.
A plugged filter or failing cell gives a slow, damped or drifting signal; a zero/span drift gives an
offset visible only against AT-1327, the fuel/air balance and the portable analyzer. Calibration:
Maintenance Procedure — O2 and CO Analyzer Calibration and Validation, Rev 2.2.

## 6. CO Measurement Notes

CO at the arch is the direct indicator of incomplete combustion. With refinery fuel gas, CO stays low
(≈ 30–80 ppm) from 4% down to about 2% burner-level O2, reaches ≈ 100–200 ppm near the burner minimum
(≈ 1.5%), then rises steeply: a small further O2 reduction can take CO above 1,000 ppm. AT-1322 Hi
(200 ppm) is the optimizer CO limit; HH (1000 ppm) indicates sub-stoichiometric firing and risk of
afterburning in the convection section or of combustible deposits reaching the APH (an APH fire
risk). A rising AT-1322 at a "normal" AIC-1321 is the signature of air leaking in below the arch, or
of an arch analyzer reading high.
