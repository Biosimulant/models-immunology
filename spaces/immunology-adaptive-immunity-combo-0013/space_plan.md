# Space Plan - immunology-adaptive-immunity-combo-0013

## Scientific Scope
- Domain: immunology
- Theme: adaptive_immunity
- Base models: immunology-sbml-verma2016-hiv-and-hpv-co-infection-t-cell-respon-biomd0000000872-model, immunology-sbml-webb2002-fas-fasl-mediated-tumor-t-cell-interact-biomd0000000661-model

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
