# Space Plan - immunology-innate-immunity-combo-0066

## Scientific Scope
- Domain: immunology
- Theme: innate_immunity
- Base models: immunology-sbml-puniya2021-cd4-th2-cell-metabolism-model-model1909260005-model, immunology-sbml-puniya2021-naive-cd4-t-cell-metabolic-model-model1909260003-model, immunology-sbml-rateitschak2012-interferon-gamma-ifn-induced-sta-biomd0000000585-model, immunology-sbml-roy2019-a-vivid-cytokines-interaction-model-on-p-model1911070001-model

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
