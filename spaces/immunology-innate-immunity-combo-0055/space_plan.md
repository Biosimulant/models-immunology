# Space Plan - immunology-innate-immunity-combo-0055

## Scientific Scope
- Domain: immunology
- Theme: innate_immunity
- Base models: immunology-sbml-almuallem2020-virus-macrophage-tumour-interactio-biomd0000001033-model, immunology-sbml-anderson2015-qualitative-behavior-of-systems-of-biomd0000000813-model, immunology-sbml-arciero2004-a-mathematical-model-of-tumor-immune-model1907310002-model

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
