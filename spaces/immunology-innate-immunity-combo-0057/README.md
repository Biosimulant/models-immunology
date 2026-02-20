# COMBO_0057 - Immunology Innate Immunity

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
- `immunology-sbml-begitt2014-stat1-cooperative-dna-binding-single-biomd0000000500-model`: Immunology: Begitt2014Stat1CooperativeDnaBindingSingleBiomd0000000500Model
- `immunology-sbml-boer1985-macrophage-t-cell-interaction-in-anti-t-model1911130003-model`: Immunology: Boer1985MacrophageTCellInteractionInAntiTModel1911130003Model
- `immunology-sbml-bordbar2010-m-tuberculosis-macrophage-model1011090002-model`: Immunology: Bordbar2010MTuberculosisMacrophageModel1011090002Model
- `immunology-sbml-bordbar2010-macrophage-metabolism-model1011090001-model`: Immunology: Bordbar2010MacrophageMetabolismModel1011090001Model

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
- immunology-sbml-begitt2014-stat1-cooperative-dna-binding-single-biomd0000000500-model :: biomodels_ebi:BIOMD0000000500 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000500
- immunology-sbml-boer1985-macrophage-t-cell-interaction-in-anti-t-model1911130003-model :: biomodels_ebi:MODEL1911130003 :: https://www.ebi.ac.uk/biomodels/MODEL1911130003
- immunology-sbml-bordbar2010-m-tuberculosis-macrophage-model1011090002-model :: biomodels_ebi:MODEL1011090002 :: https://www.ebi.ac.uk/biomodels/MODEL1011090002
- immunology-sbml-bordbar2010-macrophage-metabolism-model1011090001-model :: biomodels_ebi:MODEL1011090001 :: https://www.ebi.ac.uk/biomodels/MODEL1011090001

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
