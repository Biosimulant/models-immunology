# Space Plan - immunology-general-combo-0051

## Scientific Scope
- Domain: immunology
- Theme: general
- Base models: immunology-sbml-rodr-guez-jorge2019-boolean-model-of-combined-tc-model1903260003-model, immunology-sbml-rodr-guez-jorge2019-boolean-model-of-tcr-signali-model1903260001-model, immunology-sbml-rodr-guez-jorge2019-boolean-model-of-tlr5-signal-model1903260002-model

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
