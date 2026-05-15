# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Jarrett2018 - trastuzumab-induced immune response in murine HER2+ breast cancer model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Jarrett2018TrastuzumabInducedImmuneResponseBiomd0000000745Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000745."""

    _SBML_ID = 'BIOMD0000000745'
    _TITLE = 'Jarrett2018 - trastuzumab-induced immune response in murine HER2+ breast cancer model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'I', 'V', 'N', 'H']
    _SPECIES_LABELS = {'T': 'Unresolved Tumor Observable 1', 'I': 'Unresolved Tumor Observable 2', 'V': 'Unresolved Tumor Observable 3', 'N': 'Unresolved Tumor Observable 4', 'H': 'Unresolved Tumor Observable 5'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('T', 0.2, 'substance', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `T`.'), 'initial_unresolved_tumor_observable_2': ('I', 0.071, 'substance', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `I`.'), 'initial_unresolved_tumor_observable_3': ('V', 0.12, 'substance', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `V`.'), 'initial_unresolved_tumor_observable_4': ('N', 0.1, 'substance', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `N`.'), 'initial_unresolved_tumor_observable_5': ('H', 0.18, 'substance', 'Initial Unresolved Tumor Observable 5. Sets the initial value of bundled SBML species `H`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('T', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `T`.'), 'unresolved_tumor_observable_2': ('I', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `I`.'), 'unresolved_tumor_observable_3': ('V', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `V`.'), 'unresolved_tumor_observable_4': ('N', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `N`.'), 'unresolved_tumor_observable_5': ('H', 'native source value', 'Unresolved Tumor Observable 5. Maps to bundled source symbol `H`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000745.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
