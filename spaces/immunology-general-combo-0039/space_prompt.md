# Space Prompt - immunology-general-combo-0039

Create a scientifically coherent **immunology / general** comparative space using:
- Base models: immunology-sbml-lee2009-adaptive-immune-response-to-influenza-a-model1406230000-model, immunology-sbml-leon-triana2021-competition-between-tumour-cells-biomd0000001013-model, immunology-sbml-leon-triana2021-competition-between-tumour-cells-biomd0000001014-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
