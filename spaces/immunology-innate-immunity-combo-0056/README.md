# COMBO_0056 - Immunology Innate Immunity

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
- `immunology-sbml-bachmann2011-division-of-labor-by-dual-feedback-biomd0000000861-model`: Immunology: Bachmann2011DivisionOfLaborByDualFeedbackBiomd0000000861Model
- `immunology-sbml-baker2013-cytokine-mediated-inflammation-in-rheu-biomd0000000549-model`: Immunology: Baker2013CytokineMediatedInflammationInRheuBiomd0000000549Model
- `immunology-sbml-baker2013-cytokine-mediated-inflammation-in-rheu-biomd0000000550-model`: Immunology: Baker2013CytokineMediatedInflammationInRheuBiomd0000000550Model
- `immunology-sbml-begitt2014-stat1-cooperative-dna-binding-double-biomd0000000501-model`: Immunology: Begitt2014Stat1CooperativeDnaBindingDoubleBiomd0000000501Model

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
- immunology-sbml-bachmann2011-division-of-labor-by-dual-feedback-biomd0000000861-model :: biomodels_ebi:BIOMD0000000861 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000861
- immunology-sbml-baker2013-cytokine-mediated-inflammation-in-rheu-biomd0000000549-model :: biomodels_ebi:BIOMD0000000549 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000549
- immunology-sbml-baker2013-cytokine-mediated-inflammation-in-rheu-biomd0000000550-model :: biomodels_ebi:BIOMD0000000550 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000550
- immunology-sbml-begitt2014-stat1-cooperative-dna-binding-double-biomd0000000501-model :: biomodels_ebi:BIOMD0000000501 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000501

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
