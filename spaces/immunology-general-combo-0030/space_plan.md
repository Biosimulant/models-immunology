# Space Plan - immunology-general-combo-0030

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-dubey2008-modeling-the-interaction-between-avasc-biomd0000000886-model, immunology-sbml-eftimie2018-cancer-and-immune-biomarkers-biomd0000000741-model

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
