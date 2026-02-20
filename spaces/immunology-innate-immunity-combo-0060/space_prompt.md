# Space Prompt - immunology-innate-immunity-combo-0060

Create a scientifically coherent **immunology / innate_immunity** comparative space using:
- Base models: immunology-sbml-fribourg2014-dynamics-of-viral-antagonism-and-in-biomd0000000528-model, immunology-sbml-fribourg2014-dynamics-of-viral-antagonism-and-in-biomd0000000529-model, immunology-sbml-he2017-a-mathematical-model-of-pancreatic-cancer-biomd0000000811-model, immunology-sbml-hernandez-vargas2012-innate-immune-system-dynami-biomd0000000710-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
