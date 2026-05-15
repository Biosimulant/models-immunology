# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Nikolopoulou2018 - Tumour-immune dynamics with an immune checkpoint inhibitor."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Nikolopoulou2018TumourImmuneDynamicsWithAnModel1908270001Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL1908270001."""

    _SBML_ID = 'MODEL1908270001'
    _TITLE = 'Nikolopoulou2018 - Tumour-immune dynamics with an immune checkpoint inhibitor'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['C', 'T', 'A']
    _SPECIES_LABELS = {'C': 'Unresolved Tumor Observable 1', 'T': 'Unresolved Tumor Observable 2', 'A': 'Unresolved Tumor Observable 3', 'ModelValue_10': 'Initial for K_TQ', 'ModelValue_13': 'Initial for epsilon_C', 'ModelValue_18': 'Initial for gamma', 'ModelValue_11': 'Initial for rho_L', 'ModelValue_12': 'Initial for rho_P'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('C', 0.3968, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `C`.'), 'initial_unresolved_tumor_observable_2': ('T', 0.006, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `T`.'), 'initial_unresolved_tumor_observable_3': ('A', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `A`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('C', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `C`.'), 'unresolved_tumor_observable_2': ('T', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `T`.'), 'unresolved_tumor_observable_3': ('A', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `A`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1908270001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
