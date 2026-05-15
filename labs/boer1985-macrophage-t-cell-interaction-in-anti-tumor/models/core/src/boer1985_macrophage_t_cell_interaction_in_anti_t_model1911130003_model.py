# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Boer1985 - Macrophage T cell interaction in anti-tumor response."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Boer1985MacrophageTCellInteractionInAntiTModel1911130003Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL1911130003."""

    _SBML_ID = 'MODEL1911130003'
    _TITLE = 'Boer1985 - Macrophage T cell interaction in anti-tumor response'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['CTLP', 'CTL', 'Tumor', 'HTLP', 'HTL', 'MPH', 'Angry', 'Debris', 'PCTLP', 'IL1']
    _SPECIES_LABELS = {'CTLP': 'Cytotoxic T Lymphocyte Precursors', 'CTL': 'Cytotoxic T Lymphocytes', 'Tumor': 'Tumor', 'HTLP': 'Helper T Lymphocyte Precursors', 'HTL': 'Helper T Lymphocytes', 'MPH': 'MPH', 'Angry': 'Angry', 'Debris': 'Debris', 'PCTLP': 'PCTLP', 'IL1': 'IL1', 'ModelValue_6': 'Initial for H', 'ModelValue_1': 'Initial for KMD', 'ModelValue_3': 'Initial for KMF', 'ModelValue_2': 'Initial for KMT'}
    _PARAMETER_INPUTS = {'kill_parameter': ('Kill', 10.0, 'native source value', 'Kill Parameter. Sets bundled SBML parameter `Kill`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_tumor': ('Tumor', 0.0, 'native source value', 'Initial Tumor. Sets the initial value of bundled SBML species `Tumor`.'), 'initial_cytotoxic_t_lymphocyte_precursors': ('CTLP', 25.0, 'native source value', 'Initial Cytotoxic T Lymphocyte Precursors. Sets the initial value of bundled SBML species `CTLP`.'), 'initial_cytotoxic_t_lymphocytes': ('CTL', 0.0, 'native source value', 'Initial Cytotoxic T Lymphocytes. Sets the initial value of bundled SBML species `CTL`.'), 'initial_helper_t_lymphocyte_precursors': ('HTLP', 15.0, 'native source value', 'Initial Helper T Lymphocyte Precursors. Sets the initial value of bundled SBML species `HTLP`.'), 'initial_helper_t_lymphocytes': ('HTL', 0.0, 'native source value', 'Initial Helper T Lymphocytes. Sets the initial value of bundled SBML species `HTL`.')}
    _HEADLINE_OUTPUTS = {'tumor': ('Tumor', 'native source value', 'Tumor. Maps to bundled source symbol `Tumor`.'), 'cytotoxic_t_lymphocyte_precursors': ('CTLP', 'native source value', 'Cytotoxic T Lymphocyte Precursors. Maps to bundled source symbol `CTLP`.'), 'cytotoxic_t_lymphocytes': ('CTL', 'native source value', 'Cytotoxic T Lymphocytes. Maps to bundled source symbol `CTL`.'), 'helper_t_lymphocyte_precursors': ('HTLP', 'native source value', 'Helper T Lymphocyte Precursors. Maps to bundled source symbol `HTLP`.'), 'helper_t_lymphocytes': ('HTL', 'native source value', 'Helper T Lymphocytes. Maps to bundled source symbol `HTL`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1911130003.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
