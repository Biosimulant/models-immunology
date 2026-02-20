# Space Prompt - immunology-adaptive-immunity-combo-0013

Create a scientifically coherent **immunology / adaptive_immunity** comparative space using:
- Base models: immunology-sbml-verma2016-hiv-and-hpv-co-infection-t-cell-respon-biomd0000000872-model, immunology-sbml-webb2002-fas-fasl-mediated-tumor-t-cell-interact-biomd0000000661-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
