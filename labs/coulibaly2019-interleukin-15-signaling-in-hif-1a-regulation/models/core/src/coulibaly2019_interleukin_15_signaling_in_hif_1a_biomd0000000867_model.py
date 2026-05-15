# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Coulibaly2019 - Interleukin-15 Signaling in HIF-1a Regulation in Natural Killer Cells."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Coulibaly2019Interleukin15SignalingInHif1aBiomd0000000867Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000867."""

    _SBML_ID = 'BIOMD0000000867'
    _TITLE = 'Coulibaly2019 - Interleukin-15 Signaling in HIF-1a Regulation in Natural Killer Cells'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['y1_IL_15', 'y2_Akt', 'y3_mTOR', 'y4_HIF_1a', 'y5_HIF_1b', 'y6_HIF_1_Complex', 'y7_NF_KB', 'y8_STAT3', 'y9_HIF_1a_mRNA', 'y10_HIF_1a_aOH']
    _SPECIES_LABELS = {'y1_IL_15': 'Unresolved Signaling Observable 1', 'y2_Akt': 'y2_Akt', 'y3_mTOR': 'y3_mTOR', 'y4_HIF_1a': 'Unresolved Signaling Observable 2', 'y5_HIF_1b': 'Unresolved Signaling Observable 3', 'y6_HIF_1_Complex': 'Unresolved Signaling Observable 4', 'y7_NF_KB': 'Unresolved Signaling Observable 5', 'y8_STAT3': 'y8_STAT3', 'y9_HIF_1a_mRNA': 'y9_HIF-1a_mRNA', 'y10_HIF_1a_aOH': 'y10_HIF-1a-aOH', 'IL_15_Fold_Change': 'IL-15_Fold_Change', 'HIF_1a_Total_Fold_Change': 'HIF-1a_Total_Fold_Change', 'Metabolite_9': 'Initial for y10_HIF-1a-aOH', 'Metabolite_0': 'Initial for y1_IL-15', 'Metabolite_3': 'Initial for y4_HIF-1a', 'Metabolite_5': 'Initial for y6_HIF-1_Complex'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_unresolved_signaling_observable_1': ('y1_IL_15', 1.0, 'native source value', 'Initial Unresolved Signaling Observable 1. Sets the initial value of bundled SBML species `y1_IL_15`.'), 'initial_unresolved_signaling_observable_2': ('y4_HIF_1a', 0.05, 'native source value', 'Initial Unresolved Signaling Observable 2. Sets the initial value of bundled SBML species `y4_HIF_1a`.'), 'initial_unresolved_signaling_observable_3': ('y5_HIF_1b', 1.0, 'native source value', 'Initial Unresolved Signaling Observable 3. Sets the initial value of bundled SBML species `y5_HIF_1b`.'), 'initial_unresolved_signaling_observable_4': ('y6_HIF_1_Complex', 0.05, 'native source value', 'Initial Unresolved Signaling Observable 4. Sets the initial value of bundled SBML species `y6_HIF_1_Complex`.'), 'initial_unresolved_signaling_observable_5': ('y7_NF_KB', 1.0, 'native source value', 'Initial Unresolved Signaling Observable 5. Sets the initial value of bundled SBML species `y7_NF_KB`.')}
    _HEADLINE_OUTPUTS = {'unresolved_signaling_observable_1': ('y1_IL_15', 'native source value', 'Unresolved Signaling Observable 1. Maps to bundled source symbol `y1_IL_15`.'), 'unresolved_signaling_observable_2': ('y4_HIF_1a', 'native source value', 'Unresolved Signaling Observable 2. Maps to bundled source symbol `y4_HIF_1a`.'), 'unresolved_signaling_observable_3': ('y5_HIF_1b', 'native source value', 'Unresolved Signaling Observable 3. Maps to bundled source symbol `y5_HIF_1b`.'), 'unresolved_signaling_observable_4': ('y6_HIF_1_Complex', 'native source value', 'Unresolved Signaling Observable 4. Maps to bundled source symbol `y6_HIF_1_Complex`.'), 'unresolved_signaling_observable_5': ('y7_NF_KB', 'native source value', 'Unresolved Signaling Observable 5. Maps to bundled source symbol `y7_NF_KB`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000867.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
