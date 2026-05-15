# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Webb2002 - Fas/FasL mediated tumor T-cell interaction."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Webb2002FasFaslMediatedTumorTCellInteractBiomd0000000661Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000661."""

    _SBML_ID = 'BIOMD0000000661'
    _TITLE = 'Webb2002 - Fas/FasL mediated tumor T-cell interaction'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['T', 'LT', 'RT', 'm', 'Lm', 'Rm', 'SL']
    _SPECIES_LABELS = {'T': 'T Cells T', 'LT': 'Mfasl Lt', 'RT': 'Fasr Rt', 'm': 'Tumour Cells M', 'Lm': 'Mfasl Lm', 'Rm': 'FasR (Rm)', 'SL': 'sFasL (SL)'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_t_cells_t': ('T', 500.000000000001, 'native source value', 'Initial T Cells T. Sets the initial value of bundled SBML species `T`.'), 'initial_tumour_cells_m': ('m', 500.000000000001, 'native source value', 'Initial Tumour Cells M. Sets the initial value of bundled SBML species `m`.'), 'initial_mfasl_lt': ('LT', 0.0, 'native source value', 'Initial Mfasl Lt. Sets the initial value of bundled SBML species `LT`.'), 'initial_fasr_rt': ('RT', 10000.0000000001, 'native source value', 'Initial Fasr Rt. Sets the initial value of bundled SBML species `RT`.'), 'initial_mfasl_lm': ('Lm', 1000.0, 'native source value', 'Initial Mfasl Lm. Sets the initial value of bundled SBML species `Lm`.')}
    _HEADLINE_OUTPUTS = {'t_cells_t': ('T', 'native source value', 'T Cells T. Maps to bundled source symbol `T`.'), 'tumour_cells_m': ('m', 'native source value', 'Tumour Cells M. Maps to bundled source symbol `m`.'), 'mfasl_lt': ('LT', 'native source value', 'Mfasl Lt. Maps to bundled source symbol `LT`.'), 'fasr_rt': ('RT', 'native source value', 'Fasr Rt. Maps to bundled source symbol `RT`.'), 'mfasl_lm': ('Lm', 'native source value', 'Mfasl Lm. Maps to bundled source symbol `Lm`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000661.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
