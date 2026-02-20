# COMBO_0067 - Immunology Innate Immunity

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
- `immunology-sbml-sandip2013-modeling-the-dynamics-of-hepatitis-c-biomd0000000892-model`: Immunology: Sandip2013ModelingTheDynamicsOfHepatitisCBiomd0000000892Model
- `immunology-sbml-sandip2013-modeling-the-dynamics-of-hepatitis-c-model1912120002-model`: Immunology: Sandip2013ModelingTheDynamicsOfHepatitisCModel1912120002Model
- `immunology-sbml-schulz2009-th1-differentiation-biomd0000000215-model`: Immunology: Schulz2009Th1DifferentiationBiomd0000000215Model
- `immunology-sbml-smith2011-three-stage-innate-immune-response-to-biomd0000000924-model`: Immunology: Smith2011ThreeStageInnateImmuneResponseToBiomd0000000924Model

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
- immunology-sbml-sandip2013-modeling-the-dynamics-of-hepatitis-c-biomd0000000892-model :: biomodels_ebi:BIOMD0000000892 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000892
- immunology-sbml-sandip2013-modeling-the-dynamics-of-hepatitis-c-model1912120002-model :: biomodels_ebi:MODEL1912120002 :: https://www.ebi.ac.uk/biomodels/MODEL1912120002
- immunology-sbml-schulz2009-th1-differentiation-biomd0000000215-model :: biomodels_ebi:BIOMD0000000215 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000215
- immunology-sbml-smith2011-three-stage-innate-immune-response-to-biomd0000000924-model :: biomodels_ebi:BIOMD0000000924 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000924

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
