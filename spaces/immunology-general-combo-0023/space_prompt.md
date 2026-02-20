# Space Prompt - immunology-general-combo-0023

Create a scientifically coherent **immunology / general** comparative space using:
- Base models: immunology-sbml-cappuccio2007-tumor-immune-system-interactions-a-biomd0000001036-model, immunology-sbml-caravagna2010-tumour-suppression-by-immune-syste-biomd0000000912-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
