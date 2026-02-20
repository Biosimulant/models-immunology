# Space Prompt - immunology-innate-immunity-combo-0063

Create a scientifically coherent **immunology / innate_immunity** comparative space using:
- Base models: immunology-sbml-manda2019-acute-hepatitis-b-virus-infection-mode-model1911280002-model, immunology-sbml-maree2006-duca-type1diabetesmodel-biomd0000000381-model, immunology-sbml-miao2010-innate-and-adaptive-immune-responses-to-biomd0000000546-model, immunology-sbml-modeling-the-relevance-of-immune-and-metabolic-c-model2209160001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
