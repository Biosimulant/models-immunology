# Space Plan - immunology-general-combo-0016

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-aguilera-2014-hiv-latency-interaction-between-hi-biomd0000000573-model, immunology-sbml-al-tuwairqi2020-dynamics-of-cancer-virotherapy-w-biomd0000001035-model

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
