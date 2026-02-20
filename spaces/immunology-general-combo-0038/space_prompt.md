# Space Prompt - immunology-general-combo-0038

Create a scientifically coherent **immunology / general** comparative space using:
- Base models: immunology-sbml-kronik2008-improving-alloreactive-ctl-immunother-biomd0000000808-model, immunology-sbml-leber2016-host-immune-response-h-pylori-infectio-model1611160002-model, immunology-sbml-ledzewicz2013-on-optimal-chemotherapy-with-a-str-biomd0000000919-model
- Observability monitors:
  - observability-state-comparison-monitor
  - observability-state-metrics-monitor

Requirements:
1. No unsupported causal claims.
2. Route each base model state-like stream to monitor inputs `state_a..state_d`.
3. Explain why these models belong together.
4. Include clear interpretation guidance for visuals.
