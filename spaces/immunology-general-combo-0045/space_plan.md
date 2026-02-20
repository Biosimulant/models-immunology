# Space Plan - immunology-general-combo-0045

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-montagud2022-prostate-cancer-boolean-model-model2106070001-model, immunology-sbml-mufudza2012-estrogen-effect-on-the-dynamics-of-b-biomd0000000642-model, immunology-sbml-mullinax2016-mathematical-model-of-tumor-immune-model2109110006-model

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
