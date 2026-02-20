# Space Plan - immunology-innate-immunity-combo-0068

## Scientific Scope
- Domain: immunology
- Theme: innate_immunity
- Base models: immunology-sbml-trisilowati2018-optimal-control-of-tumor-immune-biomd0000000880-model, immunology-sbml-tsirvouli2021-cytokine-and-eicosanoid-signaling-model2109300001-model, immunology-sbml-waugh2006-diabetic-wound-healing-macrophage-dyna-biomd0000000679-model, immunology-sbml-waugh2006-diabetic-wound-healing-tgf-b-dynamics-biomd0000000680-model

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
