# Space Prompt - immunology-adaptive-immunity-combo-0073

Create a scientifically coherent **immunology / adaptive_immunity** comparative space using:
- Base models: immunology-sbml-aavani2019-the-role-of-cd4-t-cells-in-immune-sys-biomd0000000876-model, immunology-sbml-bidot2008-mathematical-modelling-of-t-cell-activ-model1910290003-model, immunology-sbml-cappuccio2006-cancer-immunotherapy-by-interleuki-biomd0000000761-model, immunology-sbml-dong2014-mathematical-modeling-on-helper-t-cells-biomd0000000783-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
