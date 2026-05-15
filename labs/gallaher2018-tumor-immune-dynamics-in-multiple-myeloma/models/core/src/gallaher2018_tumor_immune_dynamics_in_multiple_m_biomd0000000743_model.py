# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Gallaher2018 - Tumor–Immune dynamics in multiple myeloma."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Gallaher2018TumorImmuneDynamicsInMultipleMBiomd0000000743Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000743."""

    _SBML_ID = 'BIOMD0000000743'
    _TITLE = 'Gallaher2018 - Tumor–Immune dynamics in multiple myeloma'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['M', 'Tc', 'N', 'Tr']
    _SPECIES_LABELS = {'M': 'Unresolved Tumor Observable 1', 'Tc': 'Unresolved Tumor Observable 2', 'N': 'Unresolved Tumor Observable 3', 'Tr': 'Unresolved Tumor Observable 4'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('M', 4.0, 'substance', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `M`.'), 'initial_unresolved_tumor_observable_2': ('Tc', 464.0, 'substance', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `Tc`.'), 'initial_unresolved_tumor_observable_3': ('N', 227.0, 'substance', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `N`.'), 'initial_unresolved_tumor_observable_4': ('Tr', 42.0, 'substance', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `Tr`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('M', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `M`.'), 'unresolved_tumor_observable_2': ('Tc', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `Tc`.'), 'unresolved_tumor_observable_3': ('N', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `N`.'), 'unresolved_tumor_observable_4': ('Tr', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `Tr`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000743.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
