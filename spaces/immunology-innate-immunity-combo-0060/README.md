# COMBO_0060 - Immunology Innate Immunity

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
- `immunology-sbml-fribourg2014-dynamics-of-viral-antagonism-and-in-biomd0000000528-model`: Immunology: Fribourg2014DynamicsOfViralAntagonismAndInBiomd0000000528Model
- `immunology-sbml-fribourg2014-dynamics-of-viral-antagonism-and-in-biomd0000000529-model`: Immunology: Fribourg2014DynamicsOfViralAntagonismAndInBiomd0000000529Model
- `immunology-sbml-he2017-a-mathematical-model-of-pancreatic-cancer-biomd0000000811-model`: Immunology: He2017AMathematicalModelOfPancreaticCancerBiomd0000000811Model
- `immunology-sbml-hernandez-vargas2012-innate-immune-system-dynami-biomd0000000710-model`: Immunology: HernandezVargas2012InnateImmuneSystemDynamiBiomd0000000710Model

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
- immunology-sbml-fribourg2014-dynamics-of-viral-antagonism-and-in-biomd0000000528-model :: biomodels_ebi:BIOMD0000000528 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000528
- immunology-sbml-fribourg2014-dynamics-of-viral-antagonism-and-in-biomd0000000529-model :: biomodels_ebi:BIOMD0000000529 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000529
- immunology-sbml-he2017-a-mathematical-model-of-pancreatic-cancer-biomd0000000811-model :: biomodels_ebi:BIOMD0000000811 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000811
- immunology-sbml-hernandez-vargas2012-innate-immune-system-dynami-biomd0000000710-model :: biomodels_ebi:BIOMD0000000710 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000710

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
