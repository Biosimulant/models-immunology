# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Nowak1996_HostResponse_InfectiousAgents."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Nowak1996HostresponseInfectiousagentsModel1006230050Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL1006230050."""

    _SBML_ID = 'MODEL1006230050'
    _TITLE = 'Nowak1996_HostResponse_InfectiousAgents'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rateRule'
    _OBSERVABLES = ['x', 'y', 'v']
    _SPECIES_LABELS = {'x': 'Unresolved Infection Observable 1', 'y': 'Unresolved Infection Observable 2', 'v': 'Unresolved Infection Observable 3'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'unresolved_infection_observable_1': ('x', 'native source value', 'Unresolved Infection Observable 1. Maps to bundled source symbol `x`.'), 'unresolved_infection_observable_2': ('y', 'native source value', 'Unresolved Infection Observable 2. Maps to bundled source symbol `y`.'), 'unresolved_infection_observable_3': ('v', 'native source value', 'Unresolved Infection Observable 3. Maps to bundled source symbol `v`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1006230050.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
