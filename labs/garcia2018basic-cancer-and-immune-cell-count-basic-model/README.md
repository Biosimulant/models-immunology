# Garcia2018basic - cancer and immune cell count basic model Lab

Curated immunology lab using the bundled source model as the scientific source of truth.

## What You'll See

This captured run documents the default Garcia2018basic - cancer and immune cell count basic model configuration for 10.0 time units with a 1.0 communication step. Default inputs include Initial Unresolved Tumor Observable 1, Initial Unresolved Tumor Observable 2, Tumor Killing Rate, and Immune Cell Death Rate. Reported outputs include unresolved_tumor_observable_1, unresolved_tumor_observable_2, state, and summary. The screenshots below pair the run-interpretation table with Tumor-immune burden and Largest state excursions so the README shows both trajectories and the strongest state changes from the same dark-mode run.

<!-- BIOSIMULANT_VISUALS_START -->
### Output Visualizations

The run-interpretation table summarizes the configured Garcia2018basic - cancer and immune cell count basic model simulation and its final-state diagnostics.

![Garcia2018basic - cancer and immune cell count basic model Lab - run interpretation](assets/01-garcia2018basic-cancer-and-immune-cell-count-basic-model-lab-run-interpretation.png)

The Tumor-immune burden time series follows the selected immune, pathogen, tumor, or signaling quantities across the simulated horizon.

![Tumor-immune burden](assets/02-tumor-immune-burden.png)

The largest state excursions chart ranks the state variables that moved furthest during the run.

![Largest state excursions](assets/03-largest-state-excursions.png)

<!-- BIOSIMULANT_VISUALS_END -->
