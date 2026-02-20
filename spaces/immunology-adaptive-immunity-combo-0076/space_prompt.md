# Space Prompt - immunology-adaptive-immunity-combo-0076

Create a scientifically coherent **immunology / adaptive_immunity** comparative space using:
- Base models: immunology-sbml-dong2014-mathematical-modeling-on-helper-t-cells-biomd0000000783-model, immunology-sbml-dwivedi2014-crohns-il6-disease-model-anti-il6-an-biomd0000000535-model, immunology-sbml-dwivedi2014-crohns-il6-disease-model-anti-il6r-a-biomd0000000537-model, immunology-sbml-dwivedi2014-crohns-il6-disease-model-sgp130-acti-biomd0000000536-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
