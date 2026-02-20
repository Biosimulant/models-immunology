# Space Prompt - immunology-general-combo-0040

Create a scientifically coherent **immunology / general** comparative space using:
- Base models: immunology-sbml-leung2016-sirws-model-with-immune-boosting-and-c-model1808280006-model, immunology-sbml-liu2017-chemotherapy-targeted-model-of-tumor-imm-biomd0000000930-model, immunology-sbml-liu2019-logistic-regression-models-to-predict-in-model2310150001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
