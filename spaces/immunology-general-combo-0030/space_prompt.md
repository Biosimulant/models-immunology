# Space Prompt - immunology-general-combo-0030

Create a scientifically coherent **immunology / general** comparative space using:
- Base models: immunology-sbml-dubey2008-modeling-the-interaction-between-avasc-biomd0000000886-model, immunology-sbml-eftimie2018-cancer-and-immune-biomarkers-biomd0000000741-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
