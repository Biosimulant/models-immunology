# Space Plan - immunology-general-combo-0036

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-jarrett2018-trastuzumab-induced-immune-response-biomd0000000745-model, immunology-sbml-kareva2010-myeloid-cells-in-tumour-immune-intera-model2001310001-model, immunology-sbml-khajanchi2017-uniform-persistence-and-global-sta-biomd0000000921-model

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
