# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Perelson1993_HIVinfection_CD4Tcells_ModelB."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Perelson1993HivinfectionCd4tcellsModelbModel1006230093Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL1006230093."""

    _SBML_ID = 'MODEL1006230093'
    _TITLE = 'Perelson1993_HIVinfection_CD4Tcells_ModelB'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rateRule'
    _OBSERVABLES = ['T', 'T_1', 'T_2', 'V']
    _SPECIES_LABELS = {'T': 'Unresolved Infection Observable 1', 'T_1': 'Unresolved Infection Observable 2', 'T_2': 'Unresolved Infection Observable 3', 'V': 'Unresolved Infection Observable 4'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'unresolved_infection_observable_1': ('T', 'native source value', 'Unresolved Infection Observable 1. Maps to bundled source symbol `T`.'), 'unresolved_infection_observable_2': ('T_1', 'native source value', 'Unresolved Infection Observable 2. Maps to bundled source symbol `T_1`.'), 'unresolved_infection_observable_3': ('T_2', 'native source value', 'Unresolved Infection Observable 3. Maps to bundled source symbol `T_2`.'), 'unresolved_infection_observable_4': ('V', 'native source value', 'Unresolved Infection Observable 4. Maps to bundled source symbol `V`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1006230093.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
