# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Arciero2004 - A mathematical model of tumor-immune evasion and siRNA treatment."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Arciero2004AMathematicalModelOfTumorImmuneModel1907310002Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL1907310002."""

    _SBML_ID = 'MODEL1907310002'
    _TITLE = 'Arciero2004 - A mathematical model of tumor-immune evasion and siRNA treatment'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['E', 'T', 'I', 'S']
    _SPECIES_LABELS = {'E': 'Unresolved Tumor Observable 1', 'T': 'Unresolved Tumor Observable 2', 'I': 'Unresolved Tumor Observable 3', 'S': 'Unresolved Tumor Observable 4'}
    _PARAMETER_INPUTS = {'effector_cell_death_rate': ('mu_1', 0.03, 'native source value', 'Effector Cell Death Rate. Sets bundled SBML parameter `mu_1`.'), 'tumour_growth_rate': ('r', 0.18, 'native source value', 'Tumour Growth Rate. Sets bundled SBML parameter `r`.'), 'interleukin_2_decay_rate': ('mu_2', 10.0, 'native source value', 'Interleukin 2 Decay Rate. Sets bundled SBML parameter `mu_2`.'), 'transforming_growth_factor_b_decay_rate': ('mu_3', 10.0, 'native source value', 'Transforming Growth Factor B Decay Rate. Sets bundled SBML parameter `mu_3`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('E', 1000.0, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `E`.'), 'initial_unresolved_tumor_observable_2': ('T', 1.0, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `T`.'), 'initial_unresolved_tumor_observable_3': ('I', 1000.0, 'native source value', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `I`.'), 'initial_unresolved_tumor_observable_4': ('S', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `S`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('E', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `E`.'), 'unresolved_tumor_observable_2': ('T', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `T`.'), 'unresolved_tumor_observable_3': ('I', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `I`.'), 'unresolved_tumor_observable_4': ('S', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `S`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1907310002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
