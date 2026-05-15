# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Leber2016 - Host immune response - H.pylori infection."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Leber2016HostImmuneResponseHPyloriInfectioModel1611160002Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL1611160002."""

    _SBML_ID = 'MODEL1611160002'
    _TITLE = 'Leber2016 - Host immune response - H.pylori infection'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['s1', 's47', 's82', 'Total_T', 's9', 's13', 's16', 's25', 's6', 's59', 's60', 's61', 's73', 's78', 's80', 's81', 's114', 's84', 's63', 's121', 's141', 's142', 's101', 's22', 's143', 's144', 'pIL10', 'pIFNg', 's2', 's4', 's86', 's3', 's150', 's113', 's117', 's28', 's115', 's119', 's66', 's74', 's75', 's120']
    _SPECIES_LABELS = {'s1': 'Unresolved Infection Observable 1', 's47': 'Hplumdead', 's82': 'Tolb Signaling Component', 'Total_T': 'Total T', 's9': 'eDC', 's13': 'Th1', 's16': 'Th17', 's25': 'tDC', 's6': 'HP', 's59': 'HPlpdead', 's60': 'iDCdead', 's61': 'Monocytesdead', 's73': 'eDClpdead', 's78': 'Th17dead', 's80': 'Th1dead', 's81': 'Tregdead', 's114': 'iDC', 's84': 'TolB', 's63': 'M_regdead', 's121': 'tDClpdead', 's141': 'IL10', 's142': 'Interferon Gamma', 's101': 'M_reg', 's22': 'Monocytes', 's143': 'iTreg', 's144': 'Tr1', 'pIL10': 'pIL10', 'pIFNg': 'pIFNg', 's2': 'E', 's4': 'iDC', 's86': 'Edead', 's3': 'Edamaged', 's150': 'Edamageddead', 's113': 'eDC', 's117': 'tDC', 's28': 'nT', 's115': 'Th1', 's119': 'iTreg', 's66': 'nTdead', 's74': 'eDCglndead', 's75': 'tDCglndead', 's120': 'Th17'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_interferon_gamma': ('s142', 10000.0, 'native source value', 'Initial Interferon Gamma. Sets the initial value of bundled SBML species `s142`.'), 'initial_unresolved_infection_observable_1': ('s1', 100000000.0, 'native source value', 'Initial Unresolved Infection Observable 1. Sets the initial value of bundled SBML species `s1`.'), 'initial_hplumdead': ('s47', 0.0, 'native source value', 'Initial Hplumdead. Sets the initial value of bundled SBML species `s47`.'), 'initial_tolb_signaling_component': ('s82', 0.0, 'native source value', 'Initial Tolb Signaling Component. Sets the initial value of bundled SBML species `s82`.')}
    _HEADLINE_OUTPUTS = {'interferon_gamma': ('s142', 'native source value', 'Interferon Gamma. Maps to bundled source symbol `s142`.'), 'unresolved_infection_observable_1': ('s1', 'native source value', 'Unresolved Infection Observable 1. Maps to bundled source symbol `s1`.'), 'hplumdead': ('s47', 'native source value', 'Hplumdead. Maps to bundled source symbol `s47`.'), 'tolb_signaling_component': ('s82', 'native source value', 'Tolb Signaling Component. Maps to bundled source symbol `s82`.'), 'total_t': ('Total_T', 'native source value', 'Total T. Maps to bundled source symbol `Total_T`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1611160002.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
