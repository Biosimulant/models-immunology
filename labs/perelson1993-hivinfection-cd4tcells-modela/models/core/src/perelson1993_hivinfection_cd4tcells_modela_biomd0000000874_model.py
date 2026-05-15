# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Perelson1993 - HIVinfection_CD4Tcells_ModelA."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Perelson1993HivinfectionCd4tcellsModelaBiomd0000000874Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000874."""

    _SBML_ID = 'BIOMD0000000874'
    _TITLE = 'Perelson1993 - HIVinfection_CD4Tcells_ModelA'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'T_1', 'T_2', 'V']
    _SPECIES_LABELS = {'T': 'Unresolved Infection Observable 1', 'T_1': 'Unresolved Infection Observable 2', 'T_2': 'Unresolved Infection Observable 3', 'V': 'Unresolved Infection Observable 4'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_infection_observable_1': ('T', 1000.0, 'native source value', 'Initial Unresolved Infection Observable 1. Sets the initial value of bundled SBML species `T`.'), 'initial_unresolved_infection_observable_2': ('T_1', 0.0, 'native source value', 'Initial Unresolved Infection Observable 2. Sets the initial value of bundled SBML species `T_1`.'), 'initial_unresolved_infection_observable_3': ('T_2', 0.0, 'native source value', 'Initial Unresolved Infection Observable 3. Sets the initial value of bundled SBML species `T_2`.'), 'initial_unresolved_infection_observable_4': ('V', 0.001, 'native source value', 'Initial Unresolved Infection Observable 4. Sets the initial value of bundled SBML species `V`.')}
    _HEADLINE_OUTPUTS = {'unresolved_infection_observable_1': ('T', 'native source value', 'Unresolved Infection Observable 1. Maps to bundled source symbol `T`.'), 'unresolved_infection_observable_2': ('T_1', 'native source value', 'Unresolved Infection Observable 2. Maps to bundled source symbol `T_1`.'), 'unresolved_infection_observable_3': ('T_2', 'native source value', 'Unresolved Infection Observable 3. Maps to bundled source symbol `T_2`.'), 'unresolved_infection_observable_4': ('V', 'native source value', 'Unresolved Infection Observable 4. Maps to bundled source symbol `V`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000874.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
