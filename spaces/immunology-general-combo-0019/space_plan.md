# Space Plan - immunology-general-combo-0019

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-alvarez2019-a-nonlinear-mathematical-model-of-ce-biomd0000000790-model, immunology-sbml-baker-2022-immunometabolic-model-model2211070001-model

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
