# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Frascoli2014 - A dynamical model of tumour immunotherapy."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Frascoli2014ADynamicalModelOfTumourImmunotBiomd0000000787Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000787."""

    _SBML_ID = 'BIOMD0000000787'
    _TITLE = 'Frascoli2014 - A dynamical model of tumour immunotherapy'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['V_Tumor_Volume', 'C_Cytotoxic_T_Lymphocytes_Coverage']
    _SPECIES_LABELS = {'V_Tumor_Volume': 'Tumor Volume', 'C_Cytotoxic_T_Lymphocytes_Coverage': 'Cytotoxic T Lymphocytes Coverage'}
    _PARAMETER_INPUTS = {'tumor_killing_cytotoxic_t_lymphocytes_rate': ('k', 0.2, 'native source value', 'Tumor Killing Cytotoxic T Lymphocytes Rate. Sets bundled SBML parameter `k`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_tumor_volume': ('V_Tumor_Volume', 1.0, 'native source value', 'Initial Tumor Volume. Sets the initial value of bundled SBML species `V_Tumor_Volume`.'), 'initial_cytotoxic_t_lymphocytes_coverage': ('C_Cytotoxic_T_Lymphocytes_Coverage', 0.1, 'native source value', 'Initial Cytotoxic T Lymphocytes Coverage. Sets the initial value of bundled SBML species `C_Cytotoxic_T_Lymphocytes_Coverage`.')}
    _HEADLINE_OUTPUTS = {'tumor_volume': ('V_Tumor_Volume', 'native source value', 'Tumor Volume. Maps to bundled source symbol `V_Tumor_Volume`.'), 'cytotoxic_t_lymphocytes_coverage': ('C_Cytotoxic_T_Lymphocytes_Coverage', 'native source value', 'Cytotoxic T Lymphocytes Coverage. Maps to bundled source symbol `C_Cytotoxic_T_Lymphocytes_Coverage`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000787.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
