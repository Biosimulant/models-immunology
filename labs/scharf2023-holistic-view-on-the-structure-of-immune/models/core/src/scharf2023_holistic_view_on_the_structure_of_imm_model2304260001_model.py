# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Scharf2023 - Holistic View on the Structure of Immune Response: Petri Net Model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Scharf2023HolisticViewOnTheStructureOfImmModel2304260001Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL2304260001."""

    _SBML_ID = 'MODEL2304260001'
    _TITLE = 'Scharf2023 - Holistic View on the Structure of Immune Response: Petri Net Model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['P3', 'P4', 'P7', 'P8', 'P137', 'P10', 'P142', 'P17', 'P21', 'P22', 'P152', 'P154', 'P29', 'P157', 'P158', 'P164', 'P38', 'P41', 'P171', 'P174', 'P47', 'P175', 'P177', 'P179', 'P53', 'P56', 'P184', 'P58', 'P60', 'P62', 'P64', 'P66', 'P68', 'P72', 'P74', 'P78', 'P86', 'P91', 'P93', 'P95', 'P97', 'P101', 'P104', 'P106', 'P109', 'P112', 'P115', 'P118', 'P125']
    _SPECIES_LABELS = {'P3': 'T Bl', 'P4': 'Unresolved Signaling Observable 1', 'P7': 'Unresolved Signaling Observable 2', 'P8': 'T Tz', 'P137': 'Unresolved Immune Observable 1', 'P10': 'B_GC', 'P142': 'S_B3_ME', 'P17': 'M_GC', 'P21': 'DC_GC', 'P22': 'B-DC_GC', 'P152': 'AG_LZ', 'P154': 'M_LZ', 'P29': 'M_TZ', 'P157': 'M-B1-AG_LZ', 'P158': 'B1_LZ', 'P164': 'S_B1_DZ', 'P38': 'B-M_GC', 'P41': 'APC_TZ', 'P171': 'M_DZ', 'P174': 'M-B1_DZ', 'P47': 'M_SCS', 'P175': 'B1_dead_DZ', 'P177': 'M-B2_TIS', 'P179': 'B2_dead_TIS', 'P53': 'AG_TIS', 'P56': 'AG_SCS', 'P184': 'B1_GC', 'P58': 'AG-M_SCS', 'P60': 'AG-M_TZ', 'P62': 'AG-APC_TZ', 'P64': 'AG-T_TZ', 'P66': 'AG-T-B_TZ', 'P68': 'AG-T-B_LZ', 'P72': 'DC-AG_LZ', 'P74': 'B1-AG_LZ', 'P78': 'T_GC', 'P86': 'B1_DZ', 'P91': 'B2_GC', 'P93': 'B2_TZ', 'P95': 'B2_ME', 'P97': 'B2_BL', 'P101': 'B2_TIS', 'P104': 'AB_TIS', 'P106': 'B2_used_TIS', 'P109': 'AG-AB_TIS', 'P112': 'M_TIS', 'P115': 'M-AG-AB_TIS', 'P118': 'AG_dead_TIS', 'P125': 'AB_used_TIS'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_t_bl': ('P3', 0.0, 'native source value', 'Initial T Bl. Sets the initial value of bundled SBML species `P3`.'), 'initial_unresolved_signaling_observable_1': ('P4', 0.0, 'native source value', 'Initial Unresolved Signaling Observable 1. Sets the initial value of bundled SBML species `P4`.'), 'initial_unresolved_signaling_observable_2': ('P7', 0.0, 'native source value', 'Initial Unresolved Signaling Observable 2. Sets the initial value of bundled SBML species `P7`.'), 'initial_t_tz': ('P8', 0.0, 'native source value', 'Initial T Tz. Sets the initial value of bundled SBML species `P8`.'), 'initial_unresolved_immune_observable_1': ('P137', 0.0, 'native source value', 'Initial Unresolved Immune Observable 1. Sets the initial value of bundled SBML species `P137`.')}
    _HEADLINE_OUTPUTS = {'t_bl': ('P3', 'native source value', 'T Bl. Maps to bundled source symbol `P3`.'), 'unresolved_signaling_observable_1': ('P4', 'native source value', 'Unresolved Signaling Observable 1. Maps to bundled source symbol `P4`.'), 'unresolved_signaling_observable_2': ('P7', 'native source value', 'Unresolved Signaling Observable 2. Maps to bundled source symbol `P7`.'), 't_tz': ('P8', 'native source value', 'T Tz. Maps to bundled source symbol `P8`.'), 'unresolved_immune_observable_1': ('P137', 'native source value', 'Unresolved Immune Observable 1. Maps to bundled source symbol `P137`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2304260001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
