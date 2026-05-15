# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Smith2011 - Three Stage Innate Immune Response to a Pneumococcal Lung Infection."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Smith2011ThreeStageInnateImmuneResponseToBiomd0000000924Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000924."""

    _SBML_ID = 'BIOMD0000000924'
    _TITLE = 'Smith2011 - Three Stage Innate Immune Response to a Pneumococcal Lung Infection'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['Pneumococci___P', 'Susceptible_epithelial_cells__EU', 'Epithelial_cells_with_bacteria_attached__Ea', 'proinflammatory_cytokine__C', 'Neutrophils__N', 'Debris__D']
    _SPECIES_LABELS = {'Pneumococci___P': 'Pneumococci P', 'Susceptible_epithelial_cells__EU': 'Susceptible Epithelial Cells Eu', 'Epithelial_cells_with_bacteria_attached__Ea': 'Epithelial Cells With Bacteria Attached Ea', 'proinflammatory_cytokine__C': 'Proinflammatory Cytokine C', 'Neutrophils__N': 'Neutrophils N', 'Debris__D': 'Debris (D)', 'log_Pneumococcal__P': 'log Pneumococcal (P)'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_epithelial_cells_with_bacteria_attached_ea': ('Epithelial_cells_with_bacteria_attached__Ea', 0.0, 'substance', 'Initial Epithelial Cells With Bacteria Attached Ea. Sets the initial value of bundled SBML species `Epithelial_cells_with_bacteria_attached__Ea`.'), 'initial_pneumococci_p': ('Pneumococci___P', 100000.0, 'substance', 'Initial Pneumococci P. Sets the initial value of bundled SBML species `Pneumococci___P`.'), 'initial_susceptible_epithelial_cells_eu': ('Susceptible_epithelial_cells__EU', 100000000.0, 'substance', 'Initial Susceptible Epithelial Cells Eu. Sets the initial value of bundled SBML species `Susceptible_epithelial_cells__EU`.'), 'initial_proinflammatory_cytokine_c': ('proinflammatory_cytokine__C', 0.0, 'substance', 'Initial Proinflammatory Cytokine C. Sets the initial value of bundled SBML species `proinflammatory_cytokine__C`.'), 'initial_neutrophils_n': ('Neutrophils__N', 0.0, 'substance', 'Initial Neutrophils N. Sets the initial value of bundled SBML species `Neutrophils__N`.')}
    _HEADLINE_OUTPUTS = {'epithelial_cells_with_bacteria_attached_ea': ('Epithelial_cells_with_bacteria_attached__Ea', 'native source value', 'Epithelial Cells With Bacteria Attached Ea. Maps to bundled source symbol `Epithelial_cells_with_bacteria_attached__Ea`.'), 'pneumococci_p': ('Pneumococci___P', 'native source value', 'Pneumococci P. Maps to bundled source symbol `Pneumococci___P`.'), 'susceptible_epithelial_cells_eu': ('Susceptible_epithelial_cells__EU', 'native source value', 'Susceptible Epithelial Cells Eu. Maps to bundled source symbol `Susceptible_epithelial_cells__EU`.'), 'proinflammatory_cytokine_c': ('proinflammatory_cytokine__C', 'native source value', 'Proinflammatory Cytokine C. Maps to bundled source symbol `proinflammatory_cytokine__C`.'), 'neutrophils_n': ('Neutrophils__N', 'native source value', 'Neutrophils N. Maps to bundled source symbol `Neutrophils__N`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000924.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
