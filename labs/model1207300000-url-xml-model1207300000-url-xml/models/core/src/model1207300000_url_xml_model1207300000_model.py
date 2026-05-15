# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for MODEL1207300000_url.xml."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Model1207300000UrlXmlModel1207300000Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL1207300000."""

    _SBML_ID = 'MODEL1207300000'
    _TITLE = 'MODEL1207300000_url.xml'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14', 's15', 's16', 's17', 's18', 's19', 's20', 's21', 's22', 's23', 's24', 's25', 's26', 's27', 's28', 's29', 's30', 's31', 's32', 's33', 's34', 's35', 's36', 's37', 's38', 's39', 's40', 's41', 's45', 's46', 's47', 's48', 's49', 's50', 's51', 's52', 's53', 's54', 's55', 's56', 's57', 's58', 's59', 's60', 's61', 's62', 's63', 's64', 's65', 's66', 's67']
    _SPECIES_LABELS = {'s1': 'Acoa', 's2': 'Hmg Coa', 's3': 'Unresolved Signaling Observable 1', 's4': 'Unresolved Signaling Observable 1 2', 's5': 'Unresolved Signaling Observable 2', 's6': 'IsPP', 's7': 'FPP', 's8': 'Squa', 's9': '23Ox', 's10': 'Lan', 's11': '44Di', 's12': '14De', 's13': '4MZC', 's14': '3K4M', 's15': '4MZ', 's16': 'Zym', 's17': 'Cho8', 's18': 'Cho7', 's19': 'Lath', 's20': '7DeC', 's21': 'Chol', 's22': '7DeD', 's23': 'Des', 's24': 'HMGCS', 's25': 'HMGCR', 's26': 'MVK', 's27': 'PMVK', 's28': 'MVD', 's29': 'FDPS', 's30': 'FDFT1', 's31': 'SQLE', 's32': 'LSS', 's33': 'CYP51A1', 's34': 'TM7SF2', 's35': 'SC4MOL', 's36': 'NSDHL', 's37': 'HSD17B7', 's38': 'DHCR24', 's39': 'EBP', 's40': 'SC5DL', 's41': 'DHCR7', 's45': 's45', 's46': 's46', 's47': 's47', 's48': 's48', 's49': 's49', 's50': 's50', 's51': 's51', 's52': 's52', 's53': 's53', 's54': 's54', 's55': 's55', 's56': 's56', 's57': 's57', 's58': 's58', 's59': 's59', 's60': 's60', 's61': 's61', 's62': 's62', 's63': 's63', 's64': 's64', 's65': 's65', 's66': 's66', 's67': 's67'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_acoa': ('s1', 0.0, 'native source value', 'Initial Acoa. Sets the initial value of bundled SBML species `s1`.'), 'initial_hmg_coa': ('s2', 0.0, 'native source value', 'Initial Hmg Coa. Sets the initial value of bundled SBML species `s2`.'), 'initial_unresolved_signaling_observable_1': ('s3', 0.0, 'native source value', 'Initial Unresolved Signaling Observable 1. Sets the initial value of bundled SBML species `s3`.'), 'initial_unresolved_signaling_observable_1_2': ('s4', 0.0, 'native source value', 'Initial Unresolved Signaling Observable 1 2. Sets the initial value of bundled SBML species `s4`.'), 'initial_unresolved_signaling_observable_2': ('s5', 0.0, 'native source value', 'Initial Unresolved Signaling Observable 2. Sets the initial value of bundled SBML species `s5`.')}
    _HEADLINE_OUTPUTS = {'acoa': ('s1', 'native source value', 'Acoa. Maps to bundled source symbol `s1`.'), 'hmg_coa': ('s2', 'native source value', 'Hmg Coa. Maps to bundled source symbol `s2`.'), 'unresolved_signaling_observable_1': ('s3', 'native source value', 'Unresolved Signaling Observable 1. Maps to bundled source symbol `s3`.'), 'unresolved_signaling_observable_1_2': ('s4', 'native source value', 'Unresolved Signaling Observable 1 2. Maps to bundled source symbol `s4`.'), 'unresolved_signaling_observable_2': ('s5', 'native source value', 'Unresolved Signaling Observable 2. Maps to bundled source symbol `s5`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1207300000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
