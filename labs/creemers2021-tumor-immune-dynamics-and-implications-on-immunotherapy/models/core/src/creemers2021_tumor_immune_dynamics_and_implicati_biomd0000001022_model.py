# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Creemers2021 - Tumor-immune dynamics and implications on immunotherapy responses."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Creemers2021TumorImmuneDynamicsAndImplicatiBiomd0000001022Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000001022."""

    _SBML_ID = 'BIOMD0000001022'
    _TITLE = 'Creemers2021 - Tumor-immune dynamics and implications on immunotherapy responses'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'I', 'S', 'N']
    _SPECIES_LABELS = {'T': 'Tumor Cells', 'I': 'Intratumoral T Cells', 'S': 'Specific T Cells', 'N': 'Naive T Cells'}
    _PARAMETER_INPUTS = {'intratumoral_t_cell_death_rate': ('delta', 0.019, 'native source value', 'Intratumoral T Cell Death Rate. Sets bundled SBML parameter `delta`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_intratumoral_t_cells': ('I', 0.0, 'native source value', 'Initial Intratumoral T Cells. Sets the initial value of bundled SBML species `I`.'), 'initial_tumor_cells': ('T', 1.0, 'native source value', 'Initial Tumor Cells. Sets the initial value of bundled SBML species `T`.'), 'initial_specific_t_cells': ('S', 0.0, 'native source value', 'Initial Specific T Cells. Sets the initial value of bundled SBML species `S`.'), 'initial_naive_t_cells': ('N', 1000000.0, 'native source value', 'Initial Naive T Cells. Sets the initial value of bundled SBML species `N`.')}
    _HEADLINE_OUTPUTS = {'intratumoral_t_cells': ('I', 'native source value', 'Intratumoral T Cells. Maps to bundled source symbol `I`.'), 'tumor_cells': ('T', 'native source value', 'Tumor Cells. Maps to bundled source symbol `T`.'), 'specific_t_cells': ('S', 'native source value', 'Specific T Cells. Maps to bundled source symbol `S`.'), 'naive_t_cells': ('N', 'native source value', 'Naive T Cells. Maps to bundled source symbol `N`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001022.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
