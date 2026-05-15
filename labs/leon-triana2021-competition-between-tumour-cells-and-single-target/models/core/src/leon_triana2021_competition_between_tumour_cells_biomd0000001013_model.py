# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Leon-Triana2021 - Competition between tumour cells and single-target CAR T-cells."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class LeonTriana2021CompetitionBetweenTumourCellsBiomd0000001013Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000001013."""

    _SBML_ID = 'BIOMD0000001013'
    _TITLE = 'Leon-Triana2021 - Competition between tumour cells and single-target CAR T-cells'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['CAR_T_cells', 'Tumour_cells']
    _SPECIES_LABELS = {'CAR_T_cells': 'Car T Cells', 'Tumour_cells': 'Tumour Cells'}
    _PARAMETER_INPUTS = {'tumour_death_rate': ('alpha_2', 2.5e-10, 'unit_3', 'Tumour Death Rate. Sets bundled SBML parameter `alpha_2`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_car_t_cells': ('CAR_T_cells', 400000000.0, 'native source value', 'Initial Car T Cells. Sets the initial value of bundled SBML species `CAR_T_cells`.'), 'initial_tumour_cells': ('Tumour_cells', 6700000000.0, 'native source value', 'Initial Tumour Cells. Sets the initial value of bundled SBML species `Tumour_cells`.')}
    _HEADLINE_OUTPUTS = {'car_t_cells': ('CAR_T_cells', 'native source value', 'Car T Cells. Maps to bundled source symbol `CAR_T_cells`.'), 'tumour_cells': ('Tumour_cells', 'native source value', 'Tumour Cells. Maps to bundled source symbol `Tumour_cells`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001013.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
