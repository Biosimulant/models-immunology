# Space Plan - immunology-general-combo-0047

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-overgaard2007-pdmodel-il21-biomd0000000238-model, immunology-sbml-palsson2013-fully-integrated-immune-response-mod-biomd0000000608-model, immunology-sbml-patterson2022-tumour-mutation-data-driven-random-biomd0000001073-model

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
