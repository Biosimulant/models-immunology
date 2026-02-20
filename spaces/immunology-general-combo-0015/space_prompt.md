# Space Prompt - immunology-general-combo-0015

Create a scientifically coherent **immunology / general** comparative space using:
- Base models: immunology-sbml-abbott2021-prediction-of-immunotherapy-response-model2407210001-model, immunology-sbml-admon2017-modelling-tumor-growth-with-immune-res-biomd0000000904-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
