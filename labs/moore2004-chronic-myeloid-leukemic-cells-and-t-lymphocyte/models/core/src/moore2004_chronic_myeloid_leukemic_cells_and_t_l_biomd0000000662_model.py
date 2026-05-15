# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Moore2004 - Chronic Myeloid Leukemic cells and T-lymphocyte interaction."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Moore2004ChronicMyeloidLeukemicCellsAndTLBiomd0000000662Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000662."""

    _SBML_ID = 'BIOMD0000000662'
    _TITLE = 'Moore2004 - Chronic Myeloid Leukemic cells and T-lymphocyte interaction'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['CML', 'T_cell_naive', 'T_cell_effector', 'Source', 'Sink']
    _SPECIES_LABELS = {'CML': 'Unresolved Tumor Observable 3', 'T_cell_naive': 'Unresolved Tumor Observable 2', 'T_cell_effector': 'Unresolved Tumor Observable 1', 'Source': 'Source', 'Sink': 'Sink'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('T_cell_effector', 20.0, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `T_cell_effector`.'), 'initial_unresolved_tumor_observable_2': ('T_cell_naive', 1510.0, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `T_cell_naive`.'), 'initial_unresolved_tumor_observable_3': ('CML', 10000.0, 'native source value', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `CML`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('T_cell_effector', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `T_cell_effector`.'), 'unresolved_tumor_observable_2': ('T_cell_naive', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `T_cell_naive`.'), 'unresolved_tumor_observable_3': ('CML', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `CML`.'), 'source': ('Source', 'native source value', 'Source. Maps to bundled source symbol `Source`.'), 'sink': ('Sink', 'native source value', 'Sink. Maps to bundled source symbol `Sink`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000662.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
