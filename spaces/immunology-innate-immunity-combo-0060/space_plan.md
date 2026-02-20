# Space Plan - immunology-innate-immunity-combo-0060

## Scientific Scope
- Domain: immunology
- Theme: innate_immunity
- Base models: immunology-sbml-fribourg2014-dynamics-of-viral-antagonism-and-in-biomd0000000528-model, immunology-sbml-fribourg2014-dynamics-of-viral-antagonism-and-in-biomd0000000529-model, immunology-sbml-he2017-a-mathematical-model-of-pancreatic-cancer-biomd0000000811-model, immunology-sbml-hernandez-vargas2012-innate-immune-system-dynami-biomd0000000710-model

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
