# Space Plan - immunology-innate-immunity-combo-0062

## Scientific Scope
- Domain: immunology
- Theme: innate_immunity
- Base models: immunology-sbml-lavigne2021-non-spatial-model-of-viral-infection-biomd0000001021-model, immunology-sbml-leber2016-regulatory-macrophage-differentiation-model1611160001-model, immunology-sbml-lix2019-macrophage-polarization-and-tumor-cell-p-model1909230002-model, immunology-sbml-maier2022-stochastic-dynamics-of-type-i-interfer-model2210070001-model

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
