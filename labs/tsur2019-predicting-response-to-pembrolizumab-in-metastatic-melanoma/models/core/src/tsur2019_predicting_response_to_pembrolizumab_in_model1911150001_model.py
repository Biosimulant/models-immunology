# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Tsur2019 - Predicting response to pembrolizumab in metastatic melanoma by a new personalization algorithm."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Tsur2019PredictingResponseToPembrolizumabInModel1911150001Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL1911150001."""

    _SBML_ID = 'MODEL1911150001'
    _TITLE = 'Tsur2019 - Predicting response to pembrolizumab in metastatic melanoma by a new personalization algorithm'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['A_pc', 'T_il', 'M_el']
    _SPECIES_LABELS = {'A_pc': 'Unresolved Prediction Observable 1', 'T_il': 'Unresolved Prediction Observable 2', 'M_el': 'Unresolved Prediction Observable 3'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_prediction_observable_1': ('A_pc', 1.0, 'native source value', 'Initial Unresolved Prediction Observable 1. Sets the initial value of bundled SBML species `A_pc`.'), 'initial_unresolved_prediction_observable_2': ('T_il', 1.0, 'native source value', 'Initial Unresolved Prediction Observable 2. Sets the initial value of bundled SBML species `T_il`.'), 'initial_unresolved_prediction_observable_3': ('M_el', 50.0, 'native source value', 'Initial Unresolved Prediction Observable 3. Sets the initial value of bundled SBML species `M_el`.')}
    _HEADLINE_OUTPUTS = {'unresolved_prediction_observable_1': ('A_pc', 'native source value', 'Unresolved Prediction Observable 1. Maps to bundled source symbol `A_pc`.'), 'unresolved_prediction_observable_2': ('T_il', 'native source value', 'Unresolved Prediction Observable 2. Maps to bundled source symbol `T_il`.'), 'unresolved_prediction_observable_3': ('M_el', 'native source value', 'Unresolved Prediction Observable 3. Maps to bundled source symbol `M_el`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1911150001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
