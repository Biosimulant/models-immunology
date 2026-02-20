# COMBO_0061 - Immunology Innate Immunity

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
- `immunology-sbml-hu2018-dynamics-of-tumor-cd4-cytokine-host-cells-biomd0000000797-model`: Immunology: Hu2018DynamicsOfTumorCd4CytokineHostCellsBiomd0000000797Model
- `immunology-sbml-immunological-healthy-state-model-of-sphingolipi-model2301110002-model`: Immunology: ImmunologicalHealthyStateModelOfSphingolipiModel2301110002Model
- `immunology-sbml-khandibharad2022-il-12-regulation-by-il-10-in-le-model2012040002-model`: Immunology: Khandibharad2022Il12RegulationByIl10InLeModel2012040002Model
- `immunology-sbml-kim2014-tumor-model-under-immune-suppression-model1909240002-model`: Immunology: Kim2014TumorModelUnderImmuneSuppressionModel1909240002Model

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
- immunology-sbml-hu2018-dynamics-of-tumor-cd4-cytokine-host-cells-biomd0000000797-model :: biomodels_ebi:BIOMD0000000797 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000797
- immunology-sbml-immunological-healthy-state-model-of-sphingolipi-model2301110002-model :: biomodels_ebi:MODEL2301110002 :: https://www.ebi.ac.uk/biomodels/MODEL2301110002
- immunology-sbml-khandibharad2022-il-12-regulation-by-il-10-in-le-model2012040002-model :: biomodels_ebi:MODEL2012040002 :: https://www.ebi.ac.uk/biomodels/MODEL2012040002
- immunology-sbml-kim2014-tumor-model-under-immune-suppression-model1909240002-model :: biomodels_ebi:MODEL1909240002 :: https://www.ebi.ac.uk/biomodels/MODEL1909240002

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
