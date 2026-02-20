# Space Plan - immunology-general-combo-0039

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-lee2009-adaptive-immune-response-to-influenza-a-model1406230000-model, immunology-sbml-leon-triana2021-competition-between-tumour-cells-biomd0000001013-model, immunology-sbml-leon-triana2021-competition-between-tumour-cells-biomd0000001014-model

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
