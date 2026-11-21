---
doc_id: trb_rising_coil_pressure_drop
doc_type: troubleshooting
equipment: [radiant_coil, pass_flow_control, transfer_line, atmospheric_column, convection_section, heater_h101]
tags: [PDI-1101, PDI-1102, PDI-1103, PDI-1104, PT-1101, PT-1102, PT-1103, PT-1104, PT-1110, PT-1100, FIC-1101, FIC-1102, FIC-1103, FIC-1104, FY-1100, TIC-1110, TT-1111, TT-1112, TT-1113, TT-1114, TI-1121A, TI-1121B, TI-1122A, TI-1122B, TI-1123A, TI-1123B, TI-1124A, TI-1124B]
title: Troubleshooting Guide — Rising Coil Pressure Drop
revision: 1.9
date: 2026-11-20
---

# Troubleshooting Guide — Rising Coil Pressure Drop

**Document No.:** H101-TRB-002
**Symptom:** Any pass ΔP PDI-1101..PDI-1104 above 7.8 bar (Hi alarm), approaching 8.4 bar (HH alarm), or rising steadily above its start-of-run value of about 6.0 bar
**Revision:** 1.9 | **Date:** 2026-11-20
**Applicability:** Unit 100 — H-101 Crude Charge Heater
**Owner:** Fired Equipment Engineering / Unit 100 Operations
**P&ID reference:** U100-PID-101 (process coil, pass flow control)

**Revision note:** Rev 1.9 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).

> **NOTE:** PDI-1101..PDI-1104 are calculated as pass inlet pressure (PT-1101..PT-1104, downstream of FV-1101..FV-1104) minus the common coil outlet pressure PT-1110. High coil ΔP is an alarm, not a trip. HH 8.4 bar (about 40% above clean) is the hydraulic limit: beyond it the pass control valves run out of range and pass flow can no longer be guaranteed. The Rev B combustion-side change (balanced draft, air preheater) does not change the coil hydraulics; clean ΔP remains ≈ 6.0 bar per pass.

---

## 1. Immediate Actions

When any PDI-110x exceeds 7.8 bar:
1. **Check the pass flow.** ΔP rises roughly with the square of flow. Compare FIC-1101..FIC-1104 with their 71.5 t/h normal. A pass at 80 t/h shows ≈ 25% more ΔP than at 71.5 t/h with no fouling at all.
2. **Check the FV-110x output** on the high-ΔP pass. If the valve is approaching fully open, pass flow is at risk; inform the shift supervisor.
3. **Check PT-1110 and PT-1100.** A common shift in all four PDIs with PT-1110 moving points to the outlet side or the transmitter, not the coil.
4. **Check the same pass's skin TCs and outlet.** Rising TI-112xA/B with rising PDI-110x confirms coke; a coked pass's outlet TT-111x also runs slightly cooler than the others. Follow Troubleshooting Guide — High Tube Metal Temperature, Rev 2.4 if TMT is also high.
5. At **8.4 bar**: shift charge from that pass only if the other passes can take it within the 80 t/h FIC range, or reduce total charge FY-1100 (inform the C-101 operator: less charge at constant COT changes column loading and product rates). Do not let the pass flow fall below 60 t/h (FT-1151..FT-1154 trip main fuel at 43 t/h).

---

## 2. Probable Causes

### 2.1 Internal Coke in the Radiant Coil

**Description:** Coke narrows the tube bore in the hottest tubes near the outlet, where the crude is partly vaporized and velocity is highest, so even a thin layer raises ΔP noticeably. This is the second, independent coke signal alongside TMT. The coke layer also adds thermal resistance, so the pass absorbs slightly less heat.

**Diagnosis:** PDI-110x of one pass rises slowly (weeks) at constant pass flow and constant COT, **together with** TI-112xA/B of the **same** pass. That pass's outlet TT-111x runs slightly **cooler** than the other passes and TIC-1110 fires harder to hold COT, so fuel per unit duty trends up. Other passes may follow at a different rate.

**Action:** Normalise ΔP to design flow: ΔP_norm = PDI × (71.5 / FIC)². Trend ΔP_norm and TMT per pass. Forecast when ΔP_norm reaches 8.4 bar or TMT 600 °C and plan decoking per Maintenance Procedure — Mechanical Pigging Decoke of H-101 Coil, Rev 2.7.

### 2.2 Higher Flow or Higher Vaporization (No Fouling)

**Description:** The outlet half of each pass is two-phase; ΔP depends strongly on vapor fraction. Higher COT, a lighter crude (WTI Light, API 47.4, vaporizes far more at 360 °C than the ANS design crude) or lower outlet pressure all raise vapor volume and ΔP. Higher charge raises ΔP on all passes.

**Diagnosis:** **All four** PDIs move together, in step with FY-1100, TIC-1110 or a crude switch. TMTs do not rise disproportionately. ΔP_norm (Section 2.1) is unchanged when flow is the only cause.

**Action:** No maintenance action. Re-baseline the start-of-run ΔP for the crude being run (SOP — Crude Switch / Crude Blend Change at H-101, Rev 1.8). A heavier crude vaporizes less at the same COT and shows lower clean ΔP, but cokes faster.

### 2.3 Coil Outlet / Transfer Line Pressure Change

**Description:** PT-1110 (normal 2.5 barg, Hi 3.2) is set by the C-101 flash zone pressure plus transfer line loss. Higher back-pressure suppresses vaporization; lower back-pressure increases it. A deposit in the transfer line raises PT-1110.

**Diagnosis:** PT-1110 trending, all four PDIs shifting by a similar amount, pass inlet pressures PT-1101..PT-1104 following.

**Action:** Check C-101 pressure control and transfer line condition with the crude unit board.

### 2.4 Inorganic Deposits or Spalled Coke

**Description:** Salts, iron sulfide or sediment from a desalter upset, or coke flakes spalling after a thermal cycle (trip, fan-trip runback, crude switch), can lodge in return bends.

**Diagnosis:** A **step** increase in one or more PDIs immediately after an upset, trip, runback or restart, often without a matching TMT rise.

**Action:** Hold stable conditions; a lodged plug may clear itself. If ΔP remains high, plan decoking. Ask the crude unit for desalter performance data.

### 2.5 Pressure Transmitter Fault

**Description:** Drift or impulse line plugging on PT-110x or PT-1110.

**Diagnosis:** PDI changes without any matching change in FIC-110x, FV-110x output or TMT; a fault in PT-1110 shifts all four PDIs equally; a fault in one PT-110x shifts one pass only. A real coil restriction forces FV-110x to open to hold flow, so the valve drop (PT-1100 minus PT-110x) falls as PDI-110x rises; if the PDI rises but the FV-110x output and valve drop do not change, suspect the transmitter.

**Action:** Field check with a test gauge; blow down impulse lines; recalibrate.

---

## 3. Distinguishing Cause from Symptom

| What you see | What it means | How to confirm |
|---|---|---|
| One PDI up slowly + same-pass TMTs up + that pass outlet slightly cooler | Coke in that pass | ΔP_norm and TMT trends; not reversible by flow changes |
| All four PDIs up with charge, COT or lighter crude | Hydraulic / vaporization effect, not fouling | ΔP_norm unchanged; correlation with FY-1100, TIC-1110 or crude |
| All four PDIs shift equally, PT-1110 moving | Outlet side or PT-1110 transmitter | C-101 pressure; PT-1110 test gauge |
| Step jump after an upset, runback or restart | Spalled coke or deposit lodged | Time-align with event log; TMT may not change |
| One PDI changes, nothing else moves | PT-110x transmitter fault | Field gauge; impulse line check |
| PDI flat but TMT rising in same pass | Not coke-driven ΔP — or a stuck PT; check skin TCs and flames | Troubleshooting Guide — High Tube Metal Temperature, Rev 2.4 |

Rising ΔP is a **symptom**. Coke is a cause only when the same pass also shows rising TMT at constant flow.

---

## 4. Prevention / Follow-up

- Record start-of-run ΔP_norm per pass after every decoke and every crude switch as the new baseline.
- Weekly trend of ΔP_norm and hottest TMT per pass; plan decoking when the forecast crossing of 8.4 bar or 600 °C falls within the next 8 weeks.
- Keep pass flows balanced and above 60 t/h; low velocity accelerates coking.
- Coordinate with the crude unit on desalter upsets and heavy crude blends (Kearl: MCR 9.7 wt%, asphaltenes 5.7 wt%), which raise the coking rate.
- Minimise thermal cycling: each trip or fan-trip runback is a spalling opportunity.
