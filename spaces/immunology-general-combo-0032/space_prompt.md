# Space Prompt - immunology-general-combo-0032

Create a scientifically coherent **immunology / general** comparative space using:
- Base models: immunology-sbml-figueredo2013-2-immunointeraction-model-with-il2-biomd0000000754-model, immunology-sbml-figueredo2013-3-immunointeraction-full-model-biomd0000000756-model, immunology-sbml-fribourg2014-model-of-influenza-a-virus-infectio-biomd0000000889-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
