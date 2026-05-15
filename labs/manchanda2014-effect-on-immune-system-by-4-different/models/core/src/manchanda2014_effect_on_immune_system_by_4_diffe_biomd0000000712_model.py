# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Manchanda2014 - Effect on Immune System by 4 different Influenza A virus strains."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Manchanda2014EffectOnImmuneSystemBy4DiffeBiomd0000000712Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000712."""

    _SBML_ID = 'BIOMD0000000712'
    _TITLE = 'Manchanda2014 - Effect on Immune System by 4 different Influenza A virus strains'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['P', 'D', 'I', 'S']
    _SPECIES_LABELS = {'P': 'Virus Pathogenicity P', 'D': 'Antiviral Immune Defense D', 'I': 'Inflammation I', 'S': 'Clinical Score S', 'gamma': "gamma'", 'delta': "delta'", 'omega': "omega'"}
    _PARAMETER_INPUTS = {'infection_of_virus_rate': ('alpha', 3.63, 'native source value', 'Infection Of Virus Rate. Sets bundled SBML parameter `alpha`.')}
    _INITIAL_CONDITION_INPUTS = {'initial_virus_pathogenicity_p': ('P', 0.01, 'native source value', 'Initial Virus Pathogenicity P. Sets the initial value of bundled SBML species `P`.'), 'initial_antiviral_immune_defense_d': ('D', 0.0, 'native source value', 'Initial Antiviral Immune Defense D. Sets the initial value of bundled SBML species `D`.'), 'initial_inflammation_i': ('I', 0.0, 'native source value', 'Initial Inflammation I. Sets the initial value of bundled SBML species `I`.')}
    _HEADLINE_OUTPUTS = {'virus_pathogenicity_p': ('P', 'native source value', 'Virus Pathogenicity P. Maps to bundled source symbol `P`.'), 'antiviral_immune_defense_d': ('D', 'native source value', 'Antiviral Immune Defense D. Maps to bundled source symbol `D`.'), 'inflammation_i': ('I', 'native source value', 'Inflammation I. Maps to bundled source symbol `I`.'), 'clinical_score_s': ('S', 'native source value', 'Clinical Score S. Maps to bundled source symbol `S`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000712.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
