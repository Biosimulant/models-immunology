# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for dePillis2009 - Mathematical model creation for cancer chemo-immunotherapy."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Depillis2009MathematicalModelCreationForCanBiomd0000000779Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000779."""

    _SBML_ID = 'BIOMD0000000779'
    _TITLE = 'dePillis2009 - Mathematical model creation for cancer chemo-immunotherapy'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T_Tumour_Cells', 'N_Natural_Killer_Cells', 'L_CD8_T_Cells', 'C_Lymphocytes', 'M_Chemotherapy_Drug', 'I_IL_2']
    _SPECIES_LABELS = {'T_Tumour_Cells': 'Unresolved Tumor Observable 1', 'N_Natural_Killer_Cells': 'Natural Killer Cells', 'L_CD8_T_Cells': 'CD8 T Cells', 'C_Lymphocytes': 'C_Lymphocytes', 'M_Chemotherapy_Drug': 'Chemotherapy Drug', 'I_IL_2': 'Interleukin 2', 'ModelValue_34_0': 'Initial for d', 'ModelValue_35_0': 'Initial for l', 'ModelValue_36_0': 'Initial for s'}
    _PARAMETER_INPUTS = {'natural_killer_induced_tumour_death_rate': ('c', 2.9077e-13, 'native source value', 'Natural Killer Induced Tumour Death Rate. Sets bundled SBML parameter `c`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_chemotherapy_drug': ('M_Chemotherapy_Drug', 0.0, 'native source value', 'Initial Chemotherapy Drug. Sets the initial value of bundled SBML species `M_Chemotherapy_Drug`.'), 'initial_unresolved_tumor_observable_1': ('T_Tumour_Cells', 10000000.0, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `T_Tumour_Cells`.'), 'initial_cd8_t_cells': ('L_CD8_T_Cells', 526800.0, 'native source value', 'Initial CD8 T Cells. Sets the initial value of bundled SBML species `L_CD8_T_Cells`.'), 'initial_interleukin_2': ('I_IL_2', 1073.0, 'native source value', 'Initial Interleukin 2. Sets the initial value of bundled SBML species `I_IL_2`.'), 'initial_natural_killer_cells': ('N_Natural_Killer_Cells', 250000000.0, 'native source value', 'Initial Natural Killer Cells. Sets the initial value of bundled SBML species `N_Natural_Killer_Cells`.')}
    _HEADLINE_OUTPUTS = {'chemotherapy_drug': ('M_Chemotherapy_Drug', 'native source value', 'Chemotherapy Drug. Maps to bundled source symbol `M_Chemotherapy_Drug`.'), 'unresolved_tumor_observable_1': ('T_Tumour_Cells', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `T_Tumour_Cells`.'), 'cd8_t_cells': ('L_CD8_T_Cells', 'native source value', 'CD8 T Cells. Maps to bundled source symbol `L_CD8_T_Cells`.'), 'interleukin_2': ('I_IL_2', 'native source value', 'Interleukin 2. Maps to bundled source symbol `I_IL_2`.'), 'natural_killer_cells': ('N_Natural_Killer_Cells', 'native source value', 'Natural Killer Cells. Maps to bundled source symbol `N_Natural_Killer_Cells`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000779.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
