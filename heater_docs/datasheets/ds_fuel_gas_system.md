---
doc_id: ds_fuel_gas_system
doc_type: datasheet
equipment: [fuel_gas_system, fuel_gas_ko_drum, pilot_gas_system, bms_sis, burners]
tags: [FT-1201, PIC-1202, AT-1203, TT-1204, LT-1205, PT-1206, PT-1207, PT-1208, HS-1290, PT-1314, XS-1341, XS-1351, XS-1349]
title: Equipment Datasheet — Fuel Gas and Pilot Gas System (incl. V-101)
revision: 1.4
date: 2026-11-20
---

# Equipment Datasheet — Fuel Gas and Pilot Gas System (incl. V-101)

**Document No.:** H101-DS-005
**Revision:** 1.4 | **Date:** 2026-11-20
**Applicability:** Unit 100 — H-101 Crude Charge Heater
**Owner:** Unit 100 Process Engineer (process data); Instrument & Controls Engineer (SIS elements)
**P&ID Reference:** U100-PID-102 (combustion, fuel gas, burners, BMS)
**Revision note:** Rev 1.4 — updated for balanced draft and regenerative air preheater (MOC-H101-2026-07).

---

## 1. System Description

Main fuel gas for H-101 is taken from the refinery fuel gas header and passes, in order, through
the fuel gas knock-out drum **V-101**, the fuel gas mass flowmeter **FT-1201**, the SIS double block
valves **XV-1201** / **XV-1202** with the bleed valve **XV-1203** between them, the pressure control
valve **PV-1202**, and the burner manifold feeding B-101A–H. Pilot gas is a separate regulated
supply taken downstream of V-101, with its own SIS shutoff **XV-1209**, feeding the eight continuous
pilots. Fuel gas composition (AT-1203 LHV) and temperature (TT-1204) are measured on the main line.

## 2. Design Fuel Gas

| Component | mol% |
|-----------|------|
| Methane CH4 | 80 |
| Ethane C2H6 | 8 |
| Propane C3H8 | 2 |
| Hydrogen H2 | 8 |
| Nitrogen N2 | 2 |

| Property | Value |
|----------|-------|
| Molecular weight | 16.84 |
| LHV | 816 kJ/mol = **48.5 MJ/kg** (≈ 36.4 MJ/Nm³) |
| Specific gravity (air = 1) | 0.58 |
| Wobbe index (LHV basis) | ≈ 47.8 MJ/Nm³ |
| Stoichiometric air | 9.62 mol air / mol fuel (≈ 16.5 kg/kg) |
| Normal flow | 2,860 kg/h (≈ 3,800 Nm³/h); 38.5 MW LHV fired |
| Temperature at manifold | 40 °C (TT-1204) |
| Pressure at manifold | 1.2 barg (PIC-1202) |

Refinery fuel gas composition varies with unit operations elsewhere in the refinery (hydrogen
and C3+ content in particular). AT-1203 is a continuous calorimeter; its alarm band is 44–52 MJ/kg.
A composition change changes heat release at a given manifold pressure; the COT cascade corrects
it, but fired-duty and efficiency calculations must use the measured LHV, not the design value.

## 3. V-101 Fuel Gas Knock-Out Drum

| Parameter | Value |
|-----------|-------|
| Tag | V-101 |
| Orientation | Vertical, with wire-mesh demister pad |
| Size | 1,200 mm ID × 3,000 mm T/T |
| Design pressure / temperature | 6 barg / 120 °C |
| Material | SA-516 Gr 70, 3 mm CA |
| Level transmitter | LT-1205 (normal 10%, Hi alarm 50%) |
| High-high level | LSHH-1205 at 80% — **SIS main fuel trip** |
| Drain | Manual to closed drain system; steam-traced boot |
| Tracing | Steam tracing on drum and line to burner manifold |

V-101 removes condensed hydrocarbons and water carried in the refinery fuel gas. Liquid carry-over
to the burners causes flame instability, smoky flames, tip plugging and, in the worst case, a
firebox fire; LSHH-1205 therefore trips main fuel. Fuel gas downstream of V-101 should be kept at
least 10–15 °C above its hydrocarbon dew point; tracing failure in cold weather is a common cause
of LT-1205 Hi alarms and burner tip fouling.

## 4. Main Fuel Gas Valves and Instruments

| Tag | Service | Fail position / function |
|-----|---------|-------------------------|
| FT-1201 | Fuel gas mass flow, Coriolis | Normal 2,860 kg/h; Hi alarm 3,430 kg/h (≈ 120% heat release, ≈ 46 MW LHV) |
| XV-1201 | Main fuel gas upstream block (SIS) | Fail closed |
| XV-1202 | Main fuel gas downstream block (SIS) | Fail closed |
| XV-1203 | Bleed vent between XV-1201/1202 to safe location (SIS) | Fail open |
| PV-1202 | Fuel gas pressure control valve (PIC-1202) | Fail closed |
| PIC-1202 | Burner manifold pressure control | Normal 1.2 barg; Lo alarm 0.35, Hi alarm 2.2 barg |
| PT-1206 | Burner pressure low-low (SIS) | LL **trip** 0.25 barg |
| PT-1207 | Burner pressure high-high (SIS) | HH **trip** 2.5 barg |
| AT-1203 | Fuel gas LHV calorimeter | 48.5 MJ/kg; alarms 44 / 52 MJ/kg |
| TT-1204 | Fuel gas temperature | 40 °C |

| Valve data | PV-1202 |
|------------|---------|
| Type | Globe, cage-guided, equal-percentage trim |
| Size | 3" body, 2" trim |
| Normal inlet / outlet | ≈ 4.5 barg (header, after V-101) / 1.2 barg |
| Normal opening | ≈ 42% |
| Actuator | Spring-diaphragm, air to open |

The upstream refinery fuel gas header pressure is ≈ 4.5 barg. Loss of header pressure shows first
as PV-1202 driving open with PIC-1202 falling, then as the PIC-1202 Lo alarm (0.35 barg), and
finally as the PT-1206 low-low trip at 0.25 barg.

## 5. Pilot Gas System

| Parameter | Value |
|-----------|-------|
| Supply | Downstream of V-101, separate self-acting regulator |
| Pilot gas pressure | 0.7 barg (PT-1208) |
| PT-1208 Lo alarm | 0.4 barg |
| PT-1208 LL | 0.25 barg — **total trip** (main fuel trip + close XV-1209) |
| Pilot shutoff | XV-1209, SIS, fail closed |
| Pilot gas flow | ≈ 25 kg/h total (8 pilots, ≈ 40 kW each) |
| Filter | Y-strainer + 5 µm cartridge filter upstream of regulator |

Pilots are continuous and remain lit through a main fuel trip, so the heater can be re-lit
without a full purge if the trip cause is cleared promptly (subject to the conditions in SOP —
H-101 Emergency Shutdown and Trip Response, Rev 2.6). Loss of pilot gas pressure is a total trip
because main burners must never run without proven pilots.

## 6. SIS Actions on the Fuel System

| Initiator | Action |
|-----------|--------|
| Any pass flow FT-1151..1154 < 43 t/h for 2 s | Main fuel trip: close XV-1201/1202, open XV-1203; pilots stay lit |
| PT-1206 < 0.25 barg | Main fuel trip |
| PT-1207 > 2.5 barg | Main fuel trip |
| LT-1205 > 80% (LSHH-1205) | Main fuel trip |
| ≥ 3 of 8 flame scanners BS-1211..1218 lost | Main fuel trip |
| PT-1208 < 0.25 barg | Main fuel trip + close XV-1209 (total trip) |
| PT-1314 firebox pressure > +10 mmH₂O for 5 s | Main fuel trip |
| HS-1290 manual ESD | Total trip |
| FD fan stop (XS-1341), ID fan stop (XS-1351) or APH rotor stop (XS-1349) | **Not a fuel trip:** natural-draft runback — BMS clamps PIC-1202 to ≈ 0.43 barg (≤ 60% firing) |

During a natural-draft runback the BMS writes a high clamp of ≈ 0.43 barg on the PIC-1202 setpoint
(≈ 60% heat release by the √pressure relation; the clamp is verified at commissioning against fired
duty FT-1201 × AT-1203 ≤ ≈ 23 MW) and temporarily lowers the normal 0.45 barg low clamp to 0.40 barg so
that the clamp can be reached. Fuel flow falls by ≈ 40% within about a minute; the COT cascade then
cannot hold 360 °C at full charge, which reduces C-101 flash-zone vaporization — coordinate charge
and COT with the C-101 operator. Full cause and effect, voting and reset requirements are in BMS /
SIS Cause and Effect — H-101, Rev 3.3. Alarm setpoints are in Alarm and Trip Setpoint Register —
H-101 Crude Charge Heater, Rev 3.1.
