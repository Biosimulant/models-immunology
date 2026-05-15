# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Miao2014 - Dynamics and migratory pathways of virus-specific antibody-secreting cell populations."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Miao2014DynamicsAndMigratoryPathwaysOfViruModel1411130000Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL1411130000."""

    _SBML_ID = 'MODEL1411130000'
    _TITLE = 'Miao2014 - Dynamics and migratory pathways of virus-specific antibody-secreting cell populations'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8']
    _SPECIES_LABELS = {'s1': 'Cell Spleen', 's2': 'Cell Mln', 's3': 'Cell Lung', 's4': 'Unresolved Infection Observable 1', 's5': 'Unresolved Infection Observable 2', 's6': 's6', 's7': 's7', 's8': 's8'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_cell_spleen': ('s1', 3400.0, 'native source value', 'Initial Cell Spleen. Sets the initial value of bundled SBML species `s1`.'), 'initial_cell_mln': ('s2', 1100.0, 'native source value', 'Initial Cell Mln. Sets the initial value of bundled SBML species `s2`.'), 'initial_cell_lung': ('s3', 18.0, 'native source value', 'Initial Cell Lung. Sets the initial value of bundled SBML species `s3`.'), 'initial_unresolved_infection_observable_1': ('s4', 0.0, 'native source value', 'Initial Unresolved Infection Observable 1. Sets the initial value of bundled SBML species `s4`.'), 'initial_unresolved_infection_observable_2': ('s5', 0.0, 'native source value', 'Initial Unresolved Infection Observable 2. Sets the initial value of bundled SBML species `s5`.')}
    _HEADLINE_OUTPUTS = {'cell_spleen': ('s1', 'native source value', 'Cell Spleen. Maps to bundled source symbol `s1`.'), 'cell_mln': ('s2', 'native source value', 'Cell Mln. Maps to bundled source symbol `s2`.'), 'cell_lung': ('s3', 'native source value', 'Cell Lung. Maps to bundled source symbol `s3`.'), 'unresolved_infection_observable_1': ('s4', 'native source value', 'Unresolved Infection Observable 1. Maps to bundled source symbol `s4`.'), 'unresolved_infection_observable_2': ('s5', 'native source value', 'Unresolved Infection Observable 2. Maps to bundled source symbol `s5`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1411130000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
