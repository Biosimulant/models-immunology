# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Cappuccio2007 - Tumor-immune system interactions and determination of the optimal therapeutic protocol in immunotherapy."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Cappuccio2007TumorImmuneSystemInteractionsABiomd0000001036Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000001036."""

    _SBML_ID = 'BIOMD0000001036'
    _TITLE = 'Cappuccio2007 - Tumor-immune system interactions and determination of the optimal therapeutic protocol in immunotherapy'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Effector_cells', 'Tumor_cells', 'IL_2']
    _SPECIES_LABELS = {'Effector_cells': 'Effector Cells', 'Tumor_cells': 'Tumor Cells', 'IL_2': 'Interleukin 2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_effector_cells': ('Effector_cells', 1e-05, 'native source value', 'Initial Effector Cells. Sets the initial value of bundled SBML species `Effector_cells`.'), 'initial_tumor_cells': ('Tumor_cells', 1e-05, 'native source value', 'Initial Tumor Cells. Sets the initial value of bundled SBML species `Tumor_cells`.'), 'initial_interleukin_2': ('IL_2', 1e-05, 'native source value', 'Initial Interleukin 2. Sets the initial value of bundled SBML species `IL_2`.')}
    _HEADLINE_OUTPUTS = {'effector_cells': ('Effector_cells', 'native source value', 'Effector Cells. Maps to bundled source symbol `Effector_cells`.'), 'tumor_cells': ('Tumor_cells', 'native source value', 'Tumor Cells. Maps to bundled source symbol `Tumor_cells`.'), 'interleukin_2': ('IL_2', 'native source value', 'Interleukin 2. Maps to bundled source symbol `IL_2`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001036.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
