# COMBO_0053 - Immunology General

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
- `immunology-sbml-scharf2023-holistic-view-on-the-structure-of-imm-model2304260001-model`: Immunology: Scharf2023HolisticViewOnTheStructureOfImmModel2304260001Model
- `immunology-sbml-schokker2013-a-mathematical-model-representing-c-biomd0000000895-model`: Immunology: Schokker2013AMathematicalModelRepresentingCBiomd0000000895Model
- `immunology-sbml-shin2019-regulation-of-nuclear-factor-of-activat-model2003200002-model`: Immunology: Shin2019RegulationOfNuclearFactorOfActivatModel2003200002Model

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
- immunology-sbml-scharf2023-holistic-view-on-the-structure-of-imm-model2304260001-model :: biomodels_ebi:MODEL2304260001 :: https://www.ebi.ac.uk/biomodels/MODEL2304260001
- immunology-sbml-schokker2013-a-mathematical-model-representing-c-biomd0000000895-model :: biomodels_ebi:BIOMD0000000895 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000895
- immunology-sbml-shin2019-regulation-of-nuclear-factor-of-activat-model2003200002-model :: biomodels_ebi:MODEL2003200002 :: https://www.ebi.ac.uk/biomodels/MODEL2003200002

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
