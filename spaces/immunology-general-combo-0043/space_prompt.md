# Space Prompt - immunology-general-combo-0043

Create a scientifically coherent **immunology / general** comparative space using:
- Base models: immunology-sbml-makhlouf2020-no-treatment-model-of-the-role-of-c-biomd0000001042-model, immunology-sbml-malinzi2018-tumour-immune-interaction-model-biomd0000000809-model, immunology-sbml-manchanda2014-effect-on-immune-system-by-4-diffe-biomd0000000712-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
