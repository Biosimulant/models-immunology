# COMBO_0013 - Immunology Adaptive Immunity

## Scientific Question
How do adaptive immunity mechanisms compare across these models?

## Biological Context
Innate/adaptive response dynamics and inflammatory signaling.

## Mechanistic Assumptions
- Model implementations are used as published in their curated manifests without biological reinterpretation.
- Time integration uses a shared global tick compatible with model min_dt constraints.
- Comparative (non-causal) mode is used because full deterministic IO coverage for causal coupling was not satisfied.

## Why These Models Belong Together
The combination was selected from a shared domain/theme bucket with deterministic compatibility checks.
- `immunology-sbml-verma2016-hiv-and-hpv-co-infection-t-cell-respon-biomd0000000872-model`: Immunology: Verma2016HivAndHpvCoInfectionTCellResponBiomd0000000872Model
- `immunology-sbml-webb2002-fas-fasl-mediated-tumor-t-cell-interact-biomd0000000661-model`: Immunology: Webb2002FasFaslMediatedTumorTCellInteractBiomd0000000661Model

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
- immunology-sbml-verma2016-hiv-and-hpv-co-infection-t-cell-respon-biomd0000000872-model :: biomodels_ebi:BIOMD0000000872 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000872
- immunology-sbml-webb2002-fas-fasl-mediated-tumor-t-cell-interact-biomd0000000661-model :: biomodels_ebi:BIOMD0000000661 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000661

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
