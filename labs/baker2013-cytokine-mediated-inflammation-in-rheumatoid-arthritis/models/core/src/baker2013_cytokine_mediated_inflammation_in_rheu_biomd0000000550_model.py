# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Baker2013 - Cytokine Mediated Inflammation in Rheumatoid Arthritis."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Baker2013CytokineMediatedInflammationInRheuBiomd0000000550Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000550."""

    _SBML_ID = 'BIOMD0000000550'
    _TITLE = 'Baker2013 - Cytokine Mediated Inflammation in Rheumatoid Arthritis'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['species_1', 'species_2']
    _SPECIES_LABELS = {'species_1': 'Unresolved Signaling Observable 1', 'species_2': 'Unresolved Source Observable 2', 'parameter_1': 'alpha1', 'parameter_2': 'alpha2', 'parameter_3': 'alpha3', 'parameter_4': 'alpha4', 'parameter_5': 'gamma'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'unresolved_signaling_observable_1': ('species_1', 'native source value', 'Unresolved Signaling Observable 1. Maps to bundled source symbol `species_1`.'), 'unresolved_source_observable_2': ('species_2', 'native source value', 'Unresolved Source Observable 2. Maps to bundled source symbol `species_2`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000550.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
