# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Phan2017 - innate immune in oncolytic virotherapy."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Phan2017InnateImmuneInOncolyticVirotherapyBiomd0000000748Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000748."""

    _SBML_ID = 'BIOMD0000000748'
    _TITLE = 'Phan2017 - innate immune in oncolytic virotherapy'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x', 'y', 'v', 'z']
    _SPECIES_LABELS = {'x': 'Unresolved Tumor Observable 1', 'y': 'Unresolved Tumor Observable 2', 'v': 'Unresolved Tumor Observable 3', 'z': 'Unresolved Tumor Observable 4'}
    _PARAMETER_INPUTS = {'infected_tumor_killing_rate': ('c', 0.48, 'unit_0', 'Infected Tumor Killing Rate. Sets bundled SBML parameter `c`.'), 'virus_killing_by_immune_rate': ('d', 0.16, 'unit_0', 'Virus Killing By Immune Rate. Sets bundled SBML parameter `d`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('x', 0.99, 'substance', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `x`.'), 'initial_unresolved_tumor_observable_2': ('y', 0.01, 'substance', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `y`.'), 'initial_unresolved_tumor_observable_3': ('v', 0.01, 'substance', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `v`.'), 'initial_unresolved_tumor_observable_4': ('z', 0.01, 'substance', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `z`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('x', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `x`.'), 'unresolved_tumor_observable_2': ('y', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `y`.'), 'unresolved_tumor_observable_3': ('v', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `v`.'), 'unresolved_tumor_observable_4': ('z', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `z`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000748.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
