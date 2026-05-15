# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Wilkie2013r - immune-induced cancer dormancy and immune evasion-resistance."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Wilkie2013rImmuneInducedCancerDormancyAndIBiomd0000000752Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000752."""

    _SBML_ID = 'BIOMD0000000752'
    _TITLE = 'Wilkie2013r - immune-induced cancer dormancy and immune evasion-resistance'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['C', 'I', 'R']
    _SPECIES_LABELS = {'C': 'Unresolved Tumor Observable 1', 'I': 'Unresolved Tumor Observable 2', 'R': 'Unresolved Tumor Observable 3'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('C', 9000.0, 'substance', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `C`.'), 'initial_unresolved_tumor_observable_2': ('I', 100.0, 'substance', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `I`.'), 'initial_unresolved_tumor_observable_3': ('R', 1000.0, 'substance', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `R`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('C', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `C`.'), 'unresolved_tumor_observable_2': ('I', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `I`.'), 'unresolved_tumor_observable_3': ('R', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `R`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000752.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
