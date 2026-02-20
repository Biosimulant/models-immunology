# Space Prompt - immunology-inflammation-combo-0070

Create a scientifically coherent **immunology / inflammation** comparative space using:
- Base models: immunology-sbml-jarrett2015-modelling-the-interaction-between-im-biomd0000000920-model, immunology-sbml-sanchez2017-inflammatory-responses-during-acute-model1606020000-model, immunology-sbml-sherekar2023-modeling-heterogeneity-in-tnfr1-sig-model2504180001-model, immunology-sbml-soni2018-il6-induced-m2-phenotype-in-leishmania-biomd0000000873-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
