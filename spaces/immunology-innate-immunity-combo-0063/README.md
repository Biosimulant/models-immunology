# COMBO_0063 - Immunology Innate Immunity

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
- `immunology-sbml-manda2019-acute-hepatitis-b-virus-infection-mode-model1911280002-model`: Immunology: Manda2019AcuteHepatitisBVirusInfectionModeModel1911280002Model
- `immunology-sbml-maree2006-duca-type1diabetesmodel-biomd0000000381-model`: Immunology: Maree2006DucaType1diabetesmodelBiomd0000000381Model
- `immunology-sbml-miao2010-innate-and-adaptive-immune-responses-to-biomd0000000546-model`: Immunology: Miao2010InnateAndAdaptiveImmuneResponsesToBiomd0000000546Model
- `immunology-sbml-modeling-the-relevance-of-immune-and-metabolic-c-model2209160001-model`: Immunology: ModelingTheRelevanceOfImmuneAndMetabolicCModel2209160001Model

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
- immunology-sbml-manda2019-acute-hepatitis-b-virus-infection-mode-model1911280002-model :: biomodels_ebi:MODEL1911280002 :: https://www.ebi.ac.uk/biomodels/MODEL1911280002
- immunology-sbml-maree2006-duca-type1diabetesmodel-biomd0000000381-model :: biomodels_ebi:BIOMD0000000381 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000381
- immunology-sbml-miao2010-innate-and-adaptive-immune-responses-to-biomd0000000546-model :: biomodels_ebi:BIOMD0000000546 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000546
- immunology-sbml-modeling-the-relevance-of-immune-and-metabolic-c-model2209160001-model :: biomodels_ebi:MODEL2209160001 :: https://www.ebi.ac.uk/biomodels/MODEL2209160001

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
