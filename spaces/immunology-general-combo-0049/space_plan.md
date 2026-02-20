# Space Plan - immunology-general-combo-0049

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-perelson1993-hivinfection-cd4tcells-modeld-model1006230035-model, immunology-sbml-raman2005-mycolic-acid-pathway-of-m-tuberculosis-biomd0000001046-model, immunology-sbml-rangel-reyes2017-dendritic-immunotherapy-improve-model1909160002-model

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
