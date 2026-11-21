---
doc_id: trb_suspect_skin_thermocouple
doc_type: troubleshooting
equipment: [radiant_coil, radiant_section, heater_h101]
tags: [TI-1121A, TI-1121B, TI-1122A, TI-1122B, TI-1123A, TI-1123B, TI-1124A, TI-1124B, PDI-1101, PDI-1102, PDI-1103, PDI-1104, TT-1111, TT-1112, TT-1113, TT-1114, FIC-1101, FIC-1102, FIC-1103, FIC-1104, TT-1301A, TT-1301B, FT-1201, TIC-1110]
title: Troubleshooting Guide — Suspect Tube Skin Thermocouple Reading
revision: 1.4
date: 2026-11-20
---

# Troubleshooting Guide — Suspect Tube Skin Thermocouple Reading

**Document No.:** H101-TRB-009
**Symptom:** A radiant skin TC TI-1121A..TI-1124B reads flat, unusually low, erratic, failed (upscale/downscale), or disagrees with its paired TC on the same pass by more than about 25 °C
**Revision:** 1.4 | **Date:** 2026-11-20
**Applicability:** Unit 100 — H-101 Crude Charge Heater
**Owner:** Fired Equipment Engineering / Instrument Maintenance
**P&ID reference:** U100-PID-101 (radiant coil skin thermocouples)

**Revision note:** Rev 1.4 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).

> **SAFETY WARNING:** A skin TC that reads **low** is more dangerous than one that reads high. A detached TC can show a comfortable 450 °C while the tube beneath it approaches the 600 °C TMT limit. Never accept a low reading as good news until it is validated. While a TC is suspect, TMT monitoring of that pass is degraded and Integrity Operating Windows (IOW) — H-101 Radiant Coil, Rev 2.1 requires substitute monitoring.

---

## 1. Immediate Actions

1. **Flag the TC as suspect** in the DCS and shift log; do not use it alone for TMT alarm response or decoke decisions.
2. **Use the paired TC.** Each pass has two hot-zone skin TCs: TI-1121A/B (pass A), TI-1122A/B (pass B), TI-1123A/B (pass C), TI-1124A/B (pass D). The upper (A) and lower (B) TCs normally track within about 15 °C of each other. Start-of-run hottest TMT with hot combustion air is ≈ 430 °C.
3. **Arrange an IR pyrometer reading** of the tube at the TC location this shift, with emissivity set for scaled 9Cr-1Mo tube and corrected for flame and refractory reflection (the Rev B firebox runs hotter, bridgewall ≈ 845 °C, so reflection errors are larger).
4. **Check coil ΔP** PDI-110x for that pass: if ΔP is rising while the suspect TC is flat, assume the tube is coking and heating up.
5. Until validated, monitor the pass by pyrometry every shift and keep the paired TC below the 585 °C Hi alarm with margin for the uncertainty.

---

## 2. Probable Causes

### 2.1 Detached Thermocouple (Reads Low / Flat)

**Description:** Skin TCs are welded to the tube under a heat shield. If the weld cracks or the pad lifts, the junction loses contact with the tube and reads a mix of shield and gas temperature, usually lower and less variable than the tube.

**Diagnosis:** Reading low or flat; **does not respond to firing changes** (a real skin TC follows a firing change of 5% or more within a few minutes); disagrees increasingly with its paired TC; **disagrees with the coil ΔP trend** — PDI-110x of the same pass rising (coke) while the TC stays flat or falls.

**Action:** Treat as failed. Substitute pyrometry each shift. Replace at the next opportunity per Maintenance Procedure — Tube Skin Thermocouple Inspection and Replacement, Rev 1.6.

### 2.2 Shield Damage or Flame Contact (Reads High / Noisy)

**Description:** If the heat shield burns away or a flame touches the TC lead, the junction sees flue gas radiation (bridgewall ≈ 845 °C) and reads high.

**Diagnosis:** Reading high, noisy, responding to firing changes **faster** than a tube would (seconds rather than minutes), often tracking bridgewall TT-1301A/B; paired TC and PDI-110x normal; pyrometer reads much lower.

**Action:** Check for flame impingement on that tube (a real local hot spot must be excluded). If the tube is not hot, flag as faulty and plan replacement.

### 2.3 Open Circuit or Wiring / Transmitter Fault

**Description:** Broken element, failed compensating cable, wet junction box or transmitter fault.

**Diagnosis:** Reading at burnout value (upscale or downscale), step changes, spikes, or a reading that changes when the junction box is disturbed; diagnostics in the temperature transmitter.

**Action:** Instrument check of loop, junction box and transmitter outside the firebox. Many faults can be fixed on-line.

### 2.4 Real Temperature Change (Not a Fault)

**Description:** The TC is right and the tube really is hotter or cooler than its neighbour: coke in that pass, flame impingement, pass flow change or a burner out.

**Diagnosis:** The reading responds normally to firing; paired TC moves in the same direction; PDI-110x, pass flow FIC-110x and pass outlet TT-111x tell a consistent story (for coke: TMT and ΔP up together and that pass's outlet slightly cooler while TIC-1110 fires harder); pyrometer agrees.

**Action:** Treat as real: follow Troubleshooting Guide — High Tube Metal Temperature, Rev 2.4.

---

## 3. Distinguishing Cause from Symptom

| What you see | What it means | How to confirm |
|---|---|---|
| Flat / low, no response to firing, paired TC rising | Detached TC | Response to firing change; pyrometer |
| Flat TC while same-pass PDI-110x rises | Detached TC hiding a coking tube | ΔP trend; pyrometer; treat tube as hot |
| High, noisy, fast response, tracks bridgewall | Shield damage / flame contact on TC | Pyrometer; visual |
| Burnout value, spikes, steps | Wiring / transmitter fault | Loop check |
| Both TCs and PDI of the pass agree on a rise | Real tube heating | Troubleshooting Guide — High Tube Metal Temperature, Rev 2.4 |

The key cross-check is that **coke raises TMT and coil ΔP together in the same pass**. A skin TC that disagrees with both its paired TC and the ΔP trend is the TC at fault, not the tube.

---

## 4. Prevention / Follow-up

- Monthly IR pyrometer survey of all four passes, compared with TI-1121A..TI-1124B; record differences.
- Weekly check of each TC's response to normal firing changes (charge rate changes, COT setpoint moves, fan-speed changes on the FD/ID fans that alter firebox temperature).
- Inspect and replace damaged TCs and heat shields at every decoke and turnaround.
- Keep a written record of every TC flagged suspect, the substitute monitoring used and the date of repair.
