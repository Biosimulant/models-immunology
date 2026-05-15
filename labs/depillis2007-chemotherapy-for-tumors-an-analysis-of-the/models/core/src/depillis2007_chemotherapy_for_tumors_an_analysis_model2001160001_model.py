# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for dePillis2007 - Chemotherapy for tumors An analysis of the dynamics and a study of quadratic and linear optimal controls."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Depillis2007ChemotherapyForTumorsAnAnalysisModel2001160001Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL2001160001."""

    _SBML_ID = 'MODEL2001160001'
    _TITLE = 'dePillis2007 - Chemotherapy for tumors An analysis of the dynamics and a study of quadratic and linear optimal controls'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'N', 'C', 'M']
    _SPECIES_LABELS = {'T': 'Unresolved Tumor Observable 1', 'N': 'Unresolved Tumor Observable 2', 'C': 'Unresolved Tumor Observable 3', 'M': 'Unresolved Tumor Observable 4'}
    _PARAMETER_INPUTS = {'removal_of_chemotherapeutic_drug_at_ther_target_site_rate': ('gamma', 0.9, 'native source value', 'Removal Of Chemotherapeutic Drug At Ther Target Site Rate. Sets bundled SBML parameter `gamma`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('T', 1.0, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `T`.'), 'initial_unresolved_tumor_observable_2': ('N', 1.0, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `N`.'), 'initial_unresolved_tumor_observable_3': ('C', 1.0, 'native source value', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `C`.'), 'initial_unresolved_tumor_observable_4': ('M', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `M`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('T', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `T`.'), 'unresolved_tumor_observable_2': ('N', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `N`.'), 'unresolved_tumor_observable_3': ('C', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `C`.'), 'unresolved_tumor_observable_4': ('M', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `M`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2001160001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
