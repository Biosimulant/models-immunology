# Space Plan - immunology-general-combo-0032

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-figueredo2013-2-immunointeraction-model-with-il2-biomd0000000754-model, immunology-sbml-figueredo2013-3-immunointeraction-full-model-biomd0000000756-model, immunology-sbml-fribourg2014-model-of-influenza-a-virus-infectio-biomd0000000889-model

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
