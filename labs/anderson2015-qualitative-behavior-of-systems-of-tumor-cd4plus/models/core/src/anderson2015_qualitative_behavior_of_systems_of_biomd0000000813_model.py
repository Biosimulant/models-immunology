# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Anderson2015 - Qualitative behavior of systems of tumor-CD4+-cytokine interactions with treatments."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Anderson2015QualitativeBehaviorOfSystemsOfBiomd0000000813Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000813."""

    _SBML_ID = 'BIOMD0000000813'
    _TITLE = 'Anderson2015 - Qualitative behavior of systems of tumor-CD4+-cytokine interactions with treatments'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x_Tumor_Cells', 'y_CD4_T_Cells', 'z_Cytokine']
    _SPECIES_LABELS = {'x_Tumor_Cells': 'Tumor Cells', 'y_CD4_T_Cells': 'CD4 T Cells', 'z_Cytokine': 'Cytokine'}
    _PARAMETER_INPUTS = {'tumor_growth_rate': ('r', 0.03, 'native source value', 'Tumor Growth Rate. Sets bundled SBML parameter `r`.'), 'tumor_killing_rate': ('delta', 0.1, 'native source value', 'Tumor Killing Rate. Sets bundled SBML parameter `delta`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_tumor_cells': ('x_Tumor_Cells', 0.5, 'native source value', 'Initial Tumor Cells. Sets the initial value of bundled SBML species `x_Tumor_Cells`.'), 'initial_cd4_t_cells': ('y_CD4_T_Cells', 0.01, 'native source value', 'Initial CD4 T Cells. Sets the initial value of bundled SBML species `y_CD4_T_Cells`.'), 'initial_cytokine': ('z_Cytokine', 0.0, 'native source value', 'Initial Cytokine. Sets the initial value of bundled SBML species `z_Cytokine`.')}
    _HEADLINE_OUTPUTS = {'tumor_cells': ('x_Tumor_Cells', 'native source value', 'Tumor Cells. Maps to bundled source symbol `x_Tumor_Cells`.'), 'cd4_t_cells': ('y_CD4_T_Cells', 'native source value', 'CD4 T Cells. Maps to bundled source symbol `y_CD4_T_Cells`.'), 'cytokine': ('z_Cytokine', 'native source value', 'Cytokine. Maps to bundled source symbol `z_Cytokine`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000813.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
