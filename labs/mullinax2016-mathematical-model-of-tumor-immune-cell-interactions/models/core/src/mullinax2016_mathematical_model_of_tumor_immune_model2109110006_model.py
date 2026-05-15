# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Mullinax2016 - Mathematical model of tumor-immune cell interactions to optimize the meta-phenotype of TIL subpopulations."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Mullinax2016MathematicalModelOfTumorImmuneModel2109110006Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL2109110006."""

    _SBML_ID = 'MODEL2109110006'
    _TITLE = 'Mullinax2016 - Mathematical model of tumor-immune cell interactions to optimize the meta-phenotype of TIL subpopulations'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'E', 'N', 'R']
    _SPECIES_LABELS = {'T': 'Unresolved Tumor Observable 1', 'E': 'Unresolved Tumor Observable 2', 'N': 'Unresolved Tumor Observable 3', 'R': 'Unresolved Tumor Observable 4'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('T', 1.0, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `T`.'), 'initial_unresolved_tumor_observable_2': ('E', 0.1, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `E`.'), 'initial_unresolved_tumor_observable_3': ('N', 0.1, 'native source value', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `N`.'), 'initial_unresolved_tumor_observable_4': ('R', 0.1, 'native source value', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `R`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('T', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `T`.'), 'unresolved_tumor_observable_2': ('E', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `E`.'), 'unresolved_tumor_observable_3': ('N', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `N`.'), 'unresolved_tumor_observable_4': ('R', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `R`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2109110006.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
