# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Jarrah2014 - mathematical model of the immune response in muscle degeneration and subsequent regeneration in Duchenne muscular dystrophy in mdx mice."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Jarrah2014MathematicalModelOfTheImmuneRespBiomd0000001015Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000001015."""

    _SBML_ID = 'BIOMD0000001015'
    _TITLE = 'Jarrah2014 - mathematical model of the immune response in muscle degeneration and subsequent regeneration in Duchenne muscular dystrophy in mdx mice'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['H', 'D', 'M', 'C', 'N', 'R']
    _SPECIES_LABELS = {'H': 'CD4 T Helper Cells H', 'D': 'Damaged Fibres D', 'M': 'Macrophages M', 'C': 'CD8 Cytotoxic T Lymphocytes C', 'N': 'Normal Fibres N', 'R': 'Regenerative_fibres_(R)'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_cd4_t_helper_cells_h': ('H', 0.0, 'substance', 'Initial CD4 T Helper Cells H. Sets the initial value of bundled SBML species `H`.'), 'initial_macrophages_m': ('M', 400.0, 'substance', 'Initial Macrophages M. Sets the initial value of bundled SBML species `M`.'), 'initial_cd8_cytotoxic_t_lymphocytes_c': ('C', 4.0, 'substance', 'Initial CD8 Cytotoxic T Lymphocytes C. Sets the initial value of bundled SBML species `C`.'), 'initial_damaged_fibres_d': ('D', 0.0, 'substance', 'Initial Damaged Fibres D. Sets the initial value of bundled SBML species `D`.'), 'initial_normal_fibres_n': ('N', 100.0, 'substance', 'Initial Normal Fibres N. Sets the initial value of bundled SBML species `N`.')}
    _HEADLINE_OUTPUTS = {'cd4_t_helper_cells_h': ('H', 'native source value', 'CD4 T Helper Cells H. Maps to bundled source symbol `H`.'), 'macrophages_m': ('M', 'native source value', 'Macrophages M. Maps to bundled source symbol `M`.'), 'cd8_cytotoxic_t_lymphocytes_c': ('C', 'native source value', 'CD8 Cytotoxic T Lymphocytes C. Maps to bundled source symbol `C`.'), 'damaged_fibres_d': ('D', 'native source value', 'Damaged Fibres D. Maps to bundled source symbol `D`.'), 'normal_fibres_n': ('N', 'native source value', 'Normal Fibres N. Maps to bundled source symbol `N`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000001015.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
