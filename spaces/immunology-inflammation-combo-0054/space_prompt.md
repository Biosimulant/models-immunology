# Space Prompt - immunology-inflammation-combo-0054

Create a scientifically coherent **immunology / inflammation** comparative space using:
- Base models: immunology-sbml-adrianne2018-modelling-combined-virotherapy-and-model1912120003-model, immunology-sbml-jarrett2015-modelling-the-interaction-between-im-biomd0000000920-model, immunology-sbml-sanchez2017-inflammatory-responses-during-acute-model1606020000-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
