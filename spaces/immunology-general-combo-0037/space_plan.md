# Space Plan - immunology-general-combo-0037

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-khajanchi2019-stability-analysis-of-a-mathematic-biomd0000000891-model, immunology-sbml-kilian2024-immune-cell-dynamics-in-cue-induced-e-model2502180001-model, immunology-sbml-kirschner1998-immunotherapy-tumour-biomd0000000732-model

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
