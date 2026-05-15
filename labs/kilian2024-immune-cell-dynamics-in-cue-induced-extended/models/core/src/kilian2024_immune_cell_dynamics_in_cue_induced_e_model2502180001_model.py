# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Kilian2024 - Immune cell dynamics in Cue-Induced Extended Human Colitis Model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kilian2024ImmuneCellDynamicsInCueInducedEModel2502180001Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL2502180001."""

    _SBML_ID = 'MODEL2502180001'
    _TITLE = 'Kilian2024 - Immune cell dynamics in Cue-Induced Extended Human Colitis Model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Mac', 'Bcell', 'Neutr', 'Tcell', 'Epi', 'Cue', 'ActiveIBD', 'Resolution']
    _SPECIES_LABELS = {'Mac': 'Unresolved Immune Observable 2', 'Bcell': 'Cell', 'Neutr': 'Neutr', 'Tcell': 'Unresolved Immune Observable 1', 'Epi': 'Unresolved Immune Observable 3', 'Cue': 'Cue', 'ActiveIBD': 'ActiveIBD', 'Resolution': 'Resolution'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_cell': ('Bcell', 0.0468867574754616, 'native source value', 'Initial Cell. Sets the initial value of bundled SBML species `Bcell`.'), 'initial_unresolved_immune_observable_1': ('Tcell', 0.0215256076306623, 'native source value', 'Initial Unresolved Immune Observable 1. Sets the initial value of bundled SBML species `Tcell`.'), 'initial_unresolved_immune_observable_2': ('Mac', 0.0608414487144472, 'native source value', 'Initial Unresolved Immune Observable 2. Sets the initial value of bundled SBML species `Mac`.'), 'initial_neutr': ('Neutr', 0.0481656099063014, 'native source value', 'Initial Neutr. Sets the initial value of bundled SBML species `Neutr`.'), 'initial_unresolved_immune_observable_3': ('Epi', 0.300977731108012, 'native source value', 'Initial Unresolved Immune Observable 3. Sets the initial value of bundled SBML species `Epi`.')}
    _HEADLINE_OUTPUTS = {'cell': ('Bcell', 'native source value', 'Cell. Maps to bundled source symbol `Bcell`.'), 'unresolved_immune_observable_1': ('Tcell', 'native source value', 'Unresolved Immune Observable 1. Maps to bundled source symbol `Tcell`.'), 'unresolved_immune_observable_2': ('Mac', 'native source value', 'Unresolved Immune Observable 2. Maps to bundled source symbol `Mac`.'), 'neutr': ('Neutr', 'native source value', 'Neutr. Maps to bundled source symbol `Neutr`.'), 'unresolved_immune_observable_3': ('Epi', 'native source value', 'Unresolved Immune Observable 3. Maps to bundled source symbol `Epi`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2502180001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
