# Space Plan - immunology-innate-immunity-combo-0057

## Scientific Scope
- Domain: immunology
- Theme: innate_immunity
- Base models: immunology-sbml-begitt2014-stat1-cooperative-dna-binding-single-biomd0000000500-model, immunology-sbml-boer1985-macrophage-t-cell-interaction-in-anti-t-model1911130003-model, immunology-sbml-bordbar2010-m-tuberculosis-macrophage-model1011090002-model, immunology-sbml-bordbar2010-macrophage-metabolism-model1011090001-model

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
