# Space Plan - immunology-general-combo-0041

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-liu2023-predicting-the-efficacy-of-immune-checkp-biomd0000001074-model, immunology-sbml-lopez2014-a-validated-mathematical-model-of-tumo-biomd0000000784-model, immunology-sbml-louzoun2014-a-mathematical-model-for-pancreatic-model1909100002-model

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
