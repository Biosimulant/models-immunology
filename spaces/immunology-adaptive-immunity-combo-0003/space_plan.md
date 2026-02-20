# Space Plan - immunology-adaptive-immunity-combo-0003

## Scientific Scope
- Domain: immunology
- Theme: adaptive_immunity
- Base models: immunology-sbml-dwivedi2014-crohns-il6-disease-model-anti-il6-an-biomd0000000535-model, immunology-sbml-dwivedi2014-crohns-il6-disease-model-anti-il6r-a-biomd0000000537-model

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
