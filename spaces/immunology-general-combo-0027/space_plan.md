# Space Plan - immunology-general-combo-0027

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-depillis2007-chemotherapy-for-tumors-an-analysis-model2001160001-model, immunology-sbml-depillis2009-mathematical-model-creation-for-can-biomd0000000779-model

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
