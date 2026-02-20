# Space Plan - immunology-adaptive-immunity-combo-0007

## Scientific Scope
- Domain: immunology
- Theme: adaptive_immunity
- Base models: immunology-sbml-leon-triana2020-car-t-cell-therapy-in-b-cell-acu-biomd0000001011-model, immunology-sbml-leon-triana2020-car-t-cell-therapy-in-b-cell-acu-biomd0000001012-model

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
