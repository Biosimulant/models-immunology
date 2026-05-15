# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Hardiansyah2019 - QSP model of chimeric antigen receptor T-Cell therapy."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Hardiansyah2019QspModelOfChimericAntigenReModel2009230001Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL2009230001."""

    _SBML_ID = 'MODEL2009230001'
    _TITLE = 'Hardiansyah2019 - QSP model of chimeric antigen receptor T-Cell therapy'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['B_pb', 'CARTE_pb', 'IL6', 'IL10', 'IFNg', 'CARTE_t', 'CARTM_pb', 'CARTM_t']
    _SPECIES_LABELS = {'B_pb': 'Unresolved Immune Observable 1', 'CARTE_pb': 'Carte Pb', 'IL6': 'Interleukin 6', 'IL10': 'Interleukin 10', 'IFNg': 'Interferon Gamma', 'CARTE_t': 'CARTE_t', 'CARTM_pb': 'CARTM_pb', 'CARTM_t': 'CARTM_t', 'Fd_IL10': 'Fd(IL10)', 'f_B': 'f(B)', 'quantity_to_number_factor': 'quantity to number factor', 'ModelValue_26': 'Initial for UPN1'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_immune_observable_1': ('B_pb', 11000000000.0, 'native source value', 'Initial Unresolved Immune Observable 1. Sets the initial value of bundled SBML species `B_pb`.'), 'initial_carte_pb': ('CARTE_pb', 0.0, 'native source value', 'Initial Carte Pb. Sets the initial value of bundled SBML species `CARTE_pb`.'), 'initial_interleukin_6': ('IL6', 0.0, 'native source value', 'Initial Interleukin 6. Sets the initial value of bundled SBML species `IL6`.'), 'initial_interleukin_10': ('IL10', 0.0, 'native source value', 'Initial Interleukin 10. Sets the initial value of bundled SBML species `IL10`.'), 'initial_interferon_gamma': ('IFNg', 0.0, 'native source value', 'Initial Interferon Gamma. Sets the initial value of bundled SBML species `IFNg`.')}
    _HEADLINE_OUTPUTS = {'unresolved_immune_observable_1': ('B_pb', 'native source value', 'Unresolved Immune Observable 1. Maps to bundled source symbol `B_pb`.'), 'carte_pb': ('CARTE_pb', 'native source value', 'Carte Pb. Maps to bundled source symbol `CARTE_pb`.'), 'interleukin_6': ('IL6', 'native source value', 'Interleukin 6. Maps to bundled source symbol `IL6`.'), 'interleukin_10': ('IL10', 'native source value', 'Interleukin 10. Maps to bundled source symbol `IL10`.'), 'interferon_gamma': ('IFNg', 'native source value', 'Interferon Gamma. Maps to bundled source symbol `IFNg`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2009230001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
