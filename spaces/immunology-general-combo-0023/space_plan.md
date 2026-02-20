# Space Plan - immunology-general-combo-0023

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-cappuccio2007-tumor-immune-system-interactions-a-biomd0000001036-model, immunology-sbml-caravagna2010-tumour-suppression-by-immune-syste-biomd0000000912-model

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
