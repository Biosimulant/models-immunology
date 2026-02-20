# COMBO_0035 - Immunology General

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
- `immunology-sbml-isaeva2008-modelling-of-anti-tumour-immune-respo-biomd0000000910-model`: Immunology: Isaeva2008ModellingOfAntiTumourImmuneRespoBiomd0000000910Model
- `immunology-sbml-isaeva2009-different-strategies-for-cancer-treat-model2001140002-model`: Immunology: Isaeva2009DifferentStrategiesForCancerTreatModel2001140002Model
- `immunology-sbml-jarrah2014-mathematical-model-of-the-immune-resp-biomd0000001015-model`: Immunology: Jarrah2014MathematicalModelOfTheImmuneRespBiomd0000001015Model

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
- immunology-sbml-isaeva2008-modelling-of-anti-tumour-immune-respo-biomd0000000910-model :: biomodels_ebi:BIOMD0000000910 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000910
- immunology-sbml-isaeva2009-different-strategies-for-cancer-treat-model2001140002-model :: biomodels_ebi:MODEL2001140002 :: https://www.ebi.ac.uk/biomodels/MODEL2001140002
- immunology-sbml-jarrah2014-mathematical-model-of-the-immune-resp-biomd0000001015-model :: biomodels_ebi:BIOMD0000001015 :: https://www.ebi.ac.uk/biomodels/BIOMD0000001015

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
