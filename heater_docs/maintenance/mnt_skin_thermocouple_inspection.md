---
doc_id: mnt_skin_thermocouple_inspection
doc_type: maintenance
equipment: [radiant_coil, radiant_section, air_preheater]
tags: [TT-1343, TIC-1110, TI-1121A, TI-1121B, TI-1122A, TI-1122B, TI-1123A, TI-1123B, TI-1124A, TI-1124B, TT-1111, TT-1112, TT-1113, TT-1114, TT-1301A, TT-1301B, PDI-1101, PDI-1102, PDI-1103, PDI-1104]
title: Maintenance Procedure — Tube Skin Thermocouple Inspection and Replacement
revision: 1.6
date: 2026-11-20
---

# Maintenance Procedure — Tube Skin Thermocouple Inspection and Replacement

**Document No.:** H101-MNT-005
**Revision:** 1.6 | **Date:** 2026-11-20
**Revision note:** Rev 1.6 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).
**Applicability:** Unit 100 — H-101 Crude Charge Heater, radiant coil skin thermocouples TI-1121A..1124B
**Owner:** Instrument Maintenance / Fixed Equipment Engineering
**P&ID Reference:** U100-PID-101 (process coil)

---

## 1. Scope and Purpose

H-101 has two tube skin thermocouples per pass in the radiant hot zone: TI-1121A/B (Pass A), TI-1122A/B (Pass B), TI-1123A/B (Pass C), TI-1124A/B (Pass D) — "A" upper and "B" lower hot zone. They are the main measurement of coke build-up and are compared against the 585 °C Hi alarm and the 600 °C TMT operating limit for the ASTM A335 P9 tubes (Per Integrity Operating Windows (IOW) — H-101 Radiant Coil, Rev 2.1). A skin TC that reads wrong either hides real overheating or triggers an unnecessary decoke, so each is validated on-line and inspected at every outage. With hot combustion air from the air preheater E-102 the firebox runs hotter (bridgewall ≈ 845 °C) and the average radiant flux is ≈ 34 kW/m², so the clean start-of-run hottest-tube TMT is ≈ 430 °C.

Construction: Type K, mineral-insulated, Inconel 600 sheath, attached to the tube at a pad (knife-edge type) on the fire side, with a heat shield over the junction and the sheath routed along the tube and out through a sealed casing penetration.

## 2. On-Line Validation (Quarterly, and on suspicion)

1. **Consistency check.** At reference charge (286 t/h, COT 360 °C), compare the eight skin TCs. With balanced pass outlet temperatures TT-1111..1114, the upper TCs (A) should agree within about 20 °C pass-to-pass, as should the lower TCs (B).
2. **Trend check.** Skin TCs on a coking tube rise slowly (a few °C per week) and track firing. Readings that jump in steps, spike, go flat, or follow bridgewall temperature TT-1301A/B more closely than firing indicate an attachment or sheath problem. Allow for combustion-side events logged in the DCS: a natural-draft runback (fans or APH rotor stopped) drops firing and air temperature, and APH soot blowing or washing raises hot-air temperature TT-1343 slightly — all eight TCs should move together for these.
3. **Cross-check with ΔP.** A pass whose skin TC rises with no rise in its coil ΔP (PDI-1101..1104) is a candidate for a faulty TC — but not proof. A genuinely coking pass usually also runs a slightly **cooler** pass outlet (TT-1111..1114) than its neighbours, because the coke insulates the tube while TIC-1110 fires harder to hold the combined COT (Per Troubleshooting Guide — Suspect Tube Skin Thermocouple Reading, Rev 1.4).
4. **IR pyrometer survey.** Through the nearest peephole, measure the tube at the TC location with a calibrated short-wave IR pyrometer. Use emissivity 0.85 for oxidised P9 tube, and apply the vendor's background-radiation correction for the hot refractory. Accept agreement within ±20 °C; IR is a sanity check, not a calibration.

| Symptom | Likely cause |
|---|---|
| Reads high, near flue-gas temperature, little response to firing | Junction detached from the tube or heat shield lost — junction "sees" the flue gas |
| Reads low and sluggish | Poor contact at the pad, junction lifted under the shield, or sheath damage with shunting |
| Erratic, open-circuit spikes | Broken conductor, wet or damaged extension at the junction box |
| Sudden step change | Junction failure or re-making contact |

## 3. Outage Inspection (every decoke and turnaround)

Firebox entry is required — Per Safety Procedure — Firebox and Header Box Entry (Confined Space), Rev 1.7.

1. Visually inspect each pad weld, the junction and the heat shield. Record cracking, shield missing, or the sheath pulled away from its clips.
2. Inspect the sheath route: clips in place, no sag into the flame zone, no kinking at the casing penetration.
3. Electrical checks from the junction box with the heater cold: loop resistance (compare with commissioning value, ±10%), insulation resistance at 500 VDC between conductors and sheath ≥ 100 MΩ.
4. Ambient check: with the firebox cold and at uniform temperature, all eight TCs should agree within ±3 °C of a reference thermometer.
5. Check that the casing penetration seal is intact (a leaking penetration is also a tramp-air source).

## 4. Replacement

1. Replacement is done only with the coil drained, gas-free and isolated.
2. Remove the failed assembly; grind the old pad flush and confirm by UT that wall thickness at the location is above the retirement thickness.
3. Weld a new pad per the approved P9 welding procedure specification — P9 requires preheat (typically ≥ 200 °C) and post-weld heat treatment as directed by the WPS and fixed equipment engineering. Perform hardness test and dye penetrant / MT on the attachment weld.
4. Fit the new thermocouple with its junction seated in the pad, install the heat shield, clip the sheath along the original route and re-seal the casing penetration.
5. Repeat the Section 3 electrical and ambient checks and record as-left values.

## 5. Post-Start-up Verification

1. During heat-up, confirm the replaced TC tracks its pass partner and the other passes, per SOP — H-101 Cold Start-up, Purge and Burner Light-off, Rev 3.2.
2. Include the new TC in the post-decoke clean baseline (Per Maintenance Procedure — Mechanical Pigging Decoke of H-101 Coil, Rev 2.7, Section 8). A replaced TC starts a new baseline; do not splice its trend onto the old TC without a note.

## 6. Records

Record for each TC: tag, as-found condition (photo), loop and insulation resistance, ambient reading, IR comparison, replacement details (WPS, PWHT chart, NDE results), and as-left values. Inform process engineering of any replaced TC, because its history in the historian has a discontinuity at the replacement date.
