# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Zhou2015 - Circadian clock with immune regulator NPR1."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Zhou2015CircadianClockWithImmuneRegulatorNBiomd0000000577Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000577."""

    _SBML_ID = 'BIOMD0000000577'
    _TITLE = 'Zhou2015 - Circadian clock with immune regulator NPR1'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['species_1', 'species_2', 'species_3', 'species_4', 'cCOP1c', 'cCOP1d', 'cCOP1n', 'cE3', 'cE3_m', 'cE3n', 'cE4', 'cE4_m', 'cEC', 'cEG', 'cG', 'cG_m', 'cL', 'cLUX', 'cLUX_m', 'cL_m', 'cLm', 'cNI', 'cNI_m', 'cP', 'cP7', 'cP7_m', 'cP9', 'cP9_m', 'cT', 'cT_m', 'cZG', 'cZTL']
    _SPECIES_LABELS = {'species_1': 'Cabar M', 'species_2': 'Unresolved Source Observable 2', 'species_3': 'Unresolved Source Observable 3', 'species_4': 'Unresolved Source Observable 4', 'cCOP1c': 'Unresolved Signaling Observable 2', 'cCOP1d': 'cCOP1d', 'cCOP1n': 'cCOP1n', 'cE3': 'cE3', 'cE3_m': 'cE3_m', 'cE3n': 'cE3n', 'cE4': 'cE4', 'cE4_m': 'cE4_m', 'cEC': 'cEC', 'cEG': 'cEG', 'cG': 'cG', 'cG_m': 'cG_m', 'cL': 'cL', 'cLUX': 'cLUX', 'cLUX_m': 'cLUX_m', 'cL_m': 'cL_m', 'cLm': 'cLm', 'cNI': 'cNI', 'cNI_m': 'cNI_m', 'cP': 'cP', 'cP7': 'cP7', 'cP7_m': 'cP7_m', 'cP9': 'cP9', 'cP9_m': 'cP9_m', 'cT': 'cT', 'cT_m': 'cT_m', 'cZG': 'cZG', 'cZTL': 'cZTL', 'parameter_1': 'g17', 'parameter_2': 'g18', 'parameter_3': 'g19', 'parameter_4': 'g20', 'parameter_5': 'g21', 'parameter_6': 'g22', 'parameter_7': 'g', 'parameter_8': 'n15', 'parameter_9': 'h', 'parameter_10': 'i', 'parameter_11': 'j', 'parameter_12': 'g23', 'parameter_13': 'g24', 'parameter_14': 'g25', 'parameter_15': 'g26', 'parameter_16': 'g27', 'parameter_17': 'g28', 'parameter_18': 'g29', 'parameter_19': 'm38', 'parameter_20': 'm39', 'parameter_21': 'n18', 'parameter_22': 'n16', 'parameter_23': 'quantity', 'parameter_24': 'n17', 'parameter_25': 'n19', 'parameter_26': 'p31', 'parameter_27': 'p32', 'parameter_28': 'p33', 'parameter_29': 'A0'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_cabar_m': ('species_1', 0.856, 'native source value', 'Initial Cabar M. Sets the initial value of bundled SBML species `species_1`.'), 'initial_unresolved_source_observable_2': ('species_2', 0.4027, 'native source value', 'Initial Unresolved Source Observable 2. Sets the initial value of bundled SBML species `species_2`.'), 'initial_unresolved_source_observable_3': ('species_3', 0.2362, 'native source value', 'Initial Unresolved Source Observable 3. Sets the initial value of bundled SBML species `species_3`.'), 'initial_unresolved_source_observable_4': ('species_4', 0.2843, 'native source value', 'Initial Unresolved Source Observable 4. Sets the initial value of bundled SBML species `species_4`.'), 'initial_unresolved_signaling_observable_2': ('cCOP1c', 1.3143, 'native source value', 'Initial Unresolved Signaling Observable 2. Sets the initial value of bundled SBML species `cCOP1c`.')}
    _HEADLINE_OUTPUTS = {'cabar_m': ('species_1', 'native source value', 'Cabar M. Maps to bundled source symbol `species_1`.'), 'unresolved_source_observable_2': ('species_2', 'native source value', 'Unresolved Source Observable 2. Maps to bundled source symbol `species_2`.'), 'unresolved_source_observable_3': ('species_3', 'native source value', 'Unresolved Source Observable 3. Maps to bundled source symbol `species_3`.'), 'unresolved_source_observable_4': ('species_4', 'native source value', 'Unresolved Source Observable 4. Maps to bundled source symbol `species_4`.'), 'unresolved_signaling_observable_2': ('cCOP1c', 'native source value', 'Unresolved Signaling Observable 2. Maps to bundled source symbol `cCOP1c`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000577.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
