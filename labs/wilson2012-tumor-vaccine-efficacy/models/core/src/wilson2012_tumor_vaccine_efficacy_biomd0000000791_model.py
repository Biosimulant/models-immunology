# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Wilson2012 - tumor vaccine efficacy."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Wilson2012TumorVaccineEfficacyBiomd0000000791Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000791."""

    _SBML_ID = 'BIOMD0000000791'
    _TITLE = 'Wilson2012 - tumor vaccine efficacy'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'B', 'E', 'R', 'V']
    _SPECIES_LABELS = {'T': 'Unresolved Tumor Observable 1', 'B': 'Unresolved Tumor Observable 2', 'E': 'Unresolved Tumor Observable 3', 'R': 'Unresolved Tumor Observable 4', 'V': 'Unresolved Tumor Observable 5'}
    _PARAMETER_INPUTS = {'tgfb_decay_rate': ('d', 0.0007, 'unit_1', 'Tgfb Decay Rate. Sets bundled SBML parameter `d`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('T', 3.0, 'substance', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `T`.'), 'initial_unresolved_tumor_observable_2': ('B', 0.0, 'substance', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `B`.'), 'initial_unresolved_tumor_observable_3': ('E', 100.0, 'substance', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `E`.'), 'initial_unresolved_tumor_observable_4': ('R', 1.0, 'substance', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `R`.'), 'initial_unresolved_tumor_observable_5': ('V', 0.0, 'substance', 'Initial Unresolved Tumor Observable 5. Sets the initial value of bundled SBML species `V`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('T', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `T`.'), 'unresolved_tumor_observable_2': ('B', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `B`.'), 'unresolved_tumor_observable_3': ('E', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `E`.'), 'unresolved_tumor_observable_4': ('R', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `R`.'), 'unresolved_tumor_observable_5': ('V', 'native source value', 'Unresolved Tumor Observable 5. Maps to bundled source symbol `V`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000791.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
