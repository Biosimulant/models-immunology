# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Draghi2019 - Parameter identification of a model for prostate cancer treated by intermittent therapy."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Draghi2019ParameterIdentificationOfAModelFModel1911100005Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL1911100005."""

    _SBML_ID = 'MODEL1911100005'
    _TITLE = 'Draghi2019 - Parameter identification of a model for prostate cancer treated by intermittent therapy'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['p', 'a', 't_d', 't_i']
    _SPECIES_LABELS = {'p': 'Unresolved Tumor Observable 1', 'a': 'Unresolved Tumor Observable 2', 't_d': 'Unresolved Tumor Observable 3', 't_i': 'Unresolved Tumor Observable 4'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('p', 1.0, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `p`.'), 'initial_unresolved_tumor_observable_2': ('a', 1.0, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `a`.'), 'initial_unresolved_tumor_observable_3': ('t_d', 0.1, 'native source value', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `t_d`.'), 'initial_unresolved_tumor_observable_4': ('t_i', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `t_i`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('p', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `p`.'), 'unresolved_tumor_observable_2': ('a', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `a`.'), 'unresolved_tumor_observable_3': ('t_d', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `t_d`.'), 'unresolved_tumor_observable_4': ('t_i', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `t_i`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1911100005.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
