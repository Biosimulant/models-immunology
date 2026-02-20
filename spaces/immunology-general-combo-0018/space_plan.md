# Space Plan - immunology-general-combo-0018

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-alharbi2020-an-ode-based-model-of-the-dynamics-o-biomd0000001023-model, immunology-sbml-alharbi2020-tumor-and-immune-system-competition-biomd0000001052-model

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
