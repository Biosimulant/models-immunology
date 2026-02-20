# Space Plan - immunology-general-combo-0046

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-nikolopoulou2018-tumour-immune-dynamics-with-an-model1908270001-model, immunology-sbml-nowak1996-hostresponse-infectiousagents-model1006230050-model, immunology-sbml-nwabugwu2013-a-tumor-immune-mathematical-model-o-model2007090001-model

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
