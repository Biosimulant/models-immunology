# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Begitt2014 - STAT1 cooperative DNA binding - double GAS polymer model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Begitt2014Stat1CooperativeDnaBindingDoubleBiomd0000000501Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000501."""

    _SBML_ID = 'BIOMD0000000501'
    _TITLE = 'Begitt2014 - STAT1 cooperative DNA binding - double GAS polymer model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S1', 'DNA0000', 'DNA0001', 'DNA0010', 'DNA0100', 'DNA1000', 'DNA1100', 'DNA1010', 'DNA1001', 'DNA0110', 'DNA0101', 'DNA0011', 'DNA1110', 'DNA1011', 'DNA1101', 'DNA0111', 'DNA1111', 'DNA001_1', 'DNA01_10', 'DNA01_11', 'DNA011_1', 'DNA01_1_1', 'DNA101_1', 'DNA1_100', 'DNA1_101', 'DNA1_110', 'DNA11_10', 'DNA1_1_10', 'DNA1_111', 'DNA11_11', 'DNA111_1', 'DNA1_1_11', 'DNA1_11_1', 'DNA11_1_1', 'DNA1_1_1_1']
    _SPECIES_LABELS = {'S1': 'Unresolved Signaling Observable 1', 'DNA0000': 'Unresolved Signaling Observable 2', 'DNA0001': 'Unresolved Signaling Observable 3', 'DNA0010': 'Unresolved Signaling Observable 4', 'DNA0100': 'Unresolved Signaling Observable 5', 'DNA1000': 'DNA1000', 'DNA1100': 'DNA1100', 'DNA1010': 'DNA1010', 'DNA1001': 'DNA1001', 'DNA0110': 'DNA0110', 'DNA0101': 'DNA0101', 'DNA0011': 'DNA0011', 'DNA1110': 'DNA1110', 'DNA1011': 'DNA1011', 'DNA1101': 'DNA1101', 'DNA0111': 'DNA0111', 'DNA1111': 'DNA1111', 'DNA001_1': 'DNA001_1', 'DNA01_10': 'DNA01_10', 'DNA01_11': 'DNA01_11', 'DNA011_1': 'DNA011_1', 'DNA01_1_1': 'DNA01_1_1', 'DNA101_1': 'DNA101_1', 'DNA1_100': 'DNA1_100', 'DNA1_101': 'DNA1_101', 'DNA1_110': 'DNA1_110', 'DNA11_10': 'DNA11_10', 'DNA1_1_10': 'DNA1_1_10', 'DNA1_111': 'DNA1_111', 'DNA11_11': 'DNA11_11', 'DNA111_1': 'DNA111_1', 'DNA1_1_11': 'DNA1_1_11', 'DNA1_11_1': 'DNA1_11_1', 'DNA11_1_1': 'DNA11_1_1', 'DNA1_1_1_1': 'DNA1_1_1_1', 'parameter_1': 'DoubleGasOccupancy'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_signaling_observable_1': ('S1', 1.09648e-11, 'native source value', 'Initial Unresolved Signaling Observable 1. Sets the initial value of bundled SBML species `S1`.'), 'initial_unresolved_signaling_observable_2': ('DNA0000', 1e-10, 'native source value', 'Initial Unresolved Signaling Observable 2. Sets the initial value of bundled SBML species `DNA0000`.'), 'initial_unresolved_signaling_observable_3': ('DNA0001', 0.0, 'native source value', 'Initial Unresolved Signaling Observable 3. Sets the initial value of bundled SBML species `DNA0001`.'), 'initial_unresolved_signaling_observable_4': ('DNA0010', 0.0, 'native source value', 'Initial Unresolved Signaling Observable 4. Sets the initial value of bundled SBML species `DNA0010`.'), 'initial_unresolved_signaling_observable_5': ('DNA0100', 0.0, 'native source value', 'Initial Unresolved Signaling Observable 5. Sets the initial value of bundled SBML species `DNA0100`.')}
    _HEADLINE_OUTPUTS = {'unresolved_signaling_observable_1': ('S1', 'native source value', 'Unresolved Signaling Observable 1. Maps to bundled source symbol `S1`.'), 'unresolved_signaling_observable_2': ('DNA0000', 'native source value', 'Unresolved Signaling Observable 2. Maps to bundled source symbol `DNA0000`.'), 'unresolved_signaling_observable_3': ('DNA0001', 'native source value', 'Unresolved Signaling Observable 3. Maps to bundled source symbol `DNA0001`.'), 'unresolved_signaling_observable_4': ('DNA0010', 'native source value', 'Unresolved Signaling Observable 4. Maps to bundled source symbol `DNA0010`.'), 'unresolved_signaling_observable_5': ('DNA0100', 'native source value', 'Unresolved Signaling Observable 5. Maps to bundled source symbol `DNA0100`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000501.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
