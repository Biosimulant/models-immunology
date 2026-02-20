# Space Plan - immunology-innate-immunity-combo-0072

## Scientific Scope
- Domain: immunology
- Theme: innate_immunity
- Base models: immunology-sbml-wei2017-tumor-t-cell-and-cytokine-interaction-biomd0000000778-model, immunology-sbml-yamada2003-jak-stat-pathway-biomd0000000093-model, immunology-sbml-yamada2003-jak-stat-socs1-knockout-biomd0000000094-model, immunology-sbml-yu2019-a-mathematical-model-of-tumor-immune-inte-model1911270002-model

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
