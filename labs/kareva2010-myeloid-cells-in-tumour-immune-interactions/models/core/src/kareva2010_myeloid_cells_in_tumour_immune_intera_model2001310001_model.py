# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Kareva2010 - Myeloid cells in tumour-immune interactions.."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Kareva2010MyeloidCellsInTumourImmuneInteraModel2001310001Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL2001310001."""

    _SBML_ID = 'MODEL2001310001'
    _TITLE = 'Kareva2010 - Myeloid cells in tumour-immune interactions.'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['L', 'T', 'M1', 'M2']
    _SPECIES_LABELS = {'L': 'Unresolved Tumor Observable 1', 'T': 'Unresolved Tumor Observable 2', 'M1': 'Unresolved Tumor Observable 3', 'M2': 'Unresolved Tumor Observable 4'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('L', 1.0, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `L`.'), 'initial_unresolved_tumor_observable_2': ('T', 1.0, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `T`.'), 'initial_unresolved_tumor_observable_3': ('M1', 1.0, 'native source value', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `M1`.'), 'initial_unresolved_tumor_observable_4': ('M2', 1.0, 'native source value', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `M2`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('L', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `L`.'), 'unresolved_tumor_observable_2': ('T', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `T`.'), 'unresolved_tumor_observable_3': ('M1', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `M1`.'), 'unresolved_tumor_observable_4': ('M2', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `M2`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2001310001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
