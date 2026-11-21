---
doc_id: trb_high_tube_metal_temperature
doc_type: troubleshooting
equipment: [radiant_coil, radiant_section, burners, pass_flow_control, convection_section, air_preheater, flue_gas_analyzers, transfer_line, atmospheric_column, heater_h101]
tags: [TI-1121A, TI-1121B, TI-1122A, TI-1122B, TI-1123A, TI-1123B, TI-1124A, TI-1124B, PDI-1101, PDI-1102, PDI-1103, PDI-1104, TT-1111, TT-1112, TT-1113, TT-1114, FIC-1101, FIC-1102, FIC-1103, FIC-1104, TIC-1110, FT-1201, AT-1203, TT-1301A, TT-1301B, TT-1303, TIC-1345, PDT-1347, AIC-1321, AT-1322, FY-1100, TT-1100, XS-1341, XS-1351]
title: Troubleshooting Guide — High Tube Metal Temperature
revision: 2.4
date: 2026-11-20
---

# Troubleshooting Guide — High Tube Metal Temperature

**Document No.:** H101-TRB-001
**Symptom:** Any radiant tube skin TC TI-1121A..TI-1124B above 585 °C (Hi alarm), or trending toward the 600 °C TMT limit (HH alarm)
**Revision:** 2.4 | **Date:** 2026-11-20
**Applicability:** Unit 100 — H-101 Crude Charge Heater
**Owner:** Fired Equipment Engineering / Unit 100 Operations
**P&ID reference:** U100-PID-101 (process coil), U100-PID-102 (combustion, fuel gas), U100-PID-103 (air preheater, fans)

**Revision note:** Rev 2.4 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).

> **SAFETY WARNING:** High TMT is an operator alarm, not an SIS trip. The 9Cr-1Mo (P9) radiant tubes lose creep life rapidly above 600 °C. The operator is the only protection. Response times are set in Integrity Operating Windows (IOW) — H-101 Radiant Coil, Rev 2.1. With hot combustion air (≈ 300 °C from E-102) the firebox runs hotter than in the Rev A natural-draft design: start-of-run hottest TMT is ≈ 430 °C and bridgewall ≈ 845 °C.

---

## 1. Immediate Actions

When any TI-1121A..TI-1124B exceeds 585 °C:
1. **Check the reading is credible.** Compare with the paired TC on the same pass (e.g. TI-1121A vs TI-1121B), the pass coil ΔP (PDI-1101..PDI-1104) and pass outlet (TT-1111..TT-1114). If only one TC is high and nothing else on that pass has moved, go to Troubleshooting Guide — Suspect Tube Skin Thermocouple Reading, Rev 1.4, but keep treating the alarm as real until an IR pyrometer reading confirms otherwise.
2. **Look in the firebox** at the affected pass for flame impingement, long or leaning flames, or bright (cherry-red) tube spots.
3. **Reduce heat to that pass.** Raise the pass flow setpoint (FIC-1101..FIC-1104, max 80 t/h) while FY-1100 holds total charge, and correct any burner fault on that side.
4. If any valid TMT reaches **600 °C**: reduce firing at once by lowering the TIC-1110 setpoint, and reduce crude charge if needed to keep COT in range. A lower COT or charge reduces flash-zone vaporization in C-101 and shifts distillate into residue — inform the crude unit / C-101 operator before and after the move. Inform the shift superintendent and Fired Equipment Engineering. Log the exceedance for creep life assessment.
5. Never reduce a pass below 60 t/h (FIC Lo alarm) to manage temperatures; the SIS trips main fuel at 43 t/h on FT-1151..FT-1154.

---

## 2. Probable Causes

### 2.1 Internal Coke Build-up in a Pass

**Description:** Coke laid down on the inside of the hottest radiant tubes adds a thermal resistance, so the tube metal must run hotter to push heat into the crude. It also narrows the bore. Coke rate increases with film temperature and falls with velocity, so it is self-accelerating near end-of-run. Start-of-run hottest TMT is ≈ 430 °C; the 600 °C limit defines end-of-run.

**Diagnosis:** Both skin TCs of one pass rise **together with** that pass's PDI-110x over days to weeks, at constant pass flow. Because the coke resistance lets that pass absorb slightly less heat, its outlet TT-111x runs slightly **cooler** than the other passes, and TIC-1110 fires harder to hold COT — so fuel per unit duty (FT-1201 × AT-1203 ÷ absorbed duty) and all passes' TMTs creep up slowly. The rise does not reverse after soot blowing or O2 changes.

**Action:** Trend TMT and ΔP for all passes on the same chart, normalised to the same pass flow. Increase pass flow on the affected pass if hydraulics allow. Forecast when the hottest TMT will reach 600 °C or ΔP 8.4 bar and plan a decoke per Maintenance Procedure — Mechanical Pigging Decoke of H-101 Coil, Rev 2.7.

### 2.2 Flame Impingement / Burner Maldistribution

**Description:** A long, lazy or leaning flame from one of B-101A–H — plugged or eroded gas tip, damaged burner tile, misset air register, low burner-level O2 or a heavy fuel gas — licks the tubes and raises local flux far above the 1.8 × average design peak. Flame shape also changes after a fan or APH-rotor trip: in natural-draft operation (XS-1341 or XS-1351 = 0, firing clamped to ≤ 60%) the burners receive cold air through the D-102 emergency air doors at low windbox pressure, and flames lengthen.

**Diagnosis:** Usually **one** TC rises (the one nearest the burner), sometimes fast (minutes to hours). PDI-110x on that pass is unchanged; other passes normal. Often accompanied by rising CO (AT-1322) at a "normal" AIC-1321, a change in AT-1203 heating value, or a recent burner adjustment. Visual check confirms.

**Action:** Correct the burner per Maintenance Procedure — Burner Inspection, Cleaning and Tuning, Rev 2.0. Restore true burner O2 (see Troubleshooting Guide — Low Excess O2 / High CO, Rev 2.5). Reduce firing on the offending burner until fixed.

### 2.3 High Firing — Throughput, Crude or Efficiency Loss

**Description:** All tubes run hotter when more heat is released: higher charge FY-1100, a lower inlet temperature TT-1100, or an efficiency loss forcing more firing. On H-101 the efficiency losses that matter are convection fouling, air preheater fouling or seal leakage, tramp air and bypass damper leakage. A heavier crude does **not** automatically need more duty at 360 °C (it vaporizes less, so needs less latent heat per tonne, but may arrive colder) — check the model's duty for the new assay rather than assuming; it does coke faster.

**Diagnosis:** **All** passes' TMTs rise together, with bridgewall TT-1301A/B and fuel FT-1201. Coil ΔP unchanged or changing in all passes in proportion to flow. Then look for the efficiency loss: TT-1303 above its ≈ 390 °C baseline (convection fouling, drops after soot blowing); TIC-1345 above ≈ 150 °C with PDT-1347 up (APH fouling); fuel per unit duty up at constant demand.

**Action:** Treat the cause of higher firing: soot blow (Maintenance Procedure — Convection Section Soot Blowing, Rev 1.9), follow Troubleshooting Guide — High Fuel Consumption / Low Efficiency, Rev 2.1 or Troubleshooting Guide — Air Preheater Leakage, Fouling and Low Cold-End Temperature, Rev 1.0, or reduce charge (coordinate with the C-101 operator).

### 2.4 Low Flow or Maldistribution in One Pass

**Description:** A pass carrying less crude has a lower film coefficient and absorbs its share of heat at a higher temperature.

**Diagnosis:** FIC-110x lower than the other passes (or FV-110x wide open and unable to hold setpoint), TT-111x of that pass **higher**, TMT up, PDI-110x **lower** than the other passes. Note the opposite outlet-temperature sign to coke (2.1).

**Action:** Restore pass flow; check FV-110x and the FIC/FT-115x deviation alarm. See Troubleshooting Guide — Pass Outlet Temperature Imbalance, Rev 2.0.

### 2.5 Skin Thermocouple Fault Reading High

**Description:** A skin TC whose shield has burned away, or whose junction lifts into the flue gas, reads toward flue temperature (≈ 845 °C bridgewall) and becomes noisy.

**Diagnosis:** High and erratic, responds to firing changes faster than a tube can, disagrees with its paired TC, PDI-110x flat. IR pyrometry reads much lower.

**Action:** Per Troubleshooting Guide — Suspect Tube Skin Thermocouple Reading, Rev 1.4.

---

## 3. Distinguishing Cause from Symptom

High TMT and rising fuel are **symptoms**. Treating them by cutting firing alone hides the cause.

| What you see | What it means | How to confirm |
|---|---|---|
| Both TCs of one pass up + same-pass PDI-110x up, that pass outlet slightly cooler, TIC-1110 firing harder | Internal coke in that pass | TMT vs ΔP trend at constant pass flow; no recovery after soot blowing |
| One TC up, PDI flat, others normal | Flame impingement or TC fault | Firebox inspection; IR pyrometer; paired TC |
| All passes up + TT-1301A/B up + FT-1201 up | Higher firing (charge, inlet T, efficiency loss) | FY-1100, TT-1100; fuel per duty; TT-1303; TIC-1345 / PDT-1347 |
| One pass TMT and TT-111x up, PDI-110x down | Low flow in that pass | FIC-110x vs other passes; FV-110x output |
| All passes up after crude switch | Crude change altering duty and (heavy crudes) coking rate | Model duty for the assay; SOP — Crude Switch / Crude Blend Change at H-101, Rev 1.8 |
| Long flames after a fan or rotor trip | Natural-draft operation flame shape | XS-1341 / XS-1351 status; firing within the 60% clamp |

---

## 4. Prevention / Follow-up

- Trend each pass's TMT against its PDI-110x weekly; diverging pairs flag either coke (both rising) or a failed TC (TMT flat while ΔP rises).
- IR pyrometer survey of all four passes monthly and after any TMT alarm (SOP — H-101 Daily Operator Rounds and Firebox Inspection, Rev 2.1).
- Keep true burner O2 at design and do not run long flames to gain firing; firing limit ≤ 46 MW LHV (120% of normal).
- Keep the convection section and E-102 clean: a fouled heat-recovery train forces more radiant firing and higher TMTs.
- Expect faster TMT rise on heavier crudes; reforecast run length after every crude switch.
