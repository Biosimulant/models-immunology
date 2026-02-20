# COMBO_0059 - Immunology Innate Immunity

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
- `immunology-sbml-eftimie2017-2-interaction-of-th-and-macrophage-i-biomd0000000769-model`: Immunology: Eftimie20172InteractionOfThAndMacrophageIBiomd0000000769Model
- `immunology-sbml-ewald2021-innate-immune-response-during-invasive-model2105110001-model`: Immunology: Ewald2021InnateImmuneResponseDuringInvasiveModel2105110001Model
- `immunology-sbml-fatehichenar2018-mathematical-model-of-immune-re-biomd0000000848-model`: Immunology: Fatehichenar2018MathematicalModelOfImmuneReBiomd0000000848Model
- `immunology-sbml-frank2021-macrophage-polarization-biomd0000001060-model`: Immunology: Frank2021MacrophagePolarizationBiomd0000001060Model

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
- immunology-sbml-eftimie2017-2-interaction-of-th-and-macrophage-i-biomd0000000769-model :: biomodels_ebi:BIOMD0000000769 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000769
- immunology-sbml-ewald2021-innate-immune-response-during-invasive-model2105110001-model :: biomodels_ebi:MODEL2105110001 :: https://www.ebi.ac.uk/biomodels/MODEL2105110001
- immunology-sbml-fatehichenar2018-mathematical-model-of-immune-re-biomd0000000848-model :: biomodels_ebi:BIOMD0000000848 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000848
- immunology-sbml-frank2021-macrophage-polarization-biomd0000001060-model :: biomodels_ebi:BIOMD0000001060 :: https://www.ebi.ac.uk/biomodels/BIOMD0000001060

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
