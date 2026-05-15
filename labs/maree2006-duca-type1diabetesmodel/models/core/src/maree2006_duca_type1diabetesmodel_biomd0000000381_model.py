# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Maree2006_DuCa_Type1DiabetesModel."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Maree2006DucaType1diabetesmodelBiomd0000000381Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000381."""

    _SBML_ID = 'BIOMD0000000381'
    _TITLE = 'Maree2006_DuCa_Type1DiabetesModel'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['M', 'Ma', 'Bn', 'Ba', 'Cy']
    _SPECIES_LABELS = {'M': 'Unresolved Immune Observable 1', 'Ma': 'Unresolved Immune Observable 2', 'Bn': 'Unresolved Immune Observable 3', 'Ba': 'Unresolved Immune Observable 4', 'Cy': 'Unresolved Immune Observable 5', 'parameter_1': 'x'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'unresolved_immune_observable_1': ('M', 'native source value', 'Unresolved Immune Observable 1. Maps to bundled source symbol `M`.'), 'unresolved_immune_observable_2': ('Ma', 'native source value', 'Unresolved Immune Observable 2. Maps to bundled source symbol `Ma`.'), 'unresolved_immune_observable_3': ('Bn', 'native source value', 'Unresolved Immune Observable 3. Maps to bundled source symbol `Bn`.'), 'unresolved_immune_observable_4': ('Ba', 'native source value', 'Unresolved Immune Observable 4. Maps to bundled source symbol `Ba`.'), 'unresolved_immune_observable_5': ('Cy', 'native source value', 'Unresolved Immune Observable 5. Maps to bundled source symbol `Cy`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000381.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
