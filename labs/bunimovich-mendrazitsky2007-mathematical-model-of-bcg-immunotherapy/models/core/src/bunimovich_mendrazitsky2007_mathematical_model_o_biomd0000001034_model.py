# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Bunimovich-Mendrazitsky2007 - Mathematical model of BCG immunotherapy."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class BunimovichMendrazitsky2007MathematicalModelOBiomd0000001034Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000001034."""

    _SBML_ID = 'BIOMD0000001034'
    _TITLE = 'Bunimovich-Mendrazitsky2007 - Mathematical model of BCG immunotherapy'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['BCG', 'Effector_cells', 'Tumor_infected_cells', 'Tumor_uninfected_cells']
    _SPECIES_LABELS = {'BCG': 'BCG', 'Effector_cells': 'Effector Cells', 'Tumor_infected_cells': 'Tumor Infected Cells', 'Tumor_uninfected_cells': 'Tumor Uninfected Cells'}
    _PARAMETER_INPUTS = {'tumor_growth_rate': ('beta', 0.0155, 'native source value', 'Tumor Growth Rate. Sets bundled SBML parameter `beta`.'), 'tumor_growth_rate_2': ('r', 0.12, 'native source value', 'Tumor Growth Rate 2. Sets bundled SBML parameter `r`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_effector_cells': ('Effector_cells', 0.05, 'native source value', 'Initial Effector Cells. Sets the initial value of bundled SBML species `Effector_cells`.'), 'initial_tumor_infected_cells': ('Tumor_infected_cells', 0.0, 'native source value', 'Initial Tumor Infected Cells. Sets the initial value of bundled SBML species `Tumor_infected_cells`.'), 'initial_tumor_uninfected_cells': ('Tumor_uninfected_cells', 0.55, 'native source value', 'Initial Tumor Uninfected Cells. Sets the initial value of bundled SBML species `Tumor_uninfected_cells`.'), 'initial_bcg': ('BCG', 0.0, 'native source value', 'Initial BCG. Sets the initial value of bundled SBML species `BCG`.')}
    _HEADLINE_OUTPUTS = {'effector_cells': ('Effector_cells', 'native source value', 'Effector Cells. Maps to bundled source symbol `Effector_cells`.'), 'tumor_infected_cells': ('Tumor_infected_cells', 'native source value', 'Tumor Infected Cells. Maps to bundled source symbol `Tumor_infected_cells`.'), 'tumor_uninfected_cells': ('Tumor_uninfected_cells', 'native source value', 'Tumor Uninfected Cells. Maps to bundled source symbol `Tumor_uninfected_cells`.'), 'bcg': ('BCG', 'native source value', 'BCG. Maps to bundled source symbol `BCG`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001034.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
