# Space Prompt - immunology-general-combo-0016

Create a scientifically coherent **immunology / general** comparative space using:
- Base models: immunology-sbml-aguilera-2014-hiv-latency-interaction-between-hi-biomd0000000573-model, immunology-sbml-al-tuwairqi2020-dynamics-of-cancer-virotherapy-w-biomd0000001035-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
