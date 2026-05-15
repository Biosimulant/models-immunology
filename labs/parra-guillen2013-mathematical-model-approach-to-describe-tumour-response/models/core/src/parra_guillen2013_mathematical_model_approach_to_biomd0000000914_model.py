# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Parra_Guillen2013 - Mathematical model approach to describe tumour response in mice after vaccine administration_model1."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class ParraGuillen2013MathematicalModelApproachToBiomd0000000914Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000914."""

    _SBML_ID = 'BIOMD0000000914'
    _TITLE = 'Parra_Guillen2013 - Mathematical model approach to describe tumour response in mice after vaccine administration_model1'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['VAC', 'TRAN', 'SVAC', 'Ts', 'REG']
    _SPECIES_LABELS = {'VAC': 'Unresolved Tumor Observable 1', 'TRAN': 'Unresolved Tumor Observable 1 2', 'SVAC': 'Unresolved Tumor Observable 2', 'Ts': 'Unresolved Tumor Observable 2 2', 'REG': 'Unresolved Tumor Observable 3', 'Residual_error': 'Residual error'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('VAC', 1.0, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `VAC`.'), 'initial_unresolved_tumor_observable_1_2': ('TRAN', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 1 2. Sets the initial value of bundled SBML species `TRAN`.'), 'initial_unresolved_tumor_observable_2': ('SVAC', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `SVAC`.'), 'initial_unresolved_tumor_observable_2_2': ('Ts', 0.324, 'native source value', 'Initial Unresolved Tumor Observable 2 2. Sets the initial value of bundled SBML species `Ts`.'), 'initial_unresolved_tumor_observable_3': ('REG', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `REG`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('VAC', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `VAC`.'), 'unresolved_tumor_observable_1_2': ('TRAN', 'native source value', 'Unresolved Tumor Observable 1 2. Maps to bundled source symbol `TRAN`.'), 'unresolved_tumor_observable_2': ('SVAC', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `SVAC`.'), 'unresolved_tumor_observable_2_2': ('Ts', 'native source value', 'Unresolved Tumor Observable 2 2. Maps to bundled source symbol `Ts`.'), 'unresolved_tumor_observable_3': ('REG', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `REG`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000914.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
