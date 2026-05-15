# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Malinzi2018 - tumour-immune interaction model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Malinzi2018TumourImmuneInteractionModelBiomd0000000809Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000809."""

    _SBML_ID = 'BIOMD0000000809'
    _TITLE = 'Malinzi2018 - tumour-immune interaction model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x', 'y', 'u', 'ystar']
    _SPECIES_LABELS = {'x': 'Immune Cell X', 'y': 'Tumour Cell Y', 'u': 'Chemokine Concentration U', 'ystar': 'Dead Tumour Cell Ystar'}
    _PARAMETER_INPUTS = {'immune_cell_x_proliferation_rate': ('delta', 3.0218, 'native source value', 'Immune Cell X Proliferation Rate. Sets bundled SBML parameter `delta`.'), 'immune_cell_x_proliferation_rate_2': ('gamma', 2.02, 'native source value', 'Immune Cell X Proliferation Rate 2. Sets bundled SBML parameter `gamma`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_immune_cell_x': ('x', 0.3, 'native source value', 'Initial Immune Cell X. Sets the initial value of bundled SBML species `x`.'), 'initial_tumour_cell_y': ('y', 0.8, 'native source value', 'Initial Tumour Cell Y. Sets the initial value of bundled SBML species `y`.'), 'initial_dead_tumour_cell_ystar': ('ystar', 0.1, 'native source value', 'Initial Dead Tumour Cell Ystar. Sets the initial value of bundled SBML species `ystar`.'), 'initial_chemokine_concentration_u': ('u', 1e-06, 'native source value', 'Initial Chemokine Concentration U. Sets the initial value of bundled SBML species `u`.')}
    _HEADLINE_OUTPUTS = {'immune_cell_x': ('x', 'native source value', 'Immune Cell X. Maps to bundled source symbol `x`.'), 'tumour_cell_y': ('y', 'native source value', 'Tumour Cell Y. Maps to bundled source symbol `y`.'), 'dead_tumour_cell_ystar': ('ystar', 'native source value', 'Dead Tumour Cell Ystar. Maps to bundled source symbol `ystar`.'), 'chemokine_concentration_u': ('u', 'native source value', 'Chemokine Concentration U. Maps to bundled source symbol `u`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000809.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
