# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Aavani2019 - The role of CD4 T cells in immune system activation and viral reproduction in a simple model for HIV infection."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Aavani2019TheRoleOfCd4TCellsInImmuneSysBiomd0000000876Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000876."""

    _SBML_ID = 'BIOMD0000000876'
    _TITLE = 'Aavani2019 - The role of CD4 T cells in immune system activation and viral reproduction in a simple model for HIV infection'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['C_Uninfected_CD4', 'I_Infected_CD4', 'F_CTL', 'V_Virus']
    _SPECIES_LABELS = {'C_Uninfected_CD4': 'Uninfected CD4 T Cells', 'I_Infected_CD4': 'Infected CD4 T Cells', 'F_CTL': 'Cytotoxic T Lymphocytes', 'V_Virus': 'Virus'}
    _PARAMETER_INPUTS = {'cd4_uninfected_infection_rate': ('beta', 5.75e-05, 'native source value', 'CD4 Uninfected Infection Rate. Sets bundled SBML parameter `beta`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_uninfected_cd4_t_cells': ('C_Uninfected_CD4', 1000.0, 'native source value', 'Initial Uninfected CD4 T Cells. Sets the initial value of bundled SBML species `C_Uninfected_CD4`.'), 'initial_infected_cd4_t_cells': ('I_Infected_CD4', 1.0, 'native source value', 'Initial Infected CD4 T Cells. Sets the initial value of bundled SBML species `I_Infected_CD4`.'), 'initial_virus': ('V_Virus', 200.0, 'native source value', 'Initial Virus. Sets the initial value of bundled SBML species `V_Virus`.'), 'initial_cytotoxic_t_lymphocytes': ('F_CTL', 1.0, 'native source value', 'Initial Cytotoxic T Lymphocytes. Sets the initial value of bundled SBML species `F_CTL`.')}
    _HEADLINE_OUTPUTS = {'uninfected_cd4_t_cells': ('C_Uninfected_CD4', 'native source value', 'Uninfected CD4 T Cells. Maps to bundled source symbol `C_Uninfected_CD4`.'), 'infected_cd4_t_cells': ('I_Infected_CD4', 'native source value', 'Infected CD4 T Cells. Maps to bundled source symbol `I_Infected_CD4`.'), 'virus': ('V_Virus', 'native source value', 'Virus. Maps to bundled source symbol `V_Virus`.'), 'cytotoxic_t_lymphocytes': ('F_CTL', 'native source value', 'Cytotoxic T Lymphocytes. Maps to bundled source symbol `F_CTL`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000876.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
