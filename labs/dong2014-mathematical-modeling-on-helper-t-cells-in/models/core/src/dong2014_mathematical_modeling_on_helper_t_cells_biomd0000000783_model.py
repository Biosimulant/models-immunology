# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Dong2014 - Mathematical modeling on helper t cells in a tumor immune system."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Dong2014MathematicalModelingOnHelperTCellsBiomd0000000783Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000783."""

    _SBML_ID = 'BIOMD0000000783'
    _TITLE = 'Dong2014 - Mathematical modeling on helper t cells in a tumor immune system'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x_Tumor_Cells', 'y_Effector_Cells', 'z_Helper_T_Cells']
    _SPECIES_LABELS = {'x_Tumor_Cells': 'Tumor Cells', 'y_Effector_Cells': 'Effector Cells', 'z_Helper_T_Cells': 'Helper T Cells'}
    _PARAMETER_INPUTS = {'tumor_growth_rate': ('alpha', 1.636, 'native source value', 'Tumor Growth Rate. Sets bundled SBML parameter `alpha`.'), 'tumor_growth_rate_2': ('beta', 0.002, 'native source value', 'Tumor Growth Rate 2. Sets bundled SBML parameter `beta`.'), 'ec_natural_death_rate': ('delta_1', 0.3743, 'native source value', 'Ec Natural Death Rate. Sets bundled SBML parameter `delta_1`.'), 'htc_natural_death_rate': ('delta_2', 0.055, 'native source value', 'Htc Natural Death Rate. Sets bundled SBML parameter `delta_2`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_tumor_cells': ('x_Tumor_Cells', 1.0, 'native source value', 'Initial Tumor Cells. Sets the initial value of bundled SBML species `x_Tumor_Cells`.'), 'initial_effector_cells': ('y_Effector_Cells', 1.0, 'native source value', 'Initial Effector Cells. Sets the initial value of bundled SBML species `y_Effector_Cells`.'), 'initial_helper_t_cells': ('z_Helper_T_Cells', 1.0, 'native source value', 'Initial Helper T Cells. Sets the initial value of bundled SBML species `z_Helper_T_Cells`.')}
    _HEADLINE_OUTPUTS = {'tumor_cells': ('x_Tumor_Cells', 'native source value', 'Tumor Cells. Maps to bundled source symbol `x_Tumor_Cells`.'), 'effector_cells': ('y_Effector_Cells', 'native source value', 'Effector Cells. Maps to bundled source symbol `y_Effector_Cells`.'), 'helper_t_cells': ('z_Helper_T_Cells', 'native source value', 'Helper T Cells. Maps to bundled source symbol `z_Helper_T_Cells`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000783.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
