# Space Plan - immunology-general-combo-0033

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-gallaher2018-tumor-immune-dynamics-in-multiple-m-biomd0000000743-model, immunology-sbml-ganguli2018-immuno-regulatory-mechanisms-in-tumo-biomd0000000810-model, immunology-sbml-garcia2018basic-cancer-and-immune-cell-count-bas-biomd0000000742-model

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
