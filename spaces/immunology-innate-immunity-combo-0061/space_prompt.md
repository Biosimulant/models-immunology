# Space Prompt - immunology-innate-immunity-combo-0061

Create a scientifically coherent **immunology / innate_immunity** comparative space using:
- Base models: immunology-sbml-hu2018-dynamics-of-tumor-cd4-cytokine-host-cells-biomd0000000797-model, immunology-sbml-immunological-healthy-state-model-of-sphingolipi-model2301110002-model, immunology-sbml-khandibharad2022-il-12-regulation-by-il-10-in-le-model2012040002-model, immunology-sbml-kim2014-tumor-model-under-immune-suppression-model1909240002-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
