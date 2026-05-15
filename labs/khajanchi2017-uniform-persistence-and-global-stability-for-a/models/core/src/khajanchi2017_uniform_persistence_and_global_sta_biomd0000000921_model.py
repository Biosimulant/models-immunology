# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Khajanchi2017 - Uniform Persistence and Global Stability for a Brain Tumor and Immune System Interaction."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Khajanchi2017UniformPersistenceAndGlobalStaBiomd0000000921Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000921."""

    _SBML_ID = 'BIOMD0000000921'
    _TITLE = 'Khajanchi2017 - Uniform Persistence and Global Stability for a Brain Tumor and Immune System Interaction'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['G', 'M', 'C_T', 'T_beta', 'I_gamma']
    _SPECIES_LABELS = {'G': 'Unresolved Tumor Observable 1', 'M': 'Unresolved Tumor Observable 2', 'C_T': 'Unresolved Tumor Observable 3', 'T_beta': 'Unresolved Tumor Observable 4', 'I_gamma': 'Gamma'}
    _PARAMETER_INPUTS = {'the_proliferative_enhancement_effect_of_macrophagesby_interferon_gama_and_negati': ('k4', 10500.0, 'native source value', 'The Proliferative Enhancement Effect Of Macrophagesby Interferon Gama And Negati. Sets bundled SBML parameter `k4`.'), 'the_rate_of_change_of_cytotoxic_t_lymphocytes_whose_stimulation_is_followed_by_g': ('k5', 2000.0, 'native source value', 'The Rate Of Change Of Cytotoxic T Lymphocytes Whose Stimulation Is Followed By G. Sets bundled SBML parameter `k5`.'), 'clearance_of_cytotoxic_t_lymphocytes_due_to_their_interaction_with_glioma_cells': ('k3', 334450.0, 'native source value', 'Clearance Of Cytotoxic T Lymphocytes Due To Their Interaction With Glioma Cells. Sets bundled SBML parameter `k3`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_tumor_observable_1': ('G', 100000.0, 'native source value', 'Initial Unresolved Tumor Observable 1. Sets the initial value of bundled SBML species `G`.'), 'initial_unresolved_tumor_observable_2': ('M', 100000.0, 'native source value', 'Initial Unresolved Tumor Observable 2. Sets the initial value of bundled SBML species `M`.'), 'initial_unresolved_tumor_observable_3': ('C_T', 1.0, 'native source value', 'Initial Unresolved Tumor Observable 3. Sets the initial value of bundled SBML species `C_T`.'), 'initial_unresolved_tumor_observable_4': ('T_beta', 5000.0, 'native source value', 'Initial Unresolved Tumor Observable 4. Sets the initial value of bundled SBML species `T_beta`.'), 'initial_gamma': ('I_gamma', 9000.0, 'native source value', 'Initial Gamma. Sets the initial value of bundled SBML species `I_gamma`.')}
    _HEADLINE_OUTPUTS = {'unresolved_tumor_observable_1': ('G', 'native source value', 'Unresolved Tumor Observable 1. Maps to bundled source symbol `G`.'), 'unresolved_tumor_observable_2': ('M', 'native source value', 'Unresolved Tumor Observable 2. Maps to bundled source symbol `M`.'), 'unresolved_tumor_observable_3': ('C_T', 'native source value', 'Unresolved Tumor Observable 3. Maps to bundled source symbol `C_T`.'), 'unresolved_tumor_observable_4': ('T_beta', 'native source value', 'Unresolved Tumor Observable 4. Maps to bundled source symbol `T_beta`.'), 'gamma': ('I_gamma', 'native source value', 'Gamma. Maps to bundled source symbol `I_gamma`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000921.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
