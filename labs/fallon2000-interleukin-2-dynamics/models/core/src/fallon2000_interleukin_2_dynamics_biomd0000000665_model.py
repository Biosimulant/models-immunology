# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Fallon2000 - Interleukin-2 dynamics."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Fallon2000Interleukin2DynamicsBiomd0000000665Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000665."""

    _SBML_ID = 'BIOMD0000000665'
    _TITLE = 'Fallon2000 - Interleukin-2 dynamics'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Rs_0', 'Cs_0', 'Ri_0', 'Ci_0', 'Li_0', 'Ld_0', 'L_0', 'Y_0']
    _SPECIES_LABELS = {'Rs_0': 'Rs 0', 'Cs_0': 'Cs 0', 'Ri_0': 'Ri 0', 'Ci_0': 'Ci 0', 'Li_0': 'Li 0', 'Ld_0': 'Ld', 'L_0': 'L', 'Y_0': 'Y'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_rs_0': ('Rs_0', 1500.0, 'native source value', 'Initial Rs 0. Sets the initial value of bundled SBML species `Rs_0`.'), 'initial_cs_0': ('Cs_0', 1.0, 'native source value', 'Initial Cs 0. Sets the initial value of bundled SBML species `Cs_0`.'), 'initial_ri_0': ('Ri_0', 300.0, 'native source value', 'Initial Ri 0. Sets the initial value of bundled SBML species `Ri_0`.'), 'initial_ci_0': ('Ci_0', 1.0, 'native source value', 'Initial Ci 0. Sets the initial value of bundled SBML species `Ci_0`.'), 'initial_li_0': ('Li_0', 0.01, 'native source value', 'Initial Li 0. Sets the initial value of bundled SBML species `Li_0`.')}
    _HEADLINE_OUTPUTS = {'rs_0': ('Rs_0', 'native source value', 'Rs 0. Maps to bundled source symbol `Rs_0`.'), 'cs_0': ('Cs_0', 'native source value', 'Cs 0. Maps to bundled source symbol `Cs_0`.'), 'ri_0': ('Ri_0', 'native source value', 'Ri 0. Maps to bundled source symbol `Ri_0`.'), 'ci_0': ('Ci_0', 'native source value', 'Ci 0. Maps to bundled source symbol `Ci_0`.'), 'li_0': ('Li_0', 'native source value', 'Li 0. Maps to bundled source symbol `Li_0`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000665.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
