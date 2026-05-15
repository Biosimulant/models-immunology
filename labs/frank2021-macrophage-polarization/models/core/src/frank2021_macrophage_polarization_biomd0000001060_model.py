# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Frank2021 - Macrophage polarization."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Frank2021MacrophagePolarizationBiomd0000001060Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000001060."""

    _SBML_ID = 'BIOMD0000001060'
    _TITLE = 'Frank2021 - Macrophage polarization'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x1', 'x2']
    _SPECIES_LABELS = {'x1': 'Unresolved Signaling Observable 1', 'x2': 'Unresolved Signaling Observable 2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_signaling_observable_1': ('x1', 1.2, 'native source value', 'Initial Unresolved Signaling Observable 1. Sets the initial value of bundled SBML species `x1`.'), 'initial_unresolved_signaling_observable_2': ('x2', 2.0, 'native source value', 'Initial Unresolved Signaling Observable 2. Sets the initial value of bundled SBML species `x2`.')}
    _HEADLINE_OUTPUTS = {'unresolved_signaling_observable_1': ('x1', 'native source value', 'Unresolved Signaling Observable 1. Maps to bundled source symbol `x1`.'), 'unresolved_signaling_observable_2': ('x2', 'native source value', 'Unresolved Signaling Observable 2. Maps to bundled source symbol `x2`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001060.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
