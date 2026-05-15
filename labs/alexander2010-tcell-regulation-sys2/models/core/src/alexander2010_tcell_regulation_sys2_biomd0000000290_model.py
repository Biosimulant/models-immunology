# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Alexander2010_Tcell_Regulation_Sys2."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Alexander2010TcellRegulationSys2Biomd0000000290Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000290."""

    _SBML_ID = 'BIOMD0000000290'
    _TITLE = 'Alexander2010_Tcell_Regulation_Sys2'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['A', 'R', 'E', 'G', 'A_im']
    _SPECIES_LABELS = {'A': 'Unresolved Immune Observable 1', 'R': 'Unresolved Immune Observable 2', 'E': 'Unresolved Immune Observable 3', 'G': 'Unresolved Immune Observable 4', 'A_im': 'Unresolved Immune Observable 5'}
    _PARAMETER_INPUTS = {'r2_self_antigen_release_triggered_by_e_rate': ('gamma', 2000.0, 'per_day', 'R2 Self Antigen Release Triggered By E Rate. Sets bundled SBML parameter `gamma`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_immune_observable_1': ('A', 1.0, 'native source value', 'Initial Unresolved Immune Observable 1. Sets the initial value of bundled SBML species `A`.'), 'initial_unresolved_immune_observable_2': ('R', 0.0, 'native source value', 'Initial Unresolved Immune Observable 2. Sets the initial value of bundled SBML species `R`.'), 'initial_unresolved_immune_observable_3': ('E', 0.0, 'native source value', 'Initial Unresolved Immune Observable 3. Sets the initial value of bundled SBML species `E`.'), 'initial_unresolved_immune_observable_4': ('G', 100000000.0, 'native source value', 'Initial Unresolved Immune Observable 4. Sets the initial value of bundled SBML species `G`.')}
    _HEADLINE_OUTPUTS = {'unresolved_immune_observable_1': ('A', 'native source value', 'Unresolved Immune Observable 1. Maps to bundled source symbol `A`.'), 'unresolved_immune_observable_2': ('R', 'native source value', 'Unresolved Immune Observable 2. Maps to bundled source symbol `R`.'), 'unresolved_immune_observable_3': ('E', 'native source value', 'Unresolved Immune Observable 3. Maps to bundled source symbol `E`.'), 'unresolved_immune_observable_4': ('G', 'native source value', 'Unresolved Immune Observable 4. Maps to bundled source symbol `G`.'), 'unresolved_immune_observable_5': ('A_im', 'native source value', 'Unresolved Immune Observable 5. Maps to bundled source symbol `A_im`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000290.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
