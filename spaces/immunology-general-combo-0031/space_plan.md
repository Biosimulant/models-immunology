# Space Plan - immunology-general-combo-0031

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-fallon2000-interleukin-2-dynamics-biomd0000000665-model, immunology-sbml-feizabadi2011-1-immunodeficiency-in-cancer-core-biomd0000000760-model, immunology-sbml-figueredo2013-1-immunointeraction-base-model-biomd0000000753-model

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
