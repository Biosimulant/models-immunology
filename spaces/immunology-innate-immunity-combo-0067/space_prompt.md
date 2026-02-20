# Space Prompt - immunology-innate-immunity-combo-0067

Create a scientifically coherent **immunology / innate_immunity** comparative space using:
- Base models: immunology-sbml-sandip2013-modeling-the-dynamics-of-hepatitis-c-biomd0000000892-model, immunology-sbml-sandip2013-modeling-the-dynamics-of-hepatitis-c-model1912120002-model, immunology-sbml-schulz2009-th1-differentiation-biomd0000000215-model, immunology-sbml-smith2011-three-stage-innate-immune-response-to-biomd0000000924-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
