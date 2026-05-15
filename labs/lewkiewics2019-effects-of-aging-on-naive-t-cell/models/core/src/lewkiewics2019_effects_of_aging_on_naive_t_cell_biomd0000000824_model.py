# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Lewkiewics2019 - effects of aging on naive T cell populations and diversity."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Lewkiewics2019EffectsOfAgingOnNaiveTCellBiomd0000000824Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000824."""

    _SBML_ID = 'BIOMD0000000824'
    _TITLE = 'Lewkiewics2019 - effects of aging on naive T cell populations and diversity'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['myu', 'N']
    _SPECIES_LABELS = {'myu': 'Unresolved Immune Observable 1', 'N': 'Naive T Cells N'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_naive_t_cells_n': ('N', 1.0, 'native source value', 'Initial Naive T Cells N. Sets the initial value of bundled SBML species `N`.')}
    _HEADLINE_OUTPUTS = {'naive_t_cells_n': ('N', 'native source value', 'Naive T Cells N. Maps to bundled source symbol `N`.'), 'unresolved_immune_observable_1': ('myu', 'native source value', 'Unresolved Immune Observable 1. Maps to bundled source symbol `myu`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000824.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
