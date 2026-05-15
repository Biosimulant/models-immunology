# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Wodarz2007 - HIV/CD4 T-cell interaction."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Wodarz2007HivCd4TCellInteractionBiomd0000000663Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000663."""

    _SBML_ID = 'BIOMD0000000663'
    _TITLE = 'Wodarz2007 - HIV/CD4 T-cell interaction'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x', 'y', 'v']
    _SPECIES_LABELS = {'x': 'T Cell Infected', 'y': 'T Cell Uninfected', 'v': 'Free Virus'}
    _PARAMETER_INPUTS = {'uninfected_t_cell_death_rate': ('d', 0.1, 'native source value', 'Uninfected T Cell Death Rate. Sets bundled SBML parameter `d`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_t_cell_infected': ('x', 0.1, 'native source value', 'Initial T Cell Infected. Sets the initial value of bundled SBML species `x`.'), 'initial_t_cell_uninfected': ('y', 0.0, 'native source value', 'Initial T Cell Uninfected. Sets the initial value of bundled SBML species `y`.'), 'initial_free_virus': ('v', 1.0, 'native source value', 'Initial Free Virus. Sets the initial value of bundled SBML species `v`.')}
    _HEADLINE_OUTPUTS = {'t_cell_infected': ('x', 'native source value', 'T Cell Infected. Maps to bundled source symbol `x`.'), 't_cell_uninfected': ('y', 'native source value', 'T Cell Uninfected. Maps to bundled source symbol `y`.'), 'free_virus': ('v', 'native source value', 'Free Virus. Maps to bundled source symbol `v`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000663.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
