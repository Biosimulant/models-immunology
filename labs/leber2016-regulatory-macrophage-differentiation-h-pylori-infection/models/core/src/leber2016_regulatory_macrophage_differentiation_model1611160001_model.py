# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Leber2016 - Regulatory macrophage differentiation - H.pylori infection."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Leber2016RegulatoryMacrophageDifferentiationModel1611160001Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL1611160001."""

    _SBML_ID = 'MODEL1611160001'
    _TITLE = 'Leber2016 - Regulatory macrophage differentiation - H.pylori infection'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14', 's15', 's16', 's17', 's19', 's20', 's21', 's22', 's23', 's24', 's25', 'pAkt', 'eCa2', 'iCa2', 'pCREB', 'pCX3CR1', 'pERK', 'pFbxo7', 'pFOXP1', 'pIL10', 'pLANCL2', 'pM_CSF', 'pNCOR2', 'pNFAT', 'pNFkB', 'pPKA', 'pTraf2', 'pIL10R', 'pCSF1R', 'Mono', 'KLF4', 'pKLF4', 'CX3CL1', 'pCX3CL1', 'IFNg', 'pIFNg']
    _SPECIES_LABELS = {'s1': 'Cx3cr1 Receptor', 's2': 'Unresolved Infection Observable 1', 's3': 'ERK', 's4': 'Unresolved Infection Observable 2', 's5': 'Unresolved Infection Observable 3', 's6': 'cAMP', 's7': 'PKA', 's8': 'CREB', 's9': 'IL10', 's10': 'IL10R', 's11': 'Akt', 's12': 'M-CSF', 's13': 'CSF1R', 's14': 'SIRPb1', 's15': 'NFAT', 's16': 'LANCL2', 's17': 'Mreg', 's19': 'HP', 's20': 'Traf2', 's21': 'Fbxo7', 's22': 'NCOR2', 's23': 'FOXP1', 's24': 'NFkB', 's25': 'ABA', 'pAkt': 'pAkt', 'eCa2': 'eCa2+', 'iCa2': 'iCa2+', 'pCREB': 'pCREB', 'pCX3CR1': 'pCX3CR1', 'pERK': 'pERK', 'pFbxo7': 'pFbxo7', 'pFOXP1': 'pFOXP1', 'pIL10': 'pIL10', 'pLANCL2': 'pLANCL2', 'pM_CSF': 'pM-CSF', 'pNCOR2': 'pNCOR2', 'pNFAT': 'pNFAT', 'pNFkB': 'pNFkB', 'pPKA': 'pPKA', 'pTraf2': 'pTraf2', 'pIL10R': 'pIL10R', 'pCSF1R': 'pCSF1R', 'Mono': 'Mono', 'KLF4': 'KLF4', 'pKLF4': 'pKLF4', 'CX3CL1': 'CX3CL1', 'pCX3CL1': 'pCX3CL1', 'IFNg': 'IFNg', 'pIFNg': 'pIFNg'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_cx3cr1_receptor': ('s1', 0.0, 'native source value', 'Initial Cx3cr1 Receptor. Sets the initial value of bundled SBML species `s1`.'), 'initial_unresolved_infection_observable_1': ('s2', 0.0, 'native source value', 'Initial Unresolved Infection Observable 1. Sets the initial value of bundled SBML species `s2`.'), 'initial_erk': ('s3', 0.0, 'native source value', 'Initial ERK. Sets the initial value of bundled SBML species `s3`.'), 'initial_unresolved_infection_observable_2': ('s4', 0.0, 'native source value', 'Initial Unresolved Infection Observable 2. Sets the initial value of bundled SBML species `s4`.')}
    _HEADLINE_OUTPUTS = {'cx3cr1_receptor': ('s1', 'native source value', 'Cx3cr1 Receptor. Maps to bundled source symbol `s1`.'), 'unresolved_infection_observable_1': ('s2', 'native source value', 'Unresolved Infection Observable 1. Maps to bundled source symbol `s2`.'), 'erk': ('s3', 'native source value', 'ERK. Maps to bundled source symbol `s3`.'), 'unresolved_infection_observable_2': ('s4', 'native source value', 'Unresolved Infection Observable 2. Maps to bundled source symbol `s4`.'), 'unresolved_infection_observable_3': ('s5', 'native source value', 'Unresolved Infection Observable 3. Maps to bundled source symbol `s5`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1611160001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
