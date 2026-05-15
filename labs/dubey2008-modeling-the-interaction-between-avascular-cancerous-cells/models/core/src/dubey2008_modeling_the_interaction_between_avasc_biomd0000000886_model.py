# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Dubey2008 - Modeling the interaction between avascular cancerous cells and acquired immune response."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Dubey2008ModelingTheInteractionBetweenAvascBiomd0000000886Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000886."""

    _SBML_ID = 'BIOMD0000000886'
    _TITLE = 'Dubey2008 - Modeling the interaction between avascular cancerous cells and acquired immune response'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'Th', 'Tc', 'B', 'A']
    _SPECIES_LABELS = {'T': 'Unresolved Tumor Observable 1', 'Th': 'Unresolved Tumor Observable 2', 'Tc': 'Unresolved Tumor Observable 3', 'B': 'Unresolved Tumor Observable 4', 'A': 'Unresolved Tumor Observable 5'}
    _PARAMETER_INPUTS = {'introduction_of_antibody_against_cancer_rate': ('mu_4', 0.35, 'native source value', 'Introduction Of Antibody Against Cancer Rate. Sets bundled SBML parameter `mu_4`.'), 'removal_of_antibody_from_the_system_rate': ('mu_40', 0.3, 'native source value', 'Removal Of Antibody From The System Rate. Sets bundled SBML parameter `mu_40`.'), 'removal_of_antibody_from_the_system_rate_2': ('delta_1', 0.5, 'native source value', 'Removal Of Antibody From The System Rate 2. Sets bundled SBML parameter `delta_1`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('T', 9.0, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `T`.'), 'initial_unresolved_tumor_observable_2': ('Th', 7.0, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `Th`.'), 'initial_unresolved_tumor_observable_3': ('Tc', 1.0, 'native source value', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `Tc`.'), 'initial_unresolved_tumor_observable_4': ('B', 1.0, 'native source value', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `B`.'), 'initial_unresolved_tumor_observable_5': ('A', 1.0, 'native source value', 'Initial Unresolved Tumor Observable 5. Sets the initial value of bundled SBML species `A`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('T', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `T`.'), 'unresolved_tumor_observable_2': ('Th', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `Th`.'), 'unresolved_tumor_observable_3': ('Tc', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `Tc`.'), 'unresolved_tumor_observable_4': ('B', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `B`.'), 'unresolved_tumor_observable_5': ('A', 'native source value', 'Unresolved Tumor Observable 5. Maps to bundled source symbol `A`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000886.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
