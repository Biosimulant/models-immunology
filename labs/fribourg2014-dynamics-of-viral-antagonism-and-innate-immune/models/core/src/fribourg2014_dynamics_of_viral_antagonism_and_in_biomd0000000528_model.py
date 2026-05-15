# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Fribourg2014 - Dynamics of viral antagonism and innate immune response (H1N1 influenza A virus - Cal/09)."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Fribourg2014DynamicsOfViralAntagonismAndInBiomd0000000528Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000528."""

    _SBML_ID = 'BIOMD0000000528'
    _TITLE = 'Fribourg2014 - Dynamics of viral antagonism and innate immune response (H1N1 influenza A virus - Cal/09)'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['w', 'IFNb_mRNA', 'IFNb_env', 'STATP2n', 'SOCS1m', 'IRF7m', 'IRF7Pn', 'IFNa_mRNA', 'IFNa_env', 'TNFam', 'TNFenv', 'STATm', 'STAT']
    _SPECIES_LABELS = {'w': 'Unresolved Infection Observable 1', 'IFNb_mRNA': 'Interferon Beta mRNA', 'IFNb_env': 'Interferon Beta Env', 'STATP2n': 'STATP2n', 'SOCS1m': 'SOCS1m', 'IRF7m': 'IRF7m', 'IRF7Pn': 'IRF7Pn', 'IFNa_mRNA': 'Interferon Alpha mRNA', 'IFNa_env': 'Interferon Alpha Env', 'TNFam': 'TNFam', 'TNFenv': 'TNFenv', 'STATm': 'STATm', 'STAT': 'STAT'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_interferon_beta_mrna': ('IFNb_mRNA', 0.0, 'native source value', 'Initial Interferon Beta mRNA. Sets the initial value of bundled SBML species `IFNb_mRNA`.'), 'initial_interferon_beta_env': ('IFNb_env', 0.0, 'native source value', 'Initial Interferon Beta Env. Sets the initial value of bundled SBML species `IFNb_env`.'), 'initial_interferon_alpha_mrna': ('IFNa_mRNA', 0.0, 'native source value', 'Initial Interferon Alpha mRNA. Sets the initial value of bundled SBML species `IFNa_mRNA`.'), 'initial_interferon_alpha_env': ('IFNa_env', 0.0, 'native source value', 'Initial Interferon Alpha Env. Sets the initial value of bundled SBML species `IFNa_env`.')}
    _HEADLINE_OUTPUTS = {'interferon_beta_mrna': ('IFNb_mRNA', 'native source value', 'Interferon Beta mRNA. Maps to bundled source symbol `IFNb_mRNA`.'), 'interferon_beta_env': ('IFNb_env', 'native source value', 'Interferon Beta Env. Maps to bundled source symbol `IFNb_env`.'), 'interferon_alpha_mrna': ('IFNa_mRNA', 'native source value', 'Interferon Alpha mRNA. Maps to bundled source symbol `IFNa_mRNA`.'), 'interferon_alpha_env': ('IFNa_env', 'native source value', 'Interferon Alpha Env. Maps to bundled source symbol `IFNa_env`.'), 'unresolved_infection_observable_1': ('w', 'native source value', 'Unresolved Infection Observable 1. Maps to bundled source symbol `w`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000528.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
