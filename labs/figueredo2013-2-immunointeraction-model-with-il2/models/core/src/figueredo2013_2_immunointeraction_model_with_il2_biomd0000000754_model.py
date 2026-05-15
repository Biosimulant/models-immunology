# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Figueredo2013/2 - immunointeraction model with IL2."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Figueredo20132ImmunointeractionModelWithIl2Biomd0000000754Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000754."""

    _SBML_ID = 'BIOMD0000000754'
    _TITLE = 'Figueredo2013/2 - immunointeraction model with IL2'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'E', 'I']
    _SPECIES_LABELS = {'T': 'Unresolved Tumor Observable 1', 'E': 'Unresolved Tumor Observable 2', 'I': 'Unresolved Tumor Observable 3'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('T', 50.0, 'substance', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `T`.'), 'initial_unresolved_tumor_observable_2': ('E', 10.0, 'substance', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `E`.'), 'initial_unresolved_tumor_observable_3': ('I', 0.0, 'substance', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `I`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('T', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `T`.'), 'unresolved_tumor_observable_2': ('E', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `E`.'), 'unresolved_tumor_observable_3': ('I', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `I`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000754.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
