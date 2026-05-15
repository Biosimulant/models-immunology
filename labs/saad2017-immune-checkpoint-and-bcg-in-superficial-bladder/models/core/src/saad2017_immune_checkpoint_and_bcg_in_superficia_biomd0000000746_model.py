# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Saad2017 - immune checkpoint and BCG in superficial bladder cancer."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Saad2017ImmuneCheckpointAndBcgInSuperficiaBiomd0000000746Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000746."""

    _SBML_ID = 'BIOMD0000000746'
    _TITLE = 'Saad2017 - immune checkpoint and BCG in superficial bladder cancer'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['C', 'E', 'B', 'P']
    _SPECIES_LABELS = {'C': 'Unresolved Tumor Observable 1', 'E': 'Unresolved Tumor Observable 2', 'B': 'Unresolved Tumor Observable 3', 'P': 'Unresolved Tumor Observable 4'}
    _PARAMETER_INPUTS = {'cancer_growth_rate': ('r', 0.0033, 'unit_0', 'Cancer Growth Rate. Sets bundled SBML parameter `r`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('C', 100000.0, 'substance', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `C`.'), 'initial_unresolved_tumor_observable_2': ('E', 0.0, 'substance', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `E`.'), 'initial_unresolved_tumor_observable_3': ('B', 0.0, 'substance', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `B`.'), 'initial_unresolved_tumor_observable_4': ('P', 0.0, 'substance', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `P`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('C', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `C`.'), 'unresolved_tumor_observable_2': ('E', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `E`.'), 'unresolved_tumor_observable_3': ('B', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `B`.'), 'unresolved_tumor_observable_4': ('P', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `P`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000746.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
