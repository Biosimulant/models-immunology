# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Bidot2008 - Mathematical modelling of T cell activation kinetics."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bidot2008MathematicalModellingOfTCellActivModel1910290003Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL1910290003."""

    _SBML_ID = 'MODEL1910290003'
    _TITLE = 'Bidot2008 - Mathematical modelling of T cell activation kinetics'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['CD4_8', 'TL', 'TL_0', 'L', 'T', 'T_0', 'T_i', 'CD69', 'IL2Rm', 'IL2', 'CD28', 'CD28_CD80', 'CD80', 'CD28_0', 'CD28_i', 'CD69_CD69L', 'CD69L', 'CD69_0', 'CD69_i', 'IL2_IL2Rm', 'IL2_IL2Rm_0', 'IL2_IL2Rm_i', 'IL2Rs', 'IL2_IL2Rs', 'S']
    _SPECIES_LABELS = {'CD4_8': 'CD4 CD8 Binding State', 'TL': 'TL', 'TL_0': 'Tl 0', 'L': 'L', 'T': 'T', 'T_0': 'Unresolved Immune Observable 1', 'T_i': 'Unresolved Immune Observable 2', 'CD69': 'CD69', 'IL2Rm': 'IL2Rm', 'IL2': 'IL2', 'CD28': 'CD28', 'CD28_CD80': 'Cd28 Cd80 Costimulation Complex', 'CD80': 'CD80', 'CD28_0': 'CD28*', 'CD28_i': 'CD28*i', 'CD69_CD69L': 'CD69-CD69L', 'CD69L': 'CD69L', 'CD69_0': 'CD69*', 'CD69_i': 'CD69*i', 'IL2_IL2Rm': 'IL2-IL2Rm', 'IL2_IL2Rm_0': 'IL2-IL2Rm*', 'IL2_IL2Rm_i': 'IL2-IL2Rm*i', 'IL2Rs': 'IL2Rs', 'IL2_IL2Rs': 'IL2-IL2Rs', 'S': 'S', 'koff_TL': 'koff TL', 'koff_CD28': 'koff CD28', 'koff_CD4_8': 'koff CD4/8', 'koff_CD69': 'koff CD69', 'koff_IL2m': 'koff IL2m', 'koff_IL2s': 'koff IL2s', 'kon_CD28': 'kon CD28', 'kon_CD4_8': 'kon CD4/8', 'kon_CD69': 'kon CD69', 'kon_IL2m': 'kon IL2m', 'kon_IL2s': 'kon IL2s', 'kon_TL': 'kon TL', 'kp_1': "kp'1", 'kp_3': "kp'3", 's_0': "s'"}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_cd4_cd8_binding_state': ('CD4_8', 40000.0, 'native source value', 'Initial CD4 CD8 Binding State. Sets the initial value of bundled SBML species `CD4_8`.'), 'initial_cd28_cd80_costimulation_complex': ('CD28_CD80', 1.0, 'native source value', 'Initial Cd28 Cd80 Costimulation Complex. Sets the initial value of bundled SBML species `CD28_CD80`.'), 'initial_tl_0': ('TL_0', 1.0, 'native source value', 'Initial Tl 0. Sets the initial value of bundled SBML species `TL_0`.'), 'initial_unresolved_immune_observable_1': ('T_0', 1.0, 'native source value', 'Initial Unresolved Immune Observable 1. Sets the initial value of bundled SBML species `T_0`.'), 'initial_unresolved_immune_observable_2': ('T_i', 1.0, 'native source value', 'Initial Unresolved Immune Observable 2. Sets the initial value of bundled SBML species `T_i`.')}
    _HEADLINE_OUTPUTS = {'cd4_cd8_binding_state': ('CD4_8', 'native source value', 'CD4 CD8 Binding State. Maps to bundled source symbol `CD4_8`.'), 'cd28_cd80_costimulation_complex': ('CD28_CD80', 'native source value', 'Cd28 Cd80 Costimulation Complex. Maps to bundled source symbol `CD28_CD80`.'), 'tl_0': ('TL_0', 'native source value', 'Tl 0. Maps to bundled source symbol `TL_0`.'), 'unresolved_immune_observable_1': ('T_0', 'native source value', 'Unresolved Immune Observable 1. Maps to bundled source symbol `T_0`.'), 'unresolved_immune_observable_2': ('T_i', 'native source value', 'Unresolved Immune Observable 2. Maps to bundled source symbol `T_i`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1910290003.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
