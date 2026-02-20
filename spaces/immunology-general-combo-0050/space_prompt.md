# Space Prompt - immunology-general-combo-0050

Create a scientifically coherent **immunology / general** comparative space using:
- Base models: immunology-sbml-restif2007-vaccination-invasion-biomd0000000294-model, immunology-sbml-rhodes2019-immune-mediated-theory-of-metastasis-biomd0000000926-model, immunology-sbml-robertson-tessi-m-2012-a-model-of-tumor-immune-i-biomd0000000731-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
