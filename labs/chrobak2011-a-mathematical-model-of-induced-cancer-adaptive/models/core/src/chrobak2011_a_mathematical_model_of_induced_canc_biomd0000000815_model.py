# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Chrobak2011 - A mathematical model of induced cancer-adaptive immune system competition."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Chrobak2011AMathematicalModelOfInducedCancBiomd0000000815Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000815."""

    _SBML_ID = 'BIOMD0000000815'
    _TITLE = 'Chrobak2011 - A mathematical model of induced cancer-adaptive immune system competition'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x_Cancer', 'y_Immune_System']
    _SPECIES_LABELS = {'x_Cancer': 'Cancer', 'y_Immune_System': 'Immune System'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_cancer': ('x_Cancer', 0.0005, 'native source value', 'Initial Cancer. Sets the initial value of bundled SBML species `x_Cancer`.'), 'initial_immune_system': ('y_Immune_System', 0.01, 'native source value', 'Initial Immune System. Sets the initial value of bundled SBML species `y_Immune_System`.')}
    _HEADLINE_OUTPUTS = {'cancer': ('x_Cancer', 'native source value', 'Cancer. Maps to bundled source symbol `x_Cancer`.'), 'immune_system': ('y_Immune_System', 'native source value', 'Immune System. Maps to bundled source symbol `y_Immune_System`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000815.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
