# Space Prompt - immunology-innate-immunity-combo-0069

Create a scientifically coherent **immunology / innate_immunity** comparative space using:
- Base models: immunology-sbml-waugh2006-diabetic-wound-healing-treated-and-unt-biomd0000000681-model, immunology-sbml-wei2017-tumor-t-cell-and-cytokine-interaction-biomd0000000778-model, immunology-sbml-yamada2003-jak-stat-pathway-biomd0000000093-model, immunology-sbml-yamada2003-jak-stat-socs1-knockout-biomd0000000094-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
