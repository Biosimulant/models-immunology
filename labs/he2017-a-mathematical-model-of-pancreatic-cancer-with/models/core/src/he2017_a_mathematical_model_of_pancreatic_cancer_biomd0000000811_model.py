# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for He2017 - A mathematical model of pancreatic cancer with two kinds of treatments."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class He2017AMathematicalModelOfPancreaticCancerBiomd0000000811Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000811."""

    _SBML_ID = 'BIOMD0000000811'
    _TITLE = 'He2017 - A mathematical model of pancreatic cancer with two kinds of treatments'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['C_PCC', 'P_PSC', 'E_CD8', 'N_Killer', 'H_T_Helper', 'R_T_Regulatory']
    _SPECIES_LABELS = {'C_PCC': 'Unresolved Tumor Observable 1', 'P_PSC': 'Unresolved Tumor Observable 2', 'E_CD8': 'CD8', 'N_Killer': 'Killer', 'H_T_Helper': 'T Helper', 'R_T_Regulatory': 'R_T_Regulatory', 'ModelValue_2': 'Initial for a_c', 'ModelValue_8': 'Initial for a_p', 'ModelValue_0': 'Initial for k_c'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('C_PCC', 1000000000.0, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `C_PCC`.'), 'initial_unresolved_tumor_observable_2': ('P_PSC', 5600000.0, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `P_PSC`.'), 'initial_cd8': ('E_CD8', 873600000.0, 'native source value', 'Initial CD8. Sets the initial value of bundled SBML species `E_CD8`.'), 'initial_killer': ('N_Killer', 481600000.0, 'native source value', 'Initial Killer. Sets the initial value of bundled SBML species `N_Killer`.'), 'initial_t_helper': ('H_T_Helper', 2116800000.0, 'native source value', 'Initial T Helper. Sets the initial value of bundled SBML species `H_T_Helper`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('C_PCC', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `C_PCC`.'), 'unresolved_tumor_observable_2': ('P_PSC', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `P_PSC`.'), 'cd8': ('E_CD8', 'native source value', 'CD8. Maps to bundled source symbol `E_CD8`.'), 'killer': ('N_Killer', 'native source value', 'Killer. Maps to bundled source symbol `N_Killer`.'), 't_helper': ('H_T_Helper', 'native source value', 'T Helper. Maps to bundled source symbol `H_T_Helper`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000811.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
