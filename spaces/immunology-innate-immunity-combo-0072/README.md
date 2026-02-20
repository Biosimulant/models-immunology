# COMBO_0072 - Immunology Innate Immunity

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
- `immunology-sbml-wei2017-tumor-t-cell-and-cytokine-interaction-biomd0000000778-model`: Immunology: Wei2017TumorTCellAndCytokineInteractionBiomd0000000778Model
- `immunology-sbml-yamada2003-jak-stat-pathway-biomd0000000093-model`: Immunology: Yamada2003JakStatPathwayBiomd0000000093Model
- `immunology-sbml-yamada2003-jak-stat-socs1-knockout-biomd0000000094-model`: Immunology: Yamada2003JakStatSocs1KnockoutBiomd0000000094Model
- `immunology-sbml-yu2019-a-mathematical-model-of-tumor-immune-inte-model1911270002-model`: Immunology: Yu2019AMathematicalModelOfTumorImmuneInteModel1911270002Model

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
- immunology-sbml-wei2017-tumor-t-cell-and-cytokine-interaction-biomd0000000778-model :: biomodels_ebi:BIOMD0000000778 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000778
- immunology-sbml-yamada2003-jak-stat-pathway-biomd0000000093-model :: biomodels_ebi:BIOMD0000000093 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000093
- immunology-sbml-yamada2003-jak-stat-socs1-knockout-biomd0000000094-model :: biomodels_ebi:BIOMD0000000094 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000094
- immunology-sbml-yu2019-a-mathematical-model-of-tumor-immune-inte-model1911270002-model :: biomodels_ebi:MODEL1911270002 :: https://www.ebi.ac.uk/biomodels/MODEL1911270002

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
