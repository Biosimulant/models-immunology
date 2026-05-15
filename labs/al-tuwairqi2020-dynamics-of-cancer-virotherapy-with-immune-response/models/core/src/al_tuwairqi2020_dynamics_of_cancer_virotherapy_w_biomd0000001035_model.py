# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Al-Tuwairqi2020 - Dynamics of cancer virotherapy with immune response."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class AlTuwairqi2020DynamicsOfCancerVirotherapyWBiomd0000001035Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000001035."""

    _SBML_ID = 'BIOMD0000001035'
    _TITLE = 'Al-Tuwairqi2020 - Dynamics of cancer virotherapy with immune response'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['uninfected_cancer_cells', 'infected_cancer_cells', 'free_virus', 'immune_cells']
    _SPECIES_LABELS = {'uninfected_cancer_cells': 'Uninfected Cancer Cells', 'infected_cancer_cells': 'Infected Cancer Cells', 'free_virus': 'Free Virus', 'immune_cells': 'Immune Cells'}
    _PARAMETER_INPUTS = {'tumor_growth_rate': ('r_1', 0.36, 'native source value', 'Tumor Growth Rate. Sets bundled SBML parameter `r_1`.'), 'cancer_cell_infection_rate': ('a', 0.5, 'native source value', 'Cancer Cell Infection Rate. Sets bundled SBML parameter `a`.'), 'uninfected_cancer_cell_killing_death_rate': ('d_1', 0.1278, 'native source value', 'Uninfected Cancer Cell Killing Death Rate. Sets bundled SBML parameter `d_1`.'), 'infected_cancer_cell_killing_death_rate': ('c', 0.48, 'native source value', 'Infected Cancer Cell Killing Death Rate. Sets bundled SBML parameter `c`.'), 'virus_release_rate': ('b', 2.0, 'native source value', 'Virus Release Rate. Sets bundled SBML parameter `b`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_uninfected_cancer_cells': ('uninfected_cancer_cells', 0.5, 'native source value', 'Initial Uninfected Cancer Cells. Sets the initial value of bundled SBML species `uninfected_cancer_cells`.'), 'initial_infected_cancer_cells': ('infected_cancer_cells', 0.0, 'native source value', 'Initial Infected Cancer Cells. Sets the initial value of bundled SBML species `infected_cancer_cells`.'), 'initial_free_virus': ('free_virus', 0.01, 'native source value', 'Initial Free Virus. Sets the initial value of bundled SBML species `free_virus`.'), 'initial_immune_cells': ('immune_cells', 0.01, 'native source value', 'Initial Immune Cells. Sets the initial value of bundled SBML species `immune_cells`.')}
    _HEADLINE_OUTPUTS = {'uninfected_cancer_cells': ('uninfected_cancer_cells', 'native source value', 'Uninfected Cancer Cells. Maps to bundled source symbol `uninfected_cancer_cells`.'), 'infected_cancer_cells': ('infected_cancer_cells', 'native source value', 'Infected Cancer Cells. Maps to bundled source symbol `infected_cancer_cells`.'), 'free_virus': ('free_virus', 'native source value', 'Free Virus. Maps to bundled source symbol `free_virus`.'), 'immune_cells': ('immune_cells', 'native source value', 'Immune Cells. Maps to bundled source symbol `immune_cells`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001035.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
