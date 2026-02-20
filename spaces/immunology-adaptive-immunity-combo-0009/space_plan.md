# Space Plan - immunology-adaptive-immunity-combo-0009

## Scientific Scope
- Domain: immunology
- Theme: adaptive_immunity
- Base models: immunology-sbml-martinez-sanchez2015-t-cd4-lymphocyte-transcript-biomd0000000592-model, immunology-sbml-martinez-sanchez2015-t-cd4-lymphocyte-transcript-biomd0000000593-model

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
