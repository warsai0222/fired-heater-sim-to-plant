---
doc_id: mnt_tramp_air_survey
doc_type: maintenance
equipment: [heater_h101, radiant_section, convection_section, burners, air_preheater, id_fan, fd_fan, bypass_dampers, stack, flue_gas_analyzers]
tags: [AIC-1321, AT-1327, AT-1326, AT-1322, PIC-1311, PT-1312, PT-1313, PT-1352, FIC-1341, SI-1341, SI-1351, JI-1351, ZT-1361, ZT-1362, TT-1303, TIC-1345, FT-1201, AT-1203]
title: Maintenance Procedure — Tramp Air Survey and Casing Sealing
revision: 1.5
date: 2026-11-20
---

# Maintenance Procedure — Tramp Air Survey and Casing Sealing

**Document No.:** H101-MNT-003
**Revision:** 1.5 | **Date:** 2026-11-20
**Revision note:** Rev 1.5 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).
**Applicability:** Unit 100 — H-101 Crude Charge Heater (radiant section, convection section, header boxes, flue ducts to the ID fan)
**Owner:** Process Engineering (Fired Heaters) / Fixed Equipment Maintenance
**P&ID Reference:** U100-PID-102 (combustion, fuel gas, burners, BMS), U100-PID-103 (air preheater, fans, ducts, dampers)
**Frequency:** Annually, and when triggered (Section 2)

---

## 1. Scope and Purpose

H-101 is a balanced-draft heater. The ID fan K-102 holds the arch at −2.5 mmH2O (PIC-1311), so the whole flue gas path is below atmospheric pressure: floor ≈ −10 mmH2O (PT-1312), convection outlet / APH gas inlet ≈ −20 mmH2O (PT-1313), and ≈ −120 mmH2O at the ID fan inlet (PT-1352). Any opening on the gas side draws in ambient air — **tramp air**. The combustion-air side (FD discharge, APH air side, windbox) is above atmospheric, so leaks there blow hot air **out** rather than in.

Tramp air:
- **below the arch** is counted by AIC-1321, so the O2 loop delivers less FD air: AIC-1321 shows 3.0% while the burners run with less air — CO (AT-1322) and flame length rise;
- **in the convection section** raises AT-1327 above AIC-1321 and cools the gas before the convection tubes and APH;
- **in the APH gas-side casing and the ducts to the ID fan** raises AT-1326 above AT-1327 — the same signature as APH seal leakage — and loads the ID fan.

Every kilogram of tramp air is heated for no useful duty and must be moved by the ID fan, so it costs fuel and fan power (JI-1351). This procedure locates leaks by inspection and O2 profiling and seals them. APH seal leakage itself is covered by Maintenance Procedure — Air Preheater Seal Inspection, Soot Blowing and Water Washing, Rev 1.0.

## 2. Survey Triggers

1. AT-1327 − AIC-1321 above 0.8% (normal ≈ 0.2%) for more than a week.
2. AT-1326 − AT-1327 above 2.0% (normal ≈ 1.2%) where the APH leakage test does not account for the rise.
3. A result in SOP — Excess O2 Step Test (Analyzer / Air-Ingress Check), Rev 1.3 indicating tramp air below the arch or convection ingress.
4. Fuel heat input FT-1201 × AT-1203, or ID fan speed SI-1351, above the model expectation with the analyzers validated.
5. After any outage in which header boxes, peephole doors, casing panels, duct joints or the APH casing were opened.

## 3. Why Draft Matters — Leakage Scales With √Draft

Air leakage through a fixed opening behaves like flow through an orifice: **leak flow ∝ opening area × √(suction at that point)**.

1. Doubling the arch suction raises leakage through every firebox leak by about 40% (√2). With the ID fan, the arch draft is now a setpoint choice; the target is the least negative arch draft that stays safely negative (Per Control Philosophy — Excess O2 and Arch Draft Control, Rev 2.5). Over-drafting "to be safe" wastes fuel and fan power.
2. The same hole leaks more where suction is higher. Suction rises steadily through the convection section and APH to the ID fan inlet, so a small gap in an APH casing or duct expansion joint near the ID fan can pass as much air as a much larger opening on the firebox.

## 4. Inspection Checklist (on-line)

Walk the heater and ducts with a calibrated IR camera or thermometer and a smoke pencil. On the gas side, leaks show as **cool spots** and smoke drawn inward; on the air side, as **hot spots** and air blowing out.

| Location | Side | What to check |
|---|---|---|
| Peephole doors (side walls, arch ports) | Gas | Door latches, seat not warped, gasket present, closed after viewing |
| Burner fronts B-101A..H | Gas / air interface | Sight ports closed; pilot and igniter penetrations sealed; burner-to-floor seal intact |
| Header boxes | Gas | Doors bolted, gaskets present, no smoke-pencil draw at seams |
| Tube penetrations | Gas | Sleeve seals and packing intact |
| Casing panels and seams | Gas | Weld seams, expansion joints, cracked panels, missing bolts |
| Soot blower wall boxes SB-101A..F, SB-102A/B | Gas | Wall-box seals, poppet valves seat when retracted |
| APH gas-side casing, ducts and expansion joints to K-102 | Gas (high suction) | Cool spots, fabric expansion joint tears, inspection doors |
| D-101 bypass damper (closed) | Gas | Blade seals and shaft gland; ZT-1361 at 0% |
| Windbox, D-102 emergency air doors, FD ducts | Air (positive) | Hot air escaping at door seals, joints; ZT-1362 at 0% |

Mark each suspected leak with a numbered tag and photograph it.

## 5. Flue Gas O2 Profiling

With a calibrated portable O2 analyzer (dry basis), heater steady at reference charge and PIC-1311 at −2.5 mmH2O:

1. Arch sample point: confirm agreement with AIC-1321 (±0.3%).
2. Burner-level and mid-height peephole ports on each side wall (probe 300 mm in, port sealed around the probe).
3. APH gas inlet sample point: confirm agreement with AT-1327.
4. APH gas outlet sample point (before the ID fan) and compare with AT-1326 at the stack.

| Pattern | Indicates |
|---|---|
| Mid-height O2 noticeably above burner level | Leak between burners and arch |
| AT-1327 well above arch O2 | Convection section leak (header boxes, wall boxes, casing) |
| APH outlet O2 ≈ AT-1326, both well above AT-1327 | Gain is across the APH — seal leakage or APH casing |
| APH outlet O2 close to AT-1327 + normal APH gain, AT-1326 much higher | Duct or ID fan in-leakage after the APH |
| O2 high near one peephole only | Local leak at that port |
| Arch ≈ AIC-1321, AT-1327 ≈ arch + 0.2%, AT-1326 ≈ AT-1327 + 1.2% | No significant tramp air |

## 6. Sealing

| Repair | When |
|---|---|
| Close and re-latch doors; replace peephole gaskets | On-line, immediately |
| Ceramic fibre rope and high-temperature sealant at penetrations and seams | On-line where accessible and below 100 °C surface; otherwise at outage |
| Header-box gaskets, casing panels, duct expansion joints, APH casing | Outage (Per Safety Procedure — Firebox and Header Box Entry (Confined Space), Rev 1.7) |
| Damper shaft packing D-101 | On-line with damper held closed |

## 7. Post-Sealing Verification and Records

1. Repeat the O2 profile; record AIC-1321, AT-1327, AT-1326, FIC-1341, SI-1341, SI-1351, JI-1351, TT-1303, TIC-1345 and FT-1201 × AT-1203 at reference charge.
2. Expected: after sealing **below-arch** leaks, FIC-1341 and SI-1341 rise slightly for the same 3.0% O2 (more air now goes through the burners) and AT-1322 falls; after sealing **convection or duct** leaks, AT-1327 − AIC-1321 or AT-1326 − AT-1327 falls and SI-1351 / JI-1351 fall. Fuel heat input should fall in all cases.
3. File the leak tag list, photos, repairs completed and deferred, and before/after O2 profiles with process engineering.
