# Space Plan - immunology-general-combo-0053

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-scharf2023-holistic-view-on-the-structure-of-imm-model2304260001-model, immunology-sbml-schokker2013-a-mathematical-model-representing-c-biomd0000000895-model, immunology-sbml-shin2019-regulation-of-nuclear-factor-of-activat-model2003200002-model

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
