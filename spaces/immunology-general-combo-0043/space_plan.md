# Space Plan - immunology-general-combo-0043

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-makhlouf2020-no-treatment-model-of-the-role-of-c-biomd0000001042-model, immunology-sbml-malinzi2018-tumour-immune-interaction-model-biomd0000000809-model, immunology-sbml-manchanda2014-effect-on-immune-system-by-4-diffe-biomd0000000712-model

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
