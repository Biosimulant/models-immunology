# Space Prompt - immunology-general-combo-0024

Create a scientifically coherent **immunology / general** comparative space using:
- Base models: immunology-sbml-carbo2013-mucosal-immune-response-during-h-pylor-biomd0000000480-model, immunology-sbml-chowell2022-random-forest-model-to-predict-effic-biomd0000001066-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
