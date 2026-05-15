# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Yu2019 - A mathematical model of tumor-immune interactions with an immune checkpoint inhibitor."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Yu2019AMathematicalModelOfTumorImmuneInteModel1911270002Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL1911270002."""

    _SBML_ID = 'MODEL1911270002'
    _TITLE = 'Yu2019 - A mathematical model of tumor-immune interactions with an immune checkpoint inhibitor'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x', 'y', 'z', 'w']
    _SPECIES_LABELS = {'x': 'Unresolved Tumor Observable 1', 'y': 'Unresolved Tumor Observable 2', 'z': 'Unresolved Tumor Observable 3', 'w': 'Unresolved Tumor Observable 4'}
    _PARAMETER_INPUTS = {'tumor_growth_rate': ('r', 0.514, 'native source value', 'Tumor Growth Rate. Sets bundled SBML parameter `r`.'), 'tumor_death_cytokines_rate': ('delta', 0.2, 'native source value', 'Tumor Death Cytokines Rate. Sets bundled SBML parameter `delta`.'), 'th_proliferation_rate': ('beta', 0.09, 'native source value', 'Th Proliferation Rate. Sets bundled SBML parameter `beta`.'), 'interferon_gamma_decay_rate': ('mu', 34.0, 'native source value', 'Interferon Gamma Decay Rate. Sets bundled SBML parameter `mu`.'), 'ctla_4_decay_rate': ('d', 8.3178, 'native source value', 'Ctla 4 Decay Rate. Sets bundled SBML parameter `d`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('x', 250000.0, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `x`.'), 'initial_unresolved_tumor_observable_2': ('y', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `y`.'), 'initial_unresolved_tumor_observable_3': ('z', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `z`.'), 'initial_unresolved_tumor_observable_4': ('w', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `w`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('x', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `x`.'), 'unresolved_tumor_observable_2': ('y', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `y`.'), 'unresolved_tumor_observable_3': ('z', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `z`.'), 'unresolved_tumor_observable_4': ('w', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `w`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1911270002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
