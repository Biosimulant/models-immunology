# Space Plan - immunology-general-combo-0021

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-bianca2012-mathematical-modeling-of-the-immune-s-model1907260002-model, immunology-sbml-bianca2013-persistence-analysis-in-a-kolmogorov-biomd0000000900-model

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
