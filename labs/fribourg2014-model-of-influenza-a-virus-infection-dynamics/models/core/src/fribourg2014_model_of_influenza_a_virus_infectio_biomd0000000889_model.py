# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Fribourg2014 - Model of influenza A virus infection dynamics of viral antagonism and innate immune response.."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Fribourg2014ModelOfInfluenzaAVirusInfectioBiomd0000000889Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000889."""

    _SBML_ID = 'BIOMD0000000889'
    _TITLE = 'Fribourg2014 - Model of influenza A virus infection dynamics of viral antagonism and innate immune response.'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['IFNBm', 'IFNBenv', 'STATP2n', 'SOCSm', 'IRF7m', 'IRF7Pn', 'IFNam', 'IFNaenv', 'TNFam', 'TFNenv', 'STATm', 'STAT']
    _SPECIES_LABELS = {'IFNBm': 'Interferon Beta mRNA', 'IFNBenv': 'Extracellular Interferon Beta', 'STATP2n': 'Nuclear Phosphorylated Stat2', 'SOCSm': 'SOCSm', 'IRF7m': 'IRF7m', 'IRF7Pn': 'IRF7Pn', 'IFNam': 'Interferon Alpha mRNA', 'IFNaenv': 'Extracellular Interferon Alpha', 'TNFam': 'TNFam', 'TFNenv': 'TFNenv', 'STATm': 'STATm', 'STAT': 'STAT'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_interferon_beta_mrna': ('IFNBm', 1.0, 'native source value', 'Initial Interferon Beta mRNA. Sets the initial value of bundled SBML species `IFNBm`.'), 'initial_extracellular_interferon_beta': ('IFNBenv', 1.0, 'native source value', 'Initial Extracellular Interferon Beta. Sets the initial value of bundled SBML species `IFNBenv`.'), 'initial_interferon_alpha_mrna': ('IFNam', 1.0, 'native source value', 'Initial Interferon Alpha mRNA. Sets the initial value of bundled SBML species `IFNam`.'), 'initial_extracellular_interferon_alpha': ('IFNaenv', 1.0, 'native source value', 'Initial Extracellular Interferon Alpha. Sets the initial value of bundled SBML species `IFNaenv`.'), 'initial_nuclear_phosphorylated_stat2': ('STATP2n', 1.0, 'native source value', 'Initial Nuclear Phosphorylated Stat2. Sets the initial value of bundled SBML species `STATP2n`.')}
    _HEADLINE_OUTPUTS = {'interferon_beta_mrna': ('IFNBm', 'native source value', 'Interferon Beta mRNA. Maps to bundled source symbol `IFNBm`.'), 'extracellular_interferon_beta': ('IFNBenv', 'native source value', 'Extracellular Interferon Beta. Maps to bundled source symbol `IFNBenv`.'), 'interferon_alpha_mrna': ('IFNam', 'native source value', 'Interferon Alpha mRNA. Maps to bundled source symbol `IFNam`.'), 'extracellular_interferon_alpha': ('IFNaenv', 'native source value', 'Extracellular Interferon Alpha. Maps to bundled source symbol `IFNaenv`.'), 'nuclear_phosphorylated_stat2': ('STATP2n', 'native source value', 'Nuclear Phosphorylated Stat2. Maps to bundled source symbol `STATP2n`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000889.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
