# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Yamada2003_JAK_STAT_SOCS1_knockout."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Yamada2003JakStatSocs1KnockoutBiomd0000000094Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000094."""

    _SBML_ID = 'BIOMD0000000094'
    _TITLE = 'Yamada2003_JAK_STAT_SOCS1_knockout'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['R', 'JAK', 'RJ', 'IFNRJ', 'IFNRJ2', 'IFNRJ2_star', 'STAT1c', 'IFNRJ2_star_STAT1c', 'STAT1c_star', 'IFNRJ2_star_STAT1c_star', 'STAT1c_star_STAT1c_star', 'SHP2', 'IFNRJ2_star_SHP2', 'PPX', 'STAT1c_star_PPX', 'STAT1c_STAT1c_star', 'STAT1n_star_STAT1n_star', 'STAT1n_star', 'PPN', 'STAT1n_star_PPN', 'STAT1n', 'STAT1n_STAT1n_star', 'mRNAn', 'mRNAc', 'SOCS1', 'IFNRJ2_star_SOCS1', 'IFNRJ2_star_SHP2_SOCS1_STAT1c', 'STAT1c_star_STAT1c_star_PPX', 'STAT1n_star_STAT1n_star_PPN', 'IFNRJ2_star_SOCS1_STAT1c', 'IFN', 'IFNRJ2_star_SHP2_STAT1c', 'IFNRJ2_star_SHP2_SOCS1', 'IFNR']
    _SPECIES_LABELS = {'R': 'Receptor', 'JAK': 'JAK', 'RJ': 'Receptor JAK Complex', 'IFNRJ': 'Interferon Receptor JAK Complex', 'IFNRJ2': 'Ifnrj Dimer', 'IFNRJ2_star': 'Activated Ifnrj Complex', 'STAT1c': 'STAT1c', 'IFNRJ2_star_STAT1c': 'Interferon Receptor Jak2 Stat1 Complex', 'STAT1c_star': 'STAT1c_star', 'IFNRJ2_star_STAT1c_star': 'IFNRJ2_star_STAT1c_star', 'STAT1c_star_STAT1c_star': 'STAT1c_star_STAT1c_star', 'SHP2': 'SHP2', 'IFNRJ2_star_SHP2': 'IFNRJ2_star_SHP2', 'PPX': 'PPX', 'STAT1c_star_PPX': 'STAT1c_star_PPX', 'STAT1c_STAT1c_star': 'STAT1c_STAT1c_star', 'STAT1n_star_STAT1n_star': 'STAT1n_star_STAT1n_star', 'STAT1n_star': 'STAT1n_star', 'PPN': 'PPN', 'STAT1n_star_PPN': 'STAT1n_star_PPN', 'STAT1n': 'STAT1n', 'STAT1n_STAT1n_star': 'STAT1n_STAT1n_star', 'mRNAn': 'mRNAn', 'mRNAc': 'mRNAc', 'SOCS1': 'SOCS1', 'IFNRJ2_star_SOCS1': 'IFNRJ2_star_SOCS1', 'IFNRJ2_star_SHP2_SOCS1_STAT1c': 'IFNRJ2_star_SHP2_SOCS1_STAT1c', 'STAT1c_star_STAT1c_star_PPX': 'STAT1c_star_STAT1c_star_PPX', 'STAT1n_star_STAT1n_star_PPN': 'STAT1n_star_STAT1n_star_PPN', 'IFNRJ2_star_SOCS1_STAT1c': 'IFNRJ2_star_SOCS1_STAT1c', 'IFN': 'IFN', 'IFNRJ2_star_SHP2_STAT1c': 'IFNRJ2_star_SHP2_STAT1c', 'IFNRJ2_star_SHP2_SOCS1': 'IFNRJ2_star_SHP2_SOCS1', 'IFNR': 'IFNR'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_interferon_receptor_jak_complex': ('IFNRJ', 0.0, 'native source value', 'Initial Interferon Receptor JAK Complex. Sets the initial value of bundled SBML species `IFNRJ`.'), 'initial_receptor_jak_complex': ('RJ', 0.0, 'native source value', 'Initial Receptor JAK Complex. Sets the initial value of bundled SBML species `RJ`.'), 'initial_ifnrj_dimer': ('IFNRJ2', 0.0, 'native source value', 'Initial Ifnrj Dimer. Sets the initial value of bundled SBML species `IFNRJ2`.'), 'initial_activated_ifnrj_complex': ('IFNRJ2_star', 0.0, 'native source value', 'Initial Activated Ifnrj Complex. Sets the initial value of bundled SBML species `IFNRJ2_star`.'), 'initial_interferon_receptor_jak2_stat1_complex': ('IFNRJ2_star_STAT1c', 0.0, 'native source value', 'Initial Interferon Receptor Jak2 Stat1 Complex. Sets the initial value of bundled SBML species `IFNRJ2_star_STAT1c`.')}
    _HEADLINE_OUTPUTS = {'interferon_receptor_jak_complex': ('IFNRJ', 'native source value', 'Interferon Receptor JAK Complex. Maps to bundled source symbol `IFNRJ`.'), 'receptor_jak_complex': ('RJ', 'native source value', 'Receptor JAK Complex. Maps to bundled source symbol `RJ`.'), 'ifnrj_dimer': ('IFNRJ2', 'native source value', 'Ifnrj Dimer. Maps to bundled source symbol `IFNRJ2`.'), 'activated_ifnrj_complex': ('IFNRJ2_star', 'native source value', 'Activated Ifnrj Complex. Maps to bundled source symbol `IFNRJ2_star`.'), 'interferon_receptor_jak2_stat1_complex': ('IFNRJ2_star_STAT1c', 'native source value', 'Interferon Receptor Jak2 Stat1 Complex. Maps to bundled source symbol `IFNRJ2_star_STAT1c`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000094.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
