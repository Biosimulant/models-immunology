# Space Plan - immunology-general-combo-0024

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-carbo2013-mucosal-immune-response-during-h-pylor-biomd0000000480-model, immunology-sbml-chowell2022-random-forest-model-to-predict-effic-biomd0000001066-model

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
