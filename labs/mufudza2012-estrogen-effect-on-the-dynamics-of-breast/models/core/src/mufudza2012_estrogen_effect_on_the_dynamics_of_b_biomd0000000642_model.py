# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Mufudza2012 - Estrogen effect on the dynamics of breast cancer."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Mufudza2012EstrogenEffectOnTheDynamicsOfBBiomd0000000642Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000642."""

    _SBML_ID = 'BIOMD0000000642'
    _TITLE = 'Mufudza2012 - Estrogen effect on the dynamics of breast cancer'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['H', 'T', 'I', 'E']
    _SPECIES_LABELS = {'H': 'Normal Cells', 'T': 'Tumour Cells', 'I': 'Immune Cells', 'E': 'Estrogen'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'tumour_cells': ('T', 'native source value', 'Tumour Cells. Maps to bundled source symbol `T`.'), 'immune_cells': ('I', 'native source value', 'Immune Cells. Maps to bundled source symbol `I`.'), 'normal_cells': ('H', 'native source value', 'Normal Cells. Maps to bundled source symbol `H`.'), 'estrogen': ('E', 'native source value', 'Estrogen. Maps to bundled source symbol `E`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000642.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
