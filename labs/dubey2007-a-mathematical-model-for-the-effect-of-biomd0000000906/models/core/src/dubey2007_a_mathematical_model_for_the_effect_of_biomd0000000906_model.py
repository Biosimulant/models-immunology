# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Dubey2007 - A mathematical model for the effect of toxicant on the immune system (without toxicant effect) Model1."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Dubey2007AMathematicalModelForTheEffectOfBiomd0000000906Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000906."""

    _SBML_ID = 'BIOMD0000000906'
    _TITLE = 'Dubey2007 - A mathematical model for the effect of toxicant on the immune system (without toxicant effect) Model1'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['P', 'I', 'M']
    _SPECIES_LABELS = {'P': 'Unresolved Immune Observable 1', 'I': 'Unresolved Immune Observable 2', 'M': 'Unresolved Immune Observable 3'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_immune_observable_1': ('P', 1.0, 'native source value', 'Initial Unresolved Immune Observable 1. Sets the initial value of bundled SBML species `P`.'), 'initial_unresolved_immune_observable_2': ('I', 1.0, 'native source value', 'Initial Unresolved Immune Observable 2. Sets the initial value of bundled SBML species `I`.'), 'initial_unresolved_immune_observable_3': ('M', 1.0, 'native source value', 'Initial Unresolved Immune Observable 3. Sets the initial value of bundled SBML species `M`.')}
    _HEADLINE_OUTPUTS = {'unresolved_immune_observable_1': ('P', 'native source value', 'Unresolved Immune Observable 1. Maps to bundled source symbol `P`.'), 'unresolved_immune_observable_2': ('I', 'native source value', 'Unresolved Immune Observable 2. Maps to bundled source symbol `I`.'), 'unresolved_immune_observable_3': ('M', 'native source value', 'Unresolved Immune Observable 3. Maps to bundled source symbol `M`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000906.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
