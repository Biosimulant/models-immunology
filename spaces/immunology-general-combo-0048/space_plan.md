# Space Plan - immunology-general-combo-0048

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-perelson1993-hivinfection-cd4tcells-modela-biomd0000000874-model, immunology-sbml-perelson1993-hivinfection-cd4tcells-modelb-model1006230093-model, immunology-sbml-perelson1993-hivinfection-cd4tcells-modelc-model1006230075-model

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
