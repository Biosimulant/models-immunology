# COMBO_0058 - Immunology Innate Immunity

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
- `immunology-sbml-carbo2013-cytokine-driven-cd4-t-cell-differentia-biomd0000000451-model`: Immunology: Carbo2013CytokineDrivenCd4TCellDifferentiaBiomd0000000451Model
- `immunology-sbml-day2015-early-cellular-innate-and-adaptive-immun-model1911190001-model`: Immunology: Day2015EarlyCellularInnateAndAdaptiveImmunModel1911190001Model
- `immunology-sbml-den-breems2015-macrophage-in-cancer-biomd0000000759-model`: Immunology: DenBreems2015MacrophageInCancerBiomd0000000759Model
- `immunology-sbml-eftimie2017-1-interaction-of-th-and-macrophage-biomd0000000770-model`: Immunology: Eftimie20171InteractionOfThAndMacrophageBiomd0000000770Model

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
- immunology-sbml-carbo2013-cytokine-driven-cd4-t-cell-differentia-biomd0000000451-model :: biomodels_ebi:BIOMD0000000451 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000451
- immunology-sbml-day2015-early-cellular-innate-and-adaptive-immun-model1911190001-model :: biomodels_ebi:MODEL1911190001 :: https://www.ebi.ac.uk/biomodels/MODEL1911190001
- immunology-sbml-den-breems2015-macrophage-in-cancer-biomd0000000759-model :: biomodels_ebi:BIOMD0000000759 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000759
- immunology-sbml-eftimie2017-1-interaction-of-th-and-macrophage-biomd0000000770-model :: biomodels_ebi:BIOMD0000000770 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000770

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
