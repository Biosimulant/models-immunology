# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Bachmann2011 - Division of labor by dual feedback regulators controls JAK2/STAT5 signaling over broad ligand range."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Bachmann2011DivisionOfLaborByDualFeedbackBiomd0000000861Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000861."""

    _SBML_ID = 'BIOMD0000000861'
    _TITLE = 'Bachmann2011 - Division of labor by dual feedback regulators controls JAK2/STAT5 signaling over broad ligand range'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['EpoRJAK2', 'EpoRpJAK2', 'p1EpoRpJAK2', 'p2EpoRpJAK2', 'p12EpoRpJAK2', 'EpoRJAK2_CIS', 'SHP1', 'SHP1Act', 'STAT5', 'pSTAT5', 'npSTAT5', 'CISnRNA1', 'CISnRNA2', 'CISnRNA3', 'CISnRNA4', 'CISnRNA5', 'CISRNA', 'CIS', 'SOCS3nRNA1', 'SOCS3nRNA2', 'SOCS3nRNA3', 'SOCS3nRNA4', 'SOCS3nRNA5', 'SOCS3RNA', 'SOCS3', 'Epo']
    _SPECIES_LABELS = {'EpoRJAK2': 'Erythropoietin Receptor Jak2 Complex', 'EpoRpJAK2': 'Phosphorylated Erythropoietin Receptor Jak2 Complex', 'p1EpoRpJAK2': 'Phosphorylated Erythropoietin Receptor Jak2 Site 1', 'p2EpoRpJAK2': 'Phosphorylated Erythropoietin Receptor Jak2 Site 2', 'p12EpoRpJAK2': 'Phosphorylated Erythropoietin Receptor Jak2 Sites 1 2', 'EpoRJAK2_CIS': 'EpoRJAK2_CIS', 'SHP1': 'SHP1', 'SHP1Act': 'SHP1Act', 'STAT5': 'STAT5', 'pSTAT5': 'pSTAT5', 'npSTAT5': 'npSTAT5', 'CISnRNA1': 'CISnRNA1', 'CISnRNA2': 'CISnRNA2', 'CISnRNA3': 'CISnRNA3', 'CISnRNA4': 'CISnRNA4', 'CISnRNA5': 'CISnRNA5', 'CISRNA': 'CISRNA', 'CIS': 'CIS', 'SOCS3nRNA1': 'SOCS3nRNA1', 'SOCS3nRNA2': 'SOCS3nRNA2', 'SOCS3nRNA3': 'SOCS3nRNA3', 'SOCS3nRNA4': 'SOCS3nRNA4', 'SOCS3nRNA5': 'SOCS3nRNA5', 'SOCS3RNA': 'SOCS3RNA', 'SOCS3': 'SOCS3', 'Epo': 'Epo'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_erythropoietin_receptor_jak2_complex': ('EpoRJAK2', 3.97622, 'native source value', 'Initial Erythropoietin Receptor Jak2 Complex. Sets the initial value of bundled SBML species `EpoRJAK2`.'), 'initial_phosphorylated_erythropoietin_receptor_jak2_complex': ('EpoRpJAK2', 0.0, 'native source value', 'Initial Phosphorylated Erythropoietin Receptor Jak2 Complex. Sets the initial value of bundled SBML species `EpoRpJAK2`.'), 'initial_phosphorylated_erythropoietin_receptor_jak2_site_1': ('p1EpoRpJAK2', 0.0, 'native source value', 'Initial Phosphorylated Erythropoietin Receptor Jak2 Site 1. Sets the initial value of bundled SBML species `p1EpoRpJAK2`.'), 'initial_phosphorylated_erythropoietin_receptor_jak2_site_2': ('p2EpoRpJAK2', 0.0, 'native source value', 'Initial Phosphorylated Erythropoietin Receptor Jak2 Site 2. Sets the initial value of bundled SBML species `p2EpoRpJAK2`.'), 'initial_phosphorylated_erythropoietin_receptor_jak2_sites_1_2': ('p12EpoRpJAK2', 0.0, 'native source value', 'Initial Phosphorylated Erythropoietin Receptor Jak2 Sites 1 2. Sets the initial value of bundled SBML species `p12EpoRpJAK2`.')}
    _HEADLINE_OUTPUTS = {'erythropoietin_receptor_jak2_complex': ('EpoRJAK2', 'native source value', 'Erythropoietin Receptor Jak2 Complex. Maps to bundled source symbol `EpoRJAK2`.'), 'phosphorylated_erythropoietin_receptor_jak2_complex': ('EpoRpJAK2', 'native source value', 'Phosphorylated Erythropoietin Receptor Jak2 Complex. Maps to bundled source symbol `EpoRpJAK2`.'), 'phosphorylated_erythropoietin_receptor_jak2_site_1': ('p1EpoRpJAK2', 'native source value', 'Phosphorylated Erythropoietin Receptor Jak2 Site 1. Maps to bundled source symbol `p1EpoRpJAK2`.'), 'phosphorylated_erythropoietin_receptor_jak2_site_2': ('p2EpoRpJAK2', 'native source value', 'Phosphorylated Erythropoietin Receptor Jak2 Site 2. Maps to bundled source symbol `p2EpoRpJAK2`.'), 'phosphorylated_erythropoietin_receptor_jak2_sites_1_2': ('p12EpoRpJAK2', 'native source value', 'Phosphorylated Erythropoietin Receptor Jak2 Sites 1 2. Maps to bundled source symbol `p12EpoRpJAK2`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000861.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
