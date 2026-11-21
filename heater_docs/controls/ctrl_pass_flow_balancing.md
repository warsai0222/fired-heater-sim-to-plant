---
doc_id: ctrl_pass_flow_balancing
doc_type: controls
equipment: [pass_flow_control, radiant_coil, convection_section, bms_sis, transfer_line, crude_charge_pumps]
tags: [FY-1100, PT-1100, TT-1100, FIC-1101, FIC-1102, FIC-1103, FIC-1104, FT-1151, FT-1152, FT-1153, FT-1154, TT-1111, TT-1112, TT-1113, TT-1114, TIC-1110, PDI-1101, PDI-1102, PDI-1103, PDI-1104, TI-1121A, TI-1121B, TI-1122A, TI-1122B, TI-1123A, TI-1123B, TI-1124A, TI-1124B, TT-1131, TT-1132, TT-1133, TT-1134]
title: Control Narrative — Pass Flow Control and Pass Balancing
revision: 2.1
date: 2026-11-20
---

# Control Narrative — Pass Flow Control and Pass Balancing

**Document No.:** H101-CTRL-003
**Revision:** 2.1 | **Date:** 2026-11-20
**Applicability:** Unit 100 — H-101 Crude Charge Heater
**Owner:** Process Control Engineer
**P&ID Reference:** U100-PID-101 (process coil)
**Revision note:** Rev 2.1 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).

---

## 1. Purpose

Crude from the preheat train (fed by charge pumps P-101A/B) enters the H-101 inlet header (PT-1100,
11.0 barg; TT-1100, 250 °C) and is split into four passes, A–D. Each pass has its own flow
controller and control valve so that:

1. Every pass gets enough flow to protect its tubes from overheating and coking (minimum velocity).
2. The four pass outlet temperatures TT-1111..1114 can be balanced around the COT target.
3. The total charge FY-1100 is held at the unit target while individual passes are trimmed.

## 2. Loops and Final Elements

| Pass | Controller | Valve | Fail position | SIS transmitter | Coil inlet P | Outlet T |
|------|------------|-------|---------------|-----------------|--------------|----------|
| A | FIC-1101 | FV-1101 | Open | FT-1151 | PT-1101 | TT-1111 |
| B | FIC-1102 | FV-1102 | Open | FT-1152 | PT-1102 | TT-1112 |
| C | FIC-1103 | FV-1103 | Open | FT-1153 | PT-1103 | TT-1113 |
| D | FIC-1104 | FV-1104 | Open | FT-1154 | PT-1104 | TT-1114 |

| Parameter | Value |
|-----------|-------|
| Normal pass flow | 71.5 t/h (286 t/h total, ANS) |
| FIC-1101..1104 alarms | Lo 60 t/h, Hi 80 t/h |
| SIS low-low (FT-1151..1154) | 43 t/h (60% of normal), 2 s delay → main fuel trip |
| FV-1101..1104 normal ΔP | ≈ 2.5 bar (11.0 → 8.5 barg) |
| FV-1101..1104 normal opening | ≈ 55% |
| Valve type | Globe, cage-guided, equal-percentage, 4" body |

The pass flow valves **fail open**: on air or signal failure they go to full flow, because loss of
flow in a fired pass is the most dangerous condition for a fired heater (tube overheating,
rapid coking, rupture). The independent SIS transmitters FT-1151..1154 trip main fuel if any pass
falls below 43 t/h for 2 s; pilots stay lit.

## 3. Total Charge and Pass Distribution (FY-1100)

FY-1100 is the calculated total of the four pass flows (normal 286 t/h, Lo alarm 250 t/h). The
operator enters the total charge target; the pass-distribution block writes each FIC setpoint as
(total target ÷ 4) + pass bias. The four biases are constrained to sum to zero, so trimming one pass
moves the other three slightly in the opposite direction and the total charge is unchanged.

| Constraint on pass biases | Setting |
|---------------------------|---------|
| Maximum bias without engineer approval | ±8% of average pass flow (≈ ±5.7 t/h at 286 t/h) |
| Resulting pass setpoint range at design | ≈ 66–77 t/h |
| Absolute minimum pass setpoint | 60 t/h (FIC Lo alarm; IOW minimum, well above SIS LL 43 t/h) |
| Bias step size | ≤ 1 t/h per move, ≥ 10 min between moves |

## 4. Pass Balancing Practice

Balancing aims for equal **tube conditions**, not only equal outlet temperatures. The DCS deviation
alarms TDA-1111..1114 trigger when a pass outlet differs from the average of TT-1111..1114 by more
than ±6 °C. Before trimming a pass flow in response:

1. Check the pass's skin thermocouples (TI-1121A/B, TI-1122A/B, TI-1123A/B, TI-1124A/B) and coil ΔP
   (PDI-1101..1104). A pass with high TMT **and** rising ΔP is coking.
2. Check the crossover temperatures TT-1131..1134. A low crossover on one pass points to a
   convection-side cause or a flow measurement error, not a radiant problem.
3. Check the firebox for uneven flames on the side wall serving that pass (passes A/B share one
   wall, C/D the other).
4. Compare FIC-110x with the SIS transmitter FT-115x for the same pass. A deviation above 5% means
   one transmitter is wrong; balancing on a wrong flow reading moves the problem rather than fixing
   it.

## 5. Why Cutting Flow to a Hot Pass Is the Wrong Move

The intuitive response to a hot pass (high TT-111x, or high TMT) is to raise its flow; the intuitive
response to a cold pass is to cut its flow. Cutting flow is the risky one:

- A coked pass absorbs less heat (the coke insulates), so its outlet can read **cold** even though
  its tube wall is **hot**. Reducing flow to bring its outlet up to average lowers the velocity,
  raises the film temperature, and accelerates coking in exactly the pass that is already coked —
  a runaway.
- Coking is a threshold process: rate rises steeply with film temperature and with residence
  time. Lower velocity raises both.
- Lower flow in a pass also raises its outlet vaporization, which changes its share of the coil ΔP
  and can mask the ΔP signature of coke.

Rules: never reduce a pass below 60 t/h to balance outlet temperatures; when a pass shows high TMT
with rising ΔP, increase its flow (within the ±8% bias limit) and accept an outlet temperature
below average, and raise the issue for engineering review. The coking signatures are described in
Equipment Datasheet — H-101 Radiant Coil and Tubes, Rev 2.1.

## 6. Hydraulics and Loss of Control Margin

As a pass cokes, its ΔP (PDI-1101..1104, clean 6.0 bar, Hi 7.8, HH 8.4 bar) rises and its FIC opens
FV-110x further to hold flow. The FV absorbs the extra ΔP until it reaches ≈ 90% open; beyond that
the pass flow can no longer be held and falls toward the Lo alarm and then the SIS LL. The 8.4 bar
HH alarm (≈ 40% above clean) is set with this hydraulic limit in mind. A falling inlet header
pressure PT-1100 (Lo alarm 9.0 barg, e.g. from a charge-pump problem at P-101A/B) erodes the same
margin on all four passes at once. Response: Troubleshooting Guide — Rising Coil Pressure Drop,
Rev 1.9.

## 7. Crude Changes and Charge-Rate Changes

Different crudes change density, vaporization and coking tendency, so pass biases set on one crude
are not automatically right on the next. During a crude switch hold biases at zero unless a pass
is known to be limiting, then re-balance after conditions settle (typically 2–4 h). Heavy,
high-MCR/asphaltene crude (e.g. Kearl) makes the minimum-velocity rule more important. Charge-rate
changes are made on the total target, not on individual passes, in steps of ≤ 5 t/h, and are agreed with the C-101 operator because they change
transfer-line vaporization and column loading. See SOP — Crude Switch / Crude Blend Change at H-101,
Rev 1.8.

After an FD fan, ID fan or APH-rotor stop the heater runs on natural draft at ≤ 60% firing and can
absorb only ≈ 50–55% of design duty. Holding 360 °C would need a charge well below the 240 t/h
minimum (4 × 60 t/h FIC Lo alarm), so pass flows are **not** cut below 60 t/h to hold COT: the total
charge is reduced on the FY-1100 target (biases held) to the rate agreed with the C-101 operator, and
COT is allowed to fall, with C-101 adjusting for the lower flash-zone vaporization (SOP — FD / ID
Fan Trip Response and Natural-Draft Operation, Rev 1.0).

## 8. Alarm and Trip Summary

| Tag(s) | Setpoint | Type |
|--------|----------|------|
| FY-1100 | Lo 250 t/h | Operator alarm |
| FIC-1101..1104 | Lo 60 / Hi 80 t/h | Operator alarm |
| FT-1151..1154 | LL 43 t/h, 2 s | **SIS main fuel trip** |
| FT-115x vs FIC-110x | 5% deviation | Operator alarm |
| TT-1111..1114 | Lo 352 / Hi 368 °C | Operator alarm |
| TDA-1111..1114 | ±6 °C from pass average | Operator alarm |
| PDI-1101..1104 | Hi 7.8 / HH 8.4 bar | Operator alarm only (no trip) |
| PT-1100 | Lo 9.0 barg | Operator alarm |

Authoritative values: Alarm and Trip Setpoint Register — H-101 Crude Charge Heater, Rev 3.1.
