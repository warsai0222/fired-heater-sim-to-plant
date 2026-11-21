# Fired Heater Sim-to-Plant Project

A project on closing the gap between a process simulation and the real plant: physics-based
simulation, physics-informed calibration and AI reasoning, on a refinery crude charge heater. The
full proposal is [docs/fired_heater_project_proposal.md](docs/fired_heater_project_proposal.md)
(PDF alongside). **Read it before doing any work.** It is the agreed plan.

Audience-specific context (who this was written for and the questions directed at them) is kept out
of the repo in `NOTES.local.md` (gitignored).

## Working preferences
- Keep everything **local**. Do not push to GitHub or create remotes until asked. Do not commit unless asked.
- Explain things **one step at a time**, in plain language. The user is a chemical engineer, so use
  process/ChemE framing and avoid ML jargon without explanation.
- Ask before big design choices; keep every assumed number documented with its source or `ASSUMED`.

## Status (as of 2026-11-20)
- Proposal finalized and saved (docs/).
- Crude assays done: `crudes/{wti_light,alaska_north_slope,kearl}.json`, transcribed from public
  ExxonMobil Crude Summary Report PDFs (originals in `raw_assays/`, gitignored, do not redistribute).
  Light / medium / heavy: API 47.4 / 32.3 / 19.8; MCR 0.1 / 4.7 / 9.7 wt%; C7 asphaltenes
  0.0 / 1.9 / 5.7 wt%. TBP = cumulative vol % distilled at 10 °C steps (30–590 °C).
  ExxonMobil blocks curl (403). Fetch assays via a web-fetch tool instead.
- Design reference package (preliminary, pending ChemE review):
  `design/heater_design_reference.md` (hand H&MB, stream table, loops, valves, SIS trips, limits),
  `design/tag_register.csv` (86 instrument tags with setpoints), `design/equipment_list.csv`.
  Rev A (natural draft) gave ≈84%; Rev B with APH ≈91%.
- Drawings: `docs/diagrams/` — PFD U100-PFD-001, P&IDs U100-PID-101 (process coil), U100-PID-102
  (combustion/fuel/burners/BMS), U100-PID-103 (APH, FD/ID fans, ducts), as SVG + combined A3 PDF. Regenerate: `python3 scripts/draw_diagrams.py`
  (then rebuild the PDF with headless Chrome).
- RAG docs: `heater_docs/` — 42 docs (Rev B), boiler-project frontmatter format (see heater_docs/README.md).
  Not yet indexed into a vector DB.
- **No model code yet.** Next step: Phase 1, the physics model + unit tests.

## Design basis (ASSUMED, out for review)
The full design basis is **Section 5 of the proposal** (process side, coil/tubes, combustion/firebox,
maintenance/economics, plus questions for the reviewer). The user is sending the PDF to a chemical
engineer for review. Apply their corrections to Section 5 and regenerate the PDF before coding Phase 1.
Design crude: Alaska North Slope; 50,000 bbl/d; 250 → 360 °C; 4 passes; 6" Sch 40 P9 tubes;
~34 kW/m²; TMT limit ~600 °C; balanced draft + regenerative APH (Rev B); ~3% O2; pigging decoke ~4 days.
PDF regeneration: `./scripts/build_proposal_pdf.sh` (pandoc gfm → standalone HTML with
`docs/proposal.css`, then headless Chrome `--print-to-pdf --no-pdf-header-footer`). The stylesheet
resolves to Helvetica Neue on macOS and DejaVu Sans elsewhere, so rebuild on the Mac for the
intended typography.

## Direction changes (2026-11-20) — apply before Phase 1
- **Design change (DONE, Rev B):** regenerative (Ljungström) **air preheater** E-102 + **balanced draft**
  (FD fan K-101, ID fan K-102). Applied to proposal §5–8/13/14, design/ (see design/rev_b_change_note.md),
  all drawings (PFD + PID-101/102/103) and all 42 heater_docs. η ≈ 91%, fired 38.5 MW, stack ≈ 155 °C.
  Fan basis: FD ≈ 30 kW / 75 kW motor, ID ≈ 40 kW / 90 kW motor. COT stays a given target.
- **Guiding principle:** never treat the heater in a silo. COT / outlet vaporization change the
  atmospheric column cut points and product yields and everything downstream; the optimizer and
  explanations must account for that, not only fuel and decoke cost.

## Key decisions already made
- Unit: refinery **crude charge heater**. Both datasets **synthetic**: (1) as-new model run =
  "simulation dataset", (2) separate richer "truth" plant simulator with hidden degradation + noise =
  "plant dataset". The plant simulator must **differ structurally** from the model (4 passes with
  maldistribution, per-crude true coking rates, ~95% decoke recovery, drifting O2 bias, tramp-air step
  event, faulty skin TCs, AR(1) noise).
- Decisions (Type A): excess-O2 setpoint + decoke date; stretch: stack damper.
- Type B (calibrated): coke resistance (state), coking-rate multiplier per crude, convection soot,
  tramp-air leak area (∝ √draft), O2 analyzer bias, as-built mismatch.
- Coil ΔP is a second coke signal (with TMT). Vaporization: simple model (TBP-based vapor fraction,
  enthalpy incl. latent heat, homogeneous two-phase ΔP multiplier).
- Limits: TMT, coil ΔP, CO, burner O2 floor, bridgewall 760–900 °C, firing ≤120% normal, negative draft.
- Explanation layer reuses the investigation audit trail (`session_store.py`, `config.py`,
  `scripts/render_investigation_report.py`) from the sibling boiler repo
  `../industrial-ai-troubleshooting-agent-main/`. Copy the needed pieces here rather than importing
  across repos.
- Python: use a project-local venv (Python 3.13 works; system 3.15 lacks some wheels). numpy, scipy,
  pandas, pytest needed.
