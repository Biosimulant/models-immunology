# Space Prompt - immunology-innate-immunity-combo-0058

Create a scientifically coherent **immunology / innate_immunity** comparative space using:
- Base models: immunology-sbml-carbo2013-cytokine-driven-cd4-t-cell-differentia-biomd0000000451-model, immunology-sbml-day2015-early-cellular-innate-and-adaptive-immun-model1911190001-model, immunology-sbml-den-breems2015-macrophage-in-cancer-biomd0000000759-model, immunology-sbml-eftimie2017-1-interaction-of-th-and-macrophage-biomd0000000770-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
