# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Rateitschak2012 - Interferon-gamma (IFNγ) induced STAT1 signalling (PC_IFNg100)."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Rateitschak2012InterferonGammaIfnInducedStaBiomd0000000585Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000585."""

    _SBML_ID = 'BIOMD0000000585'
    _TITLE = 'Rateitschak2012 - Interferon-gamma (IFNγ) induced STAT1 signalling (PC_IFNg100)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Ifng', 'II', 'd1', 'd2', 'd3', 'd4', 'Stat1Pd', 'Stat1Pdn', 'i1', 'i2', 'i3', 'i4', 'j1', 'j2', 'j3', 'j4', 'Ir', 'Stat1U', 'Stat1Un', 'mRNA', 'Stat1ex', 'Stat1cex', 'Stat1nex', 'Stat1Pex', 'Stat1Pcex', 'Stat1Pnex', 'Socs1ex', 'RSNCex']
    _SPECIES_LABELS = {'Ifng': 'Ifng', 'II': 'II', 'd1': 'd1', 'd2': 'd2', 'd3': 'd3', 'd4': 'd4', 'Stat1Pd': 'Phosphorylated Stat1 Dimer', 'Stat1Pdn': 'Nuclear Phosphorylated Stat1 Dimer', 'i1': 'i1', 'i2': 'i2', 'i3': 'i3', 'i4': 'i4', 'j1': 'j1', 'j2': 'j2', 'j3': 'j3', 'j4': 'j4', 'Ir': 'Ir', 'Stat1U': 'Unphosphorylated Stat1', 'Stat1Un': 'Nuclear Unphosphorylated Stat1', 'mRNA': 'Socs1 mRNA', 'Stat1ex': 'STAT1 (observed)', 'Stat1cex': 'STAT1c (observed)', 'Stat1nex': 'STAT1n (observed)', 'Stat1Pex': 'STAT1D (observed)', 'Stat1Pcex': 'STAT1Dc (observed)', 'Stat1Pnex': 'STAT1Dn (observed)', 'Socs1ex': 'SOCS1 (observed)', 'RSNCex': 'RSNC (observed)', 'k9': 'k7', 'k10': 'k8', 'k11': 'k9', 'k12': 'k10', 'k13': 'k11', 'k14': 'k12', 'taud': 'tau_1', 'tau': 'tau_2', 'tauj': 'tau_3', 'scale_Stat1ex': 'WB_STAT1', 'scale_Stat1cex': 'WB_STAT1c', 'scale_Stat1nex': 'WB_STAT1n', 'scale_Stat1Pex': 'WB_STAT1D', 'scale_Stat1Pcex': 'WB_STAT1Dc', 'scale_Stat1Pnex': 'WB_STAT1Dn', 'scale_Socs1ex': 'PCR_SOCS1'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'phosphorylated_stat1_dimer': ('Stat1Pd', 'native source value', 'Phosphorylated Stat1 Dimer. Maps to bundled source symbol `Stat1Pd`.'), 'nuclear_phosphorylated_stat1_dimer': ('Stat1Pdn', 'native source value', 'Nuclear Phosphorylated Stat1 Dimer. Maps to bundled source symbol `Stat1Pdn`.'), 'unphosphorylated_stat1': ('Stat1U', 'native source value', 'Unphosphorylated Stat1. Maps to bundled source symbol `Stat1U`.'), 'nuclear_unphosphorylated_stat1': ('Stat1Un', 'native source value', 'Nuclear Unphosphorylated Stat1. Maps to bundled source symbol `Stat1Un`.'), 'socs1_mrna': ('mRNA', 'native source value', 'Socs1 mRNA. Maps to bundled source symbol `mRNA`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000585.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
