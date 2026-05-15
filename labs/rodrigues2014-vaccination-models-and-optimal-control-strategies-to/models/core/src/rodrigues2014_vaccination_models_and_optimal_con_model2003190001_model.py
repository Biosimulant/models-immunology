# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Rodrigues2014-Vaccination models and optimal control strategies to dengue."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Rodrigues2014VaccinationModelsAndOptimalConModel2003190001Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL2003190001."""

    _SBML_ID = 'MODEL2003190001'
    _TITLE = 'Rodrigues2014-Vaccination models and optimal control strategies to dengue'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S_h', 'V_h', 'I_h', 'R_h', 'A_m', 'S_m', 'I_m']
    _SPECIES_LABELS = {'S_h': 'Unresolved Model Observable 1', 'V_h': 'Unresolved Model Observable 2', 'I_h': 'Unresolved Model Observable 3', 'R_h': 'Unresolved Model Observable 4', 'A_m': 'Unresolved Model Observable 5', 'S_m': 'S_m', 'I_m': 'I_m'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'unresolved_model_observable_1': ('S_h', 'native source value', 'Unresolved Model Observable 1. Maps to bundled source symbol `S_h`.'), 'unresolved_model_observable_2': ('V_h', 'native source value', 'Unresolved Model Observable 2. Maps to bundled source symbol `V_h`.'), 'unresolved_model_observable_3': ('I_h', 'native source value', 'Unresolved Model Observable 3. Maps to bundled source symbol `I_h`.'), 'unresolved_model_observable_4': ('R_h', 'native source value', 'Unresolved Model Observable 4. Maps to bundled source symbol `R_h`.'), 'unresolved_model_observable_5': ('A_m', 'native source value', 'Unresolved Model Observable 5. Maps to bundled source symbol `A_m`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2003190001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
