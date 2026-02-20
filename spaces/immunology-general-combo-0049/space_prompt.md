# Space Prompt - immunology-general-combo-0049

Create a scientifically coherent **immunology / general** comparative space using:
- Base models: immunology-sbml-perelson1993-hivinfection-cd4tcells-modeld-model1006230035-model, immunology-sbml-raman2005-mycolic-acid-pathway-of-m-tuberculosis-biomd0000001046-model, immunology-sbml-rangel-reyes2017-dendritic-immunotherapy-improve-model1909160002-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
