# Space Prompt - immunology-adaptive-immunity-combo-0071

Create a scientifically coherent **immunology / adaptive_immunity** comparative space using:
- Base models: immunology-sbml-webb2002-fas-fasl-mediated-tumor-t-cell-interact-biomd0000000661-model, immunology-sbml-wodarz2007-hiv-cd4-t-cell-interaction-biomd0000000663-model, immunology-sbml-wu2011-influenza-specific-cd8-t-cells-model1504160000-model, immunology-sbml-wu2017-murine-bevacizumab-pk-model-model2003030003-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
