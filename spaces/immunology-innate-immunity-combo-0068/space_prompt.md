# Space Prompt - immunology-innate-immunity-combo-0068

Create a scientifically coherent **immunology / innate_immunity** comparative space using:
- Base models: immunology-sbml-trisilowati2018-optimal-control-of-tumor-immune-biomd0000000880-model, immunology-sbml-tsirvouli2021-cytokine-and-eicosanoid-signaling-model2109300001-model, immunology-sbml-waugh2006-diabetic-wound-healing-macrophage-dyna-biomd0000000679-model, immunology-sbml-waugh2006-diabetic-wound-healing-tgf-b-dynamics-biomd0000000680-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
