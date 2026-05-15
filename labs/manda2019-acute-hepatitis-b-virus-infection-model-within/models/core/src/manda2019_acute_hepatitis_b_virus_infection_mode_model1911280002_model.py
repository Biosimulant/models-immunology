# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Manda2019 - Acute hepatitis B virus infection model within the host incorporating immune cells and cytokine response."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Manda2019AcuteHepatitisBVirusInfectionModeModel1911280002Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL1911280002."""

    _SBML_ID = 'MODEL1911280002'
    _TITLE = 'Manda2019 - Acute hepatitis B virus infection model within the host incorporating immune cells and cytokine response'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['H', 'I_H', 'T_c', 'T_1', 'T_2', 'I_gamma', 'I_2', 'I_12', 'I_4', 'I_10', 'H_B']
    _SPECIES_LABELS = {'H': 'Unresolved Infection Observable 1', 'I_H': 'Unresolved Infection Observable 2', 'T_c': 'Unresolved Infection Observable 3', 'T_1': 'Unresolved Infection Observable 4', 'T_2': 'Unresolved Infection Observable 5', 'I_gamma': 'I_gamma', 'I_2': 'I_2', 'I_12': 'I_12', 'I_4': 'I_4', 'I_10': 'I_10', 'H_B': 'H_B'}
    _PARAMETER_INPUTS = {'hepatocyte_growth_rate': ('r', 0.00145, 'native source value', 'Hepatocyte Growth Rate. Sets bundled SBML parameter `r`.'), 'hepatocyte_infection_rate': ('beta', 9.9e-10, 'native source value', 'Hepatocyte Infection Rate. Sets bundled SBML parameter `beta`.'), 'infected_hepatocytes_death_rate': ('mu', 0.4, 'native source value', 'Infected Hepatocytes Death Rate. Sets bundled SBML parameter `mu`.'), 'th1_death_rate': ('mu_1', 0.5, 'native source value', 'Th1 Death Rate. Sets bundled SBML parameter `mu_1`.'), 'th2_death_rate': ('mu_2', 0.5, 'native source value', 'Th2 Death Rate. Sets bundled SBML parameter `mu_2`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_infection_observable_1': ('H', 9600000.0, 'native source value', 'Initial Unresolved Infection Observable 1. Sets the initial value of bundled SBML species `H`.'), 'initial_unresolved_infection_observable_2': ('I_H', 0.0, 'native source value', 'Initial Unresolved Infection Observable 2. Sets the initial value of bundled SBML species `I_H`.'), 'initial_unresolved_infection_observable_3': ('T_c', 1000.0, 'native source value', 'Initial Unresolved Infection Observable 3. Sets the initial value of bundled SBML species `T_c`.'), 'initial_unresolved_infection_observable_4': ('T_1', 1000.0, 'native source value', 'Initial Unresolved Infection Observable 4. Sets the initial value of bundled SBML species `T_1`.'), 'initial_unresolved_infection_observable_5': ('T_2', 1000.0, 'native source value', 'Initial Unresolved Infection Observable 5. Sets the initial value of bundled SBML species `T_2`.')}
    _HEADLINE_OUTPUTS = {'unresolved_infection_observable_1': ('H', 'native source value', 'Unresolved Infection Observable 1. Maps to bundled source symbol `H`.'), 'unresolved_infection_observable_2': ('I_H', 'native source value', 'Unresolved Infection Observable 2. Maps to bundled source symbol `I_H`.'), 'unresolved_infection_observable_3': ('T_c', 'native source value', 'Unresolved Infection Observable 3. Maps to bundled source symbol `T_c`.'), 'unresolved_infection_observable_4': ('T_1', 'native source value', 'Unresolved Infection Observable 4. Maps to bundled source symbol `T_1`.'), 'unresolved_infection_observable_5': ('T_2', 'native source value', 'Unresolved Infection Observable 5. Maps to bundled source symbol `T_2`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1911280002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
