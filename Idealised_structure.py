#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 09:58:26 2018

@author: maxvansplunteren
"""
from SVV_main import *
import scipy as np 
import pandas as pd
booms = (n_st+2+Q*19)

M_booms = np.zeros((booms,booms+4))

#determining connection between booms
for i in range(booms):
    M_booms[i][booms] = i
    M_booms[i-1][i] = 1
    try:
        M_booms[i+1][i] = 1
    except IndexError:
        M_booms[0][i] = 1
        
if Q > 0:
    Q_booms = np.zeros((Q,booms+4), dtype = M_booms.dtype)
    M_booms = np.vstack((M_booms,Q_booms))
    
    
print M_booms
