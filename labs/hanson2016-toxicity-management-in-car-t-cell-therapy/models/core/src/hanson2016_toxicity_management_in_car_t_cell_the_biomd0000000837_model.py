# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Hanson2016 - Toxicity Management in CAR T cell therapy for B-ALL."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Hanson2016ToxicityManagementInCarTCellTheBiomd0000000837Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000837."""

    _SBML_ID = 'BIOMD0000000837'
    _TITLE = 'Hanson2016 - Toxicity Management in CAR T cell therapy for B-ALL'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['C_m', 'C_e', 'H_m', 'H_e', 'L', 'Inflam', 'B', 'D']
    _SPECIES_LABELS = {'C_m': 'Unresolved Tumor Observable 1', 'C_e': 'Unresolved Tumor Observable 2', 'H_m': 'Unresolved Tumor Observable 3', 'H_e': 'Unresolved Tumor Observable 4', 'L': 'Unresolved Tumor Observable 5', 'Inflam': 'Inflam', 'B': 'B', 'D': 'D', 'ModelValue_16': 'Initial for l'}
    _PARAMETER_INPUTS = {'tumor_growth_rate': ('r_1', 0.003, 'native source value', 'Tumor Growth Rate. Sets bundled SBML parameter `r_1`.'), 'tumor_killing_c_e_rate': ('d_1', 0.0002, 'native source value', 'Tumor Killing C E Rate. Sets bundled SBML parameter `d_1`.'), 'inflammation_decay_rate': ('d_2', 1.5, 'native source value', 'Inflammation Decay Rate. Sets bundled SBML parameter `d_2`.'), 'cytotoxic_t_cells_effector_decay_rate': ('d_3', 0.004, 'native source value', 'Cytotoxic T Cells Effector Decay Rate. Sets bundled SBML parameter `d_3`.'), 'helper_t_cells_effector_decay_rate': ('d_4', 0.004, 'native source value', 'Helper T Cells Effector Decay Rate. Sets bundled SBML parameter `d_4`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('C_m', 10.0, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `C_m`.'), 'initial_unresolved_tumor_observable_2': ('C_e', 10.0, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `C_e`.'), 'initial_unresolved_tumor_observable_3': ('H_m', 10.0, 'native source value', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `H_m`.'), 'initial_unresolved_tumor_observable_4': ('H_e', 10.0, 'native source value', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `H_e`.'), 'initial_unresolved_tumor_observable_5': ('L', 1600.0, 'native source value', 'Initial Unresolved Tumor Observable 5. Sets the initial value of bundled SBML species `L`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('C_m', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `C_m`.'), 'unresolved_tumor_observable_2': ('C_e', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `C_e`.'), 'unresolved_tumor_observable_3': ('H_m', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `H_m`.'), 'unresolved_tumor_observable_4': ('H_e', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `H_e`.'), 'unresolved_tumor_observable_5': ('L', 'native source value', 'Unresolved Tumor Observable 5. Maps to bundled source symbol `L`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000837.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
