# Space Prompt - immunology-general-combo-0052

Create a scientifically coherent **immunology / general** comparative space using:
- Base models: immunology-sbml-rodrigues2014-vaccination-models-and-optimal-con-model2003190001-model, immunology-sbml-saad2017-immune-checkpoint-and-bcg-in-superficia-biomd0000000746-model, immunology-sbml-santos2016-gene-signatures-of-immune-sensitivity-model1604260000-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
