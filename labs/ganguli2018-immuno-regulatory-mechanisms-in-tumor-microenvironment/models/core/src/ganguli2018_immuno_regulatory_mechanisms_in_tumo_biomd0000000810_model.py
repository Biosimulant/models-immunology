# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Ganguli2018-immuno regulatory mechanisms in tumor microenvironment."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Ganguli2018ImmunoRegulatoryMechanismsInTumoBiomd0000000810Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000810."""

    _SBML_ID = 'BIOMD0000000810'
    _TITLE = 'Ganguli2018-immuno regulatory mechanisms in tumor microenvironment'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Cancer_Stem_Cells_S', 'Cancer_Cells_C', 'Resistant_Stem_Cells_S_R', 'Resistant_Cancer_Cells_C_R', 'M1_Tumor_Associated_Macrophages', 'M2_Tumor_Associated_Macrophages', 'Type_I_T_helper_Cell_T_H1', 'Type_II_T_helper_cells_T_H2', 'Cytotoxic_T_Cells_T_C', 'Regulatory_T_Cells_T_reg', 'Interferon_gamma', 'Cytokine_IL10', 'Cytokine_IL2', '_100000_SR']
    _SPECIES_LABELS = {'Cancer_Stem_Cells_S': 'Cancer Stem Cells S', 'Cancer_Cells_C': 'Cancer Cells C', 'Resistant_Stem_Cells_S_R': 'Resistant Stem Cells S_R', 'Resistant_Cancer_Cells_C_R': 'Resistant Cancer Cells C R', 'M1_Tumor_Associated_Macrophages': 'Unresolved Tumor Observable 1', 'M2_Tumor_Associated_Macrophages': 'Unresolved Tumor Observable 2', 'Type_I_T_helper_Cell_T_H1': 'Type I T-helper Cell T_H1', 'Type_II_T_helper_cells_T_H2': 'Type II T-helper cells T_H2', 'Cytotoxic_T_Cells_T_C': 'Cytotoxic T-Cells T_C', 'Regulatory_T_Cells_T_reg': 'Regulatory T-Cells T_reg', 'Interferon_gamma': 'Interferon_gamma', 'Cytokine_IL10': 'Cytokine IL10', 'Cytokine_IL2': 'Cytokine IL2', '_100000_SR': '100000*SR'}
    _PARAMETER_INPUTS = {'gompertzian_growth_of_cancer_cells_c_rate': ('r_1', 0.0001, 'native source value', 'Gompertzian Growth Of Cancer Cells C Rate. Sets bundled SBML parameter `r_1`.'), 'gompertzian_growth_of_resistant_cancer_cells_cr_rate': ('r_2', 1e-05, 'native source value', 'Gompertzian Growth Of Resistant Cancer Cells Cr Rate. Sets bundled SBML parameter `r_2`.'), 'proliferation_on_cancer_cells_c_interleukin_10_rate': ('k3', 2.0531, 'unit_2', 'Proliferation On Cancer Cells C Interleukin 10 Rate. Sets bundled SBML parameter `k3`.'), 'proliferation_on_resistant_cancer_cells_cr_interleukin_10_rate': ('k5', 6.7979, 'unit_2', 'Proliferation On Resistant Cancer Cells Cr Interleukin 10 Rate. Sets bundled SBML parameter `k5`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_cancer_stem_cells_s': ('Cancer_Stem_Cells_S', 1.0, 'native source value', 'Initial Cancer Stem Cells S. Sets the initial value of bundled SBML species `Cancer_Stem_Cells_S`.'), 'initial_cancer_cells_c': ('Cancer_Cells_C', 0.0, 'native source value', 'Initial Cancer Cells C. Sets the initial value of bundled SBML species `Cancer_Cells_C`.'), 'initial_resistant_cancer_cells_c_r': ('Resistant_Cancer_Cells_C_R', 0.0, 'native source value', 'Initial Resistant Cancer Cells C R. Sets the initial value of bundled SBML species `Resistant_Cancer_Cells_C_R`.'), 'initial_unresolved_tumor_observable_1': ('M1_Tumor_Associated_Macrophages', 85000.0, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `M1_Tumor_Associated_Macrophages`.'), 'initial_unresolved_tumor_observable_2': ('M2_Tumor_Associated_Macrophages', 15000.0, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `M2_Tumor_Associated_Macrophages`.')}
    _HEADLINE_OUTPUTS = {'cancer_stem_cells_s': ('Cancer_Stem_Cells_S', 'native source value', 'Cancer Stem Cells S. Maps to bundled source symbol `Cancer_Stem_Cells_S`.'), 'cancer_cells_c': ('Cancer_Cells_C', 'native source value', 'Cancer Cells C. Maps to bundled source symbol `Cancer_Cells_C`.'), 'resistant_cancer_cells_c_r': ('Resistant_Cancer_Cells_C_R', 'native source value', 'Resistant Cancer Cells C R. Maps to bundled source symbol `Resistant_Cancer_Cells_C_R`.'), 'unresolved_tumor_observable_1': ('M1_Tumor_Associated_Macrophages', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `M1_Tumor_Associated_Macrophages`.'), 'unresolved_tumor_observable_2': ('M2_Tumor_Associated_Macrophages', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `M2_Tumor_Associated_Macrophages`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000810.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
