# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Owen1998 - Tumour treatment model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Owen1998TumourTreatmentModelBiomd0000000650Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000650."""

    _SBML_ID = 'BIOMD0000000650'
    _TITLE = 'Owen1998 - Tumour treatment model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['l', 'm', 'n']
    _SPECIES_LABELS = {'l': 'Macrophage', 'm': 'Mutated Cell', 'n': 'Normal Cell'}
    _PARAMETER_INPUTS = {'treatment_start_parameter': ('treatment_start', 10.0, 'native source value', 'Treatment Start Parameter. Sets bundled SBML parameter `treatment_start`.'), 'treatment_end_parameter': ('treatment_end', 400.0, 'native source value', 'Treatment End Parameter. Sets bundled SBML parameter `treatment_end`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'macrophage': ('l', 'native source value', 'Macrophage. Maps to bundled source symbol `l`.'), 'mutated_cell': ('m', 'native source value', 'Mutated Cell. Maps to bundled source symbol `m`.'), 'normal_cell': ('n', 'native source value', 'Normal Cell. Maps to bundled source symbol `n`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000650.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
