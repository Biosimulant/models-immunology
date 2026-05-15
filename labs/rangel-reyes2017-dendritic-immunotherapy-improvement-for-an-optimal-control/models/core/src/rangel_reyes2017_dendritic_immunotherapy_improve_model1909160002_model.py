# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Rangel-Reyes2017 - Dendritic Immunotherapy Improvement for an Optimal Control Murine Model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class RangelReyes2017DendriticImmunotherapyImproveModel1909160002Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL1909160002."""

    _SBML_ID = 'MODEL1909160002'
    _TITLE = 'Rangel-Reyes2017 - Dendritic Immunotherapy Improvement for an Optimal Control Murine Model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'H', 'C', 'D', 'I', 'F_Beta', 'F_Gamma', 'M_I']
    _SPECIES_LABELS = {'T': 'Unresolved Tumor Observable 1', 'H': 'Unresolved Tumor Observable 2', 'C': 'Unresolved Tumor Observable 3', 'D': 'Unresolved Tumor Observable 4', 'I': 'Unresolved Tumor Observable 5', 'F_Beta': 'F_Beta', 'F_Gamma': 'F_Gamma', 'M_I': 'M_I'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('T', 60000.0, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `T`.'), 'initial_unresolved_tumor_observable_2': ('H', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `H`.'), 'initial_unresolved_tumor_observable_3': ('C', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `C`.'), 'initial_unresolved_tumor_observable_4': ('D', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `D`.'), 'initial_unresolved_tumor_observable_5': ('I', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 5. Sets the initial value of bundled SBML species `I`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('T', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `T`.'), 'unresolved_tumor_observable_2': ('H', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `H`.'), 'unresolved_tumor_observable_3': ('C', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `C`.'), 'unresolved_tumor_observable_4': ('D', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `D`.'), 'unresolved_tumor_observable_5': ('I', 'native source value', 'Unresolved Tumor Observable 5. Maps to bundled source symbol `I`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1909160002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
