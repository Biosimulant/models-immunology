# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Verma2016 - HIV and HPV co-infection, T-cell response."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Verma2016HivAndHpvCoInfectionTCellResponBiomd0000000872Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000872."""

    _SBML_ID = 'BIOMD0000000872'
    _TITLE = 'Verma2016 - HIV and HPV co-infection, T-cell response'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['s2', 's3', 's4', 's14', 's16', 's13', 's12']
    _SPECIES_LABELS = {'s2': 'Unresolved Infection Observable 1', 's3': 'Unresolved Infection Observable 2', 's4': 'Unresolved Infection Observable 3', 's14': 'Unresolved Infection Observable 4', 's16': 'Unresolved Infection Observable 5', 's13': 'Y2', 's12': 'Y1'}
    _PARAMETER_INPUTS = {'decay_of_t_cells_rate': ('d', 0.01, 'native source value', 'Decay Of T Cells Rate. Sets bundled SBML parameter `d`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_infection_observable_1': ('s2', 48000.0, 'native source value', 'Initial Unresolved Infection Observable 1. Sets the initial value of bundled SBML species `s2`.'), 'initial_unresolved_infection_observable_2': ('s3', 2364.02569593148, 'native source value', 'Initial Unresolved Infection Observable 2. Sets the initial value of bundled SBML species `s3`.'), 'initial_unresolved_infection_observable_3': ('s4', 250000.0, 'native source value', 'Initial Unresolved Infection Observable 3. Sets the initial value of bundled SBML species `s4`.'), 'initial_unresolved_infection_observable_4': ('s14', 0.0, 'native source value', 'Initial Unresolved Infection Observable 4. Sets the initial value of bundled SBML species `s14`.'), 'initial_unresolved_infection_observable_5': ('s16', 0.01, 'native source value', 'Initial Unresolved Infection Observable 5. Sets the initial value of bundled SBML species `s16`.')}
    _HEADLINE_OUTPUTS = {'unresolved_infection_observable_1': ('s2', 'native source value', 'Unresolved Infection Observable 1. Maps to bundled source symbol `s2`.'), 'unresolved_infection_observable_2': ('s3', 'native source value', 'Unresolved Infection Observable 2. Maps to bundled source symbol `s3`.'), 'unresolved_infection_observable_3': ('s4', 'native source value', 'Unresolved Infection Observable 3. Maps to bundled source symbol `s4`.'), 'unresolved_infection_observable_4': ('s14', 'native source value', 'Unresolved Infection Observable 4. Maps to bundled source symbol `s14`.'), 'unresolved_infection_observable_5': ('s16', 'native source value', 'Unresolved Infection Observable 5. Maps to bundled source symbol `s16`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000872.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
