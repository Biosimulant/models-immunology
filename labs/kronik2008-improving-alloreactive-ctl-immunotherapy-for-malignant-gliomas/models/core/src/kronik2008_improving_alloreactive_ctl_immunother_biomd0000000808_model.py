# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Kronik2008 - Improving alloreactive CTL immunotherapy for malignant gliomas using a simulation model of their interactive dynamics."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kronik2008ImprovingAlloreactiveCtlImmunotherBiomd0000000808Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000808."""

    _SBML_ID = 'BIOMD0000000808'
    _TITLE = 'Kronik2008 - Improving alloreactive CTL immunotherapy for malignant gliomas using a simulation model of their interactive dynamics'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'C', 'F_beta', 'F_gamma', 'M1', 'M2']
    _SPECIES_LABELS = {'T': 'Unresolved Tumor Observable 1', 'C': 'Unresolved Tumor Observable 2', 'F_beta': 'Unresolved Tumor Observable 3', 'F_gamma': 'Unresolved Tumor Observable 4', 'M1': 'Unresolved Tumor Observable 5', 'M2': 'M2', 'ModelValue_28': 'Initial for S_dose', 'ModelValue_30': 'Initial for S_interval'}
    _PARAMETER_INPUTS = {'tumor_growth_rate': ('r', 0.00035, 'native source value', 'Tumor Growth Rate. Sets bundled SBML parameter `r`.'), 's_dose': ('S_dose', 300000000.0, 'native source value', 'S Dose. Sets bundled SBML parameter `S_dose`.'), 's_dose_initial_parameter': ('ModelValue_28', 300000000.0, 'native source value', 'S Dose Initial Parameter. Sets bundled SBML parameter `ModelValue_28`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('T', 10000000000.0, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `T`.'), 'initial_unresolved_tumor_observable_2': ('C', 2000000.0, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `C`.'), 'initial_unresolved_tumor_observable_3': ('F_beta', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `F_beta`.'), 'initial_unresolved_tumor_observable_4': ('F_gamma', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `F_gamma`.'), 'initial_unresolved_tumor_observable_5': ('M1', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 5. Sets the initial value of bundled SBML species `M1`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('T', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `T`.'), 'unresolved_tumor_observable_2': ('C', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `C`.'), 'unresolved_tumor_observable_3': ('F_beta', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `F_beta`.'), 'unresolved_tumor_observable_4': ('F_gamma', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `F_gamma`.'), 'unresolved_tumor_observable_5': ('M1', 'native source value', 'Unresolved Tumor Observable 5. Maps to bundled source symbol `M1`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000808.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
