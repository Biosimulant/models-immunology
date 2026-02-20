# Space Prompt - immunology-general-combo-0041

Create a scientifically coherent **immunology / general** comparative space using:
- Base models: immunology-sbml-liu2023-predicting-the-efficacy-of-immune-checkp-biomd0000001074-model, immunology-sbml-lopez2014-a-validated-mathematical-model-of-tumo-biomd0000000784-model, immunology-sbml-louzoun2014-a-mathematical-model-for-pancreatic-model1909100002-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
