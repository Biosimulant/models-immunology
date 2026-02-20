# Space Plan - immunology-innate-immunity-combo-0063

## Scientific Scope
- Domain: immunology
- Theme: innate_immunity
- Base models: immunology-sbml-manda2019-acute-hepatitis-b-virus-infection-mode-model1911280002-model, immunology-sbml-maree2006-duca-type1diabetesmodel-biomd0000000381-model, immunology-sbml-miao2010-innate-and-adaptive-immune-responses-to-biomd0000000546-model, immunology-sbml-modeling-the-relevance-of-immune-and-metabolic-c-model2209160001-model

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
