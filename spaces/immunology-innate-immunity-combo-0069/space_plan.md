# Space Plan - immunology-innate-immunity-combo-0069

## Scientific Scope
- Domain: immunology
- Theme: innate_immunity
- Base models: immunology-sbml-waugh2006-diabetic-wound-healing-treated-and-unt-biomd0000000681-model, immunology-sbml-wei2017-tumor-t-cell-and-cytokine-interaction-biomd0000000778-model, immunology-sbml-yamada2003-jak-stat-pathway-biomd0000000093-model, immunology-sbml-yamada2003-jak-stat-socs1-knockout-biomd0000000094-model

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
