# Space Prompt - immunology-general-combo-0042

Create a scientifically coherent **immunology / general** comparative space using:
- Base models: immunology-sbml-macnamara2015-1-virotherapy-full-model-biomd0000000766-model, immunology-sbml-macnamara2015-2-virotherapy-virus-free-submodel-biomd0000000767-model, immunology-sbml-mahasa2016-tumor-immune-surveillance-model2003040001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
