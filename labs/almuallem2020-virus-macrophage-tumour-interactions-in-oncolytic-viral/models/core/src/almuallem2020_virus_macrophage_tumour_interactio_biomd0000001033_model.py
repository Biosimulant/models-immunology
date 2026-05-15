# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Almuallem2020 - Virus-macrophage-tumour interactions in oncolytic viral therapies."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Almuallem2020VirusMacrophageTumourInteractioBiomd0000001033Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000001033."""

    _SBML_ID = 'BIOMD0000001033'
    _TITLE = 'Almuallem2020 - Virus-macrophage-tumour interactions in oncolytic viral therapies'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Uninfected_tumour_cells', 'Infected_tumour_cells', 'M1_macrophages', 'Uninfected_M2_macrophages', 'Infected_M2_macrophages', 'Oncolytic_viruses']
    _SPECIES_LABELS = {'Uninfected_tumour_cells': 'Uninfected Tumour Cells', 'Infected_tumour_cells': 'Infected Tumour Cells', 'M1_macrophages': 'Unresolved Tumor Observable 1', 'Uninfected_M2_macrophages': 'Uninfected M2 Macrophages', 'Infected_M2_macrophages': 'Infected_M2_macrophages', 'Oncolytic_viruses': 'Oncolytic Viruses'}
    _PARAMETER_INPUTS = {'tumour_growth_production_rate': ('r', 0.62, 'native source value', 'Tumour Growth Production Rate. Sets bundled SBML parameter `r`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_infected_tumour_cells': ('Infected_tumour_cells', 0.0, 'native source value', 'Initial Infected Tumour Cells. Sets the initial value of bundled SBML species `Infected_tumour_cells`.'), 'initial_uninfected_tumour_cells': ('Uninfected_tumour_cells', 0.0005, 'native source value', 'Initial Uninfected Tumour Cells. Sets the initial value of bundled SBML species `Uninfected_tumour_cells`.'), 'initial_oncolytic_viruses': ('Oncolytic_viruses', 1e-05, 'native source value', 'Initial Oncolytic Viruses. Sets the initial value of bundled SBML species `Oncolytic_viruses`.'), 'initial_unresolved_tumor_observable_1': ('M1_macrophages', 2.5e-06, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `M1_macrophages`.'), 'initial_uninfected_m2_macrophages': ('Uninfected_M2_macrophages', 2.5e-07, 'native source value', 'Initial Uninfected M2 Macrophages. Sets the initial value of bundled SBML species `Uninfected_M2_macrophages`.')}
    _HEADLINE_OUTPUTS = {'infected_tumour_cells': ('Infected_tumour_cells', 'native source value', 'Infected Tumour Cells. Maps to bundled source symbol `Infected_tumour_cells`.'), 'uninfected_tumour_cells': ('Uninfected_tumour_cells', 'native source value', 'Uninfected Tumour Cells. Maps to bundled source symbol `Uninfected_tumour_cells`.'), 'oncolytic_viruses': ('Oncolytic_viruses', 'native source value', 'Oncolytic Viruses. Maps to bundled source symbol `Oncolytic_viruses`.'), 'unresolved_tumor_observable_1': ('M1_macrophages', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `M1_macrophages`.'), 'uninfected_m2_macrophages': ('Uninfected_M2_macrophages', 'native source value', 'Uninfected M2 Macrophages. Maps to bundled source symbol `Uninfected_M2_macrophages`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001033.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
