# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for FatehiChenar2018 - Mathematical model of immune response to hepatitis B."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Fatehichenar2018MathematicalModelOfImmuneReBiomd0000000848Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000848."""

    _SBML_ID = 'BIOMD0000000848'
    _TITLE = 'FatehiChenar2018 - Mathematical model of immune response to hepatitis B'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'I', 'F_1', 'F_2', 'N', 'E', 'R', 'V', 'A']
    _SPECIES_LABELS = {'T': 'Unresolved Infection Observable 1', 'I': 'Unresolved Infection Observable 2', 'F_1': 'Unresolved Infection Observable 3', 'F_2': 'Unresolved Infection Observable 4', 'N': 'Unresolved Infection Observable 5', 'E': 'E', 'R': 'R', 'V': 'V', 'A': 'A'}
    _PARAMETER_INPUTS = {'uninfected_death_rate': ('d', 0.003, 'native source value', 'Uninfected Death Rate. Sets bundled SBML parameter `d`.'), 'uninfected_infection_rate': ('beta', 7.0, 'native source value', 'Uninfected Infection Rate. Sets bundled SBML parameter `beta`.'), 'infected_death_rate': ('delta', 0.56, 'native source value', 'Infected Death Rate. Sets bundled SBML parameter `delta`.'), 'infected_killing_immune_rate': ('mu_1', 5.0, 'native source value', 'Infected Killing Immune Rate. Sets bundled SBML parameter `mu_1`.'), 'infected_killing_immune_rate_2': ('mu_2', 0.14, 'native source value', 'Infected Killing Immune Rate 2. Sets bundled SBML parameter `mu_2`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_infection_observable_1': ('T', 0.9, 'native source value', 'Initial Unresolved Infection Observable 1. Sets the initial value of bundled SBML species `T`.'), 'initial_unresolved_infection_observable_2': ('I', 0.0, 'native source value', 'Initial Unresolved Infection Observable 2. Sets the initial value of bundled SBML species `I`.'), 'initial_unresolved_infection_observable_3': ('F_1', 0.0, 'native source value', 'Initial Unresolved Infection Observable 3. Sets the initial value of bundled SBML species `F_1`.'), 'initial_unresolved_infection_observable_4': ('F_2', 0.0, 'native source value', 'Initial Unresolved Infection Observable 4. Sets the initial value of bundled SBML species `F_2`.'), 'initial_unresolved_infection_observable_5': ('N', 0.1, 'native source value', 'Initial Unresolved Infection Observable 5. Sets the initial value of bundled SBML species `N`.')}
    _HEADLINE_OUTPUTS = {'unresolved_infection_observable_1': ('T', 'native source value', 'Unresolved Infection Observable 1. Maps to bundled source symbol `T`.'), 'unresolved_infection_observable_2': ('I', 'native source value', 'Unresolved Infection Observable 2. Maps to bundled source symbol `I`.'), 'unresolved_infection_observable_3': ('F_1', 'native source value', 'Unresolved Infection Observable 3. Maps to bundled source symbol `F_1`.'), 'unresolved_infection_observable_4': ('F_2', 'native source value', 'Unresolved Infection Observable 4. Maps to bundled source symbol `F_2`.'), 'unresolved_infection_observable_5': ('N', 'native source value', 'Unresolved Infection Observable 5. Maps to bundled source symbol `N`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000848.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
