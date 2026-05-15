# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Miao2010 - Innate and adaptive immune responses to primary Influenza A Virus infection_1_1."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Miao2010InnateAndAdaptiveImmuneResponsesToBiomd0000000546Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000546."""

    _SBML_ID = 'BIOMD0000000546'
    _TITLE = 'Miao2010 - Innate and adaptive immune responses to primary Influenza A Virus infection_1_1'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['s1', 's2', 's3']
    _SPECIES_LABELS = {'s1': 'Unresolved Infection Observable 1', 's2': 'Unresolved Infection Observable 2', 's3': 'Unresolved Infection Observable 3'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_infection_observable_1': ('s1', 580000.0, 'substance', 'Initial Unresolved Infection Observable 1. Sets the initial value of bundled SBML species `s1`.'), 'initial_unresolved_infection_observable_2': ('s2', 0.0, 'substance', 'Initial Unresolved Infection Observable 2. Sets the initial value of bundled SBML species `s2`.'), 'initial_unresolved_infection_observable_3': ('s3', 1000.0, 'substance', 'Initial Unresolved Infection Observable 3. Sets the initial value of bundled SBML species `s3`.')}
    _HEADLINE_OUTPUTS = {'unresolved_infection_observable_1': ('s1', 'native source value', 'Unresolved Infection Observable 1. Maps to bundled source symbol `s1`.'), 'unresolved_infection_observable_2': ('s2', 'native source value', 'Unresolved Infection Observable 2. Maps to bundled source symbol `s2`.'), 'unresolved_infection_observable_3': ('s3', 'native source value', 'Unresolved Infection Observable 3. Maps to bundled source symbol `s3`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000546.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
