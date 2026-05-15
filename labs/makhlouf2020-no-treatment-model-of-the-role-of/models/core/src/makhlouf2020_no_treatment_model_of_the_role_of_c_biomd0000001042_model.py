# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Makhlouf2020 - No treatment model of the role of CD4 T cells in tumor-immune interactions."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Makhlouf2020NoTreatmentModelOfTheRoleOfCBiomd0000001042Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000001042."""

    _SBML_ID = 'BIOMD0000001042'
    _TITLE = 'Makhlouf2020 - No treatment model of the role of CD4 T cells in tumor-immune interactions'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Tumor_cells', 'NK_cells', 'CD8_T_cells', 'CD4_T_cells', 'Circulating_lymphocytes', 'IL_2']
    _SPECIES_LABELS = {'Tumor_cells': 'Tumor Cells', 'NK_cells': 'Natural Killer Cells', 'CD8_T_cells': 'CD8 T Cells', 'CD4_T_cells': 'CD4 T Cells', 'Circulating_lymphocytes': 'Circulating_lymphocytes', 'IL_2': 'Interleukin 2'}
    _PARAMETER_INPUTS = {'tumour_death_rate': ('c', 6.41e-11, 'unit_3', 'Tumour Death Rate. Sets bundled SBML parameter `c`.'), 'tumour_death_rate_2': ('c_1', 0.2, 'unit_4', 'Tumour Death Rate 2. Sets bundled SBML parameter `c_1`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_tumor_cells': ('Tumor_cells', 10000000.0, 'native source value', 'Initial Tumor Cells. Sets the initial value of bundled SBML species `Tumor_cells`.'), 'initial_cd8_t_cells': ('CD8_T_cells', 100.0, 'native source value', 'Initial CD8 T Cells. Sets the initial value of bundled SBML species `CD8_T_cells`.'), 'initial_cd4_t_cells': ('CD4_T_cells', 1000000.0, 'native source value', 'Initial CD4 T Cells. Sets the initial value of bundled SBML species `CD4_T_cells`.'), 'initial_interleukin_2': ('IL_2', 100000.0, 'native source value', 'Initial Interleukin 2. Sets the initial value of bundled SBML species `IL_2`.'), 'initial_natural_killer_cells': ('NK_cells', 1000.0, 'native source value', 'Initial Natural Killer Cells. Sets the initial value of bundled SBML species `NK_cells`.')}
    _HEADLINE_OUTPUTS = {'tumor_cells': ('Tumor_cells', 'native source value', 'Tumor Cells. Maps to bundled source symbol `Tumor_cells`.'), 'cd8_t_cells': ('CD8_T_cells', 'native source value', 'CD8 T Cells. Maps to bundled source symbol `CD8_T_cells`.'), 'cd4_t_cells': ('CD4_T_cells', 'native source value', 'CD4 T Cells. Maps to bundled source symbol `CD4_T_cells`.'), 'interleukin_2': ('IL_2', 'native source value', 'Interleukin 2. Maps to bundled source symbol `IL_2`.'), 'natural_killer_cells': ('NK_cells', 'native source value', 'Natural Killer Cells. Maps to bundled source symbol `NK_cells`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001042.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
