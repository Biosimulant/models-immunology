# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Bose2011 - Noise-assisted interactions of tumor and immune cells."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bose2011NoiseAssistedInteractionsOfTumorAnBiomd0000000894Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000894."""

    _SBML_ID = 'BIOMD0000000894'
    _TITLE = 'Bose2011 - Noise-assisted interactions of tumor and immune cells'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x', 'y', 'z']
    _SPECIES_LABELS = {'x': 'Unresolved Tumor Observable 1', 'y': 'Unresolved Tumor Observable 2', 'z': 'Unresolved Tumor Observable 3'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('x', 1e-06, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `x`.'), 'initial_unresolved_tumor_observable_2': ('y', 0.01, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `y`.'), 'initial_unresolved_tumor_observable_3': ('z', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `z`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('x', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `x`.'), 'unresolved_tumor_observable_2': ('y', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `y`.'), 'unresolved_tumor_observable_3': ('z', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `z`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000894.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
