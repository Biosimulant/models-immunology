# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Admon2017 - Modelling tumor growth with immune response and drug using ordinary differential equations."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Admon2017ModellingTumorGrowthWithImmuneResBiomd0000000904Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000904."""

    _SBML_ID = 'BIOMD0000000904'
    _TITLE = 'Admon2017 - Modelling tumor growth with immune response and drug using ordinary differential equations'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Ti', 'Tm', 'I', 'u']
    _SPECIES_LABELS = {'Ti': 'Unresolved Tumor Observable 1', 'Tm': 'Unresolved Tumor Observable 2', 'I': 'Unresolved Tumor Observable 3', 'u': 'Unresolved Tumor Observable 4'}
    _PARAMETER_INPUTS = {'decrease_in_drug_rate': ('gamma', 0.0, 'native source value', 'Decrease In Drug Rate. Sets bundled SBML parameter `gamma`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('Ti', 1.3, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `Ti`.'), 'initial_unresolved_tumor_observable_2': ('Tm', 1.2, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `Tm`.'), 'initial_unresolved_tumor_observable_3': ('I', 0.9, 'native source value', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `I`.'), 'initial_unresolved_tumor_observable_4': ('u', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `u`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('Ti', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `Ti`.'), 'unresolved_tumor_observable_2': ('Tm', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `Tm`.'), 'unresolved_tumor_observable_3': ('I', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `I`.'), 'unresolved_tumor_observable_4': ('u', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `u`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000904.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
