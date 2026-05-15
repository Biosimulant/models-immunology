# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Jarrett2015 - Modelling the interaction between immune response, bacterial dynamics and inflammatory damage."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Jarrett2015ModellingTheInteractionBetweenImBiomd0000000920Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000920."""

    _SBML_ID = 'BIOMD0000000920'
    _TITLE = 'Jarrett2015 - Modelling the interaction between immune response, bacterial dynamics and inflammatory damage'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['anti_inflammatory__A', 'inflammation__I', 'bacterial_infection__B', 'pro_inflammatory__P']
    _SPECIES_LABELS = {'anti_inflammatory__A': 'Anti Inflammatory A', 'inflammation__I': 'Inflammation I', 'bacterial_infection__B': 'Bacterial Infection B', 'pro_inflammatory__P': 'Pro Inflammatory P'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_bacterial_infection_b': ('bacterial_infection__B', 1.0, 'native source value', 'Initial Bacterial Infection B. Sets the initial value of bundled SBML species `bacterial_infection__B`.'), 'initial_anti_inflammatory_a': ('anti_inflammatory__A', 3.0, 'native source value', 'Initial Anti Inflammatory A. Sets the initial value of bundled SBML species `anti_inflammatory__A`.'), 'initial_inflammation_i': ('inflammation__I', 1.0, 'native source value', 'Initial Inflammation I. Sets the initial value of bundled SBML species `inflammation__I`.'), 'initial_pro_inflammatory_p': ('pro_inflammatory__P', 1.0, 'native source value', 'Initial Pro Inflammatory P. Sets the initial value of bundled SBML species `pro_inflammatory__P`.')}
    _HEADLINE_OUTPUTS = {'bacterial_infection_b': ('bacterial_infection__B', 'native source value', 'Bacterial Infection B. Maps to bundled source symbol `bacterial_infection__B`.'), 'anti_inflammatory_a': ('anti_inflammatory__A', 'native source value', 'Anti Inflammatory A. Maps to bundled source symbol `anti_inflammatory__A`.'), 'inflammation_i': ('inflammation__I', 'native source value', 'Inflammation I. Maps to bundled source symbol `inflammation__I`.'), 'pro_inflammatory_p': ('pro_inflammatory__P', 'native source value', 'Pro Inflammatory P. Maps to bundled source symbol `pro_inflammatory__P`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000920.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
