# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Robertson-Tessi M 2012 A model of tumor Immune interaction."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class RobertsonTessiM2012AModelOfTumorImmuneIBiomd0000000731Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000731."""

    _SBML_ID = 'BIOMD0000000731'
    _TITLE = 'Robertson-Tessi M 2012 A model of tumor Immune interaction'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Pool', 'Tumorcells', 'Sink', 'sl_CD8_ETC', 'func_CD8_ETC', 'sl_CD4_HTC', 'func_CD4_HTC', 'sl_TRegs', 'ul_DC', 'l_DC', 'func_TRegs', 'IL2', 'TGFb', 'IL10', 'M', 'Mh', 'Me', 'Mr']
    _SPECIES_LABELS = {'Pool': 'Source', 'Tumorcells': 'Tumorcells', 'Sink': 'Sink', 'sl_CD8_ETC': 'shortlived_CD8_ETC', 'func_CD8_ETC': 'func_CD8_ETC', 'sl_CD4_HTC': 'shortlived_CD4_HTC', 'func_CD4_HTC': 'func_CD4_HTC', 'sl_TRegs': 'shortlived_TRegs', 'ul_DC': 'unlicensed_DC', 'l_DC': 'licensed_DC', 'func_TRegs': 'func_TRegs', 'IL2': 'IL2', 'TGFb': 'TGFb', 'IL10': 'IL10', 'M': 'Memtcell', 'Mh': 'Memhelpertcells', 'Me': 'Memeffectorcells', 'Mr': 'Regmemtcell', 'log_Tumor': 'log Tumor', 'log_effector': 'log effector', 'log_Treg': 'log Treg'}
    _PARAMETER_INPUTS = {'tumor_growth_rate': ('gamma', 333.0, 'unit_0', 'Tumor Growth Rate. Sets bundled SBML parameter `gamma`.'), 'tumor_cell_killing_rate': ('k2', 1.2, 'unit_1', 'Tumor Cell Killing Rate. Sets bundled SBML parameter `k2`.'), 'tumor_cell_killing_rate_2': ('k3', 11.0, 'unit_1', 'Tumor Cell Killing Rate 2. Sets bundled SBML parameter `k3`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_memtcell': ('M', 10000000.0, 'substance', 'Initial Memtcell. Sets the initial value of bundled SBML species `M`.'), 'initial_memhelpertcells': ('Mh', 6000000.0, 'substance', 'Initial Memhelpertcells. Sets the initial value of bundled SBML species `Mh`.'), 'initial_memeffectorcells': ('Me', 3000000.0, 'substance', 'Initial Memeffectorcells. Sets the initial value of bundled SBML species `Me`.'), 'initial_regmemtcell': ('Mr', 1000000.0, 'substance', 'Initial Regmemtcell. Sets the initial value of bundled SBML species `Mr`.')}
    _HEADLINE_OUTPUTS = {'memtcell': ('M', 'native source value', 'Memtcell. Maps to bundled source symbol `M`.'), 'memhelpertcells': ('Mh', 'native source value', 'Memhelpertcells. Maps to bundled source symbol `Mh`.'), 'memeffectorcells': ('Me', 'native source value', 'Memeffectorcells. Maps to bundled source symbol `Me`.'), 'regmemtcell': ('Mr', 'native source value', 'Regmemtcell. Maps to bundled source symbol `Mr`.'), 'source': ('Pool', 'native source value', 'Source. Maps to bundled source symbol `Pool`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000731.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
