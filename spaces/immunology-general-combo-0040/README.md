# COMBO_0040 - Immunology General

## Scientific Question
How do general mechanisms compare across these models?

## Biological Context
Innate/adaptive response dynamics and inflammatory signaling.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `immunology-sbml-leung2016-sirws-model-with-immune-boosting-and-c-model1808280006-model`: Immunology: Leung2016SirwsModelWithImmuneBoostingAndCModel1808280006Model
- `immunology-sbml-liu2017-chemotherapy-targeted-model-of-tumor-imm-biomd0000000930-model`: Immunology: Liu2017ChemotherapyTargetedModelOfTumorImmBiomd0000000930Model
- `immunology-sbml-liu2019-logistic-regression-models-to-predict-in-model2310150001-model`: Immunology: Liu2019LogisticRegressionModelsToPredictInModel2310150001Model

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
- immunology-sbml-leung2016-sirws-model-with-immune-boosting-and-c-model1808280006-model :: biomodels_ebi:MODEL1808280006 :: https://www.ebi.ac.uk/biomodels/MODEL1808280006
- immunology-sbml-liu2017-chemotherapy-targeted-model-of-tumor-imm-biomd0000000930-model :: biomodels_ebi:BIOMD0000000930 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000930
- immunology-sbml-liu2019-logistic-regression-models-to-predict-in-model2310150001-model :: biomodels_ebi:MODEL2310150001 :: https://www.ebi.ac.uk/biomodels/MODEL2310150001

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
