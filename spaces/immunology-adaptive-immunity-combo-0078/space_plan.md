# Space Plan - immunology-adaptive-immunity-combo-0078

## Scientific Scope
- Domain: immunology
- Theme: adaptive_immunity
- Base models: immunology-sbml-dwivedi2014-crohns-il6-disease-model-anti-il6r-a-biomd0000000537-model, immunology-sbml-dwivedi2014-crohns-il6-disease-model-sgp130-acti-biomd0000000536-model, immunology-sbml-dwivedi2014-healthy-volunteer-il6-model-biomd0000000534-model, immunology-sbml-frascoli2014-a-dynamical-model-of-tumour-immunot-biomd0000000787-model

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
