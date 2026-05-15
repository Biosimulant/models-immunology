# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Lopez2014 - A Validated Mathematical Model of Tumor Growth Including Tumor-Host Interaction and Cell-Mediated Immune Response."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Lopez2014AValidatedMathematicalModelOfTumoBiomd0000000784Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000784."""

    _SBML_ID = 'BIOMD0000000784'
    _TITLE = 'Lopez2014 - A Validated Mathematical Model of Tumor Growth Including Tumor-Host Interaction and Cell-Mediated Immune Response'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x_Tumor_Cells', 'y_Healthy_Cells', 'z_Effector_Cells']
    _SPECIES_LABELS = {'x_Tumor_Cells': 'Tumor Cells', 'y_Healthy_Cells': 'Healthy Cells', 'z_Effector_Cells': 'Effector Cells', 'ModelValue_1': 'Initial for d', 'ModelValue_2': 'Initial for lambda', 'ModelValue_3': 'Initial for s'}
    _PARAMETER_INPUTS = {'effector_death_rate': ('d_3', 0.112, 'native source value', 'Effector Death Rate. Sets bundled SBML parameter `d_3`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_tumor_cells': ('x_Tumor_Cells', 0.1, 'native source value', 'Initial Tumor Cells. Sets the initial value of bundled SBML species `x_Tumor_Cells`.'), 'initial_effector_cells': ('z_Effector_Cells', 0.2, 'native source value', 'Initial Effector Cells. Sets the initial value of bundled SBML species `z_Effector_Cells`.'), 'initial_healthy_cells': ('y_Healthy_Cells', 0.9, 'native source value', 'Initial Healthy Cells. Sets the initial value of bundled SBML species `y_Healthy_Cells`.')}
    _HEADLINE_OUTPUTS = {'tumor_cells': ('x_Tumor_Cells', 'native source value', 'Tumor Cells. Maps to bundled source symbol `x_Tumor_Cells`.'), 'effector_cells': ('z_Effector_Cells', 'native source value', 'Effector Cells. Maps to bundled source symbol `z_Effector_Cells`.'), 'healthy_cells': ('y_Healthy_Cells', 'native source value', 'Healthy Cells. Maps to bundled source symbol `y_Healthy_Cells`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000784.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
