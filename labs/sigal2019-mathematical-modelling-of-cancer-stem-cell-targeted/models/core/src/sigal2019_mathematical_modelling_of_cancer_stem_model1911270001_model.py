# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Sigal2019 - Mathematical modelling of cancer stem cell-targeted immunotherapy."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Sigal2019MathematicalModellingOfCancerStemModel1911270001Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL1911270001."""

    _SBML_ID = 'MODEL1911270001'
    _TITLE = 'Sigal2019 - Mathematical modelling of cancer stem cell-targeted immunotherapy'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S', 'P', 'TS', 'TP', 'DS', 'DP', 'C']
    _SPECIES_LABELS = {'S': 'Unresolved Tumor Observable 1', 'P': 'Unresolved Tumor Observable 2', 'TS': 'Unresolved Tumor Observable 3', 'TP': 'Unresolved Tumor Observable 4', 'DS': 'Unresolved Tumor Observable 5', 'DP': 'DP', 'C': 'C'}
    _PARAMETER_INPUTS = {'growth_start_time_parameter': ('growth_start_time', 12.0, 'native source value', 'Growth Start Time Parameter. Sets bundled SBML parameter `growth_start_time`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('S', 10000.0, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `S`.'), 'initial_unresolved_tumor_observable_2': ('P', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `P`.'), 'initial_unresolved_tumor_observable_3': ('TS', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `TS`.'), 'initial_unresolved_tumor_observable_4': ('TP', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `TP`.'), 'initial_unresolved_tumor_observable_5': ('DS', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 5. Sets the initial value of bundled SBML species `DS`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('S', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `S`.'), 'unresolved_tumor_observable_2': ('P', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `P`.'), 'unresolved_tumor_observable_3': ('TS', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `TS`.'), 'unresolved_tumor_observable_4': ('TP', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `TP`.'), 'unresolved_tumor_observable_5': ('DS', 'native source value', 'Unresolved Tumor Observable 5. Maps to bundled source symbol `DS`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1911270001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
