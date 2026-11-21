# H-101 Crude Charge Heater — Design Reference (preliminary, Rev B)

Single source for the PFD, P&IDs, RAG documents and (later) the physics model. Every number is
**ASSUMED / preliminary hand calculation** pending chemical-engineer review (proposal Section 5).
The physics model will recompute duty, temperatures and pressure drop; where it disagrees, the model
wins and this file is updated.

**Rev B (2026-11-20):** design changed from natural draft / no air preheater to **balanced draft
(FD fan K-101 + ID fan K-102) with a regenerative (Ljungström) air preheater E-102**.

Companion files: [equipment_list.csv](equipment_list.csv), [tag_register.csv](tag_register.csv)
(all instrument tags, normal values, alarm/trip setpoints).

---

## 1. Hand heat and material balance (design case: ANS, 50,000 bbl/d, clean, as-new)

**Fuel gas** (mol): 80% CH4, 8% C2H6, 2% C3H8, 8% H2, 2% N2 → MW 16.84, LHV 816 kJ/mol = **48.5 MJ/kg**.
Stoichiometric air 9.62 mol/mol fuel. 3.0% O2 (dry) at the arch → **15% excess air** at the burners.

| Quantity | Value | How |
|---|---|---|
| Absorbed duty | 35.0 MW | Sensible (79.5 kg/s × ~2.75 kJ/kg·K × 110 K ≈ 24 MW) + latent (~40–55 wt% vaporized) |
| Radiant / convection | ≈ 26 / 9 MW (≈ 74 / 26%) | Hot combustion air raises firebox temperature, so a larger share is absorbed in the radiant section |
| Air preheater duty | ≈ 4.3 MW | Flue 390 → 160 °C; returned to the firebox as hot air |
| Efficiency (LHV) | **≈ 91%** | Stack loss ≈ 6% at 160 °C (APH gas outlet, before leak-air dilution) + wall/duct loss ≈ 2.5% |
| Fired duty | 38.5 MW LHV | 35.0 / 0.91 |
| Fuel gas | 2,860 kg/h (≈ 3,800 Nm³/h) | 38.5 MW / 48.5 MJ/kg |
| Air delivered by FD fan | 57,850 kg/h | Burner air + APH leakage |
| APH air-to-gas leakage | ≈ 6% of FD air (≈ 3,470 kg/h), as new | Typical rotary regenerative seal leakage; grows as seals wear (Type B) |
| Combustion air to burners | 54,370 kg/h at ≈ 300 °C | 15% excess air |
| Flue gas, firebox → APH | 57,230 kg/h; wet mol%: CO2 8.4, H2O 16.6, O2 2.5, N2 72.5 | Combustion balance |
| Flue gas after APH (incl. leak air) | 60,700 kg/h at ≈ 150 °C (mixed) | Leak air dilutes and cools the flue gas |
| Bridgewall temperature | ≈ 845 °C | Firebox energy balance with hot air |
| Convection outlet / APH gas inlet | ≈ 390 °C | ~140 °C approach to crude inlet |
| Crossover temperature | ≈ 292 °C | Convection duty on crude |
| Radiant area | ≈ 766 m² (80 tubes, 20 per pass, 18.3 m) | Geometry unchanged from Rev A |
| Average radiant flux | ≈ 34 kW/m² | 26 MW / 766 m² (typical range 30–38) |
| Coil velocity (liquid, inlet) | ≈ 1.6 m/s; mass flux ≈ 1,065 kg/m²·s per pass | ID 154.1 mm, ρ ≈ 680 kg/m³ at 300 °C |
| Coil ΔP (clean, per pass) | ≈ 6.0 bar (8.5 → 2.5 barg) | Dominated by the two-phase section near the outlet |
| Hottest-tube TMT (clean, SOR) | ≈ 430 °C | Peak flux ≈ 1.8 × average |
| FD fan absorbed power | ≈ 30 kW (75 kW motor) | ≈ 13.6 m³/s × ≈ 1.5 kPa / 0.75. Rise ≈ 155 mmH₂O: inlet filter/silencer −25, APH air side 50, ducts 20, windbox +60 |
| ID fan absorbed power | ≈ 40 kW (90 kW motor) | ≈ 20.2 m³/s × ≈ 1.3 kPa / 0.72. Rise ≈ 135 mmH₂O: APH inlet −20, APH gas ΔP 80, ducts/inlet box 20 → inlet −120; discharge +15 |
| Fans at 120% firing | FD ≈ 52 kW, ID ≈ 69 kW | Fan laws (power ∝ flow³); within motor ratings, speeds ≈ 84–86% (< 95% limit) |

> **Rev A → Rev B:** Rev A (natural draft, no APH) gave ≈ 84% efficiency and a ≈ 320 °C stack. The
> air preheater recovers ≈ 4.3 MW, saving ≈ 3.2 MW of fuel (≈ 235 kg/h) for ≈ 75 kW of fan electrical power.

## 2. PFD stream table (design case)

| No. | Stream | Phase | Mass flow | T (°C) | P | Notes |
|---|---|---|---|---|---|---|
| 1 | Crude from preheat train to heater inlet header | L | 286 t/h | 250 | 11.0 barg | ANS, API 32.3 |
| 2A–D | Pass inlet (after FV-1101..1104) | L | 71.5 t/h each | 250 | 8.5 barg | To convection coil |
| 3A–D | Crossover (convection → radiant) | L | 71.5 t/h each | ≈ 292 | ≈ 7.8 barg | External crossover piping |
| 4A–D | Pass outlet | V+L | 71.5 t/h each | 360 | ≈ 2.6 barg | |
| 5 | Transfer line to C-101 flash zone | V+L | 286 t/h | 360 | 2.5 barg | Vapor fraction computed by the model |
| 6 | Fuel gas to burner manifold | V | 2,860 kg/h | 40 | 1.2 barg | LHV 48.5 MJ/kg |
| 7 | Pilot gas | V | ≈ 25 kg/h | 40 | 0.7 barg | Continuous |
| 8 | Ambient air to FD fan K-101 | V | 57,850 kg/h | 25 | atm | |
| 9 | Cold air, FD discharge → APH | V | 57,850 kg/h | ≈ 30 | +130 mmH₂O | |
| 10 | Hot air, APH → burner windbox | V | 54,370 kg/h | ≈ 300 | +60 mmH₂O | After ≈ 6% leakage to the gas side |
| 11 | Flue gas at bridgewall (radiant exit) | V | 57,230 kg/h | ≈ 845 | −2.5 mmH₂O | |
| 12 | Flue gas, convection outlet → APH | V | 57,230 kg/h | ≈ 390 | −20 mmH₂O | |
| 13 | Flue gas, APH outlet → ID fan K-102 | V | 60,700 kg/h | ≈ 150 | −120 mmH₂O at fan inlet | Includes APH leak air |
| 14 | Flue gas, ID discharge → stack S-101 | V | 60,700 kg/h | ≈ 155 | +15 mmH₂O | |
| 15 | LP steam: snuffing / purge | V | intermittent | 150 | 3.5 barg | |
| 16 | LP steam: convection + APH soot blowing | V | intermittent | 150 | 3.5 barg | |
| — | Tramp air (casing leakage) | V | 0 at design | 25 | — | Enters where the casing is below atmospheric pressure (firebox, convection); degradation (Type B) |

> **O2 measurement chain:** arch O2 (AIC-1321, 3.0%) → APH gas-inlet O2 (AT-1327, ≈ 3.2%: the
> as-commissioned convection casing leaks slightly) → stack O2 (AT-1326, ≈ 4.4%: plus APH seal
> leakage). **AT-1327 − AIC-1321** tracks convection-section ingress; **AT-1326 − AT-1327** tracks APH
> seal leakage. The **as-new physics model** sets casing leakage to zero (AT-1327 = AIC-1321) and APH
> leakage to its 6% design value; growth beyond those is what calibration must discover.

## 3. Control loops

| Loop | Measured | Manipulated | Notes |
|---|---|---|---|
| COT control (master) | TIC-1110 (combined COT) | Setpoint of PIC-1202 | Cascade: COT → fuel-gas pressure. COT is a production target (given), not an optimizer decision |
| Fuel-gas pressure (slave) | PIC-1202 | PV-1202 | Clamps keep pressure between trip limits; BMS clamps the setpoint during a fan-trip runback |
| Pass flow (×4) | FIC-1101..1104 | FV-1101..1104 | Operator balances pass outlet temperatures (TT-1111..1114) by trimming pass setpoints |
| Excess O2 (master) | AIC-1321 (arch O2, dry) | Setpoint of FIC-1341 | Setpoint is a **decision variable (Type A)**; design 3.0%, range 2–4% |
| Combustion air flow (slave) | FIC-1341 | FD fan K-101 VFD (SC-1341) | Air/fuel cross-limiting: air leads on load increase, fuel leads on decrease |
| Arch draft | PIC-1311 | ID fan K-102 VFD (SC-1351) | Setpoint −2.5 mmH₂O. *Stretch decision:* draft setpoint (lower draft = less tramp air, but less margin to positive pressure) |
| APH cold end | TIC-1345 (APH gas outlet) | Cold-air bypass damper TV-1345 | Setpoint 148 °C (Lo alarm 145, limit 140): opens only when the gas outlet would fall below setpoint (cold weather / low load); closed at design (≈ 150 °C). The 140 °C gas-outlet limit is a proxy: cold-end average metal ≈ ½(150 + 30) ≈ 90 °C, so the cold-end baskets are assumed enamelled/corrosion-resistant — reviewer to confirm |
| Soot blowing | HS-1501 sequencer | SB-101A..F (convection), SB-102A/B (APH) | Daily sequence, logged as events |

## 4. Final elements and isolation valves / dampers

| Tag | Service | Fail position |
|---|---|---|
| FV-1101..1104 | Pass flow control valves | Fail open (protect coil from no flow) |
| PV-1202 | Fuel-gas pressure control valve | Fail closed |
| XV-1201 / XV-1202 | Main fuel-gas double block (SIS) | Fail closed |
| XV-1203 | Main fuel-gas bleed vent to safe location (SIS) | Fail open |
| XV-1209 | Pilot gas shutoff (SIS) | Fail closed |
| SC-1341 | FD fan K-101 variable-speed drive | Holds last speed on signal loss |
| SC-1351 | ID fan K-102 variable-speed drive | Holds last speed on signal loss |
| TV-1345 | APH cold-air bypass damper | Fail closed |
| XV-1361 (D-101) | Flue-gas bypass damper: convection outlet → stack, bypassing APH and ID fan | **Fail open** (natural-draft path) |
| XV-1362 (D-102) | Emergency air doors on the burner windbox | **Fail open** (natural-draft air) |
| XV-1401 | Firebox snuffing steam | Manually initiated |
| HV-1402 | Header-box snuffing steam | Manual |
| XV-1105A..D / XV-1106A..D | Pass inlet / outlet isolation for decoking (manual, spectacle blinds) | — |

## 5. SIS / BMS actions (summary — full cause and effect in `safe_bms_cause_and_effect`)

| Initiator | Action |
|---|---|
| Any pass flow FT-1151..1154 < 43 t/h (LL), 2 s delay | **Main fuel trip**: close XV-1201/1202, open XV-1203; pilots stay lit |
| Fuel-gas pressure PT-1206 < 0.25 barg | Main fuel trip |
| Fuel-gas pressure PT-1207 > 2.5 barg | Main fuel trip |
| KO drum level LT-1205 > 80% (HH) | Main fuel trip |
| Flame loss on ≥ 3 of 8 burners (BS-1211..1218) | Main fuel trip |
| Firebox pressure PT-1314 > +10 mmH₂O (HH), 5 s | Main fuel trip |
| Pilot gas PT-1208 < 0.25 barg | **Total trip** (main fuel trip + close XV-1209) |
| Manual ESD HS-1290 | Total trip |
| FD fan stopped (XS-1341 = 0) | **Natural-draft runback**: open XV-1362 emergency air doors and XV-1361 bypass damper, stop ID fan, clamp firing to ≤ 60% of normal |
| ID fan stopped (XS-1351 = 0) | Natural-draft runback: open XV-1361 bypass damper and XV-1362, stop FD fan, clamp firing to ≤ 60% |
| APH rotor stopped (XS-1349 = 0) | Natural-draft runback (as ID fan stop) + APH fire watch |
| Purge not complete (5 volume changes with **both fans running** and FIC-1341 ≥ 25% of design air, ≈ 14,500 kg/h; purge on natural draft is not permitted because air flow cannot be proven) | Light-off permissive blocked |

Natural-draft capability (bypass damper and emergency air doors open, fans stopped) ≈ 60% of normal
firing. Not trips (operator alarms only): high TMT, high COT, low/high O2, high CO, high coil ΔP,
low APH outlet temperature, high fan speed. These are the limits the optimizer must respect.

## 6. Operating limits used by the optimizer

| Limit | Value | Tag(s) |
|---|---|---|
| Hottest-tube TMT | ≤ 600 °C | TI-1121A..1124B (and the model's true hottest tube) |
| Coil ΔP | ≤ 8.4 bar per pass (≈ 40% above clean) | PDI-1101..1104 |
| CO | ≤ 200 ppm | AT-1322 |
| Burner (true) O2 | ≥ 1.5% dry | AIC-1321 corrected for analyzer bias and tramp air |
| Bridgewall | 760–900 °C | TT-1301A/B |
| Firing | ≤ 120% of normal heat release (≤ 46 MW LHV) | FT-1201 × AT-1203 |
| Draft | Arch negative (< 0) | PIC-1311 |
| APH gas outlet (acid dew point margin) | ≥ 140 °C | TIC-1345 |
| ID fan capacity | Speed ≤ 95% | SI-1351 |
| FD fan capacity | Speed ≤ 95% | SI-1341 |
| COT | 360 °C ± 2 (production target, **given**) | TIC-1110 |

**Objective terms:** fuel cost + **fan electrical power cost** (JI-1341 + JI-1351) + amortized decoke
cost. Downstream effects of heater outlet conditions on the atmospheric column (cut points, yields) are
**noted but not modelled** in this phase; they are an open item for discussion.

## 7. Equipment id vocabulary (RAG doc `equipment:` frontmatter)

`heater_h101, radiant_section, radiant_coil, convection_section, burners, fuel_gas_system,
fuel_gas_ko_drum, pilot_gas_system, stack, air_preheater, fd_fan, id_fan, bypass_dampers,
flue_gas_analyzers, pass_flow_control, transfer_line, snuffing_steam, soot_blowers, bms_sis,
crude_charge_pumps, atmospheric_column`

(`stack_damper` from Rev A is retired: the natural-draft stack damper is replaced by ID fan draft
control plus the D-101 bypass damper and D-102 emergency air doors, id `bypass_dampers`.)

## 8. Drawing and document numbering

- Plant: *Demo Refinery*, Unit 100 (Crude Distillation). Fictional — documents written for the demo.
- PFD: `U100-PFD-001`. P&IDs: `U100-PID-101` (process coil), `U100-PID-102` (combustion, fuel gas,
  burners, BMS), `U100-PID-103` (air preheater, FD/ID fans, ducts, dampers, stack). All Rev B.
- RAG docs: `H101-<TYPE>-<NNN>`, e.g. `H101-TRB-003`.
