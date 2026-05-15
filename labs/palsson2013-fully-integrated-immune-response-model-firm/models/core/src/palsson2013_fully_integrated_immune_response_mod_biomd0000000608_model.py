# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Palsson2013 - Fully-integrated immune response model (FIRM)."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Palsson2013FullyIntegratedImmuneResponseModBiomd0000000608Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000608."""

    _SBML_ID = 'BIOMD0000000608'
    _TITLE = 'Palsson2013 - Fully-integrated immune response model (FIRM)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x_1', 'x_2', 'x_3', 'x_4', 'x_5', 'x_6', 'x_7', 'x_8', 'x_9', 'x_10', 'x_11', 'x_12', 'x_13', 'x_14', 'x_15', 'x_16', 'x_17', 'x_18', 'x_19', 'x_20', 'x_21', 'x_22', 'x_23', 'x_24', 'x_25', 'x_26', 'x_27', 'x_28', 'x_29', 'x_30', 'x_31', 'x_32', 'x_33', 'x_34', 'x_35', 'x_36', 'x_37', 'x_38', 'x_39', 'x_40', 'x_41', 'x_42', 'x_43', 'x_44', 'x_45', 'x_46', 'x_47', 'x_48', 'x_49', 'x_50', 'x_51', 'x_52']
    _SPECIES_LABELS = {'x_1': 'Unresolved Immune Observable 1', 'x_2': 'Unresolved Immune Observable 2', 'x_3': 'Unresolved Immune Observable 3', 'x_4': 'Unresolved Immune Observable 4', 'x_5': 'Unresolved Immune Observable 5', 'x_6': 'x_6', 'x_7': 'x_7', 'x_8': 'x_8', 'x_9': 'x_9', 'x_10': 'x_10', 'x_11': 'x_11', 'x_12': 'x_12', 'x_13': 'x_13', 'x_14': 'x_14', 'x_15': 'x_15', 'x_16': 'x_16', 'x_17': 'x_17', 'x_18': 'x_18', 'x_19': 'x_19', 'x_20': 'x_20', 'x_21': 'x_21', 'x_22': 'x_22', 'x_23': 'x_23', 'x_24': 'x_24', 'x_25': 'x_25', 'x_26': 'x_26', 'x_27': 'x_27', 'x_28': 'x_28', 'x_29': 'x_29', 'x_30': 'x_30', 'x_31': 'x_31', 'x_32': 'x_32', 'x_33': 'x_33', 'x_34': 'x_34', 'x_35': 'x_35', 'x_36': 'x_36', 'x_37': 'x_37', 'x_38': 'x_38', 'x_39': 'x_39', 'x_40': 'x_40', 'x_41': 'x_41', 'x_42': 'x_42', 'x_43': 'x_43', 'x_44': 'x_44', 'x_45': 'x_45', 'x_46': 'x_46', 'x_47': 'x_47', 'x_48': 'x_48', 'x_49': 'x_49', 'x_50': 'x_50', 'x_51': 'x_51', 'x_52': 'x_52'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_immune_observable_1': ('x_1', 100000000.0, 'native source value', 'Initial Unresolved Immune Observable 1. Sets the initial value of bundled SBML species `x_1`.'), 'initial_unresolved_immune_observable_2': ('x_2', 0.0, 'native source value', 'Initial Unresolved Immune Observable 2. Sets the initial value of bundled SBML species `x_2`.'), 'initial_unresolved_immune_observable_3': ('x_3', 1e-07, 'native source value', 'Initial Unresolved Immune Observable 3. Sets the initial value of bundled SBML species `x_3`.'), 'initial_unresolved_immune_observable_4': ('x_4', 100000.0, 'native source value', 'Initial Unresolved Immune Observable 4. Sets the initial value of bundled SBML species `x_4`.'), 'initial_unresolved_immune_observable_5': ('x_5', 0.0, 'native source value', 'Initial Unresolved Immune Observable 5. Sets the initial value of bundled SBML species `x_5`.')}
    _HEADLINE_OUTPUTS = {'unresolved_immune_observable_1': ('x_1', 'native source value', 'Unresolved Immune Observable 1. Maps to bundled source symbol `x_1`.'), 'unresolved_immune_observable_2': ('x_2', 'native source value', 'Unresolved Immune Observable 2. Maps to bundled source symbol `x_2`.'), 'unresolved_immune_observable_3': ('x_3', 'native source value', 'Unresolved Immune Observable 3. Maps to bundled source symbol `x_3`.'), 'unresolved_immune_observable_4': ('x_4', 'native source value', 'Unresolved Immune Observable 4. Maps to bundled source symbol `x_4`.'), 'unresolved_immune_observable_5': ('x_5', 'native source value', 'Unresolved Immune Observable 5. Maps to bundled source symbol `x_5`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000608.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
