# Space Prompt - immunology-general-combo-0036

Create a scientifically coherent **immunology / general** comparative space using:
- Base models: immunology-sbml-jarrett2018-trastuzumab-induced-immune-response-biomd0000000745-model, immunology-sbml-kareva2010-myeloid-cells-in-tumour-immune-intera-model2001310001-model, immunology-sbml-khajanchi2017-uniform-persistence-and-global-sta-biomd0000000921-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
