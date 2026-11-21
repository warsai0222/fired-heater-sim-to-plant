---
doc_id: safe_firebox_entry
doc_type: safety
equipment: [radiant_section, convection_section, radiant_coil, burners, fuel_gas_system, pilot_gas_system, snuffing_steam, soot_blowers, air_preheater, fd_fan, id_fan, bypass_dampers, stack, bms_sis, heater_h101]
tags: [HS-1290, HS-1501, PI-1403, PIC-1202, PT-1208, TT-1301A, TT-1301B, XS-1341, XS-1351, XS-1349, ZT-1361, ZT-1362, TT-1343, TIC-1345, FIC-1341]
title: Safety Procedure — Firebox and Header Box Entry (Confined Space)
revision: 1.7
date: 2026-11-20
---

# Safety Procedure — Firebox and Header Box Entry (Confined Space)

**Document No.:** H101-SAF-004
**Revision:** 1.7 | **Date:** 2026-11-20
**Applicability:** Unit 100 — H-101 Crude Charge Heater — radiant firebox, convection section, header boxes, air preheater E-102, flue and air ducts, fan housings K-101/K-102 and S-101 stack base
**Owner:** Unit 100 Operations / Site HSE
**P&ID reference:** U100-PID-101 (process coil isolation), U100-PID-102 (fuel gas, pilot gas, snuffing steam, soot blowing), U100-PID-103 (APH, fans, ducts, dampers, stack)

**Revision note:** Rev 1.7 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).

> **SAFETY WARNING:** The H-101 firebox, convection section, header boxes, air preheater, flue/air ducts and fan housings are permit-required confined spaces. Hazards include fuel gas or hydrocarbon release, oxygen deficiency from snuffing or purge steam, carbon monoxide, hydrogen sulfide, pyrophoric iron sulfide, rotating machinery (fans and APH rotor), acidic deposits, heat stress, falling refractory and ceramic fibre dust. No person may enter without a valid confined space entry permit, completed isolation certificate and continuous gas monitoring.

---

## 1. Scope

This procedure covers entry into the H-101 radiant firebox, convection section, header boxes, the E-102 regenerative air preheater (gas and air hoods, rotor baskets), flue gas and combustion air ducts, the K-101 and K-102 fan housings, and the S-101 stack base. It applies to decoking (Maintenance Procedure — Mechanical Pigging Decoke of H-101 Coil, Rev 2.7), skin thermocouple work (Maintenance Procedure — Tube Skin Thermocouple Inspection and Replacement, Rev 1.6), APH seal inspection and washing (Maintenance Procedure — Air Preheater Seal Inspection, Soot Blowing and Water Washing, Rev 1.0), burner work and refractory or tube inspection.

---

## 2. Energy Isolation Before Entry

All process isolations are positive (blinds or removed spools), not valves alone. A closed SIS valve is not an entry isolation. Rotating equipment is locked out at the MCC and mechanically secured.

| System | Isolation | Verification |
|---|---|---|
| Main fuel gas | XV-1201/XV-1202 closed, XV-1203 open, PV-1202 closed; spectacle blind at burner manifold inlet closed; manifold vented | PIC-1202 0.0 barg, local gauge zero |
| Pilot gas | XV-1209 closed; pilot header blinded and vented | PT-1208 0.0 barg |
| Process coil | Crude drained and steamed out; pass spectacle blinds XV-1105A..D / XV-1106A..D closed | Low-point drains open, no flow |
| Firebox / header box snuffing steam | XV-1401 and HV-1402 closed, locked, blinded | PI-1403 header isolated from heater branches |
| Soot blowers | HS-1501 sequencer disabled and locked; SB-101A..F and SB-102A/B steam supply isolated; blower motors isolated | Sequencer at step 0, MCC tags |
| FD fan K-101 | Motor isolated and locked at MCC; VFD SC-1341 isolated and discharged; shaft locked against windmilling | XS-1341 = 0, MCC lock, zero-speed check at the coupling |
| ID fan K-102 | Motor isolated and locked at MCC; VFD SC-1351 isolated and discharged; shaft locked against windmilling (stack draft can turn an unlocked impeller) | XS-1351 = 0, MCC lock, zero-speed check |
| APH E-102 rotor | Main and auxiliary drives isolated and locked; rotor pinned or brake applied | XS-1349 = 0 and local check that the rotor is stationary |
| Natural-draft path | D-101 bypass damper XV-1361 and D-102 emergency air doors XV-1362 driven open, actuator air isolated, blades mechanically locked open | ZT-1361 and ZT-1362 ≥ 95% and local indicators |
| APH cold-air bypass | TV-1345 isolated in its as-left position | — |
| BMS-101 | HS-1290 pressed and held tripped; BMS in maintenance mode with lock | BMS display: total trip |

XV-1361 and XV-1362 are locked open so the firebox has a natural ventilation path from the burner windbox to S-101, and so that a blade cannot fall closed and trap fumes. For entry into E-102 or the ducts between E-102 and K-102, add blinds or locked-closed isolation dampers so that stack draft through the open bypass does not pull flue gas back into the work area; the entry supervisor confirms the flow path on U100-PID-103 before signing.

---

## 3. Cool-down and Ventilation

1. After shutdown, the ID fan K-102 may be left running on low speed (and K-101 for air supply) to force-cool the firebox, convection section and E-102. Keep the APH rotor turning until TT-1343 and TIC-1345 are close to ambient: a stopped hot rotor cools unevenly and retained deposits can smoulder.
2. Once cooled, stop the fans and rotor and apply the Section 2 lockouts **before** anyone enters. No fan may run while personnel are inside any part of the flue or air path.
3. Bridgewall TT-1301A/B below 60 °C and local air temperature at the entry point below 40 °C before entry; between 32 °C and 40 °C a heat-stress work/rest regime applies. APH baskets retain heat longer than the firebox: check temperature locally at the work face.
4. With fans locked out, ventilate with portable air movers (air, never oxygen). The open D-102 air doors and D-101 bypass give a natural through-flow for the firebox; header boxes, APH hoods and duct sections need forced ventilation.

---

## 4. Atmospheric Testing

Gas testing is by a certified gas tester, first from outside the opening and then at each work level (burner floor, mid-height, arch; APH hot end and cold end). Repeated before every entry after a break; continuous during work (personal monitors on every entrant).

| Parameter | Acceptance for entry |
|---|---|
| Oxygen | 19.5 – 23.5 vol% |
| Flammables | < 10% LEL (0% LEL for hot work) |
| Carbon monoxide | < 25 ppm |
| Hydrogen sulfide | < 1 ppm |

Steam leaking through isolations can displace oxygen; any O2 reading below 19.5% is an immediate evacuation regardless of cause.

---

## 5. Specific Hazards Inside H-101 and E-102

- **Pyrophoric iron sulfide:** forms on coil and header internals, especially after high-sulfur crudes such as Kearl (3.8 wt% sulfur). Keep exposed internals wet; treat smouldering deposits as a fire.
- **Coke and pigging debris:** sharp and may contain hydrocarbon; bag and remove first.
- **Falling refractory and deposits:** inspect arch and convection corbels from the floor before work; barricade below loose refractory.
- **Ceramic fibre insulation:** half-face respirator with P3 filters and disposable coveralls when disturbing modules.
- **Convection section:** studded tubes are an abrasion and fall hazard; work from scaffold only.
- **APH element baskets:** thin corrugated steel plates have sharp edges; cut-resistant gloves and sleeves. Do not stand on baskets; use boards across the rotor.
- **APH cold-end deposits:** the cold end operates near the acid dew point; deposits contain sulfates and condensed sulfuric acid and become strongly acidic when wet. After water washing, residual wash water is acidic. Wear acid-resistant gloves, goggles and face shield; test deposit pH before handling.
- **APH fire residue:** after any APH fire or rotor-stop event, deposits may still smoulder inside baskets. A fire watch with water hose stays at the APH access during entry.
- **Fan housings and ducts:** impeller blades can move under gravity or draft even with the motor isolated, hence the shaft lock. Ducts may have unsupported floors and accumulated ash.

---

## 6. Permit, Attendant and Rescue

1. Confined space entry permit signed by the area authority, isolation authority and entry supervisor, with the isolation certificate (including MCC lockouts for K-101, K-102 and the E-102 drives) attached.
2. A trained attendant at each entry point, in radio contact with the control room and entrants, with a log of all persons inside.
3. A written rescue plan with the rescue team on standby; rescue equipment (tripod or davit for the arch and APH hoods, stretcher for the burner floor) staged at the opening.
4. The board operator places a "personnel in firebox / APH" banner on the H-101 DCS graphics and must not operate any H-101 valve, damper, fan or drive without the entry supervisor's agreement.

---

## 7. Close-out and Return to Service

Before the permit is closed: headcount against the attendant log, tools and boards removed from the rotor and ducts, access doors closed, blinds removed in reverse order, BMS maintenance lock removed, fan and APH drive lockouts removed, and the APH rotor turned one full revolution on the auxiliary drive to confirm it is free. Return to service follows SOP — H-101 Cold Start-up, Purge and Burner Light-off, Rev 3.2, including the 5-volume-change purge with a proven purge path (both fans running, or bypass and air doors proven open) and air flow FIC-1341 ≥ 25% of design, per BMS / SIS Cause and Effect — H-101, Rev 3.3.
