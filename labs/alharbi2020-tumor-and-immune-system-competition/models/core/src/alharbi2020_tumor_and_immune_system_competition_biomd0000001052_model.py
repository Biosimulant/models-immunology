# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Alharbi2020 - Tumor and immune system competition."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Alharbi2020TumorAndImmuneSystemCompetitionBiomd0000001052Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000001052."""

    _SBML_ID = 'BIOMD0000001052'
    _TITLE = 'Alharbi2020 - Tumor and immune system competition'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['I', 'N', 'T']
    _SPECIES_LABELS = {'I': 'Unresolved Tumor Observable 1', 'N': 'Unresolved Tumor Observable 2', 'T': 'Unresolved Tumor Observable 3'}
    _PARAMETER_INPUTS = {'immune_cells_death_rate': ('delta', 0.57, 'native source value', 'Immune Cells Death Rate. Sets bundled SBML parameter `delta`.'), 'death_of_immune_cells_after_interaction_with_tumor_rate': ('mu', 0.813, 'native source value', 'Death Of Immune Cells After Interaction With Tumor Rate. Sets bundled SBML parameter `mu`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('I', 0.999999999999994, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `I`.'), 'initial_unresolved_tumor_observable_2': ('N', 0.999999999999993, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `N`.'), 'initial_unresolved_tumor_observable_3': ('T', 1.22, 'native source value', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `T`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('I', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `I`.'), 'unresolved_tumor_observable_2': ('N', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `N`.'), 'unresolved_tumor_observable_3': ('T', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `T`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001052.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
