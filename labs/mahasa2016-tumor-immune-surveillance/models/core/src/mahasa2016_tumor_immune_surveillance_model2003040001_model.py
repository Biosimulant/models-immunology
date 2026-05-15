# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Mahasa2016-tumor–immune surveillance."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Mahasa2016TumorImmuneSurveillanceModel2003040001Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL2003040001."""

    _SBML_ID = 'MODEL2003040001'
    _TITLE = 'Mahasa2016-tumor–immune surveillance'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['N', 'L', 'T0', 'TN1', 'TL1', 'TNL1']
    _SPECIES_LABELS = {'N': 'Unresolved Tumor Observable 1', 'L': 'Unresolved Tumor Observable 2', 'T0': 'Unresolved Tumor Observable 3', 'TN1': 'Unresolved Tumor Observable 4', 'TL1': 'Unresolved Tumor Observable 5', 'TNL1': 'TNL1', 'alphaN': 'alphaN+', 'alphaN_0': 'alphaN-', 'betaL': 'betaL+', 'betaL_0': 'betaL-', 'alphaL': 'alphaL+', 'alphaL_0': 'alphaL-', 'betaN': 'betaN+', 'betaN_0': 'betaN-'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('N', 100000.0, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `N`.'), 'initial_unresolved_tumor_observable_2': ('L', 100.0, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `L`.'), 'initial_unresolved_tumor_observable_3': ('T0', 10000.0, 'native source value', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `T0`.'), 'initial_unresolved_tumor_observable_4': ('TN1', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `TN1`.'), 'initial_unresolved_tumor_observable_5': ('TL1', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 5. Sets the initial value of bundled SBML species `TL1`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('N', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `N`.'), 'unresolved_tumor_observable_2': ('L', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `L`.'), 'unresolved_tumor_observable_3': ('T0', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `T0`.'), 'unresolved_tumor_observable_4': ('TN1', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `TN1`.'), 'unresolved_tumor_observable_5': ('TL1', 'native source value', 'Unresolved Tumor Observable 5. Maps to bundled source symbol `TL1`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2003040001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
