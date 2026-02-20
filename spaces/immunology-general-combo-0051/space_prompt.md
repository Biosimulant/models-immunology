# Space Prompt - immunology-general-combo-0051

Create a scientifically coherent **immunology / general** comparative space using:
- Base models: immunology-sbml-rodr-guez-jorge2019-boolean-model-of-combined-tc-model1903260003-model, immunology-sbml-rodr-guez-jorge2019-boolean-model-of-tcr-signali-model1903260001-model, immunology-sbml-rodr-guez-jorge2019-boolean-model-of-tlr5-signal-model1903260002-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
