# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Wu2011 - Influenza-specific CD8+ T cells."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Wu2011InfluenzaSpecificCd8TCellsModel1504160000Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source MODEL1504160000."""

    _SBML_ID = 'MODEL1504160000'
    _TITLE = 'Wu2011 - Influenza-specific CD8+ T cells'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['cd8_in_spleen', 'cd8_in_lung', 'cd8_in_mln', 's6', 's7', 's8']
    _SPECIES_LABELS = {'cd8_in_spleen': 'CD8 T Cells In Spleen', 'cd8_in_lung': 'CD8 T Cells In Lung', 'cd8_in_mln': 'CD8 T Cells In Mln', 's6': 'Unresolved Infection Observable 1', 's7': 'Unresolved Infection Observable 2', 's8': 's8'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_cd8_t_cells_in_spleen': ('cd8_in_spleen', 36400.0, 'native source value', 'Initial CD8 T Cells In Spleen. Sets the initial value of bundled SBML species `cd8_in_spleen`.'), 'initial_cd8_t_cells_in_lung': ('cd8_in_lung', 1310.0, 'native source value', 'Initial CD8 T Cells In Lung. Sets the initial value of bundled SBML species `cd8_in_lung`.'), 'initial_cd8_t_cells_in_mln': ('cd8_in_mln', 3960.0, 'native source value', 'Initial CD8 T Cells In Mln. Sets the initial value of bundled SBML species `cd8_in_mln`.'), 'initial_unresolved_infection_observable_1': ('s6', 0.0, 'native source value', 'Initial Unresolved Infection Observable 1. Sets the initial value of bundled SBML species `s6`.'), 'initial_unresolved_infection_observable_2': ('s7', 0.0, 'native source value', 'Initial Unresolved Infection Observable 2. Sets the initial value of bundled SBML species `s7`.')}
    _HEADLINE_OUTPUTS = {'cd8_t_cells_in_spleen': ('cd8_in_spleen', 'native source value', 'CD8 T Cells In Spleen. Maps to bundled source symbol `cd8_in_spleen`.'), 'cd8_t_cells_in_lung': ('cd8_in_lung', 'native source value', 'CD8 T Cells In Lung. Maps to bundled source symbol `cd8_in_lung`.'), 'cd8_t_cells_in_mln': ('cd8_in_mln', 'native source value', 'CD8 T Cells In Mln. Maps to bundled source symbol `cd8_in_mln`.'), 'unresolved_infection_observable_1': ('s6', 'native source value', 'Unresolved Infection Observable 1. Maps to bundled source symbol `s6`.'), 'unresolved_infection_observable_2': ('s7', 'native source value', 'Unresolved Infection Observable 2. Maps to bundled source symbol `s7`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/MODEL1504160000.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
