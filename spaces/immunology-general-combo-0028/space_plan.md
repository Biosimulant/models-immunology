# Space Plan - immunology-general-combo-0028

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-diego2021-improved-prediction-of-icb-efficacy-ac-model2407210002-model, immunology-sbml-draghi2019-parameter-identification-of-a-model-f-model1911100005-model

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
