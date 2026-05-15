# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Sontag2017 - Dynamic model of immune responses to antigen presentation by tumor or pathogen."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Sontag2017DynamicModelOfImmuneResponsesToBiomd0000001030Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000001030."""

    _SBML_ID = 'BIOMD0000001030'
    _TITLE = 'Sontag2017 - Dynamic model of immune responses to antigen presentation by tumor or pathogen'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Antigen_expressing_cells', 'Regulatory_cells', 'Effector_cells']
    _SPECIES_LABELS = {'Antigen_expressing_cells': 'Antigen Expressing Cells', 'Regulatory_cells': 'Regulatory Cells', 'Effector_cells': 'Effector Cells'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_regulatory_cells': ('Regulatory_cells', 1.0, 'native source value', 'Initial Regulatory Cells. Sets the initial value of bundled SBML species `Regulatory_cells`.'), 'initial_effector_cells': ('Effector_cells', 1.0, 'native source value', 'Initial Effector Cells. Sets the initial value of bundled SBML species `Effector_cells`.')}
    _HEADLINE_OUTPUTS = {'antigen_expressing_cells': ('Antigen_expressing_cells', 'native source value', 'Antigen Expressing Cells. Maps to bundled source symbol `Antigen_expressing_cells`.'), 'regulatory_cells': ('Regulatory_cells', 'native source value', 'Regulatory Cells. Maps to bundled source symbol `Regulatory_cells`.'), 'effector_cells': ('Effector_cells', 'native source value', 'Effector Cells. Maps to bundled source symbol `Effector_cells`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001030.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
