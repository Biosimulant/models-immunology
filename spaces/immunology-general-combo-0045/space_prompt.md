# Space Prompt - immunology-general-combo-0045

Create a scientifically coherent **immunology / general** comparative space using:
- Base models: immunology-sbml-montagud2022-prostate-cancer-boolean-model-model2106070001-model, immunology-sbml-mufudza2012-estrogen-effect-on-the-dynamics-of-b-biomd0000000642-model, immunology-sbml-mullinax2016-mathematical-model-of-tumor-immune-model2109110006-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
