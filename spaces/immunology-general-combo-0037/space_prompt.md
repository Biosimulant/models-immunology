# Space Prompt - immunology-general-combo-0037

Create a scientifically coherent **immunology / general** comparative space using:
- Base models: immunology-sbml-khajanchi2019-stability-analysis-of-a-mathematic-biomd0000000891-model, immunology-sbml-kilian2024-immune-cell-dynamics-in-cue-induced-e-model2502180001-model, immunology-sbml-kirschner1998-immunotherapy-tumour-biomd0000000732-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
