# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Leon-Triana2021 - Competition between tumour cells and dual-target CAR T-cells."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class LeonTriana2021CompetitionBetweenTumourCellsBiomd0000001014Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000001014."""

    _SBML_ID = 'BIOMD0000001014'
    _TITLE = 'Leon-Triana2021 - Competition between tumour cells and dual-target CAR T-cells'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['CAR_T_cells_on_tumour', 'Tumour_cells', 'CAR_T_cells_off_tumour', 'B_cells', 'CAR_T_cells_total']
    _SPECIES_LABELS = {'CAR_T_cells_on_tumour': 'Car T Cells On Tumour', 'Tumour_cells': 'Tumour Cells', 'CAR_T_cells_off_tumour': 'Car T Cells Off Tumour', 'B_cells': 'Cells', 'CAR_T_cells_total': 'Car T Cells Total'}
    _PARAMETER_INPUTS = {'tumour_death_rate': ('alpha_2', 2.5e-10, 'unit_3', 'Tumour Death Rate. Sets bundled SBML parameter `alpha_2`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_car_t_cells_on_tumour': ('CAR_T_cells_on_tumour', 0.0, 'native source value', 'Initial Car T Cells On Tumour. Sets the initial value of bundled SBML species `CAR_T_cells_on_tumour`.'), 'initial_car_t_cells_off_tumour': ('CAR_T_cells_off_tumour', 200000000.0, 'native source value', 'Initial Car T Cells Off Tumour. Sets the initial value of bundled SBML species `CAR_T_cells_off_tumour`.'), 'initial_tumour_cells': ('Tumour_cells', 33500000000.0, 'native source value', 'Initial Tumour Cells. Sets the initial value of bundled SBML species `Tumour_cells`.'), 'initial_cells': ('B_cells', 25000000000.0, 'native source value', 'Initial Cells. Sets the initial value of bundled SBML species `B_cells`.')}
    _HEADLINE_OUTPUTS = {'car_t_cells_on_tumour': ('CAR_T_cells_on_tumour', 'native source value', 'Car T Cells On Tumour. Maps to bundled source symbol `CAR_T_cells_on_tumour`.'), 'car_t_cells_off_tumour': ('CAR_T_cells_off_tumour', 'native source value', 'Car T Cells Off Tumour. Maps to bundled source symbol `CAR_T_cells_off_tumour`.'), 'car_t_cells_total': ('CAR_T_cells_total', 'native source value', 'Car T Cells Total. Maps to bundled source symbol `CAR_T_cells_total`.'), 'tumour_cells': ('Tumour_cells', 'native source value', 'Tumour Cells. Maps to bundled source symbol `Tumour_cells`.'), 'cells': ('B_cells', 'native source value', 'Cells. Maps to bundled source symbol `B_cells`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001014.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
