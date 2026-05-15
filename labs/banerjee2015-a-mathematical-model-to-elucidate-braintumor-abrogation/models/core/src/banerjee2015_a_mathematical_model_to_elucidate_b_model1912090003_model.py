# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Banerjee2015 - A Mathematical Model to Elucidate BrainTumor Abrogation by Immunotherapywith T11 Target Structure."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Banerjee2015AMathematicalModelToElucidateBModel1912090003Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL1912090003."""

    _SBML_ID = 'MODEL1912090003'
    _TITLE = 'Banerjee2015 - A Mathematical Model to Elucidate BrainTumor Abrogation by Immunotherapywith T11 Target Structure'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['G', 'M', 'CT', 'TB', 'IG']
    _SPECIES_LABELS = {'G': 'Unresolved Tumor Observable 1', 'M': 'Unresolved Tumor Observable 2', 'CT': 'Unresolved Tumor Observable 3', 'TB': 'Unresolved Tumor Observable 4', 'IG': 'Unresolved Tumor Observable 5'}
    _PARAMETER_INPUTS = {'cytokine_transforming_growth_factor_beta_removal_rate': ('mu_2', 6.93, 'native source value', 'Cytokine Transforming Growth Factor Beta Removal Rate. Sets bundled SBML parameter `mu_2`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('G', 857419.0, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `G`.'), 'initial_unresolved_tumor_observable_2': ('M', 943092.0, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `M`.'), 'initial_unresolved_tumor_observable_3': ('CT', 303.397, 'native source value', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `CT`.'), 'initial_unresolved_tumor_observable_4': ('TB', 9134.33, 'native source value', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `TB`.'), 'initial_unresolved_tumor_observable_5': ('IG', 0.303397, 'native source value', 'Initial Unresolved Tumor Observable 5. Sets the initial value of bundled SBML species `IG`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('G', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `G`.'), 'unresolved_tumor_observable_2': ('M', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `M`.'), 'unresolved_tumor_observable_3': ('CT', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `CT`.'), 'unresolved_tumor_observable_4': ('TB', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `TB`.'), 'unresolved_tumor_observable_5': ('IG', 'native source value', 'Unresolved Tumor Observable 5. Maps to bundled source symbol `IG`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1912090003.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
