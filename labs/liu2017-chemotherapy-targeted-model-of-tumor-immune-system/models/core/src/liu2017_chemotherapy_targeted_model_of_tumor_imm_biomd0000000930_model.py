# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Liu2017 - chemotherapy targeted model of tumor immune system."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Liu2017ChemotherapyTargetedModelOfTumorImmBiomd0000000930Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000930."""

    _SBML_ID = 'BIOMD0000000930'
    _TITLE = 'Liu2017 - chemotherapy targeted model of tumor immune system'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Tumor_Cell_Population__T', 'Effector_immune_cell_population__N', 'Circulating_lymphocyte_population__C', 'Chemotherapeutic_drug_concentration__M']
    _SPECIES_LABELS = {'Tumor_Cell_Population__T': 'Tumor Cell Population T', 'Effector_immune_cell_population__N': 'Effector Immune Cell Population N', 'Circulating_lymphocyte_population__C': 'Circulating Lymphocyte Population C', 'Chemotherapeutic_drug_concentration__M': 'Chemotherapeutic Drug Concentration M'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_effector_immune_cell_population_n': ('Effector_immune_cell_population__N', 300000.0, 'native source value', 'Initial Effector Immune Cell Population N. Sets the initial value of bundled SBML species `Effector_immune_cell_population__N`.'), 'initial_tumor_cell_population_t': ('Tumor_Cell_Population__T', 10000000.0, 'native source value', 'Initial Tumor Cell Population T. Sets the initial value of bundled SBML species `Tumor_Cell_Population__T`.'), 'initial_chemotherapeutic_drug_concentration_m': ('Chemotherapeutic_drug_concentration__M', 0.45, 'native source value', 'Initial Chemotherapeutic Drug Concentration M. Sets the initial value of bundled SBML species `Chemotherapeutic_drug_concentration__M`.'), 'initial_circulating_lymphocyte_population_c': ('Circulating_lymphocyte_population__C', 62500000000.0, 'native source value', 'Initial Circulating Lymphocyte Population C. Sets the initial value of bundled SBML species `Circulating_lymphocyte_population__C`.')}
    _HEADLINE_OUTPUTS = {'effector_immune_cell_population_n': ('Effector_immune_cell_population__N', 'native source value', 'Effector Immune Cell Population N. Maps to bundled source symbol `Effector_immune_cell_population__N`.'), 'tumor_cell_population_t': ('Tumor_Cell_Population__T', 'native source value', 'Tumor Cell Population T. Maps to bundled source symbol `Tumor_Cell_Population__T`.'), 'chemotherapeutic_drug_concentration_m': ('Chemotherapeutic_drug_concentration__M', 'native source value', 'Chemotherapeutic Drug Concentration M. Maps to bundled source symbol `Chemotherapeutic_drug_concentration__M`.'), 'circulating_lymphocyte_population_c': ('Circulating_lymphocyte_population__C', 'native source value', 'Circulating Lymphocyte Population C. Maps to bundled source symbol `Circulating_lymphocyte_population__C`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000930.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
