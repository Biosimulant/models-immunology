# Space Prompt - immunology-innate-immunity-combo-0055

Create a scientifically coherent **immunology / innate_immunity** comparative space using:
- Base models: immunology-sbml-almuallem2020-virus-macrophage-tumour-interactio-biomd0000001033-model, immunology-sbml-anderson2015-qualitative-behavior-of-systems-of-biomd0000000813-model, immunology-sbml-arciero2004-a-mathematical-model-of-tumor-immune-model1907310002-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
