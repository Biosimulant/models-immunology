# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Isaeva2008 - Modelling of Anti-Tumour Immune Response Immunocorrective Effect of Weak Centimetre Electromagnetic Waves."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Isaeva2008ModellingOfAntiTumourImmuneRespoBiomd0000000910Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000910."""

    _SBML_ID = 'BIOMD0000000910'
    _TITLE = 'Isaeva2008 - Modelling of Anti-Tumour Immune Response Immunocorrective Effect of Weak Centimetre Electromagnetic Waves'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['L', 'T', 'I2']
    _SPECIES_LABELS = {'L': 'Unresolved Tumor Observable 1', 'T': 'Unresolved Tumor Observable 2', 'I2': 'Unresolved Tumor Observable 3'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('L', 240000.0, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `L`.'), 'initial_unresolved_tumor_observable_2': ('T', 200000.0, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `T`.'), 'initial_unresolved_tumor_observable_3': ('I2', 36000000.0, 'native source value', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `I2`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('L', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `L`.'), 'unresolved_tumor_observable_2': ('T', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `T`.'), 'unresolved_tumor_observable_3': ('I2', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `I2`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000910.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
