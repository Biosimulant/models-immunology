# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Banerjee2008 - Immunotherapy with interleukin-2: A study based on mathematical modeling."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Banerjee2008ImmunotherapyWithInterleukin2AModel2001130001Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL2001130001."""

    _SBML_ID = 'MODEL2001130001'
    _TITLE = 'Banerjee2008 - Immunotherapy with interleukin-2: A study based on mathematical modeling'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x', 'y', 'z']
    _SPECIES_LABELS = {'x': 'Unresolved Signaling Observable 1', 'y': 'Unresolved Signaling Observable 2', 'z': 'Unresolved Signaling Observable 3'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_signaling_observable_1': ('x', 0.0, 'native source value', 'Initial Unresolved Signaling Observable 1. Sets the initial value of bundled SBML species `x`.'), 'initial_unresolved_signaling_observable_2': ('y', 0.05, 'native source value', 'Initial Unresolved Signaling Observable 2. Sets the initial value of bundled SBML species `y`.'), 'initial_unresolved_signaling_observable_3': ('z', 0.005, 'native source value', 'Initial Unresolved Signaling Observable 3. Sets the initial value of bundled SBML species `z`.')}
    _HEADLINE_OUTPUTS = {'unresolved_signaling_observable_1': ('x', 'native source value', 'Unresolved Signaling Observable 1. Maps to bundled source symbol `x`.'), 'unresolved_signaling_observable_2': ('y', 'native source value', 'Unresolved Signaling Observable 2. Maps to bundled source symbol `y`.'), 'unresolved_signaling_observable_3': ('z', 'native source value', 'Unresolved Signaling Observable 3. Maps to bundled source symbol `z`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2001130001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
