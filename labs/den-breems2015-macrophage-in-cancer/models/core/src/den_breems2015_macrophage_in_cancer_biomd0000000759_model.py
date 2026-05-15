# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for den Breems2015 - macrophage in cancer."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class DenBreems2015MacrophageInCancerBiomd0000000759Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000759."""

    _SBML_ID = 'BIOMD0000000759'
    _TITLE = 'den Breems2015 - macrophage in cancer'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Tn', 'Ts', 'M1', 'M2', 'Th1', 'Th2']
    _SPECIES_LABELS = {'Tn': 'Unresolved Tumor Observable 1', 'Ts': 'Unresolved Tumor Observable 2', 'M1': 'Unresolved Tumor Observable 3', 'M2': 'Unresolved Tumor Observable 4', 'Th1': 'Unresolved Tumor Observable 5', 'Th2': 'Th2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('Tn', 1000.0, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `Tn`.'), 'initial_unresolved_tumor_observable_2': ('Ts', 1000000.0, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `Ts`.'), 'initial_unresolved_tumor_observable_3': ('M1', 100.0, 'native source value', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `M1`.'), 'initial_unresolved_tumor_observable_4': ('M2', 100.0, 'native source value', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `M2`.'), 'initial_unresolved_tumor_observable_5': ('Th1', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 5. Sets the initial value of bundled SBML species `Th1`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('Tn', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `Tn`.'), 'unresolved_tumor_observable_2': ('Ts', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `Ts`.'), 'unresolved_tumor_observable_3': ('M1', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `M1`.'), 'unresolved_tumor_observable_4': ('M2', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `M2`.'), 'unresolved_tumor_observable_5': ('Th1', 'native source value', 'Unresolved Tumor Observable 5. Maps to bundled source symbol `Th1`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000759.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
