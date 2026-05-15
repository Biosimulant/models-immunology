# SPDX-FileCopyrightText: 2026-present Biosimulant Team
# SPDX-License-Identifier: Apache-2.0
"""Curated Tellurium SBML wrapper for Theinmozhi2018 - Mechanism of PD1 inhibiting TCR signaling in Tumor immune regulation."""

from __future__ import annotations

from biosim.contrib.sbml import TelluriumSBMLBioModule


class Theinmozhi2018MechanismOfPd1InhibitingTcrSBiomd0000000724Model(TelluriumSBMLBioModule):
    """Faithful BioModule wrapper around bundled SBML source BIOMD0000000724."""

    _SBML_ID = 'BIOMD0000000724'
    _TITLE = 'Theinmozhi2018 - Mechanism of PD1 inhibiting TCR signaling in Tumor immune regulation'
    _TIME_UNIT = "model_time"
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = ['LCKi', 'LCKyi', 'LCKya', 'LCKyiya', 'LCKpi', 'LCKt', 'LCKactive', 'PD1', 'PD1p1', 'PD1p2', 'CP1', 'SHP2', 'CP2', 'CPactive', 'CD28a', 'CD28i', 'PI3K', 'PI3Kb', 'CD28t', 'CD3a', 'CD3i', 'ZAP70a1', 'ZAP70i', 'ZAP70', 'ZAP70a2', 'PI3Kt', 'ZAP70t', 'LATa', 'LATi', 'LATt', 'GADS', 'SLP76', 'SLP76i', 'GADSt', 'SLP76t', 'CD3t', 'SLP76a', 'GADSa', 'LCKinactive']
    _SPECIES_LABELS = {'LCKi': 'Lcki', 'LCKyi': 'Lckyi', 'LCKya': 'Lckya', 'LCKyiya': 'Lckyiya', 'LCKpi': 'Lckpi', 'LCKt': 'LCKt', 'LCKactive': 'LCKactive', 'PD1': 'PD1', 'PD1p1': 'PD1p1', 'PD1p2': 'PD1p2', 'CP1': 'CP1', 'SHP2': 'SHP2', 'CP2': 'CP2', 'CPactive': 'CPactive', 'CD28a': 'CD28a', 'CD28i': 'CD28i', 'PI3K': 'PI3K', 'PI3Kb': 'PI3Kb', 'CD28t': 'CD28t', 'CD3a': 'CD3a', 'CD3i': 'CD3i', 'ZAP70a1': 'ZAP70a1', 'ZAP70i': 'ZAP70i', 'ZAP70': 'ZAP70', 'ZAP70a2': 'ZAP70a2', 'PI3Kt': 'PI3Kt', 'ZAP70t': 'ZAP70t', 'LATa': 'LATa', 'LATi': 'LATi', 'LATt': 'LATt', 'GADS': 'GADS', 'SLP76': 'SLP76', 'SLP76i': 'SLP76i', 'GADSt': 'GADSt', 'SLP76t': 'SLP76t', 'CD3t': 'CD3t', 'SLP76a': 'SLP76a', 'GADSa': 'GADSa', 'LCKinactive': 'LCKinactive', 'Kdpa_yiya': 'Kdpa,yiya', 'Kdpi_yi': 'Kdpi,yi', 'Kdpi_yiya': 'Kdpi,yiya', 'Kdpa_ya': 'Kdpa,ya', 'Kdpa_pi': 'Kdpa,pi', 'Kpi_i': 'Kpi,i', 'Kpi_ya': 'Kpi,ya', 'Kpa_i': 'Kpa,i', 'Kpa_yi': 'Kpa,yi', 'Kp_pd1': 'Kp,pd1', 'KMp_pd1': 'KMp,pd1', 'Ka_shp': 'Ka,shp', 'Kd1_shp': 'Kd1,shp', 'Kd2_shp': 'Kd2,shp', 'Kdp_cp2': 'Kdp,cp2', 'Kp_cd28': 'Kp,cd28', 'KMp_cd28': 'KMp,cd28', 'Kdp_cd28': 'Kdp,cd28', 'KMdp_cd28': 'KMdp,cd28', 'Ka_pi3k': 'Ka,pi3k', 'Kd_pi3k': 'Kd,pi3k', 'Kp_cd3': 'Kp,cd3', 'KMp_cd3': 'KMp,cd3', 'Kdp_cd3': 'Kdp,cd3', 'KMdp_cd3': 'KMdp,cd3', 'Ka_zap': 'Ka,zap', 'Kd_zap': 'Kd,zap', 'Kp1_zap': 'Kp1,zap', 'Kp2_zap': 'Kp2,zap', 'Kp_lat': 'Kp,lat', 'Ka_gads': 'Ka,gads', 'Kd_gads': 'Kd,gads', 'Ka_slp': 'Ka,slp', 'Kd_slp': 'Kd,slp', 'Kp_slp': 'Kp,slp', 'ModelValue_0': 'Initial for LCK_switch'}
    _PARAMETER_INPUTS = {}
    _INITIAL_CONDITION_INPUTS = {'initial_lcki': ('LCKi', 25.0, 'native source value', 'Initial Lcki. Sets the initial value of bundled SBML species `LCKi`.'), 'initial_lckyi': ('LCKyi', 25.0, 'native source value', 'Initial Lckyi. Sets the initial value of bundled SBML species `LCKyi`.'), 'initial_lckya': ('LCKya', 25.0, 'native source value', 'Initial Lckya. Sets the initial value of bundled SBML species `LCKya`.'), 'initial_lckyiya': ('LCKyiya', 25.0, 'native source value', 'Initial Lckyiya. Sets the initial value of bundled SBML species `LCKyiya`.'), 'initial_lckpi': ('LCKpi', 0.0, 'native source value', 'Initial Lckpi. Sets the initial value of bundled SBML species `LCKpi`.')}
    _HEADLINE_OUTPUTS = {'lcki': ('LCKi', 'native source value', 'Lcki. Maps to bundled source symbol `LCKi`.'), 'lckyi': ('LCKyi', 'native source value', 'Lckyi. Maps to bundled source symbol `LCKyi`.'), 'lckya': ('LCKya', 'native source value', 'Lckya. Maps to bundled source symbol `LCKya`.'), 'lckyiya': ('LCKyiya', 'native source value', 'Lckyiya. Maps to bundled source symbol `LCKyiya`.'), 'lckpi': ('LCKpi', 'native source value', 'Lckpi. Maps to bundled source symbol `LCKpi`.')}
    _STATE_OUTPUT_AS_PAYLOAD = True
    _SPECIES_LABELS_OUTPUT_AS_PAYLOAD = True
    _EXPOSE_INTEGRATION_STEP_INPUT = False

    def __init__(self, model_path: str = 'data/BIOMD0000000724.xml', integration_step: float = 0.1) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)
