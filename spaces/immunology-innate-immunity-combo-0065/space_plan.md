# Space Plan - immunology-innate-immunity-combo-0065

## Scientific Scope
- Domain: immunology
- Theme: innate_immunity
- Base models: immunology-sbml-phan2017-innate-immune-in-oncolytic-virotherapy-biomd0000000748-model, immunology-sbml-philipson2015-innate-immune-response-modulated-b-biomd0000000596-model, immunology-sbml-puniya2021-cd4-th1-cell-metabolic-model-model1909260004-model, immunology-sbml-puniya2021-cd4-th17-cell-metabolism-model-model1909260006-model

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
