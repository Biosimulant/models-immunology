# Space Prompt - immunology-innate-immunity-combo-0065

Create a scientifically coherent **immunology / innate_immunity** comparative space using:
- Base models: immunology-sbml-phan2017-innate-immune-in-oncolytic-virotherapy-biomd0000000748-model, immunology-sbml-philipson2015-innate-immune-response-modulated-b-biomd0000000596-model, immunology-sbml-puniya2021-cd4-th1-cell-metabolic-model-model1909260004-model, immunology-sbml-puniya2021-cd4-th17-cell-metabolism-model-model1909260006-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
