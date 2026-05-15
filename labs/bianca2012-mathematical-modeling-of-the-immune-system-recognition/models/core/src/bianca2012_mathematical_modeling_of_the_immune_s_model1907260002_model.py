# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Bianca2012 - Mathematical modeling of the immune system recognition to mammary carcinoma antigen."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bianca2012MathematicalModelingOfTheImmuneSModel1907260002Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL1907260002."""

    _SBML_ID = 'MODEL1907260002'
    _TITLE = 'Bianca2012 - Mathematical modeling of the immune system recognition to mammary carcinoma antigen'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['VC', 'TAA', 'B', 'TH', 'IL12', 'IL2', 'AB', 'CC', 'TC', 'APC', 'TA']
    _SPECIES_LABELS = {'VC': 'Unresolved Tumor Observable 1', 'TAA': 'Unresolved Tumor Observable 2', 'B': 'Unresolved Tumor Observable 3', 'TH': 'Unresolved Tumor Observable 4', 'IL12': 'Interleukin 12', 'IL2': 'IL2', 'AB': 'AB', 'CC': 'CC', 'TC': 'TC', 'APC': 'APC', 'TA': 'TA', 'ModelValue_45': 'Initial for startTime'}
    _PARAMETER_INPUTS = {'taa_release_vc_rate': ('gamma_21', 3.0, 'native source value', 'Taa Release Vc Rate. Sets bundled SBML parameter `gamma_21`.'), 'taa_release_cc_rate': ('gamma_28', 3.0, 'native source value', 'Taa Release Cc Rate. Sets bundled SBML parameter `gamma_28`.'), 'b_death_rate': ('mu_3', 0.693147, 'native source value', 'B Death Rate. Sets bundled SBML parameter `mu_3`.'), 'th_death_rate': ('mu_4', 0.693147, 'native source value', 'Th Death Rate. Sets bundled SBML parameter `mu_4`.'), 'interleukin_12_release_vc_rate': ('gamma_51', 10.0, 'native source value', 'Interleukin 12 Release Vc Rate. Sets bundled SBML parameter `gamma_51`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('VC', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `VC`.'), 'initial_unresolved_tumor_observable_2': ('TAA', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `TAA`.'), 'initial_unresolved_tumor_observable_3': ('B', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `B`.'), 'initial_unresolved_tumor_observable_4': ('TH', 0.0, 'native source value', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `TH`.'), 'initial_interleukin_12': ('IL12', 0.0, 'native source value', 'Initial Interleukin 12. Sets the initial value of bundled SBML species `IL12`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('VC', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `VC`.'), 'unresolved_tumor_observable_2': ('TAA', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `TAA`.'), 'unresolved_tumor_observable_3': ('B', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `B`.'), 'unresolved_tumor_observable_4': ('TH', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `TH`.'), 'interleukin_12': ('IL12', 'native source value', 'Interleukin 12. Maps to bundled source symbol `IL12`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1907260002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
