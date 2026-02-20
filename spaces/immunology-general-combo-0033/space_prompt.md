# Space Prompt - immunology-general-combo-0033

Create a scientifically coherent **immunology / general** comparative space using:
- Base models: immunology-sbml-gallaher2018-tumor-immune-dynamics-in-multiple-m-biomd0000000743-model, immunology-sbml-ganguli2018-immuno-regulatory-mechanisms-in-tumo-biomd0000000810-model, immunology-sbml-garcia2018basic-cancer-and-immune-cell-count-bas-biomd0000000742-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
