# Space Prompt - immunology-general-combo-0034

Create a scientifically coherent **immunology / general** comparative space using:
- Base models: immunology-sbml-gei-ert2020-yersinia-enterocolitica-co-infection-model2002070001-model, immunology-sbml-hancioglu2007-human-immune-response-to-influenza-biomd0000000711-model, immunology-sbml-hardiansyah2019-qsp-model-of-chimeric-antigen-re-model2009230001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
