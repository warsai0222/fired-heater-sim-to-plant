# Rev B Change Note (MOC-H101-2026-07) — Balanced Draft + Regenerative Air Preheater

**Date:** 2026-11-20. **Reason:** design-basis change requested by the project owner: H-101 now has
an air preheater and balanced draft. Supersedes the Rev A natural-draft / no-APH design.

## What changed (engineering)

| Item | Rev A | Rev B |
|---|---|---|
| Draft | Natural draft, stack damper PV-1311 / D-101 | **Balanced draft**: FD fan K-101 (VFD SC-1341) + ID fan K-102 (VFD SC-1351) |
| Air preheat | None | **Regenerative (Ljungström) APH E-102**, air ≈ 30 → 300 °C, flue 390 → 160 °C, duty ≈ 4.3 MW |
| Efficiency / fired duty / fuel | ≈ 84% / 41.7 MW / 3,095 kg/h | **≈ 91% / 38.5 MW / 2,860 kg/h** |
| Stack temperature | ≈ 320 °C (TT-1303) | **≈ 150–155 °C** (APH gas outlet TIC-1345); TT-1303 is now convection outlet / APH gas inlet ≈ 390 °C |
| Bridgewall / crossover / SOR TMT | 800 / 298 / 420 °C | **845 / 292 / 430 °C** |
| Radiant / convection split | 70/30 (24.5/10.5 MW), flux 32 kW/m² | **≈ 74/26 (26/9 MW), flux ≈ 34 kW/m²** (same 80 tubes, 766 m²) |
| Excess-O2 control | AIC-1321 → plenum louvre HV-1331 | **AIC-1321 → FIC-1341 combustion air flow → FD fan speed**; air/fuel cross-limiting |
| Draft control | PIC-1311 → stack damper PV-1311 | **PIC-1311 → ID fan speed**; stretch decision = draft setpoint |
| Natural-draft fallback | n/a | D-101 bypass damper (XV-1361, FO) + D-102 emergency air doors (XV-1362, FO); **fan or APH-rotor stop = natural-draft runback to ≤ 60% firing** (not a fuel trip) |
| New trip | — | PT-1314 firebox pressure HH +10 mmH₂O, 5 s → main fuel trip |
| O2 chain | arch 3.0, stack 3.6 | **arch AIC-1321 3.0 → APH inlet AT-1327 3.2 → stack AT-1326 4.4**. AT-1327 − AIC-1321 (≈ 0.2 normal; investigate > ≈ 0.8) = convection ingress. AT-1326 − AT-1327 (≈ 1.2 normal = ≈ 6% seal leakage; investigate > ≈ 2.0) = APH seal leakage |
| New Type B degradations | — | **APH seal leakage growth** (stack O2 ↑ vs APH inlet, ID fan speed/power ↑, APH gas outlet T ↓ by dilution, hot-air flow to burners ↓ for the same FD flow); **APH fouling** (PDT-1347 gas ΔP ↑, TT-1343 hot air ↓, TIC-1345 gas outlet ↑, efficiency ↓, ID fan load ↑) |
| Tramp air | Below arch and convection | Still present (firebox and convection are below atmospheric pressure); leakage ∝ leak area × √draft, draft now set by ID fan |
| New optimizer limits | — | APH gas outlet ≥ 140 °C (acid dew point margin); ID and FD fan speed ≤ 95%; objective adds **fan power cost** (JI-1341 + JI-1351) |
| Firing limit | ≤ 50 MW | **≤ 46 MW LHV** (120% of 38.5) |
| Tags removed | ZT-1311, ZT-1331, PV-1311, HV-1331 | — |
| Tags added | — | FIC-1341, PT-1342, TT-1343, TIC-1345, AT-1327, PDT-1347, PDT-1348, XS-1349, PT-1314, PT-1352, SI-1341, SI-1351, JI-1341, JI-1351, XS-1341, XS-1351, ZT-1361, ZT-1362; final elements SC-1341, SC-1351, TV-1345, XV-1361, XV-1362; soot blowers SB-102A/B; equipment E-102, K-101, K-102, D-102 |
| Equipment-id vocabulary | stack_damper | retired; added air_preheater, fd_fan, id_fan, bypass_dampers |
| Drawings | PFD, PID-101, PID-102 | Rev B; PID-102 combustion/fuel/BMS; **new PID-103** APH, fans, ducts, dampers, stack |

## Unchanged by decision
- **COT stays a given production target** (not an optimizer decision).
- **Downstream effects:** heater outlet conditions (COT, vaporization, outlet pressure) affect the
  atmospheric column cut points and yields. Not modelled in this phase; documents should *mention* the
  downstream consequence where relevant (e.g. a COT change or runback reduces flash-zone vaporization
  and shifts distillate into residue; coordinate with the C-101 / unit operator), and it is an open
  item for discussion.

## Master document list after Rev B (42 docs; titles and revisions fixed for cross-references)

All existing docs are reissued at +0.1 revision dated 2026-11-20 with a header line
`**Revision note:** Rev X.X — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).`
New docs are Rev 1.0 dated 2026-11-20.

| Folder | doc_id | Title | Rev | Status |
|---|---|---|---|---|
| controls/ | ctrl_alarm_trip_register | Alarm and Trip Setpoint Register — H-101 Crude Charge Heater | 3.1 | revised |
| controls/ | ctrl_cot_fuel_gas_cascade | Control Narrative — Coil Outlet Temperature / Fuel Gas Pressure Cascade | 2.3 | revised |
| controls/ | ctrl_excess_o2_and_draft | Control Philosophy — Excess O2 and Arch Draft Control | 2.5 | revised |
| controls/ | ctrl_pass_flow_balancing | Control Narrative — Pass Flow Control and Pass Balancing | 2.1 | revised |
| datasheets/ | ds_burners | Equipment Datasheet — B-101A–H Process Burners | 1.7 | revised |
| datasheets/ | ds_convection_section | Equipment Datasheet — H-101 Convection Section | 1.5 | revised |
| datasheets/ | ds_flue_gas_analyzers | Instrument Datasheet — Flue Gas O2, CO and Stack CEMS Analyzers | 1.6 | revised |
| datasheets/ | ds_fuel_gas_system | Equipment Datasheet — Fuel Gas and Pilot Gas System (incl. V-101) | 1.4 | revised |
| datasheets/ | ds_h101_crude_charge_heater | Equipment Datasheet — H-101 Crude Charge Heater (Overall) | 2.2 | revised |
| datasheets/ | ds_radiant_coil | Equipment Datasheet — H-101 Radiant Coil and Tubes | 2.1 | revised |
| datasheets/ | ds_stack_and_bypass_dampers | Equipment Datasheet — S-101 Stack, D-101 Bypass Damper and D-102 Emergency Air Doors | 1.3 | revised |
| maintenance/ | mnt_burner_inspection_tuning | Maintenance Procedure — Burner Inspection, Cleaning and Tuning | 2.0 | revised |
| maintenance/ | mnt_o2_analyzer_calibration | Maintenance Procedure — O2 and CO Analyzer Calibration and Validation | 2.2 | revised |
| maintenance/ | mnt_pigging_decoke | Maintenance Procedure — Mechanical Pigging Decoke of H-101 Coil | 2.7 | revised |
| maintenance/ | mnt_skin_thermocouple_inspection | Maintenance Procedure — Tube Skin Thermocouple Inspection and Replacement | 1.6 | revised |
| maintenance/ | mnt_soot_blowing | Maintenance Procedure — Convection Section Soot Blowing | 1.9 | revised |
| maintenance/ | mnt_tramp_air_survey | Maintenance Procedure — Tramp Air Survey and Casing Sealing | 1.5 | revised |
| safety/ | env_stack_emissions | Environmental Procedure — Stack Emissions Monitoring (CO, NOx) | 1.4 | revised |
| safety/ | safe_bms_cause_and_effect | BMS / SIS Cause and Effect — H-101 | 3.3 | revised |
| safety/ | safe_firebox_entry | Safety Procedure — Firebox and Header Box Entry (Confined Space) | 1.7 | revised |
| safety/ | safe_integrity_operating_windows | Integrity Operating Windows (IOW) — H-101 Radiant Coil | 2.1 | revised |
| safety/ | safe_tube_rupture_response | Emergency Response — Tube Rupture and Firebox Fire | 2.3 | revised |
| sops/ | sop_cold_startup_light_off | SOP — H-101 Cold Start-up, Purge and Burner Light-off | 3.2 | revised |
| sops/ | sop_crude_switch | SOP — Crude Switch / Crude Blend Change at H-101 | 1.8 | revised |
| sops/ | sop_daily_operator_rounds | SOP — H-101 Daily Operator Rounds and Firebox Inspection | 2.1 | revised |
| sops/ | sop_emergency_shutdown | SOP — H-101 Emergency Shutdown and Trip Response | 2.6 | revised |
| sops/ | sop_normal_shutdown | SOP — H-101 Normal Shutdown | 2.4 | revised |
| sops/ | sop_o2_step_test | SOP — Excess O2 Step Test (Analyzer / Air-Ingress Check) | 1.3 | revised |
| troubleshooting/ | trb_high_fuel_consumption | Troubleshooting Guide — High Fuel Consumption / Low Efficiency | 2.1 | revised |
| troubleshooting/ | trb_high_o2_reading | Troubleshooting Guide — High O2 Reading / Suspected Air Ingress | 1.6 | revised |
| troubleshooting/ | trb_high_stack_temperature | Troubleshooting Guide — High Stack Temperature | 1.7 | revised |
| troubleshooting/ | trb_high_tube_metal_temperature | Troubleshooting Guide — High Tube Metal Temperature | 2.4 | revised |
| troubleshooting/ | trb_low_o2_high_co | Troubleshooting Guide — Low Excess O2 / High CO | 2.5 | revised |
| troubleshooting/ | trb_pass_temperature_imbalance | Troubleshooting Guide — Pass Outlet Temperature Imbalance | 2.0 | revised |
| troubleshooting/ | trb_positive_draft_afterburning | Troubleshooting Guide — Positive Draft and Afterburning | 1.8 | revised |
| troubleshooting/ | trb_rising_coil_pressure_drop | Troubleshooting Guide — Rising Coil Pressure Drop | 1.9 | revised |
| troubleshooting/ | trb_suspect_skin_thermocouple | Troubleshooting Guide — Suspect Tube Skin Thermocouple Reading | 1.4 | revised |
| datasheets/ | ds_air_preheater | Equipment Datasheet — E-102 Regenerative Air Preheater | 1.0 | **new** |
| datasheets/ | ds_fd_id_fans | Equipment Datasheet — K-101 Forced Draft Fan and K-102 Induced Draft Fan | 1.0 | **new** |
| sops/ | sop_fan_trip_natural_draft | SOP — FD / ID Fan Trip Response and Natural-Draft Operation | 1.0 | **new** |
| maintenance/ | mnt_aph_inspection_washing | Maintenance Procedure — Air Preheater Seal Inspection, Soot Blowing and Water Washing | 1.0 | **new** |
| troubleshooting/ | trb_air_preheater_performance | Troubleshooting Guide — Air Preheater Leakage, Fouling and Low Cold-End Temperature | 1.0 | **new** |
