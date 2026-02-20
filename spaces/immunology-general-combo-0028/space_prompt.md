# Space Prompt - immunology-general-combo-0028

Create a scientifically coherent **immunology / general** comparative space using:
- Base models: immunology-sbml-diego2021-improved-prediction-of-icb-efficacy-ac-model2407210002-model, immunology-sbml-draghi2019-parameter-identification-of-a-model-f-model1911100005-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
