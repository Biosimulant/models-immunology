# Space Plan - immunology-general-combo-0026

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-creemers2021-tumor-immune-dynamics-and-implicati-biomd0000001022-model, immunology-sbml-depillis2005-a-validated-mathematical-model-of-c-model1907260001-model

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
