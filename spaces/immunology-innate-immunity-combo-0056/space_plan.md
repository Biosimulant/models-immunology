# Space Plan - immunology-innate-immunity-combo-0056

## Scientific Scope
- Domain: immunology
- Theme: innate_immunity
- Base models: immunology-sbml-bachmann2011-division-of-labor-by-dual-feedback-biomd0000000861-model, immunology-sbml-baker2013-cytokine-mediated-inflammation-in-rheu-biomd0000000549-model, immunology-sbml-baker2013-cytokine-mediated-inflammation-in-rheu-biomd0000000550-model, immunology-sbml-begitt2014-stat1-cooperative-dna-binding-double-biomd0000000501-model

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
