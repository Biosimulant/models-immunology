# Space Plan - immunology-general-combo-0025

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-chrobak2011-a-mathematical-model-of-induced-canc-biomd0000000815-model, immunology-sbml-coulibaly2019-interleukin-15-signaling-in-hif-1a-biomd0000000867-model

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
