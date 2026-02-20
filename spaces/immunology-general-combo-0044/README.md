# COMBO_0044 - Immunology General

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
- `immunology-sbml-miao2014-dynamics-and-migratory-pathways-of-viru-model1411130000-model`: Immunology: Miao2014DynamicsAndMigratoryPathwaysOfViruModel1411130000Model
- `immunology-sbml-model1207300000-url-xml-model1207300000-model`: Immunology: Model1207300000UrlXmlModel1207300000Model
- `immunology-sbml-mol2013-immune-signal-transduction-in-leishmania-biomd0000000477-model`: Immunology: Mol2013ImmuneSignalTransductionInLeishmaniaBiomd0000000477Model

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
- immunology-sbml-miao2014-dynamics-and-migratory-pathways-of-viru-model1411130000-model :: biomodels_ebi:MODEL1411130000 :: https://www.ebi.ac.uk/biomodels/MODEL1411130000
- immunology-sbml-model1207300000-url-xml-model1207300000-model :: biomodels_ebi:MODEL1207300000 :: https://www.ebi.ac.uk/biomodels/MODEL1207300000
- immunology-sbml-mol2013-immune-signal-transduction-in-leishmania-biomd0000000477-model :: biomodels_ebi:BIOMD0000000477 :: https://www.ebi.ac.uk/biomodels/BIOMD0000000477

## How to Run
```bash
python run_local.py --duration auto --tick-dt auto
```

## How to Interpret Outputs
Use output trajectories and summary metrics to compare mechanistic consistency across constituent models.
Interpret comparative spaces as non-causal side-by-side simulation views.
