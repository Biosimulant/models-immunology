# Space Plan - immunology-adaptive-immunity-combo-0010

## Scientific Scope
- Domain: immunology
- Theme: adaptive_immunity
- Base models: immunology-sbml-moore2004-chronic-myeloid-leukemic-cells-and-t-l-biomd0000000662-model, immunology-sbml-nanda2013-b-cell-chronic-lymphocytic-leukemia-a-model2001090002-model

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
