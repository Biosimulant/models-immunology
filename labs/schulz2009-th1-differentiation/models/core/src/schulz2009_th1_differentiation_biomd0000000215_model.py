# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Schulz2009_Th1_differentiation."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Schulz2009Th1DifferentiationBiomd0000000215Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000215."""

    _SBML_ID = 'BIOMD0000000215'
    _TITLE = 'Schulz2009_Th1_differentiation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Tbet_mRNA', 'Ifn_mRNA', 'Ag', 'Ifn_Prot', 'Rec_Prot', 'Tbet_Prot', 'Rec_mRNA']
    _SPECIES_LABELS = {'Tbet_mRNA': 'Tbet mRNA', 'Ifn_mRNA': 'Interferon mRNA', 'Ag': 'Unresolved Signaling Observable 1', 'Ifn_Prot': 'Interferon Prot', 'Rec_Prot': 'Rec Prot', 'Tbet_Prot': 'Tbet_Prot', 'Rec_mRNA': 'Rec_mRNA'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_interferon_mrna': ('Ifn_mRNA', 0.0, 'native source value', 'Initial Interferon mRNA. Sets the initial value of bundled SBML species `Ifn_mRNA`.'), 'initial_interferon_prot': ('Ifn_Prot', 0.0, 'native source value', 'Initial Interferon Prot. Sets the initial value of bundled SBML species `Ifn_Prot`.'), 'initial_tbet_mrna': ('Tbet_mRNA', 0.0440000000000001, 'native source value', 'Initial Tbet mRNA. Sets the initial value of bundled SBML species `Tbet_mRNA`.'), 'initial_rec_prot': ('Rec_Prot', 0.0, 'native source value', 'Initial Rec Prot. Sets the initial value of bundled SBML species `Rec_Prot`.')}
    _HEADLINE_OUTPUTS = {'interferon_mrna': ('Ifn_mRNA', 'native source value', 'Interferon mRNA. Maps to bundled source symbol `Ifn_mRNA`.'), 'interferon_prot': ('Ifn_Prot', 'native source value', 'Interferon Prot. Maps to bundled source symbol `Ifn_Prot`.'), 'tbet_mrna': ('Tbet_mRNA', 'native source value', 'Tbet mRNA. Maps to bundled source symbol `Tbet_mRNA`.'), 'unresolved_signaling_observable_1': ('Ag', 'native source value', 'Unresolved Signaling Observable 1. Maps to bundled source symbol `Ag`.'), 'rec_prot': ('Rec_Prot', 'native source value', 'Rec Prot. Maps to bundled source symbol `Rec_Prot`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000215.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
