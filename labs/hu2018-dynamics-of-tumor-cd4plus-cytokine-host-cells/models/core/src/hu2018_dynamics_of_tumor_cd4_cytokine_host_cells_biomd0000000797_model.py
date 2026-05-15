# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Hu2018 - Dynamics of tumor-CD4+-cytokine-host cells interactions with treatments."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Hu2018DynamicsOfTumorCd4CytokineHostCellsBiomd0000000797Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000797."""

    _SBML_ID = 'BIOMD0000000797'
    _TITLE = 'Hu2018 - Dynamics of tumor-CD4+-cytokine-host cells interactions with treatments'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x_Tumor_Cells', 'y_CD4_T_Cells', 'z_Cytokine', 'w_Healthy_Tissue']
    _SPECIES_LABELS = {'x_Tumor_Cells': 'Tumor Cells', 'y_CD4_T_Cells': 'CD4 T Cells', 'z_Cytokine': 'Cytokine', 'w_Healthy_Tissue': 'Healthy Tissue'}
    _PARAMETER_INPUTS = {'tumor_growth_rate': ('r_1', 0.514, 'native source value', 'Tumor Growth Rate. Sets bundled SBML parameter `r_1`.'), 'tumor_killing_cytokine_rate': ('c_1', 0.2, 'native source value', 'Tumor Killing Cytokine Rate. Sets bundled SBML parameter `c_1`.'), 'cd4t_natural_death_rate': ('mu_1', 0.1, 'native source value', 'Cd4t Natural Death Rate. Sets bundled SBML parameter `mu_1`.'), 'cytokine_decay_rate': ('mu_2', 34.0, 'native source value', 'Cytokine Decay Rate. Sets bundled SBML parameter `mu_2`.'), 'normal_tissue_growth_rate': ('r_2', 0.2822, 'native source value', 'Normal Tissue Growth Rate. Sets bundled SBML parameter `r_2`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_tumor_cells': ('x_Tumor_Cells', 67700.0, 'native source value', 'Initial Tumor Cells. Sets the initial value of bundled SBML species `x_Tumor_Cells`.'), 'initial_cd4_t_cells': ('y_CD4_T_Cells', 1000000.0, 'native source value', 'Initial CD4 T Cells. Sets the initial value of bundled SBML species `y_CD4_T_Cells`.'), 'initial_cytokine': ('z_Cytokine', 100000.0, 'native source value', 'Initial Cytokine. Sets the initial value of bundled SBML species `z_Cytokine`.'), 'initial_healthy_tissue': ('w_Healthy_Tissue', 1000000000.0, 'native source value', 'Initial Healthy Tissue. Sets the initial value of bundled SBML species `w_Healthy_Tissue`.')}
    _HEADLINE_OUTPUTS = {'tumor_cells': ('x_Tumor_Cells', 'native source value', 'Tumor Cells. Maps to bundled source symbol `x_Tumor_Cells`.'), 'cd4_t_cells': ('y_CD4_T_Cells', 'native source value', 'CD4 T Cells. Maps to bundled source symbol `y_CD4_T_Cells`.'), 'cytokine': ('z_Cytokine', 'native source value', 'Cytokine. Maps to bundled source symbol `z_Cytokine`.'), 'healthy_tissue': ('w_Healthy_Tissue', 'native source value', 'Healthy Tissue. Maps to bundled source symbol `w_Healthy_Tissue`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000797.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
