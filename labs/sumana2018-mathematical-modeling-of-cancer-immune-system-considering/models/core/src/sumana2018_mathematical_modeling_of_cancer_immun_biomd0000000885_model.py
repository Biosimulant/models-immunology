# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Sumana2018 - Mathematical modeling of cancer-immune system, considering the role of antibodies.."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Sumana2018MathematicalModelingOfCancerImmunBiomd0000000885Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000885."""

    _SBML_ID = 'BIOMD0000000885'
    _TITLE = 'Sumana2018 - Mathematical modeling of cancer-immune system, considering the role of antibodies.'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['B', 'P', 'A', 'T']
    _SPECIES_LABELS = {'B': 'Unresolved Tumor Observable 1', 'P': 'Unresolved Tumor Observable 2', 'A': 'Unresolved Tumor Observable 3', 'T': 'Unresolved Tumor Observable 4'}
    _PARAMETER_INPUTS = {'production_of_antibody_against_tumor_rate': ('r_1', 100.0, 'native source value', 'Production Of Antibody Against Tumor Rate. Sets bundled SBML parameter `r_1`.'), 'production_of_antibody_against_tumor_rate_2': ('r_2', 1000.0, 'native source value', 'Production Of Antibody Against Tumor Rate 2. Sets bundled SBML parameter `r_2`.'), 'removal_of_antibody_from_the_system_rate': ('mu_2', 6.884, 'native source value', 'Removal Of Antibody From The System Rate. Sets bundled SBML parameter `mu_2`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('B', 90000.0, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `B`.'), 'initial_unresolved_tumor_observable_2': ('P', 1000000.0, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `P`.'), 'initial_unresolved_tumor_observable_3': ('A', 150000000.0, 'native source value', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `A`.'), 'initial_unresolved_tumor_observable_4': ('T', 100000000.0, 'native source value', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `T`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('B', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `B`.'), 'unresolved_tumor_observable_2': ('P', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `P`.'), 'unresolved_tumor_observable_3': ('A', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `A`.'), 'unresolved_tumor_observable_4': ('T', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `T`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000885.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
