# COMBO_0036 - Immunology General

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
- `immunology-sbml-jarrett2018-trastuzumab-induced-immune-response-biomd0000000745-model`: Immunology: Jarrett2018TrastuzumabInducedImmuneResponseBiomd0000000745Model
- `immunology-sbml-kareva2010-myeloid-cells-in-tumour-immune-intera-model2001310001-model`: Immunology: Kareva2010MyeloidCellsInTumourImmuneInteraModel2001310001Model
- `immunology-sbml-khajanchi2017-uniform-persistence-and-global-sta-biomd0000000921-model`: Immunology: Khajanchi2017UniformPersistenceAndGlobalStaBiomd0000000921Model

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
- immunology-sbml-jarrett2018-trastuzumab-induced-immune-response-biomd0000000745-model :: biomodels_ebi:BIOMD0000000745 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000745
- immunology-sbml-kareva2010-myeloid-cells-in-tumour-immune-intera-model2001310001-model :: biomodels_ebi:MODEL2001310001 :: https://www.ebi.ac.uk/biomodels/MODEL2001310001
- immunology-sbml-khajanchi2017-uniform-persistence-and-global-sta-biomd0000000921-model :: biomodels_ebi:BIOMD0000000921 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000921

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
