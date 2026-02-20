# Space Plan - immunology-general-combo-0050

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-restif2007-vaccination-invasion-biomd0000000294-model, immunology-sbml-rhodes2019-immune-mediated-theory-of-metastasis-biomd0000000926-model, immunology-sbml-robertson-tessi-m-2012-a-model-of-tumor-immune-i-biomd0000000731-model

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
