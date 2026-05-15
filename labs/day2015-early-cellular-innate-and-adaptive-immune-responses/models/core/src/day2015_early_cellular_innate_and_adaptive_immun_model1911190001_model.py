# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Day2015 - Early cellular innate and adaptive immune responses to ischemia/reperfusion injury and solid organ allotransplantation."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Day2015EarlyCellularInnateAndAdaptiveImmunModel1911190001Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL1911190001."""

    _SBML_ID = 'MODEL1911190001'
    _TITLE = 'Day2015 - Early cellular innate and adaptive immune responses to ischemia/reperfusion injury and solid organ allotransplantation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['D', 'DG', 'I', 'A', 'TP', 'TA']
    _SPECIES_LABELS = {'D': 'Unresolved Immune Observable 1', 'DG': 'Unresolved Immune Observable 2', 'I': 'Unresolved Immune Observable 3', 'A': 'Unresolved Immune Observable 4', 'TP': 'Unresolved Immune Observable 5', 'TA': 'TA'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_immune_observable_1': ('D', 4.0, 'native source value', 'Initial Unresolved Immune Observable 1. Sets the initial value of bundled SBML species `D`.'), 'initial_unresolved_immune_observable_2': ('DG', 0.0, 'native source value', 'Initial Unresolved Immune Observable 2. Sets the initial value of bundled SBML species `DG`.'), 'initial_unresolved_immune_observable_3': ('I', 0.0, 'native source value', 'Initial Unresolved Immune Observable 3. Sets the initial value of bundled SBML species `I`.'), 'initial_unresolved_immune_observable_4': ('A', 0.125, 'native source value', 'Initial Unresolved Immune Observable 4. Sets the initial value of bundled SBML species `A`.'), 'initial_unresolved_immune_observable_5': ('TP', 0.0, 'native source value', 'Initial Unresolved Immune Observable 5. Sets the initial value of bundled SBML species `TP`.')}
    _HEADLINE_OUTPUTS = {'unresolved_immune_observable_1': ('D', 'native source value', 'Unresolved Immune Observable 1. Maps to bundled source symbol `D`.'), 'unresolved_immune_observable_2': ('DG', 'native source value', 'Unresolved Immune Observable 2. Maps to bundled source symbol `DG`.'), 'unresolved_immune_observable_3': ('I', 'native source value', 'Unresolved Immune Observable 3. Maps to bundled source symbol `I`.'), 'unresolved_immune_observable_4': ('A', 'native source value', 'Unresolved Immune Observable 4. Maps to bundled source symbol `A`.'), 'unresolved_immune_observable_5': ('TP', 'native source value', 'Unresolved Immune Observable 5. Maps to bundled source symbol `TP`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1911190001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
