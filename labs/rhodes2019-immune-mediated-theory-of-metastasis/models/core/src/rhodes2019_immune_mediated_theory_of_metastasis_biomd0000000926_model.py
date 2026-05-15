# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Rhodes2019 - Immune-Mediated theory of Metastasis."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Rhodes2019ImmuneMediatedTheoryOfMetastasisBiomd0000000926Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000926."""

    _SBML_ID = 'BIOMD0000000926'
    _TITLE = 'Rhodes2019 - Immune-Mediated theory of Metastasis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Tumor_Cell_u_1', 'TE_immune_Cell_y_1', 'CT_immune_Cell_x_1', 'Tumor_Cell_u_2', 'CT_immune_Cell_x_2', 'TE_immune_Cell_y_2', 'Necrotic_Cell_v_1', 'Necrotic_Cell_v_2']
    _SPECIES_LABELS = {'Tumor_Cell_u_1': 'Tumor Cell U 1', 'TE_immune_Cell_y_1': 'Te Immune Cell Y 1', 'CT_immune_Cell_x_1': 'Ct Immune Cell X 1', 'Tumor_Cell_u_2': 'Tumor Cell(u_2)', 'CT_immune_Cell_x_2': 'Ct Immune Cell X 2', 'TE_immune_Cell_y_2': 'Te Immune Cell Y 2', 'Necrotic_Cell_v_1': 'Necrotic Cell(v_1)', 'Necrotic_Cell_v_2': 'Necrotic Cell(v_2)', 'v_v2_minv_maxv_lowv_upv': 'v(v2;minv,maxv,lowv,upv)', 'e_x2_0_maxct_lowesstct_upestct': 'e(x2,0,maxct,lowesstct,upestct)', 'v_y2_minestte_maxestte_lowestte_upestte': 'v(y2,minestte,maxestte,lowestte,upestte)'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_te_immune_cell_y_1': ('TE_immune_Cell_y_1', 0.001, 'native source value', 'Initial Te Immune Cell Y 1. Sets the initial value of bundled SBML species `TE_immune_Cell_y_1`.'), 'initial_ct_immune_cell_x_1': ('CT_immune_Cell_x_1', 1694915.25423729, 'native source value', 'Initial Ct Immune Cell X 1. Sets the initial value of bundled SBML species `CT_immune_Cell_x_1`.'), 'initial_ct_immune_cell_x_2': ('CT_immune_Cell_x_2', 1694915.25423729, 'native source value', 'Initial Ct Immune Cell X 2. Sets the initial value of bundled SBML species `CT_immune_Cell_x_2`.'), 'initial_te_immune_cell_y_2': ('TE_immune_Cell_y_2', 1e-10, 'native source value', 'Initial Te Immune Cell Y 2. Sets the initial value of bundled SBML species `TE_immune_Cell_y_2`.'), 'initial_tumor_cell_u_1': ('Tumor_Cell_u_1', 1.0, 'native source value', 'Initial Tumor Cell U 1. Sets the initial value of bundled SBML species `Tumor_Cell_u_1`.')}
    _HEADLINE_OUTPUTS = {'te_immune_cell_y_1': ('TE_immune_Cell_y_1', 'native source value', 'Te Immune Cell Y 1. Maps to bundled source symbol `TE_immune_Cell_y_1`.'), 'ct_immune_cell_x_1': ('CT_immune_Cell_x_1', 'native source value', 'Ct Immune Cell X 1. Maps to bundled source symbol `CT_immune_Cell_x_1`.'), 'ct_immune_cell_x_2': ('CT_immune_Cell_x_2', 'native source value', 'Ct Immune Cell X 2. Maps to bundled source symbol `CT_immune_Cell_x_2`.'), 'te_immune_cell_y_2': ('TE_immune_Cell_y_2', 'native source value', 'Te Immune Cell Y 2. Maps to bundled source symbol `TE_immune_Cell_y_2`.'), 'tumor_cell_u_1': ('Tumor_Cell_u_1', 'native source value', 'Tumor Cell U 1. Maps to bundled source symbol `Tumor_Cell_u_1`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000926.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
