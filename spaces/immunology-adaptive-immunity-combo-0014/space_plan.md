# Space Plan - immunology-adaptive-immunity-combo-0014

## Scientific Scope
- Domain: immunology
- Theme: adaptive_immunity
- Base models: immunology-sbml-wodarz2007-hiv-cd4-t-cell-interaction-biomd0000000663-model, immunology-sbml-wu2011-influenza-specific-cd8-t-cells-model1504160000-model

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
