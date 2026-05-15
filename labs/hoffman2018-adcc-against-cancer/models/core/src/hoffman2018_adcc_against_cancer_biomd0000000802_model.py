# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Hoffman2018- ADCC against cancer."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Hoffman2018AdccAgainstCancerBiomd0000000802Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000802."""

    _SBML_ID = 'BIOMD0000000802'
    _TITLE = 'Hoffman2018- ADCC against cancer'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['A', 'R', 'S', 'C']
    _SPECIES_LABELS = {'A': 'Unresolved Tumor Observable 1', 'R': 'Unresolved Tumor Observable 2', 'S': 'Unresolved Tumor Observable 3', 'C': 'Unresolved Tumor Observable 4'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('A', 1.0, 'substance', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `A`.'), 'initial_unresolved_tumor_observable_2': ('R', 0.0, 'substance', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `R`.'), 'initial_unresolved_tumor_observable_3': ('S', 1.0, 'substance', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `S`.'), 'initial_unresolved_tumor_observable_4': ('C', 0.0, 'substance', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `C`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('A', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `A`.'), 'unresolved_tumor_observable_2': ('R', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `R`.'), 'unresolved_tumor_observable_3': ('S', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `S`.'), 'unresolved_tumor_observable_4': ('C', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `C`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000802.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
