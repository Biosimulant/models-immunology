# Space Plan - immunology-general-combo-0040

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-leung2016-sirws-model-with-immune-boosting-and-c-model1808280006-model, immunology-sbml-liu2017-chemotherapy-targeted-model-of-tumor-imm-biomd0000000930-model, immunology-sbml-liu2019-logistic-regression-models-to-predict-in-model2310150001-model

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
