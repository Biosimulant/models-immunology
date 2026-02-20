# Space Plan - immunology-inflammation-combo-0054

## Scientific Scope
- Domain: immunology
- Theme: inflammation
- Base models: immunology-sbml-adrianne2018-modelling-combined-virotherapy-and-model1912120003-model, immunology-sbml-jarrett2015-modelling-the-interaction-between-im-biomd0000000920-model, immunology-sbml-sanchez2017-inflammatory-responses-during-acute-model1606020000-model

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
