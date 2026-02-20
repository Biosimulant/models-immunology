# Space Plan - immunology-innate-immunity-combo-0059

## Scientific Scope
- Domain: immunology
- Theme: innate_immunity
- Base models: immunology-sbml-eftimie2017-2-interaction-of-th-and-macrophage-i-biomd0000000769-model, immunology-sbml-ewald2021-innate-immune-response-during-invasive-model2105110001-model, immunology-sbml-fatehichenar2018-mathematical-model-of-immune-re-biomd0000000848-model, immunology-sbml-frank2021-macrophage-polarization-biomd0000001060-model

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
