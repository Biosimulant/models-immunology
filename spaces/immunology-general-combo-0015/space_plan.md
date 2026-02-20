# Space Plan - immunology-general-combo-0015

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-abbott2021-prediction-of-immunotherapy-response-model2407210001-model, immunology-sbml-admon2017-modelling-tumor-growth-with-immune-res-biomd0000000904-model

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
