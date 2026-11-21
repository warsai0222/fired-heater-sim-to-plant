# H-101 Plant Document Library (RAG docs) — Rev B

42 synthetic controlled documents for the H-101 crude charge heater, written for the demo (fictional
"Demo Refinery, Unit 100"). **Rev B (2026-11-20, MOC-H101-2026-07): balanced draft (FD fan K-101 +
ID fan K-102) with a regenerative air preheater E-102** — see `design/rev_b_change_note.md`.
Same frontmatter format as the boiler project's `RAG docs/` (`doc_id, doc_type, equipment, tags,
title, revision, date`; one chunk per `##` section), so its `build_docs_db.py` indexer can be reused.

| Folder | Count | Content |
|---|---|---|
| datasheets/ | 9 | heater overall, radiant coil, convection, burners, fuel/pilot gas + V-101, stack + bypass damper + emergency air doors, analyzers, **air preheater**, **FD/ID fans** |
| controls/ | 4 | alarm & trip register (all 86 tags), COT cascade, pass balancing, excess O2 & draft philosophy |
| sops/ | 7 | cold start-up, normal / emergency shutdown, crude switch, daily rounds, O2 step test, **fan trip / natural-draft operation** |
| maintenance/ | 7 | pigging decoke, soot blowing, tramp-air survey, analyzer calibration, skin TCs, burners, **APH seal inspection & washing** |
| safety/ | 5 | BMS cause & effect, IOWs, tube rupture, firebox entry, stack emissions |
| troubleshooting/ | 10 | high TMT, rising ΔP, high stack T, high fuel, low O2/high CO, high O2, positive draft, pass imbalance, suspect skin TC, **APH leakage/fouling/cold end** |

Sources of truth: `design/heater_design_reference.md`, `design/tag_register.csv`,
`design/equipment_list.csv`, `design/rev_b_change_note.md`, drawings in `docs/diagrams/`.
Validated: every frontmatter tag is in the register, every equipment id is in the vocabulary, every
body tag exists, titles/revisions match the master list, and all 189 cross-references resolve.
Values not in the design files (pig sizes, calibration gases, APH rotor size, controller tuning, …)
are typical values chosen by the writers — reviewable, not vendor data. Docs intentionally do not
reveal the plant simulator's hidden degradations. Downstream (atmospheric column) effects are
mentioned where relevant but not modelled.
