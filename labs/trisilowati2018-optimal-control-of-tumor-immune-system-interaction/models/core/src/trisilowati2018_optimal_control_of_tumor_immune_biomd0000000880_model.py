# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Trisilowati2018 - Optimal control of tumor-immune system interaction with treatment."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Trisilowati2018OptimalControlOfTumorImmuneBiomd0000000880Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000880."""

    _SBML_ID = 'BIOMD0000000880'
    _TITLE = 'Trisilowati2018 - Optimal control of tumor-immune system interaction with treatment'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T_Tumor_Cells', 'L_CD8_T_Cells', 'D_Dendritic_Cells', 'H_CD4_T_Cells']
    _SPECIES_LABELS = {'T_Tumor_Cells': 'Unresolved Tumor Observable 1', 'L_CD8_T_Cells': 'CD8 T Cells', 'D_Dendritic_Cells': 'Dendritic Cells', 'H_CD4_T_Cells': 'CD4 T Cells', 'b_1__1': 'b_1_-1', 'b_2__1': 'b_2_-1', 'b_3__1': 'b_3_-1'}
    _PARAMETER_INPUTS = {'tumor_death_cd8_rate': ('alpha_1', 4.2e-08, 'native source value', 'Tumor Death CD8 Rate. Sets bundled SBML parameter `alpha_1`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('T_Tumor_Cells', 1000000.0, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `T_Tumor_Cells`.'), 'initial_cd8_t_cells': ('L_CD8_T_Cells', 10.0, 'native source value', 'Initial CD8 T Cells. Sets the initial value of bundled SBML species `L_CD8_T_Cells`.'), 'initial_cd4_t_cells': ('H_CD4_T_Cells', 5.0, 'native source value', 'Initial CD4 T Cells. Sets the initial value of bundled SBML species `H_CD4_T_Cells`.'), 'initial_dendritic_cells': ('D_Dendritic_Cells', 10.0, 'native source value', 'Initial Dendritic Cells. Sets the initial value of bundled SBML species `D_Dendritic_Cells`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('T_Tumor_Cells', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `T_Tumor_Cells`.'), 'cd8_t_cells': ('L_CD8_T_Cells', 'native source value', 'CD8 T Cells. Maps to bundled source symbol `L_CD8_T_Cells`.'), 'cd4_t_cells': ('H_CD4_T_Cells', 'native source value', 'CD4 T Cells. Maps to bundled source symbol `H_CD4_T_Cells`.'), 'dendritic_cells': ('D_Dendritic_Cells', 'native source value', 'Dendritic Cells. Maps to bundled source symbol `D_Dendritic_Cells`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000880.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
