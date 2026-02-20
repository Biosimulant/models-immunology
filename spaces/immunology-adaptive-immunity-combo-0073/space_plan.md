# Space Plan - immunology-adaptive-immunity-combo-0073

## Scientific Scope
- Domain: immunology
- Theme: adaptive_immunity
- Base models: immunology-sbml-aavani2019-the-role-of-cd4-t-cells-in-immune-sys-biomd0000000876-model, immunology-sbml-bidot2008-mathematical-modelling-of-t-cell-activ-model1910290003-model, immunology-sbml-cappuccio2006-cancer-immunotherapy-by-interleuki-biomd0000000761-model, immunology-sbml-dong2014-mathematical-modeling-on-helper-t-cells-biomd0000000783-model

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
