# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Alharbi2020 - An ODE-based model of the dynamics of tumor cell progression and its effects on normal cell growth and immune system functionality."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Alharbi2020AnOdeBasedModelOfTheDynamicsOBiomd0000001023Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000001023."""

    _SBML_ID = 'BIOMD0000001023'
    _TITLE = 'Alharbi2020 - An ODE-based model of the dynamics of tumor cell progression and its effects on normal cell growth and immune system functionality'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Normal_cells', 'Tumor_cells', 'Immune_cells']
    _SPECIES_LABELS = {'Normal_cells': 'Normal Cells', 'Tumor_cells': 'Tumor Cells', 'Immune_cells': 'Immune Cells'}
    _PARAMETER_INPUTS = {'normal_cell_growth_rate': ('r', 0.4312, 'native source value', 'Normal Cell Growth Rate. Sets bundled SBML parameter `r`.'), 'normal_cell_growth_rate_2': ('beta_1', 2.99e-06, 'native source value', 'Normal Cell Growth Rate 2. Sets bundled SBML parameter `beta_1`.'), 'normal_cell_death_inhibition_rate': ('gamma', 0.9314, 'native source value', 'Normal Cell Death Inhibition Rate. Sets bundled SBML parameter `gamma`.'), 'tumor_cell_growth_rate': ('alpha_1', 0.4426, 'native source value', 'Tumor Cell Growth Rate. Sets bundled SBML parameter `alpha_1`.'), 'tumor_cell_growth_rate_2': ('alpha_2', 0.4, 'native source value', 'Tumor Cell Growth Rate 2. Sets bundled SBML parameter `alpha_2`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_tumor_cells': ('Tumor_cells', 1.0, 'native source value', 'Initial Tumor Cells. Sets the initial value of bundled SBML species `Tumor_cells`.'), 'initial_immune_cells': ('Immune_cells', 1.22, 'native source value', 'Initial Immune Cells. Sets the initial value of bundled SBML species `Immune_cells`.'), 'initial_normal_cells': ('Normal_cells', 1.0, 'native source value', 'Initial Normal Cells. Sets the initial value of bundled SBML species `Normal_cells`.')}
    _HEADLINE_OUTPUTS = {'tumor_cells': ('Tumor_cells', 'native source value', 'Tumor Cells. Maps to bundled source symbol `Tumor_cells`.'), 'immune_cells': ('Immune_cells', 'native source value', 'Immune Cells. Maps to bundled source symbol `Immune_cells`.'), 'normal_cells': ('Normal_cells', 'native source value', 'Normal Cells. Maps to bundled source symbol `Normal_cells`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001023.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
