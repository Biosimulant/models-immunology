# Malinzi2018 - tumour-immune interaction model Lab

Curated immunology lab using the bundled source model as the scientific source of truth.

## What You'll See

This captured run documents the default Malinzi2018 - tumour-immune interaction model configuration for 10.0 time units with a 1.0 communication step. Default inputs include Initial Immune Cell X, Initial Tumour Cell Y, Initial Dead Tumour Cell Ystar, and Initial Chemokine Concentration U. Reported outputs include immune_cell_x, tumour_cell_y, dead_tumour_cell_ystar, and chemokine_concentration_u. The screenshots below pair the run-interpretation table with Tumor-immune burden and Largest state excursions so the README shows both trajectories and the strongest state changes from the same dark-mode run.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

The run-interpretation table summarizes the configured Malinzi2018 - tumour-immune interaction model simulation and its final-state diagnostics.

![Malinzi2018 - tumour-immune interaction model Lab - run interpretation](assets/01-malinzi2018-tumour-immune-interaction-model-lab-run-interpretation.png)

The Tumor-immune burden time series follows the selected immune, pathogen, tumor, or signaling quantities across the simulated horizon.

![Tumor-immune burden](assets/02-tumor-immune-burden.png)

The largest state excursions chart ranks the state variables that moved furthest during the run.

![Largest state excursions](assets/03-largest-state-excursions.png)

<!-- BIOSIMULANT_VISUALS_END -->
