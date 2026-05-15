# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Ewald2021 - Innate immune response during invasive aspergillosis by dynamic optimization."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Ewald2021InnateImmuneResponseDuringInvasiveModel2105110001Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL2105110001."""

    _SBML_ID = 'MODEL2105110001'
    _TITLE = 'Ewald2021 - Innate immune response during invasive aspergillosis by dynamic optimization'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['NEU', 'AEC', 'AM', 'SWO', 'CYT', 'HYP']
    _SPECIES_LABELS = {'NEU': 'Unresolved Immune Observable 1', 'AEC': 'Unresolved Immune Observable 2', 'AM': 'Unresolved Immune Observable 3', 'SWO': 'Unresolved Immune Observable 4', 'CYT': 'Unresolved Immune Observable 5', 'HYP': 'HYP'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_immune_observable_1': ('NEU', 0.2628, 'native source value', 'Initial Unresolved Immune Observable 1. Sets the initial value of bundled SBML species `NEU`.'), 'initial_unresolved_immune_observable_2': ('AEC', 11.43, 'native source value', 'Initial Unresolved Immune Observable 2. Sets the initial value of bundled SBML species `AEC`.'), 'initial_unresolved_immune_observable_3': ('AM', 0.2926, 'native source value', 'Initial Unresolved Immune Observable 3. Sets the initial value of bundled SBML species `AM`.'), 'initial_unresolved_immune_observable_4': ('SWO', 0.0, 'native source value', 'Initial Unresolved Immune Observable 4. Sets the initial value of bundled SBML species `SWO`.'), 'initial_unresolved_immune_observable_5': ('CYT', 0.0, 'native source value', 'Initial Unresolved Immune Observable 5. Sets the initial value of bundled SBML species `CYT`.')}
    _HEADLINE_OUTPUTS = {'unresolved_immune_observable_1': ('NEU', 'native source value', 'Unresolved Immune Observable 1. Maps to bundled source symbol `NEU`.'), 'unresolved_immune_observable_2': ('AEC', 'native source value', 'Unresolved Immune Observable 2. Maps to bundled source symbol `AEC`.'), 'unresolved_immune_observable_3': ('AM', 'native source value', 'Unresolved Immune Observable 3. Maps to bundled source symbol `AM`.'), 'unresolved_immune_observable_4': ('SWO', 'native source value', 'Unresolved Immune Observable 4. Maps to bundled source symbol `SWO`.'), 'unresolved_immune_observable_5': ('CYT', 'native source value', 'Unresolved Immune Observable 5. Maps to bundled source symbol `CYT`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2105110001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
