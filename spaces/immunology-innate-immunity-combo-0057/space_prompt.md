# Space Prompt - immunology-innate-immunity-combo-0057

Create a scientifically coherent **immunology / innate_immunity** comparative space using:
- Base models: immunology-sbml-begitt2014-stat1-cooperative-dna-binding-single-biomd0000000500-model, immunology-sbml-boer1985-macrophage-t-cell-interaction-in-anti-t-model1911130003-model, immunology-sbml-bordbar2010-m-tuberculosis-macrophage-model1011090002-model, immunology-sbml-bordbar2010-macrophage-metabolism-model1011090001-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
