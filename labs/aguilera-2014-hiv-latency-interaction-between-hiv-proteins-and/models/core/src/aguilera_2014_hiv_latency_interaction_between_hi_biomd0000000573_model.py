# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Aguilera 2014 - HIV latency. Interaction between HIV proteins and immune response."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Aguilera2014HivLatencyInteractionBetweenHiBiomd0000000573Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000573."""

    _SBML_ID = 'BIOMD0000000573'
    _TITLE = 'Aguilera 2014 - HIV latency. Interaction between HIV proteins and immune response'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['V', 'C']
    _SPECIES_LABELS = {'V': 'Unresolved Infection Observable 1', 'C': 'Unresolved Infection Observable 2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_infection_observable_1': ('V', 1.0, 'native source value', 'Initial Unresolved Infection Observable 1. Sets the initial value of bundled SBML species `V`.'), 'initial_unresolved_infection_observable_2': ('C', 0.0, 'native source value', 'Initial Unresolved Infection Observable 2. Sets the initial value of bundled SBML species `C`.')}
    _HEADLINE_OUTPUTS = {'unresolved_infection_observable_1': ('V', 'native source value', 'Unresolved Infection Observable 1. Maps to bundled source symbol `V`.'), 'unresolved_infection_observable_2': ('C', 'native source value', 'Unresolved Infection Observable 2. Maps to bundled source symbol `C`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000573.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
