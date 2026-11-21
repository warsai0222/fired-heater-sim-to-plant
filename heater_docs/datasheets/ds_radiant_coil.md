---
doc_id: ds_radiant_coil
doc_type: datasheet
equipment: [radiant_coil, radiant_section, heater_h101, transfer_line]
tags: [TI-1121A, TI-1121B, TI-1122A, TI-1122B, TI-1123A, TI-1123B, TI-1124A, TI-1124B, PDI-1101, PDI-1102, PDI-1103, PDI-1104, PT-1101, PT-1102, PT-1103, PT-1104, PT-1110, TT-1111, TT-1112, TT-1113, TT-1114, TIC-1110, TT-1301A, TT-1301B]
title: Equipment Datasheet — H-101 Radiant Coil and Tubes
revision: 2.1
date: 2026-11-20
---

# Equipment Datasheet — H-101 Radiant Coil and Tubes

**Document No.:** H101-DS-002
**Revision:** 2.1 | **Date:** 2026-11-20
**Applicability:** Unit 100 — H-101 Crude Charge Heater
**Owner:** Fixed Equipment (Mechanical Integrity) Engineer
**P&ID Reference:** U100-PID-101 (process coil)
**Revision note:** Rev 2.1 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).

---

## 1. Description

The H-101 radiant coil is four parallel passes (A–D) of horizontal tubes arranged along the two side
walls and the hip/roof of the cabin firebox. Passes A and B are on one side wall, passes C and D on
the other, so each side wall sees the same burner row (B-101A–H) on the firebox centreline. Each
pass enters the radiant section from the external crossover (crossover temperature TT-1131..1134,
≈ 292 °C) at the hip/roof tubes and flows downward along the side wall, leaving at the lowest wall
tube to the outlet header and transfer line (COT TIC-1110, 360 °C). The outlet tubes therefore carry
the hottest, most vaporized fluid in the coil.

## 2. Tube Data

| Parameter | Value |
|-----------|-------|
| Number of tubes | 80 (20 per pass): 56 wall tubes (28 per side wall) + 24 hip/roof tubes (12 per side) |
| Tube size | 6" NPS Sch 40: OD 168.3 mm, wall 7.11 mm, ID 154.1 mm |
| Material | 9Cr-1Mo, ASTM A335 P9 (seamless) |
| Effective (fired) length | 18.3 m per tube; ≈ 362 m of tube per pass |
| Tube spacing | 305 mm centre-to-centre (≈ 1.8 × OD), single row, 1.5 × OD from wall |
| Return bends | Welded long-radius (1.5D) 180° bends, ASTM A234 WP9, in header boxes at both ends |
| Tube supports | Cast 25Cr-20Ni intermediate wall hangers at ≈ 6 m spacing |
| Radiant surface area | ≈ 766 m² (outside) |
| Corrosion allowance | 3.0 mm |
| Design pressure (elastic) | 20 barg |
| Design pressure (rupture, API 530) | 10 barg |
| Design metal temperature | 630 °C |
| Design life (API 530 rupture) | 100,000 h |
| Hydrotest pressure | 30 barg |

## 3. Process-Side Design Conditions (ANS, 50,000 bbl/d, clean)

| Parameter | Value | Tag |
|-----------|-------|-----|
| Pass flow | 71.5 t/h | FIC-1101..1104 |
| Mass flux | ≈ 1,065 kg/m²·s per pass | — |
| Inlet liquid velocity | ≈ 1.6 m/s (ρ ≈ 680 kg/m³ at 300 °C) | — |
| Coil inlet pressure | 8.5 barg | PT-1101..1104 |
| Coil outlet pressure | 2.5 barg | PT-1110 |
| Coil ΔP, clean (start of run) | ≈ 6.0 bar per pass | PDI-1101..1104 |
| Pass outlet temperature | 360 °C | TT-1111..1114 |
| Radiant duty | ≈ 26 MW (≈ 6.5 MW per pass; ≈ 74% of absorbed) | — |
| Average flux | ≈ 34 kW/m² (26 MW / 766 m²) | — |
| Peak flux (peak/average) | ≈ 61 kW/m² (≈ 1.8) | — |
| Hottest-tube TMT, clean (SOR) | ≈ 430 °C | TI-1121A..1124B |

With hot combustion air from the air preheater E-102 (≈ 300 °C) the firebox runs hotter than in the
Rev A natural-draft design (bridgewall TT-1301A/B ≈ 845 °C vs ≈ 800 °C), so the radiant section now
takes ≈ 74% of the absorbed duty and the average flux and clean TMT are slightly higher. A loss of
air preheat (APH fouling, natural-draft operation) moves duty back toward the convection section.

Most of the clean ΔP is generated in the two-phase section near the outlet, where vaporization
accelerates the flow. Coil ΔP is therefore sensitive to both coke thickness (bore restriction) and
outlet vaporization (crude type, COT and outlet pressure).

## 4. Tube Metal Temperature Limits

| Limit | Value | Basis |
|-------|-------|-------|
| Clean SOR hottest-tube TMT | ≈ 430 °C | Design calculation (Rev B flux) |
| TMT High alarm | 585 °C | Operator alarm, TI-1121A..1124B |
| TMT operating limit (HH alarm) | **600 °C** | P9 operating limit / end-of-run criterion — alarm only, **not a trip** |
| Design metal temperature | 630 °C | API 530 rupture design |
| P9 oxidation limit (API 530 reference) | ≈ 705 °C | Not an operating target |

The 600 °C operating limit leaves margin below the 630 °C design metal temperature for skin
thermocouple uncertainty and for tubes hotter than the two measured locations per pass. Operation
above 600 °C consumes creep life rapidly and is governed by Integrity Operating Windows (IOW) —
H-101 Radiant Coil, Rev 2.1.

## 5. Tube Skin Thermocouples

| Tag | Pass | Location |
|-----|------|----------|
| TI-1121A / TI-1121B | A | Hot zone upper / hot zone lower |
| TI-1122A / TI-1122B | B | Hot zone upper / hot zone lower |
| TI-1123A / TI-1123B | C | Hot zone upper / hot zone lower |
| TI-1124A / TI-1124B | D | Hot zone upper / hot zone lower |

| Parameter | Value |
|-----------|-------|
| Type | Type K, mineral-insulated, Inconel 600 sheath, 6 mm |
| Attachment | Weld-pad (knife-edge) at tube crown facing the burners, with radiation shield |
| Routing | Along tube to wall penetration, slack loop for thermal expansion |
| Accuracy | ±2.2 °C or ±0.75% (Type K, standard limits) plus installation error |

Two measured locations per pass cannot see every tube. The thermocouples are placed in the zone of
highest predicted flux × fluid temperature, but the model's true hottest tube may be elsewhere.
A detached or poorly attached weld pad loses contact with the tube wall and usually reads **low**: the
junction is then cooled by the radiation shield and lead wire and no longer follows the tube metal,
so a real TMT rise can be hidden. A skin thermocouple that stops rising while the coil ΔP
of the same pass keeps rising should be treated as suspect — see Troubleshooting Guide — Suspect
Tube Skin Thermocouple Reading, Rev 1.4, and Maintenance Procedure — Tube Skin Thermocouple
Inspection and Replacement, Rev 1.6.

## 6. Coking Behaviour and Run-Length Signatures

Coke forms on the inside wall of the hottest tubes, where the oil film temperature is highest.
Coke is an insulating layer: for the same heat flux, the tube wall must run hotter to push heat
through it, and the layer narrows the bore. The two radiant-coil signatures of coking therefore
move **together**:

- Skin TMT (TI-1121A..1124B) rises gradually at constant COT and charge rate.
- Coil ΔP (PDI-1101..1104) rises in the same pass.
- The coked pass absorbs slightly **less** heat, so its outlet (TT-1111..1114) runs slightly
  **cooler** than the others, and TIC-1110 fires the whole box harder to hold the mixed COT.

A TMT rise without a ΔP rise points to a flux change (firing, flame pattern, lower pass flow) or an
instrument problem rather than coke. A ΔP rise without a TMT rise can be a vaporization change
(crude, COT, outlet pressure PT-1110) or a coked pass whose skin thermocouple is unreliable.

Coking is a threshold process: below a critical film temperature it is slow, above it the rate
rises steeply. Higher film temperature (higher flux, higher COT, coke already present) and lower
velocity (reduced pass flow, longer residence time) both raise the rate. Reducing the flow of a
hot pass to "balance" outlet temperatures therefore accelerates its coking — see Control Narrative
— Pass Flow Control and Pass Balancing, Rev 2.1.

End of run is reached when either the hottest TMT reaches 600 °C or coil ΔP reaches 8.4 bar
(≈ 40% above clean), whichever comes first. Lowering COT to extend the run is a production decision,
not a coil decision: it reduces C-101 flash-zone vaporization and shifts distillate into residue, so
it is agreed with the C-101 operator. Decoking is by mechanical pigging per Maintenance
Procedure — Mechanical Pigging Decoke of H-101 Coil, Rev 2.7.

## 7. Coil ΔP Instrumentation

| Tag | Measurement | Normal | Hi alarm | HH alarm |
|-----|-------------|--------|----------|----------|
| PDI-1101 | Pass A: PT-1101 minus PT-1110 | 6.0 bar | 7.8 bar | 8.4 bar |
| PDI-1102 | Pass B: PT-1102 minus PT-1110 | 6.0 bar | 7.8 bar | 8.4 bar |
| PDI-1103 | Pass C: PT-1103 minus PT-1110 | 6.0 bar | 7.8 bar | 8.4 bar |
| PDI-1104 | Pass D: PT-1104 minus PT-1110 | 6.0 bar | 7.8 bar | 8.4 bar |

The ΔP is calculated from pressure transmitters, so it includes the convection coil, crossover and
radiant coil of the pass. All ΔP alarms are operator alarms; none trips the heater. Because ΔP
varies roughly with the square of flow, compare ΔP at the same pass flow (FIC-1101..1104) and crude.
