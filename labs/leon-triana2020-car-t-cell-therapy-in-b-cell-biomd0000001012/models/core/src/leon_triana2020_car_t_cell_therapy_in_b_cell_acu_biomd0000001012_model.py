# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Leon-Triana2020 - CAR T-cell therapy in B-cell acute lymphoblastic leukaemia with contribution from immature B cells."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class LeonTriana2020CarTCellTherapyInBCellAcuBiomd0000001012Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000001012."""

    _SBML_ID = 'BIOMD0000001012'
    _TITLE = 'Leon-Triana2020 - CAR T-cell therapy in B-cell acute lymphoblastic leukaemia with contribution from immature B cells'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['CAR_T_cells', 'Leukaemic_B_cells', 'B_cells_healthy', 'B_cell_progenitors']
    _SPECIES_LABELS = {'CAR_T_cells': 'Car T Cells', 'Leukaemic_B_cells': 'Leukaemic B Cells', 'B_cells_healthy': 'Cells Healthy', 'B_cell_progenitors': 'Cell Progenitors'}
    _PARAMETER_INPUTS = {'cartcell_proliferation_rate': ('beta', 0.1, 'native source value', 'Cartcell Proliferation Rate. Sets bundled SBML parameter `beta`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_car_t_cells': ('CAR_T_cells', 10000000.0, 'native source value', 'Initial Car T Cells. Sets the initial value of bundled SBML species `CAR_T_cells`.'), 'initial_leukaemic_b_cells': ('Leukaemic_B_cells', 50000000000.0, 'native source value', 'Initial Leukaemic B Cells. Sets the initial value of bundled SBML species `Leukaemic_B_cells`.'), 'initial_cells_healthy': ('B_cells_healthy', 25000000000.0, 'native source value', 'Initial Cells Healthy. Sets the initial value of bundled SBML species `B_cells_healthy`.'), 'initial_cell_progenitors': ('B_cell_progenitors', 10000000.0, 'native source value', 'Initial Cell Progenitors. Sets the initial value of bundled SBML species `B_cell_progenitors`.')}
    _HEADLINE_OUTPUTS = {'car_t_cells': ('CAR_T_cells', 'native source value', 'Car T Cells. Maps to bundled source symbol `CAR_T_cells`.'), 'leukaemic_b_cells': ('Leukaemic_B_cells', 'native source value', 'Leukaemic B Cells. Maps to bundled source symbol `Leukaemic_B_cells`.'), 'cells_healthy': ('B_cells_healthy', 'native source value', 'Cells Healthy. Maps to bundled source symbol `B_cells_healthy`.'), 'cell_progenitors': ('B_cell_progenitors', 'native source value', 'Cell Progenitors. Maps to bundled source symbol `B_cell_progenitors`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001012.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
