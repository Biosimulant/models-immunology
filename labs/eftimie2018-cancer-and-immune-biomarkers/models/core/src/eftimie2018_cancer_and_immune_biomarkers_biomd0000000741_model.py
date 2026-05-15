# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Eftimie2018 - Cancer and Immune biomarkers."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Eftimie2018CancerAndImmuneBiomarkersBiomd0000000741Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000741."""

    _SBML_ID = 'BIOMD0000000741'
    _TITLE = 'Eftimie2018 - Cancer and Immune biomarkers'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['NT', 'NI', 'BT', 'BI']
    _SPECIES_LABELS = {'NT': 'Unresolved Tumor Observable 1', 'NI': 'Unresolved Tumor Observable 2', 'BT': 'Unresolved Tumor Observable 3', 'BI': 'Unresolved Tumor Observable 4', 'cil_conc': 'cil-conc', 'dil_conc': 'dil-conc', 'cca_conc': 'cca-conc', 'dca_conc': 'dca-conc', 'ModelValue_18': 'Initial for cca-conc', 'ModelValue_16': 'Initial for cil-conc', 'ModelValue_19': 'Initial for dca-conc', 'ModelValue_17': 'Initial for dil-conc', 'ModelValue_8': 'Initial for vpl'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('NT', 1.0, 'substance', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `NT`.'), 'initial_unresolved_tumor_observable_2': ('NI', 0.0, 'substance', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `NI`.'), 'initial_unresolved_tumor_observable_3': ('BT', 0.0, 'substance', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `BT`.'), 'initial_unresolved_tumor_observable_4': ('BI', 0.0, 'substance', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `BI`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('NT', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `NT`.'), 'unresolved_tumor_observable_2': ('NI', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `NI`.'), 'unresolved_tumor_observable_3': ('BT', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `BT`.'), 'unresolved_tumor_observable_4': ('BI', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `BI`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000741.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
