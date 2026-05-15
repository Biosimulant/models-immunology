# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Overgaard2007_PDmodel_IL21."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Overgaard2007PdmodelIl21Biomd0000000238Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000238."""

    _SBML_ID = 'BIOMD0000000238'
    _TITLE = 'Overgaard2007_PDmodel_IL21'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'rateRule'
    _OBSERVABLES = ['M', 'T', 'BR']
    _SPECIES_LABELS = {'M': 'Metabolic Rate', 'T': 'Temperature', 'BR': 'Bound Receptor', 'E_slow': 'Slow Effect', 'E_fast': 'Fast Effect', 'f_prime': 'Priming', 'T_a': 'ambient temperature', 'T_b': 'basiline temperature', 'delta_T': 'temperature difference', 'M_c': 'circadian rhythm', 'km': 'rate constant Metabolism', 'c': 'specific heat constant', 'k': 'heat conductance', 'kb': 'heat conductance baselinevalue', 'Ns': 'No. of transit compartment (slow)', 'Nf': 'No. of transit compartment (fast)', 'Ts': 'mean total delay (slow)', 'Tf': 'mena total delay (fast)'}
    _PARAMETER_INPUTS = {'rate_constant_metabolism_parameter': ('km', 1.1375, 'native source value', 'Rate Constant Metabolism Parameter. Sets bundled SBML parameter `km`.'), 'amt_dose': ('AMT_dose', 3.0, 'native source value', 'Amt Dose. Sets bundled SBML parameter `AMT_dose`.'), 'delta_high_dose': ('delta_high_dose', 1.0, 'native source value', 'Delta High Dose. Sets bundled SBML parameter `delta_high_dose`.')}
    _INITIAL_CONDITION_INPUTS = {}
    _HEADLINE_OUTPUTS = {'metabolic_rate': ('M', 'native source value', 'Metabolic Rate. Maps to bundled source symbol `M`.'), 'temperature': ('T', 'native source value', 'Temperature. Maps to bundled source symbol `T`.'), 'bound_receptor': ('BR', 'native source value', 'Bound Receptor. Maps to bundled source symbol `BR`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000238.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
