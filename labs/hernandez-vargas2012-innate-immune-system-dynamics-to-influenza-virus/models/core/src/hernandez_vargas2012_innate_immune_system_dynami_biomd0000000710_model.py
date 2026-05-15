# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Hernandez-Vargas2012 - Innate immune system dynamics to Influenza virus."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class HernandezVargas2012InnateImmuneSystemDynamiBiomd0000000710Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000710."""

    _SBML_ID = 'BIOMD0000000710'
    _TITLE = 'Hernandez-Vargas2012 - Innate immune system dynamics to Influenza virus'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['U_H', 'U_E', 'U_I', 'U_R', 'V', 'IFN', 'K']
    _SPECIES_LABELS = {'U_H': 'Healthy Epithelial Cells U H', 'U_E': 'Partially Infected Epithelial Cells U E', 'U_I': 'Infected Epithelial Cells U I', 'U_R': 'Resistant Epithelial cells (U_R)', 'V': 'Viral Load V', 'IFN': 'Interferon Interferon', 'K': 'Natural Killers (K)', 'Metabolite_0_0': 'Initial for Healthy Epithelial cells (U_H)', 'Metabolite_6_0': 'Initial for Natural Killers (K)'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_partially_infected_epithelial_cells_u_e': ('U_E', 0.0, 'native source value', 'Initial Partially Infected Epithelial Cells U E. Sets the initial value of bundled SBML species `U_E`.'), 'initial_infected_epithelial_cells_u_i': ('U_I', 0.0, 'native source value', 'Initial Infected Epithelial Cells U I. Sets the initial value of bundled SBML species `U_I`.'), 'initial_viral_load_v': ('V', 0.001, 'native source value', 'Initial Viral Load V. Sets the initial value of bundled SBML species `V`.'), 'initial_interferon_interferon': ('IFN', 0.0, 'native source value', 'Initial Interferon Interferon. Sets the initial value of bundled SBML species `IFN`.'), 'initial_healthy_epithelial_cells_u_h': ('U_H', 500000000.0, 'native source value', 'Initial Healthy Epithelial Cells U H. Sets the initial value of bundled SBML species `U_H`.')}
    _HEADLINE_OUTPUTS = {'partially_infected_epithelial_cells_u_e': ('U_E', 'native source value', 'Partially Infected Epithelial Cells U E. Maps to bundled source symbol `U_E`.'), 'infected_epithelial_cells_u_i': ('U_I', 'native source value', 'Infected Epithelial Cells U I. Maps to bundled source symbol `U_I`.'), 'viral_load_v': ('V', 'native source value', 'Viral Load V. Maps to bundled source symbol `V`.'), 'interferon_interferon': ('IFN', 'native source value', 'Interferon Interferon. Maps to bundled source symbol `IFN`.'), 'healthy_epithelial_cells_u_h': ('U_H', 'native source value', 'Healthy Epithelial Cells U H. Maps to bundled source symbol `U_H`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000710.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
