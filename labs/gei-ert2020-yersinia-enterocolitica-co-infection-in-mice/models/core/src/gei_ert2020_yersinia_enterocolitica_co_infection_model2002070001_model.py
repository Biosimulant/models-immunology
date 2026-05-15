# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Geißert2020 - Yersinia enterocolitica co-infection in mice."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class GeiErt2020YersiniaEnterocoliticaCoInfectionModel2002070001Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL2002070001."""

    _SBML_ID = 'MODEL2002070001'
    _TITLE = 'Geißert2020 - Yersinia enterocolitica co-infection in mice'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6']
    _SPECIES_LABELS = {'x1': 'Commensal Bacteria In Mucosa', 'x2': 'Wild Type Yersinia Enterocolitica In Mucosa', 'x3': 'Mutant Yersinia Enterocolitica In Mucosa', 'x4': 'Commensal Bacteria In Lumen', 'x5': 'Wild Type Yersinia Enterocolitica In Lumen', 'x6': 'Mutant Yersnia enterocolitica in lumen', 'b1': 'Maximum growth rate of intestinal bacteria', 'b2': 'Maximum growth rate of wilt-type Yersinia enterocolitica', 'b3': 'Maximum growth rate of mutant Yersinia enterocolitica', 'b4': 'Carrying capacity of the mucosa', 'b5': 'Carrying capacity of the lumen', 'b6': 'Immunity adjustment factor for wild-type Yersinia enterocolitica', 'b7': 'Immunity adjustment factor for mutant Yersinia enterocolitica', 'b8': 'Maximum rate of immune growth', 'c1': 'Maximum immunity action', 'c2': 'Rate at which intestines are discharged', 'c3': 'Maximum capacity of the immune system', 'x7': 'Strength of immune reaction'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_wild_type_yersinia_enterocolitica_in_mucosa': ('x2', 10.0, 'item', 'Initial Wild Type Yersinia Enterocolitica In Mucosa. Sets the initial value of bundled SBML species `x2`.'), 'initial_wild_type_yersinia_enterocolitica_in_lumen': ('x5', 1000.0, 'item', 'Initial Wild Type Yersinia Enterocolitica In Lumen. Sets the initial value of bundled SBML species `x5`.')}
    _HEADLINE_OUTPUTS = {'commensal_bacteria_in_mucosa': ('x1', 'native source value', 'Commensal Bacteria In Mucosa. Maps to bundled source symbol `x1`.'), 'commensal_bacteria_in_lumen': ('x4', 'native source value', 'Commensal Bacteria In Lumen. Maps to bundled source symbol `x4`.'), 'wild_type_yersinia_enterocolitica_in_mucosa': ('x2', 'native source value', 'Wild Type Yersinia Enterocolitica In Mucosa. Maps to bundled source symbol `x2`.'), 'mutant_yersinia_enterocolitica_in_mucosa': ('x3', 'native source value', 'Mutant Yersinia Enterocolitica In Mucosa. Maps to bundled source symbol `x3`.'), 'wild_type_yersinia_enterocolitica_in_lumen': ('x5', 'native source value', 'Wild Type Yersinia Enterocolitica In Lumen. Maps to bundled source symbol `x5`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2002070001.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
