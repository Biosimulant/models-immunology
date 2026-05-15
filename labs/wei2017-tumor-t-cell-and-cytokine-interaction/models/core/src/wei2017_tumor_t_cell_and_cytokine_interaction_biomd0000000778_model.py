# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Wei2017 - tumor, T cell and cytokine interaction."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Wei2017TumorTCellAndCytokineInteractionBiomd0000000778Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000778."""

    _SBML_ID = 'BIOMD0000000778'
    _TITLE = 'Wei2017 - tumor, T cell and cytokine interaction'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'I', 'C']
    _SPECIES_LABELS = {'T': 'Unresolved Tumor Observable 1', 'I': 'Unresolved Tumor Observable 2', 'C': 'Unresolved Tumor Observable 3'}
    _PARAMETER_INPUTS = {'tumor_growth_rate': ('r', 0.01, 'unit_0', 'Tumor Growth Rate. Sets bundled SBML parameter `r`.'), 'tumor_killing_rate': ('d', 0.1, 'unit_0', 'Tumor Killing Rate. Sets bundled SBML parameter `d`.'), 'immune_cell_growth_rate': ('beta', 0.1, 'unit_0', 'Immune Cell Growth Rate. Sets bundled SBML parameter `beta`.'), 'immune_cell_growth_rate_2': ('k', 1000.0, 'unit_1', 'Immune Cell Growth Rate 2. Sets bundled SBML parameter `k`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('T', 0.5, 'substance', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `T`.'), 'initial_unresolved_tumor_observable_2': ('I', 0.01, 'substance', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `I`.'), 'initial_unresolved_tumor_observable_3': ('C', 0.0, 'substance', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `C`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('T', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `T`.'), 'unresolved_tumor_observable_2': ('I', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `I`.'), 'unresolved_tumor_observable_3': ('C', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `C`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000778.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
