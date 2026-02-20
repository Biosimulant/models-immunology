# Space Plan - immunology-adaptive-immunity-combo-0011

## Scientific Scope
- Domain: immunology
- Theme: adaptive_immunity
- Base models: immunology-sbml-sanjuan2013-evolution-of-hiv-t-cell-epitope-cont-model1302180002-model, immunology-sbml-sanjuan2013-evolution-of-hiv-t-cell-epitope-immu-model1302180001-model

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
