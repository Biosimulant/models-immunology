# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Figueredo2013/3 - immunointeraction full model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Figueredo20133ImmunointeractionFullModelBiomd0000000756Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000756."""

    _SBML_ID = 'BIOMD0000000756'
    _TITLE = 'Figueredo2013/3 - immunointeraction full model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'E', 'I', 'S']
    _SPECIES_LABELS = {'T': 'Unresolved Tumor Observable 1', 'E': 'Unresolved Tumor Observable 2', 'I': 'Unresolved Tumor Observable 3', 'S': 'Unresolved Tumor Observable 4'}
    _PARAMETER_INPUTS = {'tumor_death_rate': ('k', 10000000000.0, 'unit_0', 'Tumor Death Rate. Sets bundled SBML parameter `k`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('T', 1.0, 'substance', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `T`.'), 'initial_unresolved_tumor_observable_2': ('E', 1.0, 'substance', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `E`.'), 'initial_unresolved_tumor_observable_3': ('I', 10.0, 'substance', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `I`.'), 'initial_unresolved_tumor_observable_4': ('S', 0.0, 'substance', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `S`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('T', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `T`.'), 'unresolved_tumor_observable_2': ('E', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `E`.'), 'unresolved_tumor_observable_3': ('I', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `I`.'), 'unresolved_tumor_observable_4': ('S', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `S`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000756.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
