# COMBO_0068 - Immunology Innate Immunity

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
- `immunology-sbml-trisilowati2018-optimal-control-of-tumor-immune-biomd0000000880-model`: Immunology: Trisilowati2018OptimalControlOfTumorImmuneBiomd0000000880Model
- `immunology-sbml-tsirvouli2021-cytokine-and-eicosanoid-signaling-model2109300001-model`: Immunology: Tsirvouli2021CytokineAndEicosanoidSignalingModel2109300001Model
- `immunology-sbml-waugh2006-diabetic-wound-healing-macrophage-dyna-biomd0000000679-model`: Immunology: Waugh2006DiabeticWoundHealingMacrophageDynaBiomd0000000679Model
- `immunology-sbml-waugh2006-diabetic-wound-healing-tgf-b-dynamics-biomd0000000680-model`: Immunology: Waugh2006DiabeticWoundHealingTgfBDynamicsBiomd0000000680Model

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
- immunology-sbml-trisilowati2018-optimal-control-of-tumor-immune-biomd0000000880-model :: biomodels_ebi:BIOMD0000000880 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000880
- immunology-sbml-tsirvouli2021-cytokine-and-eicosanoid-signaling-model2109300001-model :: biomodels_ebi:MODEL2109300001 :: https://www.ebi.ac.uk/biomodels/MODEL2109300001
- immunology-sbml-waugh2006-diabetic-wound-healing-macrophage-dyna-biomd0000000679-model :: biomodels_ebi:BIOMD0000000679 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000679
- immunology-sbml-waugh2006-diabetic-wound-healing-tgf-b-dynamics-biomd0000000680-model :: biomodels_ebi:BIOMD0000000680 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000680

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
