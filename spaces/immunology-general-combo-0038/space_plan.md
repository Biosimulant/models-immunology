# Space Plan - immunology-general-combo-0038

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-kronik2008-improving-alloreactive-ctl-immunother-biomd0000000808-model, immunology-sbml-leber2016-host-immune-response-h-pylori-infectio-model1611160002-model, immunology-sbml-ledzewicz2013-on-optimal-chemotherapy-with-a-str-biomd0000000919-model

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
