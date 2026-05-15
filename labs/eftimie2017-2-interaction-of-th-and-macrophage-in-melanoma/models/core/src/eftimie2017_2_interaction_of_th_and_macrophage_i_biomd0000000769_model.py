# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Eftimie2017/2 - interaction of Th and macrophage in melanoma."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Eftimie20172InteractionOfThAndMacrophageIBiomd0000000769Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000769."""

    _SBML_ID = 'BIOMD0000000769'
    _TITLE = 'Eftimie2017/2 - interaction of Th and macrophage in melanoma'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'H1', 'H2', 'M1', 'M2']
    _SPECIES_LABELS = {'T': 'Unresolved Tumor Observable 1', 'H1': 'Unresolved Tumor Observable 2', 'H2': 'Unresolved Tumor Observable 3', 'M1': 'Unresolved Tumor Observable 4', 'M2': 'Unresolved Tumor Observable 5'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('T', 100000.0, 'substance', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `T`.'), 'initial_unresolved_tumor_observable_2': ('H1', 0.0, 'substance', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `H1`.'), 'initial_unresolved_tumor_observable_3': ('H2', 0.0, 'substance', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `H2`.'), 'initial_unresolved_tumor_observable_4': ('M1', 100.0, 'substance', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `M1`.'), 'initial_unresolved_tumor_observable_5': ('M2', 0.0, 'substance', 'Initial Unresolved Tumor Observable 5. Sets the initial value of bundled SBML species `M2`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('T', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `T`.'), 'unresolved_tumor_observable_2': ('H1', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `H1`.'), 'unresolved_tumor_observable_3': ('H2', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `H2`.'), 'unresolved_tumor_observable_4': ('M1', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `M1`.'), 'unresolved_tumor_observable_5': ('M2', 'native source value', 'Unresolved Tumor Observable 5. Maps to bundled source symbol `M2`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000769.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
