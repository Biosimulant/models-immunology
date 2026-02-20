# Space Plan - immunology-general-combo-0052

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-rodrigues2014-vaccination-models-and-optimal-con-model2003190001-model, immunology-sbml-saad2017-immune-checkpoint-and-bcg-in-superficia-biomd0000000746-model, immunology-sbml-santos2016-gene-signatures-of-immune-sensitivity-model1604260000-model

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
