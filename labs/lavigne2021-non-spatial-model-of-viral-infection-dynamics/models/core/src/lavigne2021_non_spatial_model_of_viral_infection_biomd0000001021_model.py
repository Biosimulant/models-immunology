# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Lavigne2021 - Non-spatial model of viral infection dynamics and interferon response of well-mixed viral infection."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Lavigne2021NonSpatialModelOfViralInfectionBiomd0000001021Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000001021."""

    _SBML_ID = 'BIOMD0000001021'
    _TITLE = 'Lavigne2021 - Non-spatial model of viral infection dynamics and interferon response of well-mixed viral infection'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Target_cells', 'Infected_cells', 'Infected_cells_antiviral', 'Refractory_cells', 'Virions', 'IFN', 'Fraction_target_cells_remaining']
    _SPECIES_LABELS = {'Target_cells': 'Target Cells', 'Infected_cells': 'Infected Cells', 'Infected_cells_antiviral': 'Infected Cells Antiviral', 'Refractory_cells': 'Refractory Cells', 'Virions': 'Virions', 'IFN': 'Interferon', 'Fraction_target_cells_remaining': 'Fraction_target_cells_remaining', 'Metabolite_0': 'Initial for Target_cells'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_infected_cells_antiviral': ('Infected_cells_antiviral', 0.0, 'native source value', 'Initial Infected Cells Antiviral. Sets the initial value of bundled SBML species `Infected_cells_antiviral`.'), 'initial_infected_cells': ('Infected_cells', 0.0, 'native source value', 'Initial Infected Cells. Sets the initial value of bundled SBML species `Infected_cells`.'), 'initial_interferon': ('IFN', 0.0, 'native source value', 'Initial Interferon. Sets the initial value of bundled SBML species `IFN`.'), 'initial_target_cells': ('Target_cells', 400000000.0, 'native source value', 'Initial Target Cells. Sets the initial value of bundled SBML species `Target_cells`.'), 'initial_refractory_cells': ('Refractory_cells', 0.0, 'native source value', 'Initial Refractory Cells. Sets the initial value of bundled SBML species `Refractory_cells`.')}
    _HEADLINE_OUTPUTS = {'infected_cells_antiviral': ('Infected_cells_antiviral', 'native source value', 'Infected Cells Antiviral. Maps to bundled source symbol `Infected_cells_antiviral`.'), 'infected_cells': ('Infected_cells', 'native source value', 'Infected Cells. Maps to bundled source symbol `Infected_cells`.'), 'interferon': ('IFN', 'native source value', 'Interferon. Maps to bundled source symbol `IFN`.'), 'target_cells': ('Target_cells', 'native source value', 'Target Cells. Maps to bundled source symbol `Target_cells`.'), 'refractory_cells': ('Refractory_cells', 'native source value', 'Refractory Cells. Maps to bundled source symbol `Refractory_cells`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001021.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
