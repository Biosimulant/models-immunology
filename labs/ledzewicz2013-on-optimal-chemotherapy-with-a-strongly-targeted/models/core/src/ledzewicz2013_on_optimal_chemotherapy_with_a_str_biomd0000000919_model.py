# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Ledzewicz2013 - On optimal chemotherapy with a strongly targeted agent for a model of tumor immune system interactions with generalized logistic growth."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Ledzewicz2013OnOptimalChemotherapyWithAStrBiomd0000000919Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000919."""

    _SBML_ID = 'BIOMD0000000919'
    _TITLE = 'Ledzewicz2013 - On optimal chemotherapy with a strongly targeted agent for a model of tumor immune system interactions with generalized logistic growth'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['y', 'x']
    _SPECIES_LABELS = {'y': 'Unresolved Tumor Observable 1', 'x': 'Unresolved Tumor Observable 2'}
    _PARAMETER_INPUTS = {'a_constant_rate_of_influx_of_t_cells_generated_through_the_primary_organs_rate': ('alpha', 0.1181, 'native source value', 'A Constant Rate Of Influx Of T Cells Generated Through The Primary Organs Rate. Sets bundled SBML parameter `alpha`.'), 'natural_death_of_t_cells_rate': ('delta', 0.37451, 'native source value', 'Natural Death Of T Cells Rate. Sets bundled SBML parameter `delta`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('y', 0.1, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `y`.'), 'initial_unresolved_tumor_observable_2': ('x', 600.0, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `x`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('y', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `y`.'), 'unresolved_tumor_observable_2': ('x', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `x`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000919.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
