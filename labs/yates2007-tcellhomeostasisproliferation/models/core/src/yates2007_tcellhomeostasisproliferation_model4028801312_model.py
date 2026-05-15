# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Yates2007_TcellHomeostasisProliferation."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Yates2007TcellhomeostasisproliferationModel4028801312Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL4028801312."""

    _SBML_ID = 'MODEL4028801312'
    _TITLE = 'Yates2007_TcellHomeostasisProliferation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rateRule'
    _OBSERVABLES = ['x', 'y']
    _SPECIES_LABELS = {'x': 'Unresolved Infection Observable 1', 'y': 'Unresolved Infection Observable 2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'unresolved_infection_observable_1': ('x', 'native source value', 'Unresolved Infection Observable 1. Maps to bundled source symbol `x`.'), 'unresolved_infection_observable_2': ('y', 'native source value', 'Unresolved Infection Observable 2. Maps to bundled source symbol `y`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL4028801312.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
