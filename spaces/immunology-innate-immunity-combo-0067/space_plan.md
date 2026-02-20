# Space Plan - immunology-innate-immunity-combo-0067

## Scientific Scope
- Domain: immunology
- Theme: innate_immunity
- Base models: immunology-sbml-sandip2013-modeling-the-dynamics-of-hepatitis-c-biomd0000000892-model, immunology-sbml-sandip2013-modeling-the-dynamics-of-hepatitis-c-model1912120002-model, immunology-sbml-schulz2009-th1-differentiation-biomd0000000215-model, immunology-sbml-smith2011-three-stage-innate-immune-response-to-biomd0000000924-model

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
