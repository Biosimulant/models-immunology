# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Cappuccio2006 - Cancer immunotherapy by interleukin-21."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Cappuccio2006CancerImmunotherapyByInterleukiBiomd0000000761Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000761."""

    _SBML_ID = 'BIOMD0000000761'
    _TITLE = 'Cappuccio2006 - Cancer immunotherapy by interleukin-21'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['U', 'X', 'Y', 'M', 'P', 'Z']
    _SPECIES_LABELS = {'U': 'Interleukin 21', 'X': 'Natural Killer T Cells', 'Y': 'CD8 T Cells', 'M': 'CD8 Memory Factor', 'P': 'P_Cytotoxic_Protein', 'Z': 'Tumor Sa', 'D': 'nD'}
    _PARAMETER_INPUTS = {'tumor_growth_rate': ('c', 5.1, 'unit_6', 'Tumor Growth Rate. Sets bundled SBML parameter `c`.'), 'tumor_killing_by_natural_killer_cells_rate': ('k1', 0.05, 'unit_7', 'Tumor Killing By Natural Killer Cells Rate. Sets bundled SBML parameter `k1`.'), 'tumor_killing_by_cd8_t_cells_rate': ('k2', 0.0485, 'unit_7', 'Tumor Killing By CD8 T Cells Rate. Sets bundled SBML parameter `k2`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_natural_killer_t_cells': ('X', 1.95185, 'native source value', 'Initial Natural Killer T Cells. Sets the initial value of bundled SBML species `X`.'), 'initial_cd8_t_cells': ('Y', 0.066, 'native source value', 'Initial CD8 T Cells. Sets the initial value of bundled SBML species `Y`.'), 'initial_tumor_sa': ('Z', 2.0, 'native source value', 'Initial Tumor Sa. Sets the initial value of bundled SBML species `Z`.'), 'initial_interleukin_21': ('U', 0.0, 'native source value', 'Initial Interleukin 21. Sets the initial value of bundled SBML species `U`.'), 'initial_cd8_memory_factor': ('M', 0.0, 'native source value', 'Initial CD8 Memory Factor. Sets the initial value of bundled SBML species `M`.')}
    _HEADLINE_OUTPUTS = {'natural_killer_t_cells': ('X', 'native source value', 'Natural Killer T Cells. Maps to bundled source symbol `X`.'), 'cd8_t_cells': ('Y', 'native source value', 'CD8 T Cells. Maps to bundled source symbol `Y`.'), 'tumor_sa': ('Z', 'native source value', 'Tumor Sa. Maps to bundled source symbol `Z`.'), 'interleukin_21': ('U', 'native source value', 'Interleukin 21. Maps to bundled source symbol `U`.'), 'cd8_memory_factor': ('M', 'native source value', 'CD8 Memory Factor. Maps to bundled source symbol `M`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000761.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
