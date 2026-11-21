---
doc_id: trb_pass_temperature_imbalance
doc_type: troubleshooting
equipment: [pass_flow_control, radiant_coil, convection_section, burners, transfer_line, atmospheric_column, bms_sis, heater_h101]
tags: [TT-1111, TT-1112, TT-1113, TT-1114, TIC-1110, FIC-1101, FIC-1102, FIC-1103, FIC-1104, FY-1100, FT-1151, FT-1152, FT-1153, FT-1154, PDI-1101, PDI-1102, PDI-1103, PDI-1104, TI-1121A, TI-1121B, TI-1122A, TI-1122B, TI-1123A, TI-1123B, TI-1124A, TI-1124B, TT-1131, TT-1132, TT-1133, TT-1134, BS-1211, BS-1218, PT-1342, XS-1341, XS-1351]
title: Troubleshooting Guide — Pass Outlet Temperature Imbalance
revision: 2.0
date: 2026-11-20
---

# Troubleshooting Guide — Pass Outlet Temperature Imbalance

**Document No.:** H101-TRB-008
**Symptom:** Pass deviation alarm TDA-1111..TDA-1114 — any pass outlet temperature TT-1111..TT-1114 more than ±6 °C from the average of the four passes
**Revision:** 2.0 | **Date:** 2026-11-20
**Applicability:** Unit 100 — H-101 Crude Charge Heater
**Owner:** Unit 100 Operations / Fired Equipment Engineering
**P&ID reference:** U100-PID-101 (pass flow control, coil temperatures), U100-PID-102 (burners, windbox)

**Revision note:** Rev 2.0 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).

> **NOTE:** The combined COT (TIC-1110) can be on target at 360 °C while one pass runs hot and another cold. A hot pass cokes faster and its tubes run hotter. Pass balancing is done by the operator trimming pass flow setpoints FIC-1101..FIC-1104 with total charge FY-1100 held constant, per Control Narrative — Pass Flow Control and Pass Balancing, Rev 2.1. COT remains a given production target; the combined outlet sets C-101 flash-zone vaporization, so balancing must not move TIC-1110.

---

## 1. Immediate Actions

1. **Check pass flows first.** Compare FIC-1101..FIC-1104 (normal 71.5 t/h each). Check that each FV-1101..FV-1104 output is not saturated and that there is no deviation alarm between the FIC and its SIS transmitter FT-1151..FT-1154.
2. **Check the skin TMTs and ΔP of the deviating pass** (TI-112xA/B, PDI-110x) before trimming flow, so that the trim does not hide a coke problem. Note whether the deviating pass is hot or **cold** — a coked pass usually runs slightly cold (Section 2.2).
3. **Trim pass flow:** in steps of 1–2 t/h, keeping FY-1100 constant. Wait about 15 minutes between steps for TT-111x to settle.
4. **Limits on trimming:** no pass below 60 t/h (FIC Lo alarm) or above 80 t/h (FIC Hi alarm). The SIS trips main fuel if any FT-1151..FT-1154 falls below 43 t/h for 2 s.
5. If a pass cannot be balanced within these limits, inform the shift supervisor and Fired Equipment Engineering.

---

## 2. Probable Causes

### 2.1 Pass Flow Maldistribution

**Description:** One pass carries less crude because its FV is limited, its flow transmitter reads high, or its coil resistance has risen and the valve is running out of range.

**Diagnosis:** Hot pass has a lower true flow: FIC-110x below setpoint with FV-110x near full open, or FIC-110x and FT-115x disagree (one transmitter wrong). Hot pass PDI-110x lower than the others if flow really is low. Crossover TT-113x of the same pass also higher (low flow heats up in the convection section too).

**Action:** Correct the flow measurement or valve; trim flows. Calibrate FIC-110x against FT-115x.

### 2.2 Coke in One Pass

**Description:** Coke in a pass raises its TMT and its coil ΔP. Because coke adds thermal resistance, a coked pass absorbs slightly less heat, so its outlet runs a little **cooler** than the other passes; TIC-1110 then fires harder to hold COT, which raises every pass's TMT and the fuel per unit duty.

**Diagnosis:** TT-111x of the affected pass slightly below the average, **with** TI-112xA/B **and** PDI-110x of the same pass rising at constant flow over weeks. Cutting flow on that pass "fixes" the outlet temperature for a while, but TMT and ΔP keep rising faster.

**Action:** Do **not** reduce flow on a coked pass to raise its outlet — low velocity accelerates coking. Hold or raise its flow (within 80 t/h) and accept a small outlet deviation; plan decoking per Troubleshooting Guide — High Tube Metal Temperature, Rev 2.4 and Maintenance Procedure — Mechanical Pigging Decoke of H-101 Coil, Rev 2.7.

### 2.3 Firing Maldistribution (Burner Pattern or Air Distribution)

**Description:** Passes run along the side walls of the cabin box above the single row of floor burners B-101A–H, which share one hot-air windbox. A burner out, a long flame, uneven fuel pressure between burners, or uneven air distribution in the windbox heats one wall more. Air distribution changes markedly after a fan or APH-rotor trip: in natural-draft operation (XS-1341 / XS-1351 = 0) cold air enters through the D-102 emergency air doors, windbox pressure PT-1342 collapses from its ≈ +60 mmH2O normal, and the burners nearest the doors may receive more air than those farther away.

**Diagnosis:** Imbalance begins with a burner event (scanner BS-1211..BS-1218 lost or flickering), a burner or register adjustment, or a fan trip; TMTs of the passes on the hot side rise together; PDI unchanged; flows equal.

**Action:** Restore the burner and balance firing per Maintenance Procedure — Burner Inspection, Cleaning and Tuning, Rev 2.0; then rebalance flows. After a fan trip, rebalance only once the runback has settled (SOP — FD / ID Fan Trip Response and Natural-Draft Operation, Rev 1.0).

### 2.4 Convection / Crossover Imbalance

**Description:** Uneven fouling or flue bypassing in the convection section gives different crossover temperatures, which carry through to the outlet.

**Diagnosis:** TT-1131..TT-1134 crossover temperatures (normal ≈ 292 °C) differ by more than about 5 °C with equal flows; radiant TMTs normal.

**Action:** Soot blow (Maintenance Procedure — Convection Section Soot Blowing, Rev 1.9); check soot blower SB-101A..F coverage.

### 2.5 Outlet Thermocouple Fault

**Description:** A TT-111x thermowell element drifts or fails.

**Diagnosis:** One TT-111x deviates while its flow, crossover temperature TT-113x, TMTs and PDI are all normal; the combined TIC-1110 does not move as the flow-weighted average of the four pass outlets would predict.

**Action:** Do not trim flow on a suspect reading. Check the element; replace or recalibrate.

---

## 3. Distinguishing Cause from Symptom

| What you see | What it means | How to confirm |
|---|---|---|
| Hot pass, flow low, PDI low, crossover high | Flow maldistribution | FIC vs FT-115x; FV output |
| Slightly cool pass, its TMTs and PDI rising together, TIC-1110 firing harder | Coke in that pass | TMT and ΔP trends at constant flow |
| Hot side after a burner event or fan trip, flows equal | Firing / air maldistribution | Scanner history, XS-1341 / XS-1351, PT-1342, visual |
| Crossover TT-113x already unequal | Convection imbalance | Crossover trend, soot blow response |
| One TT-111x off, nothing else moves | Outlet TC fault | Compare with TIC-1110 heat balance |

The pass deviation alarm is a **symptom**. Flow trimming treats the symptom; always identify the cause before deciding the trim is the fix. Reducing flow to a coked pass to "balance" it is the most damaging response, because low velocity accelerates coking.

---

## 4. Prevention / Follow-up

- Balance passes on TMT as well as outlet temperature; the goal is equal hottest-tube TMT, not only equal TT-111x.
- Log every flow trim with the reason; a pass that needs repeated trims in the same direction over weeks is a coke indicator.
- Check FIC-110x against FT-115x weekly.
- After a crude switch, rebalance passes once conditions have settled (SOP — Crude Switch / Crude Blend Change at H-101, Rev 1.8); a heavier crude cokes faster, so watch TMT/ΔP pairs more closely.
