# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Begitt2014 - STAT1 cooperative DNA binding - single GAS polymer model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Begitt2014Stat1CooperativeDnaBindingSingleBiomd0000000500Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000500."""

    _SBML_ID = 'BIOMD0000000500'
    _TITLE = 'Begitt2014 - STAT1 cooperative DNA binding - single GAS polymer model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['S1', 'DNA_000', 'DNA_100', 'DNA_010', 'DNA_001', 'DNA_110', 'DNA_101', 'DNA_011', 'DNA_111', 'DNA_1B10', 'DNA_01B1', 'DNA_1B11', 'DNA_11B1', 'DNA_1B1B1']
    _SPECIES_LABELS = {'S1': 'Unresolved Signaling Observable 1', 'DNA_000': 'DNA 000', 'DNA_100': 'DNA 100', 'DNA_010': 'DNA 010', 'DNA_001': 'DNA 001', 'DNA_110': 'DNA_110', 'DNA_101': 'DNA_101', 'DNA_011': 'DNA_011', 'DNA_111': 'DNA_111', 'DNA_1B10': 'DNA_1B10', 'DNA_01B1': 'DNA_01B1', 'DNA_1B11': 'DNA_1B11', 'DNA_11B1': 'DNA_11B1', 'DNA_1B1B1': 'DNA_1B1B1', 'parameter_1': 'GAS_siteOccupancy'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_signaling_observable_1': ('S1', 1e-10, 'native source value', 'Initial Unresolved Signaling Observable 1. Sets the initial value of bundled SBML species `S1`.'), 'initial_dna_000': ('DNA_000', 1e-10, 'native source value', 'Initial DNA 000. Sets the initial value of bundled SBML species `DNA_000`.'), 'initial_dna_100': ('DNA_100', 0.0, 'native source value', 'Initial DNA 100. Sets the initial value of bundled SBML species `DNA_100`.'), 'initial_dna_010': ('DNA_010', 0.0, 'native source value', 'Initial DNA 010. Sets the initial value of bundled SBML species `DNA_010`.'), 'initial_dna_001': ('DNA_001', 0.0, 'native source value', 'Initial DNA 001. Sets the initial value of bundled SBML species `DNA_001`.')}
    _HEADLINE_OUTPUTS = {'unresolved_signaling_observable_1': ('S1', 'native source value', 'Unresolved Signaling Observable 1. Maps to bundled source symbol `S1`.'), 'dna_000': ('DNA_000', 'native source value', 'DNA 000. Maps to bundled source symbol `DNA_000`.'), 'dna_100': ('DNA_100', 'native source value', 'DNA 100. Maps to bundled source symbol `DNA_100`.'), 'dna_010': ('DNA_010', 'native source value', 'DNA 010. Maps to bundled source symbol `DNA_010`.'), 'dna_001': ('DNA_001', 'native source value', 'DNA 001. Maps to bundled source symbol `DNA_001`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000500.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
