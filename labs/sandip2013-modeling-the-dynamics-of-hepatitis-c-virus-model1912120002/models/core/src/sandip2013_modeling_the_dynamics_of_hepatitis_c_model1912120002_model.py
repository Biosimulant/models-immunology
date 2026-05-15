# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Sandip2013 - Modeling the dynamics of hepatitis C virus with combined antiviral drug therapy: interferon and ribavirin.."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Sandip2013ModelingTheDynamicsOfHepatitisCModel1912120002Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL1912120002."""

    _SBML_ID = 'MODEL1912120002'
    _TITLE = 'Sandip2013 - Modeling the dynamics of hepatitis C virus with combined antiviral drug therapy: interferon and ribavirin.'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'I', 'VI', 'VNI']
    _SPECIES_LABELS = {'T': 'Unresolved Infection Observable 1', 'I': 'Unresolved Infection Observable 2', 'VI': 'Unresolved Infection Observable 3', 'VNI': 'Unresolved Infection Observable 4'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_infection_observable_1': ('T', 17000000.0, 'native source value', 'Initial Unresolved Infection Observable 1. Sets the initial value of bundled SBML species `T`.'), 'initial_unresolved_infection_observable_2': ('I', 1.0, 'native source value', 'Initial Unresolved Infection Observable 2. Sets the initial value of bundled SBML species `I`.'), 'initial_unresolved_infection_observable_3': ('VI', 1.0, 'native source value', 'Initial Unresolved Infection Observable 3. Sets the initial value of bundled SBML species `VI`.'), 'initial_unresolved_infection_observable_4': ('VNI', 1.0, 'native source value', 'Initial Unresolved Infection Observable 4. Sets the initial value of bundled SBML species `VNI`.')}
    _HEADLINE_OUTPUTS = {'unresolved_infection_observable_1': ('T', 'native source value', 'Unresolved Infection Observable 1. Maps to bundled source symbol `T`.'), 'unresolved_infection_observable_2': ('I', 'native source value', 'Unresolved Infection Observable 2. Maps to bundled source symbol `I`.'), 'unresolved_infection_observable_3': ('VI', 'native source value', 'Unresolved Infection Observable 3. Maps to bundled source symbol `VI`.'), 'unresolved_infection_observable_4': ('VNI', 'native source value', 'Unresolved Infection Observable 4. Maps to bundled source symbol `VNI`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1912120002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
