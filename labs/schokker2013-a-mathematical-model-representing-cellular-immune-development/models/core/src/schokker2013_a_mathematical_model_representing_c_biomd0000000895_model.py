# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Schokker2013 - A mathematical model representing cellular immune development and response to Salmonella of chicken intestinal tissue."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Schokker2013AMathematicalModelRepresentingCBiomd0000000895Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000895."""

    _SBML_ID = 'BIOMD0000000895'
    _TITLE = 'Schokker2013 - A mathematical model representing cellular immune development and response to Salmonella of chicken intestinal tissue'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['CD4', 'CD8', 'Mr', 'Ma', 'Mi', 'Se', 'Si', 'CD4rec', 'Mrrec']
    _SPECIES_LABELS = {'CD4': 'CD4', 'CD8': 'CD8', 'Mr': 'Unresolved Immune Observable 1', 'Ma': 'Unresolved Immune Observable 2', 'Mi': 'Mi', 'Se': 'Se', 'Si': 'Si', 'CD4rec': 'CD4 Receptor', 'Mrrec': 'Mrrec'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_cd4': ('CD4', 9000000.0, 'native source value', 'Initial CD4. Sets the initial value of bundled SBML species `CD4`.'), 'initial_cd8': ('CD8', 7000000.0, 'native source value', 'Initial CD8. Sets the initial value of bundled SBML species `CD8`.'), 'initial_cd4_receptor': ('CD4rec', 27000000.0, 'native source value', 'Initial CD4 Receptor. Sets the initial value of bundled SBML species `CD4rec`.'), 'initial_unresolved_immune_observable_1': ('Mr', 9000000.0, 'native source value', 'Initial Unresolved Immune Observable 1. Sets the initial value of bundled SBML species `Mr`.'), 'initial_unresolved_immune_observable_2': ('Ma', 0.0, 'native source value', 'Initial Unresolved Immune Observable 2. Sets the initial value of bundled SBML species `Ma`.')}
    _HEADLINE_OUTPUTS = {'cd4': ('CD4', 'native source value', 'CD4. Maps to bundled source symbol `CD4`.'), 'cd8': ('CD8', 'native source value', 'CD8. Maps to bundled source symbol `CD8`.'), 'cd4_receptor': ('CD4rec', 'native source value', 'CD4 Receptor. Maps to bundled source symbol `CD4rec`.'), 'unresolved_immune_observable_1': ('Mr', 'native source value', 'Unresolved Immune Observable 1. Maps to bundled source symbol `Mr`.'), 'unresolved_immune_observable_2': ('Ma', 'native source value', 'Unresolved Immune Observable 2. Maps to bundled source symbol `Ma`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000895.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
