# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Maier2022 - Stochastic Dynamics of Type I Interferon Responses."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Maier2022StochasticDynamicsOfTypeIInterferModel2210070001Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL2210070001."""

    _SBML_ID = 'MODEL2210070001'
    _TITLE = 'Maier2022 - Stochastic Dynamics of Type I Interferon Responses'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['IFN', 'R2', 'RC', 'AR', 'R1', 'STAT1_c', 'pSTAT1', 'STAT2_c', 'pSTAT2', 'dimerSTAT', 'IRF9_c', 'STAT2_IRF9_c', 'ISGF3_c', 'ISGF3_n', 'STAT2_IRF9_n', 'I_irf9', 'irf9', 'I_mxa', 'mxa', 'I_ifit1', 'ifit1', 'I_socs', 'socs', 'irf9_0', 'socs_0', 'mxa_0', 'ifit1_0', 'mIRF9_n', 'mSOCS_n', 'mMXA_n', 'mIFIT1_n', 'mIRF9_c', 'mSOCS_c', 'mMXA_c', 'mIFIT1_c', 'SOCS', 'MXA', 'IFIT1', 'IRF9_n', 'STAT1_n', 'STAT2_n', 'IR', 'MXA_0', 'IFIT1_0']
    _SPECIES_LABELS = {'IFN': 'Interferon', 'R2': 'R2', 'RC': 'RC', 'AR': 'AR', 'R1': 'R1', 'STAT1_c': 'Cytosolic Stat1', 'pSTAT1': 'Pstat1', 'STAT2_c': 'STAT2_c', 'pSTAT2': 'pSTAT2', 'dimerSTAT': 'dimerSTAT', 'IRF9_c': 'IRF9_c', 'STAT2_IRF9_c': 'Cytosolic Stat2 Irf9 Complex', 'ISGF3_c': 'ISGF3_c', 'ISGF3_n': 'ISGF3_n', 'STAT2_IRF9_n': 'Nuclear Stat2 Irf9 Complex', 'I_irf9': 'I_irf9', 'irf9': 'irf9', 'I_mxa': 'I_mxa', 'mxa': 'mxa', 'I_ifit1': 'I_ifit1', 'ifit1': 'ifit1', 'I_socs': 'I_socs', 'socs': 'socs', 'irf9_0': 'irf9*', 'socs_0': 'socs*', 'mxa_0': 'mxa*', 'ifit1_0': 'ifit1*', 'mIRF9_n': 'mIRF9_n', 'mSOCS_n': 'mSOCS_n', 'mMXA_n': 'mMXA_n', 'mIFIT1_n': 'mIFIT1_n', 'mIRF9_c': 'mIRF9_c', 'mSOCS_c': 'mSOCS_c', 'mMXA_c': 'mMXA_c', 'mIFIT1_c': 'mIFIT1_c', 'SOCS': 'SOCS', 'MXA': 'MXA', 'IFIT1': 'IFIT1', 'IRF9_n': 'IRF9_n', 'STAT1_n': 'STAT1_n', 'STAT2_n': 'STAT2_n', 'IR': 'IR', 'MXA_0': 'MXA_0', 'IFIT1_0': 'IFIT1_0', 'k__11_1': 'k__11.1', 'k__11_2': 'k__11.2', 'k__13_1': 'k__13.1', 'k__13_2': 'k__13.2', 'k__15_1': 'k__15.1', 'k__15_2': 'k__15.2', 'k__17_1': 'k__17.1', 'k__17_2': 'k__17.2', 'k__19_1': 'k__19.1', 'k__19_2': 'k__19.2', 'k__28__fixed': 'k__28 (fixed)', 'k__29__fixed': 'k__29 (fixed)', 'k__30_fixed': 'k__30(fixed)', 'k__31_fixed': 'k__31(fixed)', 'k__37__fixed': 'k__37 (fixed)', 'k__38_fixed': 'k__38(fixed)', 'k__39_fixed': 'k__39(fixed)', 'k__40__fixed': 'k__40 (fixed)', 'k__46__fixed': 'k__46 (fixed)'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_cytosolic_stat2_irf9_complex': ('STAT2_IRF9_c', 231.21387283237, 'native source value', 'Initial Cytosolic Stat2 Irf9 Complex. Sets the initial value of bundled SBML species `STAT2_IRF9_c`.'), 'initial_nuclear_stat2_irf9_complex': ('STAT2_IRF9_n', 2407.40740740741, 'native source value', 'Initial Nuclear Stat2 Irf9 Complex. Sets the initial value of bundled SBML species `STAT2_IRF9_n`.'), 'initial_interferon': ('IFN', 11560.6936416185, 'native source value', 'Initial Interferon. Sets the initial value of bundled SBML species `IFN`.'), 'initial_cytosolic_stat1': ('STAT1_c', 983430.057803468, 'native source value', 'Initial Cytosolic Stat1. Sets the initial value of bundled SBML species `STAT1_c`.'), 'initial_pstat1': ('pSTAT1', 0.0, 'native source value', 'Initial Pstat1. Sets the initial value of bundled SBML species `pSTAT1`.')}
    _HEADLINE_OUTPUTS = {'cytosolic_stat2_irf9_complex': ('STAT2_IRF9_c', 'native source value', 'Cytosolic Stat2 Irf9 Complex. Maps to bundled source symbol `STAT2_IRF9_c`.'), 'nuclear_stat2_irf9_complex': ('STAT2_IRF9_n', 'native source value', 'Nuclear Stat2 Irf9 Complex. Maps to bundled source symbol `STAT2_IRF9_n`.'), 'interferon': ('IFN', 'native source value', 'Interferon. Maps to bundled source symbol `IFN`.'), 'cytosolic_stat1': ('STAT1_c', 'native source value', 'Cytosolic Stat1. Maps to bundled source symbol `STAT1_c`.'), 'pstat1': ('pSTAT1', 'native source value', 'Pstat1. Maps to bundled source symbol `pSTAT1`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2210070001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
