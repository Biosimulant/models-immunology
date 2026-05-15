# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Tsur2019 - Response of patients with melanoma to immune checkpoint blockade."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Tsur2019ResponseOfPatientsWithMelanomaToIBiomd0000000838Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000838."""

    _SBML_ID = 'BIOMD0000000838'
    _TITLE = 'Tsur2019 - Response of patients with melanoma to immune checkpoint blockade'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['A', 'T', 'M']
    _SPECIES_LABELS = {'A': 'Unresolved Prediction Observable 1', 'T': 'Unresolved Prediction Observable 2', 'M': 'Unresolved Prediction Observable 3'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_prediction_observable_1': ('A', 14119.9020779221, 'native source value', 'Initial Unresolved Prediction Observable 1. Sets the initial value of bundled SBML species `A`.'), 'initial_unresolved_prediction_observable_2': ('T', 66094173.0355407, 'native source value', 'Initial Unresolved Prediction Observable 2. Sets the initial value of bundled SBML species `T`.'), 'initial_unresolved_prediction_observable_3': ('M', 1000000.0, 'native source value', 'Initial Unresolved Prediction Observable 3. Sets the initial value of bundled SBML species `M`.')}
    _HEADLINE_OUTPUTS = {'unresolved_prediction_observable_1': ('A', 'native source value', 'Unresolved Prediction Observable 1. Maps to bundled source symbol `A`.'), 'unresolved_prediction_observable_2': ('T', 'native source value', 'Unresolved Prediction Observable 2. Maps to bundled source symbol `T`.'), 'unresolved_prediction_observable_3': ('M', 'native source value', 'Unresolved Prediction Observable 3. Maps to bundled source symbol `M`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000838.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
