# models-immunology

Curated collection of **immunology** simulation models for the **biosim** platform. This repository contains comprehensive computational models of immune system dynamics, including T cell and B cell regulation, tumor-immune interactions, viral infections, immunotherapy, cytokine signaling, and immune response mechanisms.

## What's Inside

### Models (211 packages)

Each model is a self-contained simulation component with a `model.yaml` manifest, spanning innate and adaptive immunity, cancer immunology, infectious disease immunology, and immunotherapy.

**Immunology** — immune system dynamics, host-pathogen interactions, and immune-mediated therapies:

#### Key Model Categories

**T Cell Biology & Regulation:**
- CD4+ and CD8+ T cell dynamics and activation
- T regulatory cell (Treg) suppression mechanisms
- T cell differentiation and polarization (Th1, Th2, Th17)
- T follicular helper (Tfh) cell regulation
- Thymic selection and T cell development

**Tumor-Immune Interactions:**
- Tumor growth with immune surveillance and escape
- Cancer immunotherapy response modeling
- Oncolytic virotherapy combined with immunotherapy
- Checkpoint inhibitor dynamics (anti-PD-1, anti-CTLA-4)
- CAR-T cell therapy modeling
- Tumor-infiltrating lymphocyte (TIL) dynamics

**Viral Infections & Immune Response:**
- HIV latency and immune system interactions
- Influenza infection and immune clearance
- Hepatitis B/C viral dynamics with immune control
- SARS-CoV-2 infection and immune response
- Chronic viral infection and exhaustion

**Cytokine Signaling & Inflammation:**
- Interleukin signaling networks (IL-2, IL-6, IL-10, IL-12, IL-17)
- TNF-α and NF-κB inflammatory pathways
- Interferon (IFN-α, IFN-γ) antiviral responses
- TGF-β immunosuppressive signaling
- Cytokine-mediated inflammation in autoimmune diseases

**Innate Immunity:**
- Macrophage polarization (M1/M2)
- Natural killer (NK) cell cytotoxicity
- Dendritic cell maturation and antigen presentation
- Complement system activation
- Pattern recognition receptor (PRR) signaling

**B Cell & Antibody Responses:**
- B cell activation and differentiation
- Antibody production and class switching
- Germinal center dynamics
- Memory B cell formation
- Antibody-dependent cellular cytotoxicity (ADCC)

**Autoimmunity & Immune Dysregulation:**
- Rheumatoid arthritis inflammatory networks
- Systemic lupus erythematosus (SLE) models
- Multiple sclerosis immune-mediated demyelination
- Type 1 diabetes autoimmune destruction

**Immunotherapy & Interventions:**
- Checkpoint blockade therapy
- Adoptive cell transfer (ACT) therapies
- Vaccine-induced immune response
- Immunomodulatory drug effects
- Combination immunotherapy strategies

**Note:** This repository contains 211 models covering comprehensive aspects of immunology from molecular signaling to whole-organism immune dynamics. For a complete list, see the `models/` directory.

## Layout

```
models-immunology/
├── models/<model-slug>/     # One model package per folder, each with model.yaml
├── libs/                    # Shared helper code for curated models
├── templates/model-pack/    # Starter template for new model packs
├── scripts/                 # Manifest and entrypoint validation scripts
├── docs/                    # Governance documentation
└── .github/workflows/       # CI/CD pipeline
```

## How It Works

### Model Interface

Every model implements the `biosim.BioModule` interface:

- **`inputs()`** — declares named input signals the module consumes
- **`outputs()`** — declares named output signals the module produces
- **`advance_to(t)`** — advances the model's internal state to time `t`

Models can be composed to simulate multi-scale immune responses from molecular signaling → cellular dynamics → tissue-level immunity.

### Model Standards

All models in this repository:
- Use SBML (Systems Biology Markup Language) format
- Are sourced from BioModels and immunology-specific repositories
- Include tellurium runtime for SBML execution
- Provide `state` output for monitoring immune dynamics
- Support configurable timesteps via `min_dt` parameter

## Getting Started

### Prerequisites

- Python 3.11+
- `biosim` framework

### Install biosim

```bash
pip install "biosim @ git+https://github.com/BioSimulant/biosim.git@main"
```

### Using Models

To integrate immunology models:

1. Reference models by `manifest_path` (e.g., `models/immunology-sbml-alexander2010-tcell-regulation-sys1/model.yaml`)
2. Wire immune cell populations to cytokine signals and tumor dynamics
3. Compose multi-scale immune system simulations
4. Configure simulation parameters for acute vs chronic responses

## Validation & CI

Three scripts enforce repository integrity on every push:

| Script | Purpose |
|--------|---------|
| `scripts/validate_manifests.py` | Schema validation for all model.yaml files |
| `scripts/check_entrypoints.py` | Verifies Python entrypoints are importable and callable |
| `scripts/check_public_boundary.sh` | Prevents business-sensitive content in this public repo |

The CI pipeline runs: **secret scan** → **manifest validation** → **smoke sandbox** (Docker).

## Contributing

- All dependencies must use exact version pinning (`==`)
- Model slugs use kebab-case with domain prefix (`immunology-sbml-`)
- Models must follow the `biosim.BioModule` interface
- SBML models use tellurium runtime for execution

## Domain-Specific Notes

**Immunology Focus Areas:**
- **Adaptive Immunity**: T and B cell-mediated responses, memory formation, tolerance
- **Innate Immunity**: Macrophages, NK cells, dendritic cells, complement
- **Tumor Immunology**: Immune surveillance, escape mechanisms, immunotherapy
- **Infection & Immunity**: Viral/bacterial clearance, chronic infection, immune exhaustion
- **Cytokine Networks**: Pro-inflammatory vs anti-inflammatory balance, feedback regulation
- **Autoimmunity**: Loss of self-tolerance, inflammatory cascades
- **Immunotherapy**: Checkpoint blockade, CAR-T, vaccines, combination therapies
- **Multi-Scale Modeling**: From receptor signaling → cell activation → tissue inflammation → systemic immunity

## License

This repository is dual-licensed:

- **Code** (scripts, templates, Python modules): Apache-2.0 (`LICENSE-CODE.txt`)
- **Model/content** (manifests, docs, wiring/config): CC BY 4.0 (`LICENSE-CONTENT.txt`)

Attribution guidance: `ATTRIBUTION.md`
