# Space Plan - immunology-general-combo-0020

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-banerjee2008-immunotherapy-with-interleukin-2-a-model2001130001-model, immunology-sbml-banerjee2015-a-mathematical-model-to-elucidate-b-model1912090003-model

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
