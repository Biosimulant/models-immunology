# Space Prompt - immunology-adaptive-immunity-combo-0010

Create a scientifically coherent **immunology / adaptive_immunity** comparative space using:
- Base models: immunology-sbml-moore2004-chronic-myeloid-leukemic-cells-and-t-l-biomd0000000662-model, immunology-sbml-nanda2013-b-cell-chronic-lymphocytic-leukemia-a-model2001090002-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
