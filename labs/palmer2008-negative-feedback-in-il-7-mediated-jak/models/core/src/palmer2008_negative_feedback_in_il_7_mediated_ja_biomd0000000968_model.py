# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Palmer2008 - Negative Feedback in IL-7 mediated Jak-Stat signaling."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Palmer2008NegativeFeedbackInIl7MediatedJaBiomd0000000968Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000968."""

    _SBML_ID = 'BIOMD0000000968'
    _TITLE = 'Palmer2008 - Negative Feedback in IL-7 mediated Jak-Stat signaling'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['IL7', 'pJAK1', 'STAT5', 'pSTAT5', 'SOCS1', 'IL7IL7RJAK1', 'IL7RJAK1', 'IL7IL7RpJAK1', 'IL7IL7RpJAK1STAT5', 'IL7IL7RpJAK1SOCS1']
    _SPECIES_LABELS = {'IL7': 'IL7', 'pJAK1': 'pJAK1', 'STAT5': 'STAT5', 'pSTAT5': 'pSTAT5', 'SOCS1': 'SOCS1', 'IL7IL7RJAK1': 'Interleukin 7 Receptor Jak1 Complex', 'IL7RJAK1': 'Interleukin 7 Receptor Jak1', 'IL7IL7RpJAK1': 'Phosphorylated Interleukin 7 Receptor Jak1 Complex', 'IL7IL7RpJAK1STAT5': 'Interleukin 7 Receptor Jak1 Stat5 Complex', 'IL7IL7RpJAK1SOCS1': 'Interleukin 7 Receptor Jak1 Socs1 Complex'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_interleukin_7_receptor_jak1_stat5_complex': ('IL7IL7RpJAK1STAT5', 0.0, 'substance', 'Initial Interleukin 7 Receptor Jak1 Stat5 Complex. Sets the initial value of bundled SBML species `IL7IL7RpJAK1STAT5`.'), 'initial_interleukin_7_receptor_jak1_complex': ('IL7IL7RJAK1', 0.0, 'substance', 'Initial Interleukin 7 Receptor Jak1 Complex. Sets the initial value of bundled SBML species `IL7IL7RJAK1`.'), 'initial_interleukin_7_receptor_jak1': ('IL7RJAK1', 1.66053904042716, 'substance', 'Initial Interleukin 7 Receptor Jak1. Sets the initial value of bundled SBML species `IL7RJAK1`.'), 'initial_phosphorylated_interleukin_7_receptor_jak1_complex': ('IL7IL7RpJAK1', 0.0, 'substance', 'Initial Phosphorylated Interleukin 7 Receptor Jak1 Complex. Sets the initial value of bundled SBML species `IL7IL7RpJAK1`.'), 'initial_interleukin_7_receptor_jak1_socs1_complex': ('IL7IL7RpJAK1SOCS1', 0.0, 'substance', 'Initial Interleukin 7 Receptor Jak1 Socs1 Complex. Sets the initial value of bundled SBML species `IL7IL7RpJAK1SOCS1`.')}
    _HEADLINE_OUTPUTS = {'interleukin_7_receptor_jak1_stat5_complex': ('IL7IL7RpJAK1STAT5', 'native source value', 'Interleukin 7 Receptor Jak1 Stat5 Complex. Maps to bundled source symbol `IL7IL7RpJAK1STAT5`.'), 'interleukin_7_receptor_jak1_complex': ('IL7IL7RJAK1', 'native source value', 'Interleukin 7 Receptor Jak1 Complex. Maps to bundled source symbol `IL7IL7RJAK1`.'), 'interleukin_7_receptor_jak1': ('IL7RJAK1', 'native source value', 'Interleukin 7 Receptor Jak1. Maps to bundled source symbol `IL7RJAK1`.'), 'phosphorylated_interleukin_7_receptor_jak1_complex': ('IL7IL7RpJAK1', 'native source value', 'Phosphorylated Interleukin 7 Receptor Jak1 Complex. Maps to bundled source symbol `IL7IL7RpJAK1`.'), 'interleukin_7_receptor_jak1_socs1_complex': ('IL7IL7RpJAK1SOCS1', 'native source value', 'Interleukin 7 Receptor Jak1 Socs1 Complex. Maps to bundled source symbol `IL7IL7RpJAK1SOCS1`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000968.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
