# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Nanda2013 - B cell chronic lymphocytic leukemia A model with immune response."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Nanda2013BCellChronicLymphocyticLeukemiaAModel2001090002Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL2001090002."""

    _SBML_ID = 'MODEL2001090002'
    _TITLE = 'Nanda2013 - B cell chronic lymphocytic leukemia A model with immune response'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['B', 'N', 'T', 'TH', 'H']
    _SPECIES_LABELS = {'B': 'Unresolved Tumor Observable 1', 'N': 'Unresolved Tumor Observable 2', 'T': 'Unresolved Tumor Observable 3', 'TH': 'Unresolved Tumor Observable 4', 'H': 'Unresolved Tumor Observable 5', 'ModelValue_5_0': 'Initial for fw', 'ModelValue_6_0': 'Initial for h5', 'ModelValue_7_0': 'Initial for h84'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('B', 34.0, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `B`.'), 'initial_unresolved_tumor_observable_2': ('N', 504.0, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `N`.'), 'initial_unresolved_tumor_observable_3': ('T', 2.0, 'native source value', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `T`.'), 'initial_unresolved_tumor_observable_4': ('TH', 1.0, 'native source value', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `TH`.'), 'initial_unresolved_tumor_observable_5': ('H', 1.0, 'native source value', 'Initial Unresolved Tumor Observable 5. Sets the initial value of bundled SBML species `H`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('B', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `B`.'), 'unresolved_tumor_observable_2': ('N', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `N`.'), 'unresolved_tumor_observable_3': ('T', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `T`.'), 'unresolved_tumor_observable_4': ('TH', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `TH`.'), 'unresolved_tumor_observable_5': ('H', 'native source value', 'Unresolved Tumor Observable 5. Maps to bundled source symbol `H`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2001090002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
