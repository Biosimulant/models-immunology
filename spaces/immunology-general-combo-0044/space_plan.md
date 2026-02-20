# Space Plan - immunology-general-combo-0044

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-miao2014-dynamics-and-migratory-pathways-of-viru-model1411130000-model, immunology-sbml-model1207300000-url-xml-model1207300000-model, immunology-sbml-mol2013-immune-signal-transduction-in-leishmania-biomd0000000477-model

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
