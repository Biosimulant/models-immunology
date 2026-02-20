# Space Prompt - immunology-general-combo-0047

Create a scientifically coherent **immunology / general** comparative space using:
- Base models: immunology-sbml-overgaard2007-pdmodel-il21-biomd0000000238-model, immunology-sbml-palsson2013-fully-integrated-immune-response-mod-biomd0000000608-model, immunology-sbml-patterson2022-tumour-mutation-data-driven-random-biomd0000001073-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
