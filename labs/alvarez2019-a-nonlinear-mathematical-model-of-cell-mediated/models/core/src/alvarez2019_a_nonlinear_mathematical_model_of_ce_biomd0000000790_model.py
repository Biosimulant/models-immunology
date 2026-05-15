# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Alvarez2019 - A nonlinear mathematical model of cell-mediated immune response for tumor phenotypic heterogeneity."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Alvarez2019ANonlinearMathematicalModelOfCeBiomd0000000790Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000790."""

    _SBML_ID = 'BIOMD0000000790'
    _TITLE = 'Alvarez2019 - A nonlinear mathematical model of cell-mediated immune response for tumor phenotypic heterogeneity'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T_1', 'T_2', 'E_1_Innate', 'E_2_Adaptive']
    _SPECIES_LABELS = {'T_1': 'Unresolved Tumor Observable 1', 'T_2': 'Unresolved Tumor Observable 2', 'E_1_Innate': 'Unresolved Tumor Observable 3', 'E_2_Adaptive': 'Unresolved Tumor Observable 4'}
    _PARAMETER_INPUTS = {'tumor_killing_t1_e2_rate': ('beta', 1.101e-10, 'native source value', 'Tumor Killing T1 E2 Rate. Sets bundled SBML parameter `beta`.'), 'e1_death_rate': ('c_2', 0.0412, 'native source value', 'E1 Death Rate. Sets bundled SBML parameter `c_2`.'), 'e2_death_rate': ('d_3', 0.02, 'native source value', 'E2 Death Rate. Sets bundled SBML parameter `d_3`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('T_1', 80000000.0, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `T_1`.'), 'initial_unresolved_tumor_observable_2': ('T_2', 20000000.0, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `T_2`.'), 'initial_unresolved_tumor_observable_3': ('E_1_Innate', 10500000.0, 'native source value', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `E_1_Innate`.'), 'initial_unresolved_tumor_observable_4': ('E_2_Adaptive', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `E_2_Adaptive`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('T_1', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `T_1`.'), 'unresolved_tumor_observable_2': ('T_2', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `T_2`.'), 'unresolved_tumor_observable_3': ('E_1_Innate', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `E_1_Innate`.'), 'unresolved_tumor_observable_4': ('E_2_Adaptive', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `E_2_Adaptive`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000790.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
