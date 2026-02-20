# Space Plan - immunology-innate-immunity-combo-0064

## Scientific Scope
- Domain: immunology
- Theme: innate_immunity
- Base models: immunology-sbml-mol2013-leishmania-macrophage-signaling-network-model1203220000-model, immunology-sbml-owen1998-tumour-treatment-model-biomd0000000650-model, immunology-sbml-palmer2008-negative-feedback-in-il-7-mediated-ja-biomd0000000968-model, immunology-sbml-parra-guillen2013-mathematical-model-approach-to-biomd0000000914-model

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
