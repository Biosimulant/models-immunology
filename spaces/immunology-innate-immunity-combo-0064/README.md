# COMBO_0064 - Immunology Innate Immunity

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
- `immunology-sbml-mol2013-leishmania-macrophage-signaling-network-model1203220000-model`: Immunology: Mol2013LeishmaniaMacrophageSignalingNetworkModel1203220000Model
- `immunology-sbml-owen1998-tumour-treatment-model-biomd0000000650-model`: Immunology: Owen1998TumourTreatmentModelBiomd0000000650Model
- `immunology-sbml-palmer2008-negative-feedback-in-il-7-mediated-ja-biomd0000000968-model`: Immunology: Palmer2008NegativeFeedbackInIl7MediatedJaBiomd0000000968Model
- `immunology-sbml-parra-guillen2013-mathematical-model-approach-to-biomd0000000914-model`: Immunology: ParraGuillen2013MathematicalModelApproachToBiomd0000000914Model

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
- immunology-sbml-mol2013-leishmania-macrophage-signaling-network-model1203220000-model :: biomodels_ebi:MODEL1203220000 :: https://www.ebi.ac.uk/biomodels/MODEL1203220000
- immunology-sbml-owen1998-tumour-treatment-model-biomd0000000650-model :: biomodels_ebi:BIOMD0000000650 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000650
- immunology-sbml-palmer2008-negative-feedback-in-il-7-mediated-ja-biomd0000000968-model :: biomodels_ebi:BIOMD0000000968 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000968
- immunology-sbml-parra-guillen2013-mathematical-model-approach-to-biomd0000000914-model :: biomodels_ebi:BIOMD0000000914 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000914

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
