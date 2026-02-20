# Space Plan - immunology-general-combo-0034

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-gei-ert2020-yersinia-enterocolitica-co-infection-model2002070001-model, immunology-sbml-hancioglu2007-human-immune-response-to-influenza-biomd0000000711-model, immunology-sbml-hardiansyah2019-qsp-model-of-chimeric-antigen-re-model2009230001-model

## Wiring Plan
- Comparative mode with monitor-only routing.
- Each base model state-like output connects to monitor ports `state_a..state_d`.
- No direct causal links among base models unless explicitly upgraded later.

## Visualization Plan
- Include `StateComparisonMonitor` and `StateMetricsMonitor`.
- Require at least:
  - one timeseries visual,
  - one summary table visual.

## Validation Gates
- space schema validity
- wiring endpoint validity
- smoke run success
- repo manifest/entrypoint validators pass
