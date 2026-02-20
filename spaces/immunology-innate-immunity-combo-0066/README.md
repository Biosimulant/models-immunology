# COMBO_0066 - Immunology Innate Immunity

## Scientific Question
How do innate immunity mechanisms compare across these models?

## Biological Context
Innate/adaptive response dynamics and inflammatory signaling.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `immunology-sbml-puniya2021-cd4-th2-cell-metabolism-model-model1909260005-model`: Immunology: Puniya2021Cd4Th2CellMetabolismModelModel1909260005Model
- `immunology-sbml-puniya2021-naive-cd4-t-cell-metabolic-model-model1909260003-model`: Immunology: Puniya2021NaiveCd4TCellMetabolicModelModel1909260003Model
- `immunology-sbml-rateitschak2012-interferon-gamma-ifn-induced-sta-biomd0000000585-model`: Immunology: Rateitschak2012InterferonGammaIfnInducedStaBiomd0000000585Model
- `immunology-sbml-roy2019-a-vivid-cytokines-interaction-model-on-p-model1911070001-model`: Immunology: Roy2019AVividCytokinesInteractionModelOnPModel1911070001Model

## Wiring Rationale
- Comparative (non-causal) mode: no direct causal links were created.

## Visualization Strategy
- Monitor-driven visualization is required for this space.
- State streams are routed into explicit monitor ports (`state_a..state_d`) to avoid signal overwrite.
- At minimum, monitor visuals include one timeseries panel and one summary table.
- Rationale: A dedicated monitor model receives all participating model state streams (`state_a..state_d`) so trajectories can be compared in one place without claiming causal coupling when IO semantics are incomplete.

## Expected Behaviors
- Model output trajectories under shared runtime settings.
- Cross-model agreement/divergence in key state or metric signals.
- Relative behavior comparison without causal linkage claims.

## Known Limitations
- No new biology is introduced beyond what upstream models encode.
- Cross-model semantic matching is rule-based and may under-connect uncertain routes.

## Source Provenance
- immunology-sbml-puniya2021-cd4-th2-cell-metabolism-model-model1909260005-model :: biomodels_ebi:MODEL1909260005 :: https://www.ebi.ac.uk/biomodels/MODEL1909260005
- immunology-sbml-puniya2021-naive-cd4-t-cell-metabolic-model-model1909260003-model :: biomodels_ebi:MODEL1909260003 :: https://www.ebi.ac.uk/biomodels/MODEL1909260003
- immunology-sbml-rateitschak2012-interferon-gamma-ifn-induced-sta-biomd0000000585-model :: biomodels_ebi:BIOMD0000000585 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000585
- immunology-sbml-roy2019-a-vivid-cytokines-interaction-model-on-p-model1911070001-model :: biomodels_ebi:MODEL1911070001 :: https://www.ebi.ac.uk/biomodels/MODEL1911070001

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
