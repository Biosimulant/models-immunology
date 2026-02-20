# Space Plan - immunology-inflammation-combo-0070

## Scientific Scope
- Domain: immunology
- Theme: inflammation
- Base models: immunology-sbml-jarrett2015-modelling-the-interaction-between-im-biomd0000000920-model, immunology-sbml-sanchez2017-inflammatory-responses-during-acute-model1606020000-model, immunology-sbml-sherekar2023-modeling-heterogeneity-in-tnfr1-sig-model2504180001-model, immunology-sbml-soni2018-il6-induced-m2-phenotype-in-leishmania-biomd0000000873-model

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
