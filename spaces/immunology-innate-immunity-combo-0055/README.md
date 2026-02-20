# COMBO_0055 - Immunology Innate Immunity

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
- `immunology-sbml-almuallem2020-virus-macrophage-tumour-interactio-biomd0000001033-model`: Immunology: Almuallem2020VirusMacrophageTumourInteractioBiomd0000001033Model
- `immunology-sbml-anderson2015-qualitative-behavior-of-systems-of-biomd0000000813-model`: Immunology: Anderson2015QualitativeBehaviorOfSystemsOfBiomd0000000813Model
- `immunology-sbml-arciero2004-a-mathematical-model-of-tumor-immune-model1907310002-model`: Immunology: Arciero2004AMathematicalModelOfTumorImmuneModel1907310002Model

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
- immunology-sbml-almuallem2020-virus-macrophage-tumour-interactio-biomd0000001033-model :: biomodels_ebi:BIOMD0000001033 :: https://www.ebi.ac.uk/biomodels/BIOMD0000001033
- immunology-sbml-anderson2015-qualitative-behavior-of-systems-of-biomd0000000813-model :: biomodels_ebi:BIOMD0000000813 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000813
- immunology-sbml-arciero2004-a-mathematical-model-of-tumor-immune-model1907310002-model :: biomodels_ebi:MODEL1907310002 :: https://www.ebi.ac.uk/biomodels/MODEL1907310002

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
