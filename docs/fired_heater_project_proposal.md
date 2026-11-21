# Closing the Sim-to-Plant Gap: Fired Heater Calibration, Optimization & Explanation

**Project proposal — crude charge heater digital twin**

---

## 1. Summary

Process simulations describe a plant *as designed*: clean tubes, no air leaks, perfect instruments.
Real plants degrade, so an uncalibrated model drifts away from reality, and **optimizing on that model
produces recommendations that fail on the real plant.**

This project builds an end-to-end workflow on a **refinery crude charge heater** (fired heater) that:

1. **Estimates** the heater's current degraded condition from plant data — tube coking, convection
   fouling, tramp-air ingress, air-preheater seal leakage and fouling, O2 analyzer bias — with honest
   uncertainty.
2. **Recommends** the best operating settings and maintenance timing — excess-O2 setpoint and decoke
   date — using a calibrated physics-based model, within all safety and equipment limits.
3. **Explains** every recommendation: which degradation drives it, which limit is binding, what it is
   worth, how confident we are, and when maintenance beats an operating change.

The headline result the project is designed to demonstrate:

> The same optimizer, run on the as-new model vs. the calibrated model, gives different
> recommendations. Applied to the plant, the as-new recommendation violates limits; the calibrated
> one stays feasible and costs less.

---

## 2. Problem Statement

> **Given** plant data, **estimate** the heater's current degraded condition, **recommend** the
> optimal operating settings and maintenance timing within all limits using a physics-based model,
> and **explain** each recommendation by the specific condition and binding limit driving it —
> including when maintenance (decoking) is worth more than an operating change.

### Core idea: separate what you decide from what degrades

| Kind | Meaning | Examples |
|---|---|---|
| **Type A — decisions** | Knobs the operator/optimizer sets | Excess-O2 setpoint, decoke date; *stretch:* arch draft setpoint (ID fan) |
| **Given conditions** | Set by production or weather | Crude flow, inlet temperature, coil outlet temperature (COT) target, crude blend + assay, fuel-gas composition, ambient |
| **Type B — degradation** | Equipment condition, not directly measured | Coke layer in tubes, coking rate per crude, convection soot, tramp-air leak area, O2 analyzer bias, as-built mismatch |

**Closing the gap means calibrating Type B, not pinning Type A.** The calibrated model reproduces how
the *degraded* plant responds, while the decision variables stay free for optimization. Optimizing
on an uncalibrated model finds the optimum of a plant that doesn't exist.

**Calibration must be physics-based, not black-box.** A model curve-fitted to historical data only
knows the narrow operating band the plant has run in, and the optimum usually lies outside it.
Physically meaningful parameters (coke resistance, leak area, sensor bias) let the model extrapolate
correctly to settings the plant has never run.

---

## 3. Why a Crude Charge Heater

- **High value:** fired heaters are among the largest energy consumers in refineries and petrochemical
  plants; small efficiency and run-length gains are worth a lot.
- **Realistic degradations:** tube coking, convection-section fouling, tramp-air ingress through
  peepholes and seals, air-preheater seal leakage and cold-end fouling, O2 analyzer drift, tube
  creep-life consumption.
- **A genuine trade-off:** low excess air saves fuel but risks CO; coke forces higher tube-metal
  temperatures until a decoke is required. *Operate harder now, or decoke sooner?*
- **Operation affects degradation:** hotter tube walls coke faster and higher velocity coke slower, so
  today's decisions change tomorrow's condition.

---

## 4. Data

No real heater data is available, so both datasets are synthesized, with one strict rule.

### 4.1 Two datasets

| Dataset | What it is | Role |
|---|---|---|
| **Simulation dataset** | The physics model run with *as-new* Type B (clean, no leaks, perfect sensors) | What engineering software "thinks" the heater does |
| **Plant dataset** | A separate, richer "truth" simulator with hidden realistic degradation, events and sensor noise. About 18 months hourly, covering 1–2 decoke cycles | Stands in for the plant historian |

Also generated: a **maintenance/event log** (decokes, soot-blows, crude switches) that calibration
may use, and a **hidden truth table** (true Type B over time). Calibration never reads the truth table;
it is the answer key used only for grading.

### 4.2 The rule: the plant simulator must differ structurally from the model

If both came from the same equations, calibration would look perfect and prove nothing. The plant
simulator adds real-world effects the model does not have:

| Real-world effect | Plant simulator | Model |
|---|---|---|
| Flow maldistribution | 4 passes; one runs hotter and cokes faster | 1 lumped pass |
| Crude-dependent coking | True coking rate per crude differs from the assay-based prior, plus noise | Learns it via calibration |
| Imperfect decoking | Each decoke removes ~95% of the coke, so the heater slowly ages | Must discover it |
| Sensor drift | O2 analyzer bias drifts over months | Estimates bias per window |
| Sudden events | Tramp air steps up (e.g. damaged peephole) | Must detect the change |
| Air preheater wear | Regenerative APH seal leakage grows over months; cold-end fouling raises gas-side ΔP | Must estimate leakage and fouling from the O2 chain, fan load and APH temperatures |
| Instrument faults | Some skin thermocouples read low (detachment) | Reads at face value unless flagged |
| Noise | Gaussian + time-correlated (AR(1)) noise | None |

### 4.3 Crude assays (real, public)

Crude switches are planned and logged in real refineries, so the **crude blend and its assay are known
inputs**. What the assay does *not* give is the actual coking rate in the heater, so that is learned by
calibration, with the assay (micro carbon residue, asphaltenes) used only as a prior.

- Source: publicly published **ExxonMobil Crude Summary Reports**, which give density/API, viscosity at
  several temperatures, TBP distillation in 10 °C steps, UOP K, molecular weight, micro carbon residue
  (MCR) and C7 asphaltenes.
- Selected crudes:

| Role | Crude (assay ref, date) | API | Sulfur (wt%) | MCR (wt%) | C7 asphaltenes (wt%) | Vol % distilled at 360 °C (TBP) |
|---|---|---|---|---|---|---|
| Light | WTI Light, Texas (WTLEX26Y, 2026-02-27) | 47.4 | 0.07 | 0.1 | 0.0 | 78.6 |
| Medium (design crude) | Alaska North Slope (ANS25Y, 2025-11-21) | 32.3 | 1.04 | 4.7 | 1.9 | 60.0 |
| Heavy | Kearl, Alberta (KEARL23B, 2023-10-26) | 19.8 | 3.83 | 9.7 | 5.7 | 37.4 |

- The spread in MCR and asphaltenes gives a clear low → high coking-tendency range; the spread in
  distillation gives very different outlet vaporization at the same COT.
- Only the extracted key properties are stored, with source and assay date; raw files are not
  redistributed.

---

## 5. Design Basis (assumed, for review)

No real heater datasheet is available, so the model is built on a **typical mid-sized refinery crude
charge heater**. These values define the *as-new* design that the plant simulator degrades from. All
are assumptions; reviewer corrections are welcome. The last column is for the reviewer.

### 5.1 Process side

| Item | Proposed value | Basis / rationale | Reviewer: OK / change |
|---|---|---|---|
| Design crude | Alaska North Slope (medium, API 32.3) | Mid-range crude; light and heavy crudes run as off-design cases | |
| Throughput | 50,000 bbl/day (≈ 7,950 m³/d, ≈ 286 t/h for ANS) | Typical single-heater capacity for a mid-sized crude unit | |
| Coil inlet temperature | 250 °C | Downstream of a typical crude preheat train | |
| Coil outlet temperature (COT) | 360 °C | Typical atmospheric-column feed temperature (≈ 350–370 °C) | |
| Coil outlet pressure | ≈ 2.5 barg | Flash-zone pressure of the atmospheric column plus transfer-line loss | |
| Outlet vaporization | Computed from TBP (simple flash approximation) | Varies strongly by crude (see 4.3) | |
| Absorbed duty | ≈ 35 MW (computed by the model) | Sensible heat + latent heat of vaporization for ANS at design rate | |
| Radiant / convection split | ≈ 74% / 26% of absorbed duty (≈ 26 / 9 MW) | Hot combustion air raises firebox temperature, shifting duty to the radiant section | |

### 5.2 Coil and tubes

| Item | Proposed value | Basis / rationale | Reviewer: OK / change |
|---|---|---|---|
| Number of passes | 4 | Common for this capacity; enables maldistribution effects | |
| Radiant tubes | 6-inch Sch 40 (OD 168.3 mm, wall 7.1 mm), horizontal | Common crude-heater tube size | |
| Tube material | 9Cr-1Mo (ASTM A335 P9) | Typical for crude service with sulfur and naphthenic acid | |
| Average radiant heat flux | ≈ 34 kW/m² (outside tube area) | Typical crude-heater design range ≈ 30–38 kW/m² | |
| Radiant tube area | ≈ 766 m² (80 tubes, 20 per pass, 18.3 m effective) | Follows from duty and flux | |
| Convection section | Studded/finned tubes, process service | Recovers flue-gas heat before the stack | |
| Mass velocity in coil | Computed (target in typical crude-heater range) | Sets tube-side h_i, ΔP and coking rate | |
| Max tube metal temperature (TMT) limit | ≈ 600 °C | Conservative operating limit for P9; drives end-of-run | |
| Clean-coil pressure drop | Computed; pump/hydraulic limit set ≈ 40% above clean | Sets the ΔP constraint as coke narrows the bore | |

### 5.3 Combustion and firebox

| Item | Proposed value | Basis / rationale | Reviewer: OK / change |
|---|---|---|---|
| Draft type | **Balanced draft**: FD fan + ID fan, both with VFDs; natural-draft fallback via a flue-gas bypass damper and emergency air doors (≈ 60% firing) | Required with an air preheater; ID fan holds arch draft, FD fan sets combustion air (O₂) | |
| Arch draft | ≈ −2.5 mm H₂O | Keep negative pressure everywhere at the arch | |
| Fuel | Refinery fuel gas ≈ 80% CH₄, 8% C₂H₆, 2% C₃H₈, 8% H₂, 2% N₂ (mol) | Typical refinery fuel-gas mix; composition varies in the plant simulator | |
| Design excess O₂ (arch, dry) | ≈ 3% (operating range ≈ 2–4%) | Typical for forced-draft gas firing | |
| Bridgewall temperature | Operating envelope 760–900 °C | Fired-heater operating practice | |
| Burner capacity | 120% of normal heat release | Standard burner design margin | |
| Air preheater | **Regenerative (Ljungström)**: air ≈ 30 → 300 °C, flue 390 → 160 °C, duty ≈ 4.3 MW; seal leakage ≈ 6% of air when new | Common on large crude heaters; adds realistic degradations (seal leakage, cold-end fouling) | |
| APH cold-end limit | Flue gas leaving APH ≥ 140 °C; cold-air bypass damper protects it | Margin above the acid dew point of refinery fuel gas | |
| Fans | FD ≈ 30 kW, ID ≈ 40 kW absorbed (75 / 90 kW motors); capacity limit 95% speed | Fan power enters the cost; ID capacity can limit firing as the APH fouls or leaks | |
| Design efficiency | ≈ 91% (LHV), computed (fired ≈ 38.5 MW, fuel ≈ 2,860 kg/h) | Stack ≈ 150–155 °C after the air preheater. *(Rev A without an APH gave ≈ 84% / ≈ 320 °C; an earlier 88% figure was not achievable without an APH.)* | |
| Wall / casing heat loss | 1.5–3% of fired duty | Fired-heater practice | |
| Ambient temperature | 25 °C (varies daily in the plant simulator) | Reference condition | |

### 5.4 Maintenance and economics

| Item | Proposed value | Basis / rationale | Reviewer: OK / change |
|---|---|---|---|
| Decoking method | Mechanical pigging | Preferred modern method; faster, no thermal shock | |
| Decoke downtime | ≈ 4 days | Includes cool-down, pigging and restart | |
| Decoke recovery | ≈ 95% of coke removed per decoke (plant simulator only) | Models gradual ageing between decokes | |
| Fuel price, decoke cost, value of lost throughput | Typical values, each with a sensitivity band | Results reported across the band, not at one guess | |

### 5.5 Questions for the reviewing chemical engineer

1. Is 50,000 bbl/day with 4 passes and ~34 kW/m² a realistic combination, or would you change the
   pass count or flux?
2. Is ~600 °C a sensible end-of-run TMT limit for 9Cr-1Mo in this service?
3. Is ~2.5 barg COT pressure and the simple TBP-based vaporization adequate, or should outlet
   vaporization be estimated differently (e.g. an EFV curve)?
4. Is a regenerative APH with ≈ 6% seal leakage when new, and a 140 °C cold-end limit, a sensible basis for
   refinery fuel gas? Would you expect a recuperative APH instead at this size?
5. Any typical values you would use for clean-coil ΔP, coking-rate constants, or decoke cost?

---

## 6. Physics Model (the "simulation" side)

The model follows the heat from fuel to stack using standard, well-known correlations. It is kept
deliberately simple: fast enough to calibrate and optimize thousands of times, and easy to explain.

```
FD fan → air preheater (air side) → hot air → burners → radiant box → tubes (crude heats & partially vaporizes)
                                                            ↓
            stack ← ID fan ← air preheater (gas side) ← convection section
```

| Component | What it computes |
|---|---|
| **Crude properties** | From each assay: liquid heat capacity and enthalpy (API / UOP K correlations), viscosity vs temperature (ASTM D341 fit), **vaporized fraction vs temperature** (from TBP), so enthalpy includes latent heat; simple two-phase pressure-drop multiplier |
| **Fuel & combustion** | Refinery fuel gas (CH4/C2H6/H2/N2) → heating value, stoichiometric air, flue-gas composition; O2 ↔ excess air. **Tramp air enters after the burners**, so the analyzer sees it and the burners don't, and true burner O2 is lower than measured. CO rises sharply at low burner O2. |
| **Radiant section** | Well-stirred firebox (Lobo–Evans style): energy balance + radiant exchange → bridgewall temperature, radiant duty |
| **Tubes & coke** | Tube-side heat transfer + coke layer resistance → **tube metal temperature (TMT)**. Coke also narrows the bore, so **coil pressure drop rises**: a second, independent coke signal |
| **Draft, fans & leaks** | ID fan holds arch draft; FD fan delivers combustion air; fan curves → speed and power. **Tramp air ∝ leak area × √draft** where the casing is below atmospheric pressure |
| **Air preheater** | Regenerative exchanger (ε-NTU) with **seal leakage** (air bypassing to the gas side) and **fouling** → hot-air temperature, flue gas outlet temperature, gas-side ΔP, extra ID fan load; cold-end temperature vs acid dew point |
| **Convection section** | ε-NTU exchanger with soot fouling → convection outlet (APH inlet) temperature |
| **Efficiency & cost** | Stack loss + wall losses (1.5–3%) → efficiency → fuel required to reach the COT target; plus fan electrical power → cost per hour |
| **Coking rate** | **Ebert–Panchal threshold fouling model**: rate rises with film temperature and falls with velocity |
| **Creep life** *(stretch)* | Larson–Miller life fraction consumed from TMT history |

**Inputs:** design data (fixed), given conditions, Type A decisions, Type B values.
**Fuel flow is an output**: the model computes the fuel needed to hit the COT target. In the plant,
fuel flow is measured, and the mismatch is one of calibration's key clues.

**Outputs:** every measured tag (fuel flow, combustion air flow, bridgewall, convection outlet, hot-air
and APH outlet temperatures, arch / APH-inlet / stack O2, APH ΔP, fan speeds and power, pass skin
TMTs, coil ΔP per pass, draft) plus the hidden quantities: true burner O2, CO,
efficiency, true hottest-tube temperature, remaining run length.

Every assumed constant (fuel composition, TMT limit, coking constants, prices) lives in one
assumptions file with its source or an explicit `ASSUMED` tag.

---

## 7. Calibration — Estimating Hidden Degradation

**Method:** rolling weekly windows. In each window, Type B parameters are adjusted by weighted
nonlinear least squares until the model reproduces the plant data. Coke is carried forward as a
running state and reset at logged decokes, producing a week-by-week history of the heater's condition.

**Each degradation leaves its own fingerprint:**

| Degradation | Fingerprint in the data |
|---|---|
| Tube coke | TMT ↑ **and** coil ΔP ↑ together |
| Convection soot | Convection outlet (APH inlet) temperature ↑, tubes normal |
| Tramp air below the arch | Fuel per duty ↑, CO can appear at a normal arch O2 reading |
| Convection-section ingress | APH-inlet O2 rises above arch O2 |
| APH seal leakage | Stack O2 rises above APH-inlet O2; ID fan speed/power ↑; APH flue outlet cooler (dilution) |
| APH fouling | APH gas-side ΔP ↑, hot-air temperature ↓, APH flue outlet ↑, ID fan load ↑ |
| O2 analyzer bias | O2 reading shifted; everything else consistent with a different true O2 |

**Honest uncertainty:**
- Every estimate carries a confidence interval. Because plant noise is time-correlated, intervals
  are corrected for effective sample size and cross-checked with a block bootstrap.
- **Identifiability check:** at a constant O2 setpoint, tramp air and analyzer bias produce nearly the
  same fingerprint. The workflow detects this (parameter correlation, condition number) and reports it
  instead of guessing.
- **Resolution:** a small O2 step test (±0.5% for ~2 h each) separates the two. The demo shows the
  before/after, so the system says **what extra data to collect** when it is unsure.

**Grading (possible because the plant is synthetic):**
- Estimated vs true Type B over 18 months, with intervals: the truth should lie inside them.
- Prediction error on held-out weeks: the as-new model's error grows over time; the calibrated model's
  stays small.

---

## 8. Optimization — O2 Setpoint and Decoke Timing

1. **Forecast:** project coke growth with the calibrated coking rate for the current crude → predicted
   date the hottest tube reaches its TMT limit (or ΔP reaches the pump limit) → **remaining run length**.
2. **Objective:** fuel cost + fan power cost + amortized decoke cost (lost production during downtime + pigging/crew),
   with a sensitivity band on decoke cost.
3. **Constraints:**

| Limit | Reason |
|---|---|
| Hottest-tube TMT ≤ design limit | Tube integrity / rupture risk |
| Coil ΔP ≤ pump limit | Hydraulic capacity |
| CO ≤ limit | Emissions, incomplete combustion |
| True burner O2 ≥ minimum | Flame stability |
| Bridgewall temperature 760–900 °C | Operating envelope |
| Firing ≤ 120% of normal heat release | Burner design margin |
| Draft negative everywhere | Safety: no hot-gas leakage |
| APH flue outlet ≥ 140 °C | Acid dew point corrosion at the APH cold end |
| ID / FD fan speed ≤ 95% | Fan capacity (tightens as the APH fouls or leaks) |

4. **Search:** grid search over O2 setpoint × decoke date. With two decisions it is fast,
   deterministic, and directly produces the trade-off curves.
5. **Binding limits & shadow prices:** report which limit stops further improvement and what relaxing
   it would be worth.
6. **Key comparison:** optimize on the **as-new** and on the **calibrated** model, then apply both
   recommendations to the plant simulator:
   - As-new: O2 too low (unaware of tramp air) and decoke too late (unaware of coke), so CO and TMT
     limits are breached.
   - Calibrated: feasible, lower total cost.
7. **Maintenance vs operations:** "decoke on date X" vs "raise O2 / reduce firing to manage TMT",
   compared in the same $/day unit.
8. **Stretch:** arch draft setpoint (ID fan) as a third decision. Less draft reduces tramp air and fuel
   use and saves ID fan power, bounded by the negative-draft limit and the firebox high-pressure trip.

---

## 9. Explanation Layer

Recommendations are only useful if engineers trust them. Each run is logged as a step-by-step
**investigation audit trail**, reusing the audit system from my existing plant-troubleshooting
assistant:

1. Calibration results (Type B ± intervals, identifiability flags)
2. Observations (e.g. fuel use vs as-new prediction)
3. Rejection of the as-new recommendation, with the limit it would violate
4. **Cause-vs-symptom check**: rising fuel and TMT are symptoms; the cause is identified from the
   fingerprints above
5. Conclusion with confidence derived from intervals and identifiability, not judgment
6. Corrective actions, each stating the driving **condition**, the **binding limit**, the **$/day
   value**, and a **document citation** (title + revision)

A small set of heater documents (datasheet, operating limits, decoking procedure, O2 control
philosophy) is written for the demo so recommendations can cite procedures; this is stated openly.

The audit trail renders into a full **engineering report** (every step, for SME review) and a
**summary** (root cause, confidence, causal chain, actions). Conclusions that skip the cause-vs-symptom
check are flagged automatically.

**Live interaction:** the calibrated model is exposed as tools (calibrate / optimize / what-if) that an
AI assistant can call, so questions like *"What if we delay the decoke by three weeks?"* are answered
by running the physics model, not by the language model guessing. AI reasoning sits on top of a
deterministic simulation engine.

---

## 10. Deliverables

1. **GitHub repository**: model, plant simulator, calibration, optimization, explanation, tests, and a
   README (problem, approach, how to run, results, assumptions).
2. **Interactive demo page** (single self-contained page):
   problem → Type A vs B → the two datasets and the growing gap → calibration vs truth → step-test
   identifiability → run-length forecast → as-new vs calibrated on the plant → decoke trade-off curve →
   explanation excerpt → assumptions & limitations. Sliders for O2 setpoint, decoke date and decoke
   cost over precomputed results.
3. **Live walkthrough**: demo page plus live what-if questions answered through the model.

---

## 11. Build Phases

Each phase ends with something demonstrable.

| Phase | Build | Demonstrable output |
|---|---|---|
| 1 | Physics model + unit tests | What-if plots: O2 vs efficiency/CO, coke vs TMT and ΔP |
| 2 | Plant simulator + both datasets | Plot of the gap growing between as-new simulation and plant |
| 3 | Calibration (rolling, intervals, identifiability, step test) | Estimated vs true degradation over time |
| 4 | Optimization (O2 + decoke timing, run-length forecast) | As-new vs calibrated recommendations applied to the plant |
| 5 | Explanation (audit trail, heater docs, report) | Rendered investigation report and summary |
| 6 | Demo page + README | Shareable page and repository |

---

## 12. Validation

- **Physics checks:** combustion element balance closes (<0.1%); O2 ↔ excess-air round-trip; firebox
  and convection energy balances close (<0.5%); efficiency at design in a typical fired-heater range;
  TMT and ΔP rise monotonically with coke; coking rate rises with film temperature and falls with
  velocity.
- **Calibration:** true Type B inside 95% intervals on held-out windows across several random seeds;
  tramp-air/bias confounding flagged without a step test and resolved with one; calibrated prediction
  error far below as-new.
- **Optimization:** as-new recommendation violates at least one limit on the plant simulator;
  calibrated recommendation is feasible and no more expensive.
- **End-to-end:** one command regenerates data, results, the investigation report and the demo page.

---

## 13. Assumptions & Limitations

- **Synthetic data:** results are only as credible as the plant simulator's realism, which is why it
  deliberately differs from the model. A natural next step is validation on real heater data.
- **Assumed constants:** fuel-gas composition, TMT limit, coking-model constants, decoke cost and
  prices are typical values, shown with sensitivity bands.
- **Simplified vaporization:** enthalpy and vapor fraction from assay correlations, not a rigorous
  flash; two-phase ΔP via a simple multiplier.
- **Steady-state:** the model ignores fast dynamics; hourly data is treated as quasi-steady.
- **Downstream not modelled (yet):** heater outlet conditions (COT, vaporization, outlet pressure)
  change the atmospheric column's cut points and product yields. COT is treated as a given target
  here; the downstream coupling is flagged in explanations and is an open item for discussion.
- **Out of scope:** start-up/shutdown, refractory dry-out, burner light-off and flame stability
  transients, refractory/casing and tube-support mechanical integrity.

---

## 14. Open Questions for Discussion

1. Is a crude charge heater the right showcase, or would another unit type be a closer match to the
   intended application?
2. Advisory recommendations (operator decides) vs closed-loop setpoints: which matters more in
   practice?
3. Preferred success metric: calibration accuracy, $/day improvement, or operator trust/explainability?
4. Is there representative (even anonymized) heater data that could replace or validate the
   synthetic plant later?
5. **The heater is not a silo.** Its outlet conditions set flash-zone vaporization and so the
   atmospheric column's cut points, yields and everything downstream. How far should the next phase
   go: a yield/value link on COT and vaporization, a shortcut column model, or coupling to an existing
   column simulation? Should COT then become a decision variable?

---

## Appendix A — Repository Layout (planned)

```
crudes/*.json                  extracted assay properties (+ source, assay date)
heater_model/                  physics model: assumptions, crude, fuel, combustion, radiant, tubes,
                               draft, convection, efficiency, coking, creep, model,
                               calibrate, optimize, explain
heater_plant/                  "truth" plant simulator + degradation scenarios
heater_docs/                   heater datasheet, limits, decoking SOP, O2 control (demo docs)
scripts/run_demo.py            generate | gap | calibrate | optimize | explain | all
scripts/build_demo_page.py     builds demo/index.html from demo/results.json
tests/                         physics, calibration and optimization tests (pytest)
```

Builds on the existing plant-troubleshooting repository: reuses its investigation audit store and
report renderer, and adds optional MCP tools (`heater_calibrate`, `heater_optimize`, `heater_whatif`)
for the live walkthrough.

## Appendix B — Key References

- API Standard 560, *Fired Heaters for General Refinery Service*
- API Standard 530, *Calculation of Heater-tube Thickness in Petroleum Refineries* (creep / Larson–Miller)
- Ebert, W. & Panchal, C.B. (1997), threshold fouling model for crude oil
- Lobo, W.E. & Evans, J.E. (1939), radiant-section heat transfer in fired heaters
- ExxonMobil Crude Summary Reports (public crude assays)
- What Is Piping, *Fired Heaters* (overview of sections, operating limits and troubleshooting)
