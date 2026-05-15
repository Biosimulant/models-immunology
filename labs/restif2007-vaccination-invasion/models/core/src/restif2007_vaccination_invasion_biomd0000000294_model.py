# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Restif2007 - Vaccination invasion."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Restif2007VaccinationInvasionBiomd0000000294Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000294."""

    _SBML_ID = 'BIOMD0000000294'
    _TITLE = 'Restif2007 - Vaccination invasion'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['N', 'S', 'I1', 'I2', 'R1', 'R2', 'V', 'Iv2', 'J2', 'J1', 'R']
    _SPECIES_LABELS = {'N': 'Unresolved Immune Observable 1', 'S': 'Unresolved Immune Observable 2', 'I1': 'Unresolved Immune Observable 3', 'I2': 'Unresolved Immune Observable 4', 'R1': 'Unresolved Immune Observable 5', 'R2': 'R2', 'V': 'V', 'Iv2': 'Iv2', 'J2': 'J2', 'J1': 'J1', 'R': 'R', 'l_e': 'life expectancy', 'tInf': 'infectious period (d)', 'tImm': 'immune period (yr)', 'tImm_V': 'vaccine immune period (yr)'}
    _PARAMETER_INPUTS = {'vaccine_immune_period_yr_parameter': ('tImm_V', 50.0, 'time', 'Vaccine Immune Period Yr Parameter. Sets bundled SBML parameter `tImm_V`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_immune_observable_1': ('N', 1.0, 'native source value', 'Initial Unresolved Immune Observable 1. Sets the initial value of bundled SBML species `N`.'), 'initial_unresolved_immune_observable_2': ('S', 0.0588235, 'native source value', 'Initial Unresolved Immune Observable 2. Sets the initial value of bundled SBML species `S`.'), 'initial_unresolved_immune_observable_3': ('I1', 0.00176967, 'native source value', 'Initial Unresolved Immune Observable 3. Sets the initial value of bundled SBML species `I1`.'), 'initial_unresolved_immune_observable_4': ('I2', 1e-06, 'native source value', 'Initial Unresolved Immune Observable 4. Sets the initial value of bundled SBML species `I2`.'), 'initial_unresolved_immune_observable_5': ('R1', 0.439407, 'native source value', 'Initial Unresolved Immune Observable 5. Sets the initial value of bundled SBML species `R1`.')}
    _HEADLINE_OUTPUTS = {'unresolved_immune_observable_1': ('N', 'native source value', 'Unresolved Immune Observable 1. Maps to bundled source symbol `N`.'), 'unresolved_immune_observable_2': ('S', 'native source value', 'Unresolved Immune Observable 2. Maps to bundled source symbol `S`.'), 'unresolved_immune_observable_3': ('I1', 'native source value', 'Unresolved Immune Observable 3. Maps to bundled source symbol `I1`.'), 'unresolved_immune_observable_4': ('I2', 'native source value', 'Unresolved Immune Observable 4. Maps to bundled source symbol `I2`.'), 'unresolved_immune_observable_5': ('R1', 'native source value', 'Unresolved Immune Observable 5. Maps to bundled source symbol `R1`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000294.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
