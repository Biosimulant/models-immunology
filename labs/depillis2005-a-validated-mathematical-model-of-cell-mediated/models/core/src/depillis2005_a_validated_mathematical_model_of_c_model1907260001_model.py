# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for dePillis2005 - A validated mathematical model of cell-mediated immune response to tumor growth."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Depillis2005AValidatedMathematicalModelOfCModel1907260001Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL1907260001."""

    _SBML_ID = 'MODEL1907260001'
    _TITLE = 'dePillis2005 - A validated mathematical model of cell-mediated immune response to tumor growth'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'N', 'L']
    _SPECIES_LABELS = {'T': 'Unresolved Tumor Observable 1', 'N': 'Unresolved Tumor Observable 2', 'L': 'Unresolved Tumor Observable 3', 'ModelValue_17_0': 'Initial for Tumor_Cell_Surface_Area', 'ModelValue_3_0': 'Initial for d', 'ModelValue_4_0': 'Initial for lambda', 'ModelValue_5_0': 'Initial for s'}
    _PARAMETER_INPUTS = {'tumor_killing_natural_killer_rate': ('c', 3.23e-07, 'native source value', 'Tumor Killing Natural Killer Rate. Sets bundled SBML parameter `c`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('T', 100.0, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `T`.'), 'initial_unresolved_tumor_observable_2': ('N', 1000.0, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `N`.'), 'initial_unresolved_tumor_observable_3': ('L', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `L`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('T', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `T`.'), 'unresolved_tumor_observable_2': ('N', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `N`.'), 'unresolved_tumor_observable_3': ('L', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `L`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1907260001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
