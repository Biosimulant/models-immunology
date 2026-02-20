# Space Plan - immunology-innate-immunity-combo-0058

## Scientific Scope
- Domain: immunology
- Theme: innate_immunity
- Base models: immunology-sbml-carbo2013-cytokine-driven-cd4-t-cell-differentia-biomd0000000451-model, immunology-sbml-day2015-early-cellular-innate-and-adaptive-immun-model1911190001-model, immunology-sbml-den-breems2015-macrophage-in-cancer-biomd0000000759-model, immunology-sbml-eftimie2017-1-interaction-of-th-and-macrophage-biomd0000000770-model

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
