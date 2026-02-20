# Space Prompt - immunology-innate-immunity-combo-0059

Create a scientifically coherent **immunology / innate_immunity** comparative space using:
- Base models: immunology-sbml-eftimie2017-2-interaction-of-th-and-macrophage-i-biomd0000000769-model, immunology-sbml-ewald2021-innate-immune-response-during-invasive-model2105110001-model, immunology-sbml-fatehichenar2018-mathematical-model-of-immune-re-biomd0000000848-model, immunology-sbml-frank2021-macrophage-polarization-biomd0000001060-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
