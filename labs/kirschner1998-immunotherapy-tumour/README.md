# Kirschner1998 Immunotherapy Tumour Lab

Curated immunology lab using the bundled source model as the scientific source of truth.

## What You'll See

This captured run documents the default Kirschner1998 Immunotherapy Tumour configuration for 10.0 time units with a 1.0 communication step. Default inputs include Initial Tumor, Initial Immune Cells, and Initial Interleukin 2. Reported outputs include tumor, immune_cells, source, and sink. The screenshots below pair the run-interpretation table with Tumor-immune burden and Largest state excursions so the README shows both trajectories and the strongest state changes from the same dark-mode run.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

The run-interpretation table summarizes the configured Kirschner1998 Immunotherapy Tumour simulation and its final-state diagnostics.

![Kirschner1998_Immunotherapy_Tumour Lab - run interpretation](assets/01-kirschner1998-immunotherapy-tumour-lab-run-interpretation.png)

The Tumor-immune burden time series follows the selected immune, pathogen, tumor, or signaling quantities across the simulated horizon.

![Tumor-immune burden](assets/02-tumor-immune-burden.png)

The largest state excursions chart ranks the state variables that moved furthest during the run.

![Largest state excursions](assets/03-largest-state-excursions.png)

<!-- BIOSIMULANT_VISUALS_END -->
