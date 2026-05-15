# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Bianca2013 - Persistence analysis in a Kolmogorov-type model for cancer-immune system competition."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bianca2013PersistenceAnalysisInAKolmogorovBiomd0000000900Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000900."""

    _SBML_ID = 'BIOMD0000000900'
    _TITLE = 'Bianca2013 - Persistence analysis in a Kolmogorov-type model for cancer-immune system competition'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['C', 'B', 'T']
    _SPECIES_LABELS = {'C': 'Unresolved Tumor Observable 1', 'B': 'Unresolved Tumor Observable 2', 'T': 'Unresolved Tumor Observable 3'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('C', 1.0, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `C`.'), 'initial_unresolved_tumor_observable_2': ('B', 1.0, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `B`.'), 'initial_unresolved_tumor_observable_3': ('T', 1.0, 'native source value', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `T`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('C', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `C`.'), 'unresolved_tumor_observable_2': ('B', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `B`.'), 'unresolved_tumor_observable_3': ('T', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `T`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000900.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
