---
doc_id: mnt_soot_blowing
doc_type: maintenance
equipment: [convection_section, soot_blowers, air_preheater, id_fan, stack, flue_gas_analyzers]
tags: [HS-1501, TT-1303, TT-1302, TT-1131, TT-1132, TT-1133, TT-1134, PIC-1311, PT-1313, SI-1351, XS-1349, PDT-1347, PDT-1348, TIC-1345, TT-1343, AIC-1321, AT-1327, AT-1326, FT-1201, AT-1203, TIC-1110]
title: Maintenance Procedure — Convection Section Soot Blowing
revision: 1.9
date: 2026-11-20
---

# Maintenance Procedure — Convection Section Soot Blowing

**Document No.:** H101-MNT-002
**Revision:** 1.9 | **Date:** 2026-11-20
**Revision note:** Rev 1.9 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).
**Applicability:** Unit 100 — H-101 Crude Charge Heater, convection soot blowers SB-101A..F and air preheater soot blowers SB-102A/B
**Owner:** Unit 100 Operations (Console Operator) / Process Engineering
**P&ID Reference:** U100-PID-102 (combustion, fuel gas, burners, BMS), U100-PID-103 (air preheater, fans, ducts)
**Frequency:** Once per day (day shift), plus on demand

---

## 1. Scope and Purpose

The H-101 convection section has 2 bare shield rows and 6 studded rows of process coil. Deposits on the studs (fuel-gas combustion scale, refractory dust and, after upsets, soot) reduce convection heat transfer: crossover temperatures TT-1131..1134 fall, more duty shifts to the radiant section, and the convection outlet / APH gas inlet temperature TT-1303 rises. Downstream, the regenerative air preheater E-102 collects the finer deposits on its heating elements; APH fouling raises the gas-side pressure drop PDT-1347, lowers the hot-air temperature TT-1343, raises the APH gas outlet temperature TIC-1345 and loads the ID fan.

The true stack loss is set by the APH gas outlet: every 20 °C rise in TIC-1345 costs roughly 1% of fired duty. A 20 °C rise in TT-1303 costs only about a third of that, because the APH recovers most of it, but it shifts load onto the APH and raises TIC-1345 and ID fan load.

Sequencer HS-1501 runs six retractable blowers SB-101A..F (convection) and two APH blowers SB-102A/B from the 3.5 barg LP steam header. A daily sequence is normally enough on fuel gas; a falling effect over weeks indicates deposits that need off-line washing (Per Maintenance Procedure — Air Preheater Seal Inspection, Soot Blowing and Water Washing, Rev 1.0, for the APH).

## 2. Preconditions

1. H-101 steady: COT 360 °C on TIC-1110 in CASCADE; no crude switch or step test in progress (Per SOP — Excess O2 Step Test (Analyzer / Air-Ingress Check), Rev 1.3).
2. Balanced draft in service: PIC-1311 in AUTO at −2.5 mmH2O on the ID fan, with **SI-1351 ≤ 90%** (headroom for the steam volume). Never soot blow on natural draft.
3. APH rotor turning (**XS-1349 = 1**) — the SB-102A/B lance must sweep the whole rotating matrix; blowing on a stopped rotor erodes one sector.
4. **TIC-1345 ≥ 145 °C** before SB-102A/B run. Steam on a cold, acid-wetted cold end turns deposits into a hard, plugging paste.
5. LP steam ≥ 3.0 barg at the blower supply; no blower in fault on the HS-1501 panel; all lances retracted.

## 3. Pre-Blow Readings

Record 30-minute averages immediately before starting:

| Tag | Description | Normal (clean) |
|---|---|---|
| TT-1303 | Convection outlet / APH gas inlet | ≈ 390 °C (Hi 440 °C) |
| TT-1302 | Between shield and studded rows | ≈ 740 °C |
| TT-1131..1134 | Pass crossover temperatures | ≈ 292 °C (Hi 310 °C) |
| PT-1313 | Convection outlet draft | ≈ −20 mmH2O |
| PDT-1347 / PDT-1348 | APH gas / air ΔP | 80 / 50 mmH2O (Hi 120 / 75) |
| TT-1343 | APH hot air | ≈ 300 °C |
| TIC-1345 | APH gas outlet | ≈ 150 °C |
| SI-1351 | ID fan speed | ≈ 72% |
| FT-1201 × AT-1203 | Fuel heat input | ≈ 38.5 MW LHV at design |

## 4. Soot-Blowing Sequence

1. **Warm and drain the steam supply** (field): blow down condensate at the header drain until dry steam issues (about 5 minutes). Wet steam erodes studs and APH elements and causes thermal shock.
2. Start HS-1501 in AUTO. It runs **convection first, then the APH**: SB-101A → SB-101F from the bottom (hottest) studded row upward, then SB-102A and SB-102B, so deposits loosened in the convection section and carried downstream are removed from the APH in the same sequence.
3. Each convection lance travels in, rotates and blows in and out (about 5 minutes per blower). The APH blowers traverse across the face of the turning rotor; allow at least one full rotor revolution per traverse (≈ 10 minutes per APH blower). The full sequence takes about 55 minutes.
4. Watch PIC-1311 during each lance: the steam adds volume and the ID fan speeds up to hold draft. If the arch rises above −1.0 mmH2O or SI-1351 reaches 95%, put the sequencer on HOLD.
5. AT-1327 and AT-1326 may read off-normal while steam is in the gas; this is expected. AIC-1321 at the arch is upstream and should not be affected.
6. Field operator confirms each lance retracts fully and each wall-box poppet valve closes.
7. If a lance fails to retract, stop the sequence, keep low steam flow on it to cool it, and retract by hand crank. A lance left in the gas without steam will bend.

## 5. Effectiveness Check — Convection (SB-101A..F)

Record TT-1303 and TT-1131..1134 **30–60 minutes after the sequence ends**, at the same charge and COT.

| Result (TT-1303 drop) | Meaning | Action |
|---|---|---|
| 5–15 °C, crossovers up slightly | Normal clean-up | None; log |
| < 3 °C, TT-1303 near baseline | Convection already clean | None; consider reducing frequency |
| < 3 °C, TT-1303 ≥ 15 °C above post-decoke / post-wash baseline | Deposits not removed, or a blower not reaching its row | Check lance strokes and steam pressure; repeat; if still ineffective, plan off-line convection wash |
| TT-1303 rises after blowing | Possible afterburning or instrument issue | Inform console; Per Troubleshooting Guide — Positive Draft and Afterburning, Rev 1.8 |

## 6. Effectiveness Check — Air Preheater (SB-102A/B)

Record PDT-1347, TT-1343, TIC-1345 and SI-1351 at the same time as Section 5.

| Result | Meaning | Action |
|---|---|---|
| PDT-1347 down a few mmH2O, TT-1343 up, SI-1351 down | Normal APH clean-up | None; log |
| PDT-1347 near clean baseline (≈ 80 mmH2O), no change | APH clean | None |
| PDT-1347 ≥ 15 mmH2O above post-wash baseline and not recovering over several days | Cold-end plugging not removed by steam | Increase blowing to twice daily for 3 days; if no recovery, plan off-line water wash |
| TIC-1345 or TT-1343 rising fast after blowing, or hot spot on APH casing | Possible APH deposit fire | Inform console immediately; keep rotor turning; Per Troubleshooting Guide — Air Preheater Leakage, Fouling and Low Cold-End Temperature, Rev 1.0 |

Read TIC-1345 with care: cleaning the **convection** lowers TT-1303 and so also lowers TIC-1345, while cleaning the **APH** lowers TIC-1345 and raises TT-1343. Judge the APH by PDT-1347 and TT-1343 first. If TIC-1345 is sitting on its 145 °C setpoint with cold-air bypass TV-1345 open, TIC-1345 says nothing about fouling — use PDT-1347 and TT-1343 only.

A rising TT-1303 or TIC-1345 that soot blowing does not recover should also be checked against tramp air, APH leakage and excess O2 before blaming fouling (Per Troubleshooting Guide — High Stack Temperature, Rev 1.7).

## 7. Logging

1. HS-1501 writes a soot-blow event (start, end, each blower) to the DCS event log; confirm it appears.
2. The console operator records start/end, any faults or holds, pre- and post-blow TT-1303, PDT-1347, TT-1343 and TIC-1345, and the changes.
3. Process engineering uses the events to separate the daily sawtooth in TT-1303 and PDT-1347 from long-term convection and APH fouling trends; missing events make those trends unreliable.
