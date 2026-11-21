---
doc_id: sop_crude_switch
doc_type: sop
equipment: [heater_h101, radiant_coil, pass_flow_control, fuel_gas_system, fd_fan, id_fan, air_preheater, transfer_line, atmospheric_column, crude_charge_pumps]
tags: [FY-1100, TT-1100, PT-1100, FIC-1101, FIC-1102, FIC-1103, FIC-1104, TIC-1110, TT-1111, TT-1112, TT-1113, TT-1114, TI-1121A, TI-1121B, TI-1122A, TI-1122B, TI-1123A, TI-1123B, TI-1124A, TI-1124B, PDI-1101, PDI-1102, PDI-1103, PDI-1104, FT-1201, AT-1203, PIC-1202, TT-1301A, TT-1301B, PT-1110, AIC-1321, FIC-1341, SI-1341, SI-1351, TIC-1345, HS-1501]
title: SOP — Crude Switch / Crude Blend Change at H-101
revision: 1.8
date: 2026-11-20
---

# SOP — Crude Switch / Crude Blend Change at H-101

**Document No.:** H101-SOP-004
**Revision:** 1.8 | **Date:** 2026-11-20
**Revision note:** Rev 1.8 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).
**Applicability:** Unit 100 — H-101 Crude Charge Heater
**Owner:** Unit 100 Operations / Process Engineering
**P&ID Reference:** U100-PID-101 (process coil), U100-PID-103 (air preheater, FD/ID fans)

---

## 1. Scope and Purpose

This procedure covers a change of crude tank or crude blend feeding H-101. The crude slate is planned in advance: the blend recipe and the assay for every crude are issued by planning before the switch and are logged. A crude switch changes the mass the coil heats, the fraction vaporized at the coil outlet, and the coking tendency of the oil — so it can change firing, tube metal temperatures, coil pressure drop and the products made in C-101. The switch time must be logged exactly, because the heater performance model and the coking-trend calibration use it to separate a feed change from equipment degradation.

COT (360 °C on TIC-1110) is a **given production target** set by the unit plan. It is not adjusted by the heater operator to suit the heater.

## 2. Crude Properties That Matter at H-101

| Property (assay) | WTI Light (WTLEX26Y) | Alaska North Slope — design (ANS25Y) | Kearl — heavy (KEARL23B) |
|---|---|---|---|
| API gravity | 47.4 | 32.3 | 19.8 |
| Density at 15 °C, g/cc | 0.791 | 0.864 | 0.935 |
| Micro carbon residue, wt% | 0.1 | 4.7 | 9.7 |
| C7 asphaltenes, wt% | 0.0 | 1.9 | 5.7 |
| Sulfur, wt% | 0.07 | 1.04 | 3.83 |
| TAN, mg KOH/g | 0.05 | 0.41 | 2.08 |
| TBP distilled at 360 °C, vol% | 78.6 | 60.0 | 37.4 |
| 370 °C+ residue yield, wt% | 22.4 | 43.5 | 67.1 |

Micro carbon residue (MCR) and asphaltenes are the main indicators of coking tendency in the radiant coil. Kearl has roughly twice the MCR and three times the asphaltenes of the design crude.

## 3. What to Expect When Switching to a Heavier Crude

1. **Duty does not automatically rise.** At the same bbl/d a heavier crude is more mass (Kearl ≈ 8% more t/h than ANS), but much less of it vaporizes at 360 °C (TBP at 360 °C: 37% vs 60% vol), so less latent heat is absorbed. The two effects partly cancel, and the heavier crude can need the same, more or less duty depending on the blend and on the preheat temperature TT-1100. **Confirm the expected firing with the heater performance model** for the planned blend; judge firing as heat input FT-1201 × AT-1203, not fuel mass alone.
2. **Less vaporization at the coil outlet.** C-101 receives less flash-zone vapour at the same COT: distillate yield falls and atmospheric residue rises. This is a column and planning matter, coordinated with the C-101 operator; a COT change above 362 °C is a change to the production target and needs process engineering and planning approval (it also raises TMT and coking rate).
3. **Higher tube metal temperatures.** A heavy, viscous crude has a lower inside film coefficient, so TI-1121A..1124B run hotter for the same heat flux.
4. **Faster coking.** Expect a faster rise in TMT and coil ΔP (PDI-1101..1104) over the following days and weeks; the decoke date may move forward. Higher sulfur and TAN also raise the corrosion concern in the outlet tubes, transfer line and column (inform fixed equipment engineering).
5. **Lighter crude (e.g. WTI Light)** cokes slowly, but more vaporization raises velocity and ΔP in the two-phase outlet tubes, and lower density reduces t/h — watch the FY-1100 Lo alarm (250 t/h) and FIC-1101..1104 Lo alarm (60 t/h). C-101 receives more vapour: overhead and side-draw loads rise.
6. **Combustion side.** If firing rises, the FD and ID fans rise with it through FIC-1341 and PIC-1311. Check SI-1341 and SI-1351 have headroom to the 95% capacity limit, and that TIC-1345 stays above 145 °C if firing falls.

## 4. Pre-Switch Checks

1. Obtain from planning: new tank number, blend recipe (vol% of each crude), assay reference IDs, planned switch time, and the C-101 cut-point/yield targets for the new crude.
2. Run the heater performance model for the new blend at the planned charge and COT; note the expected heat input and hottest-tube TMT.
3. Confirm the new tank has settled and been water-drained; a water slug flashes in the coil and upsets pass flows.
4. Record a pre-switch snapshot (1-hour averages): FY-1100, TT-1100, TIC-1110, FT-1201, AT-1203, TI-1121A..1124B, PDI-1101..1104, TT-1301A/B, AIC-1321, FIC-1341, SI-1341, SI-1351, TIC-1345.
5. Confirm TMT margin of at least 30 °C to the 585 °C Hi alarm and ΔP margin of at least 0.5 bar to the 7.8 bar Hi alarm. If not, do not switch to a heavier crude without process engineering approval.
6. Suspend non-essential changes (O2 setpoint changes, step tests, HS-1501 soot blowing) for the switch period.

## 5. Switch and Ramp Rules

| Rule | Limit |
|---|---|
| Blend change rate | ≤ 20 vol% of the blend per hour, or tank swing over ≥ 2 h |
| COT | Hold 360 ± 2 °C on TIC-1110 in CASCADE |
| Firing rate change | ≤ 5% of FT-1201 in any 10 minutes |
| Firing limit | FT-1201 Hi alarm 3,430 kg/h (≈ 120% of normal heat release, ≤ 46 MW LHV) |
| Pass balance | TT-1111..1114 within ±6 °C of average (TDA-1111..1114) |
| TMT | Hold below 585 °C (Hi alarm); limit 600 °C |
| Fan speed | SI-1341 and SI-1351 ≤ 95% |

1. Open the new tank suction and swing gradually at the rate above with the crude unit console.
2. The new crude takes about 1.5 hours to travel from the tank through the desalter and preheat train to the heater inlet. Watch TT-1100 and PT-1100 for the arrival and tell the C-101 operator when it arrives.
3. If FT-1201 approaches the Hi alarm, any TMT reaches 575 °C, or a fan speed reaches 95%, stop the swing and hold; reduce charge if needed, in agreement with the column operator.
4. Re-balance passes per Control Narrative — Pass Flow Control and Pass Balancing, Rev 2.1.

## 6. Logging (Mandatory)

1. Log in the shift log **and** as a DCS operator event "CRUDE SWITCH": time the swing started, time new crude reached the heater inlet, time the swing finished, blend recipe and assay IDs.
2. Log a post-switch snapshot (same tags as Section 4 step 4) once the heater has been steady for 4–6 hours. Compare the measured heat input with the model prediction from Section 4 step 2. This is the new reference for TMT and ΔP trending.
3. Notify process engineering; the model calibration uses the logged switch times to avoid attributing a feed effect to fouling or coking.
