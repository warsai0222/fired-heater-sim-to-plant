---
doc_id: mnt_o2_analyzer_calibration
doc_type: maintenance
equipment: [flue_gas_analyzers, radiant_section, convection_section, air_preheater, fd_fan, stack]
tags: [AIC-1321, AT-1322, AT-1327, AT-1326, AT-1325, FIC-1341, PIC-1311, FT-1201]
title: Maintenance Procedure — O2 and CO Analyzer Calibration and Validation
revision: 2.2
date: 2026-11-20
---

# Maintenance Procedure — O2 and CO Analyzer Calibration and Validation

**Document No.:** H101-MNT-004
**Revision:** 2.2 | **Date:** 2026-11-20
**Revision note:** Rev 2.2 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).
**Applicability:** Unit 100 — H-101 Crude Charge Heater, analyzer package AN-101
**Owner:** Instrument and Analyzer Maintenance
**P&ID Reference:** U100-PID-102 (combustion, fuel gas, burners, BMS), U100-PID-103 (air preheater, ducts, stack)

---

## 1. Scope and Purpose

This procedure covers calibration and validation of the H-101 O2 measurement chain and arch CO:

- **AIC-1321** arch O2 (dry) — the control measurement; it resets the combustion air flow setpoint FIC-1341, which drives the FD fan;
- **AT-1322** arch CO;
- **AT-1327** O2 at the convection outlet / APH gas inlet (dry);
- comparison against the stack CEMS O2 **AT-1326** (after the APH).

An AIC-1321 reading that drifts high makes the heater run short of air (CO and flame-length risk); one that drifts low wastes fuel and fan power. Neither is visible on a steady O2 trend. AT-1327 and AT-1326 are used to separate convection-section ingress and APH seal leakage, so a drift in either is mistaken for a leak unless they are validated too. Instrument details: Instrument Datasheet — Flue Gas O2, CO and Stack CEMS Analyzers, Rev 1.6. Regulatory CEMS calibration (AT-1326, AT-1325) follows Environmental Procedure — Stack Emissions Monitoring (CO, NOx), Rev 1.4.

## 2. Frequency

| Activity | Frequency |
|---|---|
| Automatic or manual zero/span check AIC-1321, AT-1322, AT-1327 | Weekly |
| Full calibration with as-found / as-left record | Monthly |
| O2 chain comparison and portable analyzer check | Monthly, and on request from the console or process engineering |
| Probe, filter and sample line inspection | Quarterly |

## 3. Reference Gases

All cylinders certified ±1% relative, within expiry date, certificate number recorded.

| Gas | Use | Concentration |
|---|---|---|
| Nitrogen (≥ 99.999%) | O2 zero, CO zero | < 5 ppm O2 |
| O2 in N2 | O2 span | 8.0% O2 |
| O2 in N2 | O2 mid-point (near setpoint) | 3.0% O2 |
| CO in N2 | CO span | 800 ppm (range 0–1,000 ppm) |
| CO in N2 | CO mid-point | 200 ppm |

Gases are introduced at the **probe calibration port** (upstream of the filter and sample line), not at the cabinet, so the whole sample system — including possible line leaks — is tested.

## 4. Calibration Procedure (AIC-1321, AT-1322, AT-1327)

1. Inform the console. For AIC-1321: put AIC-1321 in MANUAL so FIC-1341 holds its present air flow setpoint (FIC-1341 stays in AUTO on the FD fan). The heater must be steady; the console watches PIC-1311, AT-1322 and fuel. AT-1327 is indication only and needs no loop change.
2. **As-found zero:** N2 at the probe port; stable reading (≥ 3 minutes). Record O2 (and CO for AT-1322).
3. **As-found span:** 8.0% O2, then 800 ppm CO. Record.
4. **As-found mid-point:** 3.0% O2 and 200 ppm CO. Mid-points catch non-linearity near the operating point.
5. Evaluate per Section 5. If adjustment is needed, adjust zero then span per the vendor manual and repeat zero, span and mid-point to record as-left values.
6. Record **T90** (switch to 90% of final reading). Acceptance ≤ 60 s for O2.
7. Return to process; confirm the reading returns to its pre-check value within 0.2% O2; return AIC-1321 to AUTO (cascade).

## 5. Drift Tolerances and Actions

| Measurement | As-found error | Action |
|---|---|---|
| O2 (any point) | ≤ ±0.1% O2 | No adjustment; record |
| O2 | > ±0.1% and ≤ ±0.3% | Adjust; record as-found and as-left |
| O2 | > ±0.3% | Adjust; raise a notification; inform process engineering — historian data since the last good calibration is suspect (for AT-1327, so is any leakage trend based on it) |
| O2 | > ±0.5%, or zero and span off in the same direction | As above, and inspect the sample system for leaks (air in-leakage reads high) |
| CO | ≤ ±10 ppm or ±5% of reading, whichever larger | No adjustment |
| CO | Larger | Adjust; record |
| T90 | > 60 s | Clean or replace filter / probe |

## 6. Validation Against Independent Measurements — the O2 Chain

**Portable analyzer.** With the heater steady, insert a calibrated portable O2/CO analyzer (dry basis, bump-tested that day) at the arch sample point beside AIC-1321, then at the APH gas-inlet sample point beside AT-1327. Average 5 readings over 5 minutes alongside each analyzer. Acceptance: ±0.3% O2.

**Chain differences.** O2 can only rise along the flue path (air leaks in; nothing removes O2 except afterburning of combustibles). Track:

| Difference | Normal | Investigate | Meaning if high | Meaning if low / negative |
|---|---|---|---|---|
| AT-1327 − AIC-1321 | ≈ 0.2% | > 0.8% | Convection-section air ingress (Per Maintenance Procedure — Tramp Air Survey and Casing Sealing, Rev 1.5) | AIC-1321 reading high or AT-1327 low — or afterburning (check AT-1322) |
| AT-1326 − AT-1327 | ≈ 1.2% | > 2.0% | APH seal leakage, or duct in-leakage after the APH (Per Maintenance Procedure — Air Preheater Seal Inspection, Soot Blowing and Water Washing, Rev 1.0) | Below ≈ 0.8%: AT-1327 reading high or AT-1326 low |

Interpretation rules:
1. A **sudden** change in a difference with no change in heater operation points to an analyzer, not the heater — leaks grow gradually or step with an event (door left open, outage).
2. A difference that changes but the portable confirms both analyzers means a real leak change.
3. A third, independent check on AIC-1321 is the air balance: FIC-1341 compared with the air the heater model expects for the indicated O2 and current fuel (FT-1201). FIC-1341 includes APH leakage, so use it only after the AT-1326 − AT-1327 difference has been checked.

When the gas checks and portable checks pass but O2 is still disputed, run SOP — Excess O2 Step Test (Analyzer / Air-Ingress Check), Rev 1.3.

## 7. Records

Record for each analyzer: date, technician, cylinder certificates, as-found / as-left zero, span and mid-point, T90, portable comparison values, both chain differences, and any adjustments. Copy any as-found O2 error greater than ±0.3% to the shift log and to process engineering with the date of the last good calibration, so historian data in between can be flagged.
