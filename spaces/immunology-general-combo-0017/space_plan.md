# Space Plan - immunology-general-combo-0017

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-alexander2010-tcell-regulation-sys1-biomd0000000289-model, immunology-sbml-alexander2010-tcell-regulation-sys2-biomd0000000290-model

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
