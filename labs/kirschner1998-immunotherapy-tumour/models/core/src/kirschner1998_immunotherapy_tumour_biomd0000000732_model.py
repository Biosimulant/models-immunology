# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Kirschner1998_Immunotherapy_Tumour."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kirschner1998ImmunotherapyTumourBiomd0000000732Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000732."""

    _SBML_ID = 'BIOMD0000000732'
    _TITLE = 'Kirschner1998_Immunotherapy_Tumour'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Source', 'Tumor', 'Sink', 'IL2', 'Immune_cells']
    _SPECIES_LABELS = {'Source': 'Source', 'Tumor': 'Tumor', 'Sink': 'Sink', 'IL2': 'Interleukin 2', 'Immune_cells': 'Immune Cells'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_tumor': ('Tumor', 1.0, 'native source value', 'Initial Tumor. Sets the initial value of bundled SBML species `Tumor`.'), 'initial_immune_cells': ('Immune_cells', 0.0, 'native source value', 'Initial Immune Cells. Sets the initial value of bundled SBML species `Immune_cells`.'), 'initial_interleukin_2': ('IL2', 0.0, 'native source value', 'Initial Interleukin 2. Sets the initial value of bundled SBML species `IL2`.')}
    _HEADLINE_OUTPUTS = {'tumor': ('Tumor', 'native source value', 'Tumor. Maps to bundled source symbol `Tumor`.'), 'immune_cells': ('Immune_cells', 'native source value', 'Immune Cells. Maps to bundled source symbol `Immune_cells`.'), 'source': ('Source', 'native source value', 'Source. Maps to bundled source symbol `Source`.'), 'sink': ('Sink', 'native source value', 'Sink. Maps to bundled source symbol `Sink`.'), 'interleukin_2': ('IL2', 'native source value', 'Interleukin 2. Maps to bundled source symbol `IL2`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000732.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
