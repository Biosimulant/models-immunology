# Space Prompt - immunology-general-combo-0035

Create a scientifically coherent **immunology / general** comparative space using:
- Base models: immunology-sbml-isaeva2008-modelling-of-anti-tumour-immune-respo-biomd0000000910-model, immunology-sbml-isaeva2009-different-strategies-for-cancer-treat-model2001140002-model, immunology-sbml-jarrah2014-mathematical-model-of-the-immune-resp-biomd0000001015-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
