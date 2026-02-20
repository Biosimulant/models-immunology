# Space Prompt - immunology-innate-immunity-combo-0056

Create a scientifically coherent **immunology / innate_immunity** comparative space using:
- Base models: immunology-sbml-bachmann2011-division-of-labor-by-dual-feedback-biomd0000000861-model, immunology-sbml-baker2013-cytokine-mediated-inflammation-in-rheu-biomd0000000549-model, immunology-sbml-baker2013-cytokine-mediated-inflammation-in-rheu-biomd0000000550-model, immunology-sbml-begitt2014-stat1-cooperative-dna-binding-double-biomd0000000501-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
