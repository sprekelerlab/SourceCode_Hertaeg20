#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Appendix 2 Figure 1. 
Multi-pathway balance of excitation and inhibition in different pPE neuron circuits.
"""

# %% Import  & settings

import numpy as np
from Model_Network import Neurons, Network, Stimulation, Simulation, RunStaticNetwork, SaveNetworkPara
from Plot_NetResults import Bar_pathways, Plot_PopulationRate

import warnings
warnings.filterwarnings("ignore")
dtype = np.float32

# %% Appendix 2 Figure 1

"""
Please note:    
    To reproduce all panels of the figure, 
    vary parameter 'Panel' (see below).
"""

folder = 'Appx_2_Fig_1'

### Choose panel
Panel = 4 # [c, d, e, f] = [1, 2, 3, 4]
PanelABC = ['c', 'd', 'e', 'f']
fln = PanelABC[Panel-1]
VS, VV = np.int32(0), np.int32(1) 

### Define neuron and network parameters
if Panel==1: # c
    VE, VP, MP = 1, 1, 1
    wSV, wVS, wPP, wEP = -0.6, -0.5, -0.1, -40.0
elif Panel==2: # d
    VE, VP, MP = 1, 0, 1
    wSV, wVS, wPP, wEP = -0.6, -0.5, -0.1, -40.0
elif Panel==3: # e
    VE, VP, MP = 0, 1, 1
    wSV, wVS, wPP, wEP = -0.6, -0.5, -1.5, -40.0
elif Panel==4: # f
    VE, VP, MP = 0, 0, 1
    wSV, wVS, wPP, wEP = -0.6, -0.5, -1.5, -40.0

wPV = -(VP + abs(wSV)*MP - (1-wPP)/(-0.07*wEP) * VE) # gain = 0.07
wPS = -(abs(wVS)*abs(wPV) + (1-wSV*wVS)*MP) 

NeuPar = Neurons()
NetPar = Network(NeuPar, wPP=wPP, wPS=wPS, wPV=wPV, wEP=wEP, flag_hetero=0)

### Define input parameters
stim_max, SD = 50.0, 10.0
r0 = np.array([1,2,2,4])

StimPar = Stimulation(NeuPar, NetPar, SD, None, stim_max, r0 = r0, VE=VE, VP=VP, MP=MP, VS=VS, VV=VV)

### Define simulation parameters
SimPar = Simulation()

### Run simulation
RunStaticNetwork(NeuPar, NetPar, StimPar, SimPar, folder, fln)
SaveNetworkPara(NeuPar, NetPar, StimPar, None, folder, fln)

### Analyse & plot network
Bar_pathways(NeuPar, NetPar, VE, VP, MP, folder, fln, pPE_flag = True)
Plot_PopulationRate(NeuPar, folder, fln)
