# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Louzoun2014 - A mathematical model for pancreatic cancer growth and treatments."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Louzoun2014AMathematicalModelForPancreaticModel1909100002Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL1909100002."""

    _SBML_ID = 'MODEL1909100002'
    _TITLE = 'Louzoun2014 - A mathematical model for pancreatic cancer growth and treatments'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['C', 'P', 'R', 'T']
    _SPECIES_LABELS = {'C': 'Unresolved Tumor Observable 1', 'P': 'Unresolved Tumor Observable 2', 'R': 'Unresolved Tumor Observable 3', 'T': 'Unresolved Tumor Observable 4', 'ModelValue_0': 'Initial for C_0', 'ModelValue_1': 'Initial for P_0', 'ModelValue_2': 'Initial for k_c', 'ModelValue_6': 'Initial for k_p', 'ModelValue_9': 'Initial for lambda_p', 'ModelValue_11': 'Initial for lambda_r'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('C', 200.0, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `C`.'), 'initial_unresolved_tumor_observable_2': ('P', 99250.0, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `P`.'), 'initial_unresolved_tumor_observable_3': ('R', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `R`.'), 'initial_unresolved_tumor_observable_4': ('T', 0.091, 'native source value', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `T`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('C', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `C`.'), 'unresolved_tumor_observable_2': ('P', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `P`.'), 'unresolved_tumor_observable_3': ('R', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `R`.'), 'unresolved_tumor_observable_4': ('T', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `T`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1909100002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
