# Space Prompt - immunology-innate-immunity-combo-0066

Create a scientifically coherent **immunology / innate_immunity** comparative space using:
- Base models: immunology-sbml-puniya2021-cd4-th2-cell-metabolism-model-model1909260005-model, immunology-sbml-puniya2021-naive-cd4-t-cell-metabolic-model-model1909260003-model, immunology-sbml-rateitschak2012-interferon-gamma-ifn-induced-sta-biomd0000000585-model, immunology-sbml-roy2019-a-vivid-cytokines-interaction-model-on-p-model1911070001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
