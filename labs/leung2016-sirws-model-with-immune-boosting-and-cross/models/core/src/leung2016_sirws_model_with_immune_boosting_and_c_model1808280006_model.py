# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Leung2016 - SIRWS model with immune boosting and cross-immunity between two pathogens."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Leung2016SirwsModelWithImmuneBoostingAndCModel1808280006Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL1808280006."""

    _SBML_ID = 'MODEL1808280006'
    _TITLE = 'Leung2016 - SIRWS model with immune boosting and cross-immunity between two pathogens'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['X_SS', 'X_IS', 'X_RS', 'X_WS', 'X_SI', 'X_II', 'X_RI', 'X_WI', 'X_SR', 'X_IR', 'X_RR', 'X_WR', 'X_SW', 'X_IW', 'X_RW', 'X_WW']
    _SPECIES_LABELS = {'X_SS': 'Unresolved Signaling Observable 1', 'X_IS': 'Unresolved Signaling Observable 2', 'X_RS': 'Unresolved Signaling Observable 3', 'X_WS': 'Unresolved Signaling Observable 4', 'X_SI': 'Unresolved Signaling Observable 5', 'X_II': 'X_II', 'X_RI': 'X_RI', 'X_WI': 'X_WI', 'X_SR': 'X_SR', 'X_IR': 'X_IR', 'X_RR': 'X_RR', 'X_WR': 'X_WR', 'X_SW': 'X_SW', 'X_IW': 'X_IW', 'X_RW': 'X_RW', 'X_WW': 'X_WW'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_signaling_observable_1': ('X_SS', 0.058, 'native source value', 'Initial Unresolved Signaling Observable 1. Sets the initial value of bundled SBML species `X_SS`.'), 'initial_unresolved_signaling_observable_2': ('X_IS', 0.001, 'native source value', 'Initial Unresolved Signaling Observable 2. Sets the initial value of bundled SBML species `X_IS`.'), 'initial_unresolved_signaling_observable_3': ('X_RS', 0.41, 'native source value', 'Initial Unresolved Signaling Observable 3. Sets the initial value of bundled SBML species `X_RS`.'), 'initial_unresolved_signaling_observable_4': ('X_WS', 0.1, 'native source value', 'Initial Unresolved Signaling Observable 4. Sets the initial value of bundled SBML species `X_WS`.'), 'initial_unresolved_signaling_observable_5': ('X_SI', 0.001, 'native source value', 'Initial Unresolved Signaling Observable 5. Sets the initial value of bundled SBML species `X_SI`.')}
    _HEADLINE_OUTPUTS = {'unresolved_signaling_observable_1': ('X_SS', 'native source value', 'Unresolved Signaling Observable 1. Maps to bundled source symbol `X_SS`.'), 'unresolved_signaling_observable_2': ('X_IS', 'native source value', 'Unresolved Signaling Observable 2. Maps to bundled source symbol `X_IS`.'), 'unresolved_signaling_observable_3': ('X_RS', 'native source value', 'Unresolved Signaling Observable 3. Maps to bundled source symbol `X_RS`.'), 'unresolved_signaling_observable_4': ('X_WS', 'native source value', 'Unresolved Signaling Observable 4. Maps to bundled source symbol `X_WS`.'), 'unresolved_signaling_observable_5': ('X_SI', 'native source value', 'Unresolved Signaling Observable 5. Maps to bundled source symbol `X_SI`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1808280006.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
