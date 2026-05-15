# Owen1998 - Tumour treatment model Lab

Curated immunology lab using the bundled source model as the scientific source of truth.

## What You'll See

This captured run documents the default Owen1998 - Tumour treatment model configuration for 10.0 time units with a 1.0 communication step. Default inputs include Treatment Start Parameter and Treatment End Parameter. Reported outputs include macrophage, mutated_cell, normal_cell, and state. The screenshots below pair the run-interpretation table with Tumor-immune burden and Largest state excursions so the README shows both trajectories and the strongest state changes from the same dark-mode run.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

The run-interpretation table summarizes the configured Owen1998 - Tumour treatment model simulation and its final-state diagnostics.

![Owen1998 - Tumour treatment model Lab - run interpretation](assets/01-owen1998-tumour-treatment-model-lab-run-interpretation.png)

The Tumor-immune burden time series follows the selected immune, pathogen, tumor, or signaling quantities across the simulated horizon.

![Tumor-immune burden](assets/02-tumor-immune-burden.png)

The largest state excursions chart ranks the state variables that moved furthest during the run.

![Largest state excursions](assets/03-largest-state-excursions.png)

<!-- BIOSIMULANT_VISUALS_END -->
