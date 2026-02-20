# COMBO_0054 - Immunology Inflammation

## Scientific Question
How do inflammation mechanisms compare across these models?

## Biological Context
Innate/adaptive response dynamics and inflammatory signaling.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `immunology-sbml-adrianne2018-modelling-combined-virotherapy-and-model1912120003-model`: Immunology: Adrianne2018ModellingCombinedVirotherapyAndModel1912120003Model
- `immunology-sbml-jarrett2015-modelling-the-interaction-between-im-biomd0000000920-model`: Immunology: Jarrett2015ModellingTheInteractionBetweenImBiomd0000000920Model
- `immunology-sbml-sanchez2017-inflammatory-responses-during-acute-model1606020000-model`: Immunology: Sanchez2017InflammatoryResponsesDuringAcuteModel1606020000Model

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
- immunology-sbml-adrianne2018-modelling-combined-virotherapy-and-model1912120003-model :: biomodels_ebi:MODEL1912120003 :: https://www.ebi.ac.uk/biomodels/MODEL1912120003
- immunology-sbml-jarrett2015-modelling-the-interaction-between-im-biomd0000000920-model :: biomodels_ebi:BIOMD0000000920 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000920
- immunology-sbml-sanchez2017-inflammatory-responses-during-acute-model1606020000-model :: biomodels_ebi:MODEL1606020000 :: https://www.ebi.ac.uk/biomodels/MODEL1606020000

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
