# Space Prompt - immunology-general-combo-0031

Create a scientifically coherent **immunology / general** comparative space using:
- Base models: immunology-sbml-fallon2000-interleukin-2-dynamics-biomd0000000665-model, immunology-sbml-feizabadi2011-1-immunodeficiency-in-cancer-core-biomd0000000760-model, immunology-sbml-figueredo2013-1-immunointeraction-base-model-biomd0000000753-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
