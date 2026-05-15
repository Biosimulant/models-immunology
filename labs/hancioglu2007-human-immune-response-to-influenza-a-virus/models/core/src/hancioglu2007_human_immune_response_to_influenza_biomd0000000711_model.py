# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Hancioglu2007 - Human Immune Response to Influenza A virus Infection."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Hancioglu2007HumanImmuneResponseToInfluenzaBiomd0000000711Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000711."""

    _SBML_ID = 'BIOMD0000000711'
    _TITLE = 'Hancioglu2007 - Human Immune Response to Influenza A virus Infection'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Viral_Load__V', 'Healthy_Epithelial_cells__H', 'Infected_Epithelial_cells__I', 'APC_cells__M', 'Interferons__F', 'Resistant_cells__R', 'Effector_cells__E', 'Plasma_cells__P', 'Antibodies__A', 'Antigenic_compatibility__S', 'Dead_cells__D']
    _SPECIES_LABELS = {'Viral_Load__V': 'Viral Load V', 'Healthy_Epithelial_cells__H': 'Healthy Epithelial Cells H', 'Infected_Epithelial_cells__I': 'Infected Epithelial Cells I', 'APC_cells__M': 'Antigen Presenting Cell Cells M', 'Interferons__F': 'Interferons F', 'Resistant_cells__R': 'Resistant cells (R)', 'Effector_cells__E': 'Effector cells (E)', 'Plasma_cells__P': 'Plasma cells (P)', 'Antibodies__A': 'Antibodies (A)', 'Antigenic_compatibility__S': 'Antigenic compatibility (S)', 'Dead_cells__D': 'Dead cells (D)'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_viral_load_v': ('Viral_Load__V', 0.01, 'native source value', 'Initial Viral Load V. Sets the initial value of bundled SBML species `Viral_Load__V`.'), 'initial_infected_epithelial_cells_i': ('Infected_Epithelial_cells__I', 0.0, 'native source value', 'Initial Infected Epithelial Cells I. Sets the initial value of bundled SBML species `Infected_Epithelial_cells__I`.'), 'initial_healthy_epithelial_cells_h': ('Healthy_Epithelial_cells__H', 1.0, 'native source value', 'Initial Healthy Epithelial Cells H. Sets the initial value of bundled SBML species `Healthy_Epithelial_cells__H`.'), 'initial_antigen_presenting_cell_cells_m': ('APC_cells__M', 0.0, 'native source value', 'Initial Antigen Presenting Cell Cells M. Sets the initial value of bundled SBML species `APC_cells__M`.'), 'initial_interferons_f': ('Interferons__F', 0.0, 'native source value', 'Initial Interferons F. Sets the initial value of bundled SBML species `Interferons__F`.')}
    _HEADLINE_OUTPUTS = {'viral_load_v': ('Viral_Load__V', 'native source value', 'Viral Load V. Maps to bundled source symbol `Viral_Load__V`.'), 'infected_epithelial_cells_i': ('Infected_Epithelial_cells__I', 'native source value', 'Infected Epithelial Cells I. Maps to bundled source symbol `Infected_Epithelial_cells__I`.'), 'healthy_epithelial_cells_h': ('Healthy_Epithelial_cells__H', 'native source value', 'Healthy Epithelial Cells H. Maps to bundled source symbol `Healthy_Epithelial_cells__H`.'), 'antigen_presenting_cell_cells_m': ('APC_cells__M', 'native source value', 'Antigen Presenting Cell Cells M. Maps to bundled source symbol `APC_cells__M`.'), 'interferons_f': ('Interferons__F', 'native source value', 'Interferons F. Maps to bundled source symbol `Interferons__F`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000711.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
