# Space Prompt - immunology-innate-immunity-combo-0064

Create a scientifically coherent **immunology / innate_immunity** comparative space using:
- Base models: immunology-sbml-mol2013-leishmania-macrophage-signaling-network-model1203220000-model, immunology-sbml-owen1998-tumour-treatment-model-biomd0000000650-model, immunology-sbml-palmer2008-negative-feedback-in-il-7-mediated-ja-biomd0000000968-model, immunology-sbml-parra-guillen2013-mathematical-model-approach-to-biomd0000000914-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
