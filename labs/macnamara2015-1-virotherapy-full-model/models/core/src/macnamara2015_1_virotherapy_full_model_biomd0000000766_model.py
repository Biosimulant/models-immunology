# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Macnamara2015/1 - virotherapy full model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Macnamara20151VirotherapyFullModelBiomd0000000766Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000766."""

    _SBML_ID = 'BIOMD0000000766'
    _TITLE = 'Macnamara2015/1 - virotherapy full model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['U', 'I', 'M', 'E', 'V']
    _SPECIES_LABELS = {'U': 'Unresolved Tumor Observable 1', 'I': 'Unresolved Tumor Observable 2', 'M': 'Unresolved Tumor Observable 3', 'E': 'Unresolved Tumor Observable 4', 'V': 'Unresolved Tumor Observable 5'}
    _PARAMETER_INPUTS = {'tumor_growth_rate': ('r', 0.927, 'unit_0', 'Tumor Growth Rate. Sets bundled SBML parameter `r`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('U', 1000000.0, 'substance', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `U`.'), 'initial_unresolved_tumor_observable_2': ('I', 0.0, 'substance', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `I`.'), 'initial_unresolved_tumor_observable_3': ('M', 1.0, 'substance', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `M`.'), 'initial_unresolved_tumor_observable_4': ('E', 0.0, 'substance', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `E`.'), 'initial_unresolved_tumor_observable_5': ('V', 1.0, 'substance', 'Initial Unresolved Tumor Observable 5. Sets the initial value of bundled SBML species `V`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('U', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `U`.'), 'unresolved_tumor_observable_2': ('I', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `I`.'), 'unresolved_tumor_observable_3': ('M', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `M`.'), 'unresolved_tumor_observable_4': ('E', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `E`.'), 'unresolved_tumor_observable_5': ('V', 'native source value', 'Unresolved Tumor Observable 5. Maps to bundled source symbol `V`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000766.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
