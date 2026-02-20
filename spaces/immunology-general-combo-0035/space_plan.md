# Space Plan - immunology-general-combo-0035

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-isaeva2008-modelling-of-anti-tumour-immune-respo-biomd0000000910-model, immunology-sbml-isaeva2009-different-strategies-for-cancer-treat-model2001140002-model, immunology-sbml-jarrah2014-mathematical-model-of-the-immune-resp-biomd0000001015-model

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
