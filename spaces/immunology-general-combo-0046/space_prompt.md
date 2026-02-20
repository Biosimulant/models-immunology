# Space Prompt - immunology-general-combo-0046

Create a scientifically coherent **immunology / general** comparative space using:
- Base models: immunology-sbml-nikolopoulou2018-tumour-immune-dynamics-with-an-model1908270001-model, immunology-sbml-nowak1996-hostresponse-infectiousagents-model1006230050-model, immunology-sbml-nwabugwu2013-a-tumor-immune-mathematical-model-o-model2007090001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
