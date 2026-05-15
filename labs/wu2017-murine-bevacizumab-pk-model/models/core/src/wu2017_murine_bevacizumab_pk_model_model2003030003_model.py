# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Wu2017 - Murine Bevacizumab PK model."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Wu2017MurineBevacizumabPkModelModel2003030003Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL2003030003."""

    _SBML_ID = 'MODEL2003030003'
    _TITLE = 'Wu2017 - Murine Bevacizumab PK model'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Cs_iv', 'At_iv', 'Cs_sc', 'At_sc', 'CLN_sc', 'Asc']
    _SPECIES_LABELS = {'Cs_iv': 'Cs Iv', 'At_iv': 'At Iv', 'Cs_sc': 'Cs Sc', 'At_sc': 'At Sc', 'CLN_sc': 'Cln Sc', 'Asc': 'Asc'}
    _PARAMETER_INPUTS = {'dose_iv_parameter': ('dose_iv', 0.45, 'native source value', 'Dose Iv Parameter. Sets bundled SBML parameter `dose_iv`.'), 'dose_sc_parameter': ('dose_sc', 0.45, 'native source value', 'Dose Sc Parameter. Sets bundled SBML parameter `dose_sc`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'cs_iv': ('Cs_iv', 'native source value', 'Cs Iv. Maps to bundled source symbol `Cs_iv`.'), 'at_iv': ('At_iv', 'native source value', 'At Iv. Maps to bundled source symbol `At_iv`.'), 'cs_sc': ('Cs_sc', 'native source value', 'Cs Sc. Maps to bundled source symbol `Cs_sc`.'), 'at_sc': ('At_sc', 'native source value', 'At Sc. Maps to bundled source symbol `At_sc`.'), 'cln_sc': ('CLN_sc', 'native source value', 'Cln Sc. Maps to bundled source symbol `CLN_sc`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL2003030003.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
