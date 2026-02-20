# Space Prompt - immunology-general-combo-0048

Create a scientifically coherent **immunology / general** comparative space using:
- Base models: immunology-sbml-perelson1993-hivinfection-cd4tcells-modela-biomd0000000874-model, immunology-sbml-perelson1993-hivinfection-cd4tcells-modelb-model1006230093-model, immunology-sbml-perelson1993-hivinfection-cd4tcells-modelc-model1006230075-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
