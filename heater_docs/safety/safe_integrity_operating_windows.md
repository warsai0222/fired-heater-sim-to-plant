---
doc_id: safe_integrity_operating_windows
doc_type: safety
equipment: [radiant_coil, radiant_section, pass_flow_control, transfer_line, burners, fuel_gas_system, air_preheater, fd_fan, id_fan, bms_sis, heater_h101]
tags: [TI-1121A, TI-1121B, TI-1122A, TI-1122B, TI-1123A, TI-1123B, TI-1124A, TI-1124B, FIC-1101, FIC-1102, FIC-1103, FIC-1104, FT-1151, FT-1152, FT-1153, FT-1154, TIC-1110, PDI-1101, PDI-1102, PDI-1103, PDI-1104, FT-1201, AT-1203, TT-1301A, TT-1301B, TIC-1345, SI-1341, SI-1351, PIC-1311, PT-1314, FY-1100]
title: Integrity Operating Windows (IOW) — H-101 Radiant Coil
revision: 2.1
date: 2026-11-20
---

# Integrity Operating Windows (IOW) — H-101 Radiant Coil

**Document No.:** H101-SAF-002
**Revision:** 2.1 | **Date:** 2026-11-20
**Applicability:** Unit 100 — H-101 Crude Charge Heater
**Owner:** Fired Equipment Engineering (with Inspection and Process Safety)
**P&ID reference:** U100-PID-101 (process coil), U100-PID-102 (fuel gas, firebox pressure), U100-PID-103 (APH, fans)

**Revision note:** Rev 2.1 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).

> **SAFETY NOTE:** The H-101 radiant coil is 6" Sch 40 ASTM A335 P9 (9Cr-1Mo), 80 tubes in 4 passes of 20. Coil failure releases hot crude above its auto-ignition temperature into a fired box. None of the limits in this document is an SIS trip except minimum pass flow (FT-1151..FT-1154 < 43 t/h) and firebox pressure (PT-1314 > +10 mmH2O), both of which cause a main fuel trip. Every other IOW depends on the operator responding within the stated time.

---

## 1. Purpose and IOW Levels

This document sets the Integrity Operating Windows for H-101, following the API RP 584 approach. The coil windows (Section 2) are primary; Section 6 adds the combustion-side and air preheater windows that protect the coil, casing and E-102. Each variable has up to two limits:

- **Standard IOW limit:** damage is accelerating or margin is lost. Corrective action within the stated response time; inform the shift supervisor.
- **Critical IOW limit:** rapid or unacceptable damage is possible. Immediate action; if not recovered in time, bring the heater to a safe condition (reduced firing / charge, then controlled shutdown per SOP — H-101 Normal Shutdown, Rev 2.4).

Every critical exceedance, and every standard exceedance longer than its response time, is logged with start time, peak value and duration and reported to Fired Equipment Engineering the same day.

---

## 2. IOW Table — H-101 Radiant Coil

| Variable | Tag(s) | Standard limit | Critical limit | Response time (std / crit) | Damage mechanism |
|---|---|---|---|---|---|
| Tube metal temperature (hottest valid TC) | TI-1121A..TI-1124B | 585 °C (Hi) | 600 °C (HH, TMT design operating limit) | 2 h / 30 min | Creep, oxidation, accelerated coking |
| Pass flow (each pass) | FIC-1101..FIC-1104, FT-1151..FT-1154 | 60 t/h (FIC Lo) | 43 t/h (SIS LL, MFT after 2 s) | 15 min / automatic | Film overheating, coke |
| Coil outlet temperature | TIC-1110 | 368 °C (Hi) | 375 °C (HH) | 30 min / 15 min | Cracking, coke in coil and transfer line |
| Coil ΔP (each pass) | PDI-1101..PDI-1104 | 7.8 bar (Hi) | 8.4 bar (HH, ≈ 40% above clean 6.0) | 1 shift / 2 h | Coke restriction, pass starvation |
| Firing rate (heat release) | FT-1201 × AT-1203 | 110% of normal (≈ 42.4 MW LHV) | 120% of normal (≈ 46 MW LHV; FT-1201 Hi 3,430 kg/h at 48.5 MJ/kg) | 1 shift / 30 min | High flux, flame impingement, burner overload |
| Bridgewall temperature | TT-1301A/B | 900 °C (Hi) | 930 °C (HH) | 1 h / 15 min | High radiant flux, tube support and refractory overheating |

Normal (start-of-run, design crude ANS) values: hottest TMT ≈ 430 °C, pass flow 71.5 t/h, COT 360 °C, coil ΔP 6.0 bar per pass, fired duty 38.5 MW LHV (≈ 91% efficiency with the air preheater), bridgewall ≈ 845 °C. Average radiant flux at normal firing is ≈ 34 kW/m² (radiant share ≈ 74%, higher than Rev A because hot combustion air raises firebox temperature); the 120% firing limit corresponds to ≈ 41 kW/m² average and ≈ 73 kW/m² peak (peak/average ≈ 1.8). Firing is calculated as FT-1201 × AT-1203 because fuel LHV varies.

---

## 3. Tube Metal Temperature IOW — Required Response

**Standard (any TI-1121A..TI-1124B > 585 °C):**
1. Confirm the reading: compare with the paired TC (A/B), the pass PDI-110x and pass outlet TT-111x. If suspect, follow Troubleshooting Guide — Suspect Tube Skin Thermocouple Reading, Rev 1.4 and obtain an IR pyrometer reading within the response time.
2. Look for flame impingement on that pass (SOP — H-101 Daily Operator Rounds and Firebox Inspection, Rev 2.1).
3. Reduce heat input to that pass: raise its flow setpoint (≤ 80 t/h) with FY-1100 constant, correct any burner problem, or reduce firing.
4. Diagnose per Troubleshooting Guide — High Tube Metal Temperature, Rev 2.4.

**Critical (any valid TMT ≥ 600 °C):**
1. Reduce firing immediately until the hottest valid TMT is below 600 °C — lower the TIC-1110 setpoint and, if needed, charge FY-1100 to keep COT in range at lower firing. A lower COT or charge reduces C-101 flash-zone vaporization and shifts yields; coordinate with the C-101 / unit operator.
2. If not below 600 °C within 30 minutes, reduce to minimum stable charge (≥ 60 t/h per pass) and consult the shift superintendent and Fired Equipment Engineering on a controlled shutdown and decoke per Maintenance Procedure — Mechanical Pigging Decoke of H-101 Coil, Rev 2.7.
3. Never trade TMT against pass flow: no pass below 60 t/h to "balance" temperatures.

---

## 4. Creep Life Consumption When TMT Exceeds the Limit

The 600 °C limit is set so the coil reaches its design creep life (typically 100,000 h) at end-of-run conditions. Fired Equipment Engineering assesses every exceedance with the Larson–Miller parameter **LMP = T × (C + log₁₀ t_r)** (T in K, t_r rupture life in h, C ≈ 20 for 9Cr-1Mo). For each period at Tᵢ for tᵢ, the life fraction consumed is tᵢ / t_r(Tᵢ, σ), with t_r from the API 530 / API 579 minimum Larson–Miller curve for P9 at the current hoop stress σ; fractions are summed (Robinson's rule). Near 600 °C, rupture life roughly halves for every 10–15 °C increase, so a few days at 615 °C can consume as much life as months at 600 °C. Wall thinning raises stress, so the same TMT consumes life faster late in tube life. Cumulative fraction above 0.5 triggers a retirement review; any excursion above 650 °C, or visible bulging, sagging or hot spots, requires an inspection hold point at the next shutdown.

---

## 5. Pass Flow, COT, Firing and ΔP Windows

- **Pass flow:** FIC Lo 60 t/h is the standard limit; the SIS FT-1151..FT-1154 LL (43 t/h, 2 s) closes XV-1201/XV-1202 per BMS / SIS Cause and Effect — H-101, Rev 3.3.
- **COT:** TIC-1110 target 360 °C ± 2 (a given production target). Sustained operation above 368 °C increases cracking and coke in the last radiant tubes and the transfer line.
- **Firing:** burner design margin is 120% of normal heat release (≈ 46 MW LHV). During a natural-draft runback BMS-101 clamps firing to ≤ 60% of normal; the coil windows still apply and charge must be reduced to keep COT.
- **Coil ΔP:** compare at the same pass flow; a rise of more than 1.0 bar above start-of-run at constant flow is a coke indicator and triggers decoke planning. HH 8.4 bar is the hydraulic limit.

---

## 6. Combustion-Side and APH Windows That Protect the Coil and Casing

| Variable | Tag(s) | Standard limit | Critical limit | Response time (std / crit) | Damage mechanism / reason |
|---|---|---|---|---|---|
| APH gas outlet (cold end) | TIC-1345 | 145 °C (Lo) | 140 °C (LL; acid dew point margin) | 4 h / 1 h | Sulfuric acid condensation, cold-end corrosion and fouling of E-102 baskets |
| ID fan speed | SI-1351 | 95% (Hi) | — | 1 h | No margin left to hold arch draft; risk of positive firebox pressure |
| FD fan speed | SI-1341 | 95% (Hi) | — | 1 h | No margin left to hold excess O2 on a load or fuel swing |
| Arch draft | PIC-1311 | −0.5 mmH2O (Hi) | 0.0 mmH2O (HH); PT-1314 trips MFT at +10 mmH2O for 5 s | 15 min / immediate | Hot gas leakage through casing and peepholes, casing and support overheating, personnel exposure |

Response times in this section are typical site values chosen for this heater and are subject to review.

- **APH cold end:** the coldest metal in E-102 sits at the cold end, between the gas outlet and the incoming air temperature, so the cold-end metal is always colder than TIC-1345. Holding the gas outlet at or above 145 °C (140 °C minimum) builds in margin for this. TIC-1345 raises cold-end temperature by opening the cold-air bypass TV-1345. Low TIC-1345 is most likely in cold weather and at low firing; it is an alarm and optimizer limit, not a trip. Response is in Troubleshooting Guide — Air Preheater Leakage, Fouling and Low Cold-End Temperature, Rev 1.0. Note that APH seal leakage cools the measured gas outlet by dilution, so a low TIC-1345 is not always a colder element.
- **Fan capacity:** a fan at 95% speed cannot respond to a disturbance. The response is to reduce firing (and charge) to restore margin and to find the cause — rising APH gas-side ΔP (PDT-1347), seal leakage or convection fouling for the ID fan; air-side ΔP or leakage for the FD fan. Fans are protected by their own drives; loss of a fan is a natural-draft runback, not a fuel trip.
- **Arch draft:** the firebox must stay below atmospheric pressure. Response is in Troubleshooting Guide — Positive Draft and Afterburning, Rev 1.8. Running draft more negative than −2.5 mmH2O is not "safer": it pulls in more tramp air and costs ID fan power.

---

## 7. Escalation and Records

| Exceedance | Notify | Record |
|---|---|---|
| Standard IOW, corrected within response time | Shift supervisor | Shift log |
| Standard IOW beyond response time | Shift superintendent, Fired Equipment Engineer (same day) | IOW exceedance record |
| Critical IOW | Shift superintendent immediately; Fired Equipment Engineer and Inspection within 1 h | IOW exceedance record; creep life assessment (Section 4) or APH cold-end inspection request |
| Repeated critical IOW in one run | Area manager | Management of change / run-length review |

Heavier crudes such as Kearl (API 19.8, MCR 9.7 wt%, C7 asphaltenes 5.7 wt%) do **not** automatically need more duty for the same COT (lower vaporization at 360 °C offsets the higher mass per barrel; confirm with the model for the new assay), but they coke faster than the design crude ANS, so the TMT and ΔP windows are approached sooner. Crude changes follow SOP — Crude Switch / Crude Blend Change at H-101, Rev 1.8.
