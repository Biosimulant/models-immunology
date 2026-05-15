# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Garcia2018basic - cancer and immune cell count basic model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Garcia2018basicCancerAndImmuneCellCountBasBiomd0000000742Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000742."""

    _SBML_ID = 'BIOMD0000000742'
    _TITLE = 'Garcia2018basic - cancer and immune cell count basic model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'E']
    _SPECIES_LABELS = {'T': 'Unresolved Tumor Observable 1', 'E': 'Unresolved Tumor Observable 2'}
    _PARAMETER_INPUTS = {'tumor_killing_rate': ('k', 0.0001, 'unit_0', 'Tumor Killing Rate. Sets bundled SBML parameter `k`.'), 'immune_cell_death_rate': ('d', 0.02, 'unit_0', 'Immune Cell Death Rate. Sets bundled SBML parameter `d`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('T', 100.0, 'substance', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `T`.'), 'initial_unresolved_tumor_observable_2': ('E', 1000.0, 'substance', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `E`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('T', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `T`.'), 'unresolved_tumor_observable_2': ('E', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `E`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000742.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
