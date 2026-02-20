# COMBO_0042 - Immunology General

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
- `immunology-sbml-macnamara2015-1-virotherapy-full-model-biomd0000000766-model`: Immunology: Macnamara20151VirotherapyFullModelBiomd0000000766Model
- `immunology-sbml-macnamara2015-2-virotherapy-virus-free-submodel-biomd0000000767-model`: Immunology: Macnamara20152VirotherapyVirusFreeSubmodelBiomd0000000767Model
- `immunology-sbml-mahasa2016-tumor-immune-surveillance-model2003040001-model`: Immunology: Mahasa2016TumorImmuneSurveillanceModel2003040001Model

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
- immunology-sbml-macnamara2015-1-virotherapy-full-model-biomd0000000766-model :: biomodels_ebi:BIOMD0000000766 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000766
- immunology-sbml-macnamara2015-2-virotherapy-virus-free-submodel-biomd0000000767-model :: biomodels_ebi:BIOMD0000000767 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000767
- immunology-sbml-mahasa2016-tumor-immune-surveillance-model2003040001-model :: biomodels_ebi:MODEL2003040001 :: https://www.ebi.ac.uk/biomodels/MODEL2003040001

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
