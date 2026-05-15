# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Adrianne2018 - Modelling combined virotherapy and immunotherapy: strengthening the antitumour immune response mediated by IL-12 and GM-CSF expression."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Adrianne2018ModellingCombinedVirotherapyAndModel1912120003Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL1912120003."""

    _SBML_ID = 'MODEL1912120003'
    _TITLE = 'Adrianne2018 - Modelling combined virotherapy and immunotherapy: strengthening the antitumour immune response mediated by IL-12 and GM-CSF expression'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['U', 'I', 'V', 'A', 'H', 'K', 'uv', 'species']
    _SPECIES_LABELS = {'U': 'Unresolved Tumor Observable 1', 'I': 'Unresolved Tumor Observable 2', 'V': 'Unresolved Tumor Observable 3', 'A': 'Unresolved Tumor Observable 4', 'H': 'Unresolved Tumor Observable 5', 'K': 'K', 'uv': 'uv', 'species': 'species'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('U', 85.0, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `U`.'), 'initial_unresolved_tumor_observable_2': ('I', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `I`.'), 'initial_unresolved_tumor_observable_3': ('V', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `V`.'), 'initial_unresolved_tumor_observable_4': ('A', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `A`.'), 'initial_unresolved_tumor_observable_5': ('H', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 5. Sets the initial value of bundled SBML species `H`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('U', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `U`.'), 'unresolved_tumor_observable_2': ('I', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `I`.'), 'unresolved_tumor_observable_3': ('V', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `V`.'), 'unresolved_tumor_observable_4': ('A', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `A`.'), 'unresolved_tumor_observable_5': ('H', 'native source value', 'Unresolved Tumor Observable 5. Maps to bundled source symbol `H`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1912120003.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
