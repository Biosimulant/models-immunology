# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Waugh2006 - Diabetic Wound Healing - TGF-B Dynamics."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Waugh2006DiabeticWoundHealingTgfBDynamicsBiomd0000000680Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000680."""

    _SBML_ID = 'BIOMD0000000680'
    _TITLE = 'Waugh2006 - Diabetic Wound Healing - TGF-B Dynamics'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['K_T', 'phi_I', 'phi_R', 'T']
    _SPECIES_LABELS = {'K_T': 'Unresolved Immune Observable 1', 'phi_I': 'Phi I', 'phi_R': 'Phi R', 'T': 'Unresolved Immune Observable 2'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'unresolved_immune_observable_1': ('K_T', 'native source value', 'Unresolved Immune Observable 1. Maps to bundled source symbol `K_T`.'), 'phi_i': ('phi_I', 'native source value', 'Phi I. Maps to bundled source symbol `phi_I`.'), 'phi_r': ('phi_R', 'native source value', 'Phi R. Maps to bundled source symbol `phi_R`.'), 'unresolved_immune_observable_2': ('T', 'native source value', 'Unresolved Immune Observable 2. Maps to bundled source symbol `T`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000680.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
