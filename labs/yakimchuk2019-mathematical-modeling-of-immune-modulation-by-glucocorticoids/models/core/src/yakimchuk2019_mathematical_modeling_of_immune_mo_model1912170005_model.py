# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Yakimchuk2019 - Mathematical modeling of immune modulation by glucocorticoids."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Yakimchuk2019MathematicalModelingOfImmuneMoModel1912170005Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL1912170005."""

    _SBML_ID = 'MODEL1912170005'
    _TITLE = 'Yakimchuk2019 - Mathematical modeling of immune modulation by glucocorticoids'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Te', 'N', 'A', 'Tr', 'T_dc']
    _SPECIES_LABELS = {'Te': 'Unresolved Immune Observable 1', 'N': 'Unresolved Immune Observable 2', 'A': 'Unresolved Immune Observable 3', 'Tr': 'Unresolved Immune Observable 4', 'T_dc': 'Unresolved Immune Observable 5', 'Tr_0': 'Tr'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_immune_observable_1': ('Te', 1.0, 'native source value', 'Initial Unresolved Immune Observable 1. Sets the initial value of bundled SBML species `Te`.'), 'initial_unresolved_immune_observable_2': ('N', 1.0, 'native source value', 'Initial Unresolved Immune Observable 2. Sets the initial value of bundled SBML species `N`.'), 'initial_unresolved_immune_observable_3': ('A', 1.0, 'native source value', 'Initial Unresolved Immune Observable 3. Sets the initial value of bundled SBML species `A`.'), 'initial_unresolved_immune_observable_4': ('Tr', 1.0, 'native source value', 'Initial Unresolved Immune Observable 4. Sets the initial value of bundled SBML species `Tr`.'), 'initial_unresolved_immune_observable_5': ('T_dc', 1.0, 'native source value', 'Initial Unresolved Immune Observable 5. Sets the initial value of bundled SBML species `T_dc`.')}
    _HEADLINE_OUTPUTS = {'unresolved_immune_observable_1': ('Te', 'native source value', 'Unresolved Immune Observable 1. Maps to bundled source symbol `Te`.'), 'unresolved_immune_observable_2': ('N', 'native source value', 'Unresolved Immune Observable 2. Maps to bundled source symbol `N`.'), 'unresolved_immune_observable_3': ('A', 'native source value', 'Unresolved Immune Observable 3. Maps to bundled source symbol `A`.'), 'unresolved_immune_observable_4': ('Tr', 'native source value', 'Unresolved Immune Observable 4. Maps to bundled source symbol `Tr`.'), 'unresolved_immune_observable_5': ('T_dc', 'native source value', 'Unresolved Immune Observable 5. Maps to bundled source symbol `T_dc`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1912170005.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
