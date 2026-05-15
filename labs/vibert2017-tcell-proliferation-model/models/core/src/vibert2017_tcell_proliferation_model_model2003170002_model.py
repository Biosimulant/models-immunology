# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Vibert2017 - Tcell proliferation model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Vibert2017TcellProliferationModelModel2003170002Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL2003170002."""

    _SBML_ID = 'MODEL2003170002'
    _TITLE = 'Vibert2017 - Tcell proliferation model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['M', 'M_p', 'G', 'S', 'G_p', 'S_p', 'G_tf', 'S_tf', 'M_tf']
    _SPECIES_LABELS = {'M': 'Unresolved Immune Observable 1', 'M_p': 'Unresolved Immune Observable 2', 'G': 'Unresolved Immune Observable 3', 'S': 'Unresolved Immune Observable 4', 'G_p': 'Unresolved Immune Observable 5', 'S_p': 'S_p', 'G_tf': 'G_tf', 'S_tf': 'S_tf', 'M_tf': 'M_tf'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_immune_observable_1': ('M', 12.0, 'native source value', 'Initial Unresolved Immune Observable 1. Sets the initial value of bundled SBML species `M`.'), 'initial_unresolved_immune_observable_2': ('M_p', 0.0, 'native source value', 'Initial Unresolved Immune Observable 2. Sets the initial value of bundled SBML species `M_p`.'), 'initial_unresolved_immune_observable_3': ('G', 4.88455, 'native source value', 'Initial Unresolved Immune Observable 3. Sets the initial value of bundled SBML species `G`.'), 'initial_unresolved_immune_observable_4': ('S', 88.8988, 'native source value', 'Initial Unresolved Immune Observable 4. Sets the initial value of bundled SBML species `S`.'), 'initial_unresolved_immune_observable_5': ('G_p', 0.0, 'native source value', 'Initial Unresolved Immune Observable 5. Sets the initial value of bundled SBML species `G_p`.')}
    _HEADLINE_OUTPUTS = {'unresolved_immune_observable_1': ('M', 'native source value', 'Unresolved Immune Observable 1. Maps to bundled source symbol `M`.'), 'unresolved_immune_observable_2': ('M_p', 'native source value', 'Unresolved Immune Observable 2. Maps to bundled source symbol `M_p`.'), 'unresolved_immune_observable_3': ('G', 'native source value', 'Unresolved Immune Observable 3. Maps to bundled source symbol `G`.'), 'unresolved_immune_observable_4': ('S', 'native source value', 'Unresolved Immune Observable 4. Maps to bundled source symbol `S`.'), 'unresolved_immune_observable_5': ('G_p', 'native source value', 'Unresolved Immune Observable 5. Maps to bundled source symbol `G_p`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2003170002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
