# Space Plan - immunology-innate-immunity-combo-0061

## Scientific Scope
- Domain: immunology
- Theme: innate_immunity
- Base models: immunology-sbml-hu2018-dynamics-of-tumor-cd4-cytokine-host-cells-biomd0000000797-model, immunology-sbml-immunological-healthy-state-model-of-sphingolipi-model2301110002-model, immunology-sbml-khandibharad2022-il-12-regulation-by-il-10-in-le-model2012040002-model, immunology-sbml-kim2014-tumor-model-under-immune-suppression-model1909240002-model

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
