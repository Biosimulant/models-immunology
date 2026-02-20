# Space Prompt - immunology-innate-immunity-combo-0062

Create a scientifically coherent **immunology / innate_immunity** comparative space using:
- Base models: immunology-sbml-lavigne2021-non-spatial-model-of-viral-infection-biomd0000001021-model, immunology-sbml-leber2016-regulatory-macrophage-differentiation-model1611160001-model, immunology-sbml-lix2019-macrophage-polarization-and-tumor-cell-p-model1909230002-model, immunology-sbml-maier2022-stochastic-dynamics-of-type-i-interfer-model2210070001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
