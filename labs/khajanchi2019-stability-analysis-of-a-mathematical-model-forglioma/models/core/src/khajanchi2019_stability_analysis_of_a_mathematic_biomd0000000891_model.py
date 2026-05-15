# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Khajanchi2019 - Stability Analysis of a Mathematical Model forGlioma-Immune Interaction under OptimalTherapy."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Khajanchi2019StabilityAnalysisOfAMathematicBiomd0000000891Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000891."""

    _SBML_ID = 'BIOMD0000000891'
    _TITLE = 'Khajanchi2019 - Stability Analysis of a Mathematical Model forGlioma-Immune Interaction under OptimalTherapy'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['u', 'v', 'w']
    _SPECIES_LABELS = {'u': 'Unresolved Immune Observable 1', 'v': 'Unresolved Immune Observable 2', 'w': 'Unresolved Immune Observable 3'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_immune_observable_1': ('u', 0.1, 'native source value', 'Initial Unresolved Immune Observable 1. Sets the initial value of bundled SBML species `u`.'), 'initial_unresolved_immune_observable_2': ('v', 0.55, 'native source value', 'Initial Unresolved Immune Observable 2. Sets the initial value of bundled SBML species `v`.'), 'initial_unresolved_immune_observable_3': ('w', 0.2, 'native source value', 'Initial Unresolved Immune Observable 3. Sets the initial value of bundled SBML species `w`.')}
    _HEADLINE_OUTPUTS = {'unresolved_immune_observable_1': ('u', 'native source value', 'Unresolved Immune Observable 1. Maps to bundled source symbol `u`.'), 'unresolved_immune_observable_2': ('v', 'native source value', 'Unresolved Immune Observable 2. Maps to bundled source symbol `v`.'), 'unresolved_immune_observable_3': ('w', 'native source value', 'Unresolved Immune Observable 3. Maps to bundled source symbol `w`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000891.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
