#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 09:58:26 2018

@author: maxvansplunteren and Tim
"""
from SVV_input import *
import scipy as np 
import pandas as pd


# this next part is not part of the code, only temporatily added
#=====
def CentroidStringers(st_n, beta_sttr, C_a, h, S_st): #[0]returns array with centroids z location of stringers, [1]returns array with centroids z location of stringers array[1,2,3,4,5,6,17,16,15,14,13,12,8,10,7,11,9]
   
   z_cst = S_st*cos(beta_sttr)*st_n-0.5*S_st #stiffener 1-6&12-17
   z_cst = np.append(z_cst,z_cst)
   y_cst = S_st*sin(beta_sttr)*st_n-0.5*S_st #stiffener 1-6
   y_cst = np.append(y_cst,-(S_st*sin(beta_sttr)*st_n-0.5*S_st)) #stiffener 12-17 (negative wrt 1-6)
   #semi circular part
   z_cst = np.append(z_cst, cos(S_st*2*pi/(2*pi*(h/2)))*(h/2)+C_a-(h/2))#stiffener 8&10
   z_cst = np.append(z_cst, cos(S_st*2*pi/(2*pi*(h/2)))*(h/2)+C_a-(h/2))
   y_cst = np.append(y_cst,sin(S_st*2*pi/(2*pi*(h/2)))*(h/2)) #stiffener 8
   y_cst = np.append(y_cst,-sin(S_st*2*pi/(2*pi*(h/2)))*(h/2)) #stiffener 10
   z_cst = np.append(z_cst,cos(2*S_st*2*pi/(2*pi*(h/2)))*(h/2)+C_a-(h/2)) #stiffener 7&11
   z_cst = np.append(z_cst,cos(2*S_st*2*pi/(2*pi*(h/2)))*(h/2)+C_a-(h/2))
   y_cst = np.append(y_cst,sin(2*S_st*2*pi/(2*pi*(h/2)))*(h/2)) #stiffener 7
   y_cst = np.append(y_cst,-sin(2*S_st*2*pi/(2*pi*(h/2)))*(h/2)) #stiffener 11
   z_cst = np.append(z_cst,C_a) #stiffener 9
   y_cst = np.append(y_cst,0) #stiffener 9
   return z_cst, y_cst

z_cst = CentroidStringers(st_n, beta_sttr, C_a, h, S_st)[0]
y_cst = CentroidStringers(st_n, beta_sttr, C_a, h, S_st)[1]


def BetaStringers(beta_sttr, S_st, h): #returns array with angles matching y_cst and z_cst array[1,2,3,4,5,6,17,16,15,14,13,12,8,10,7,11,9]
   beta_st = []
   for i in range(12):
       beta_st = np.append(beta_st, beta_sttr)
   beta_st = np.append(beta_st, S_st/(h/2)) #stringer 8
   beta_st = np.append(beta_st, -S_st/(h/2)) #stringer 10
   beta_st = np.append(beta_st, 2*S_st/(h/2)) #stringer 7
   beta_st = np.append(beta_st, -2*S_st/(h/2)) #stringer 11
   beta_st = np.append(beta_st, 0.5*pi) #stringer 9
   return beta_st
#=====




# for debuggin only
Q = 0


booms = (n_st+2+Q*20)

M_booms = np.zeros((booms,booms+4))

# determining connection between booms, output matrix 4 extra columns on the end. 
# [boom number /// area boom /// boom z coordinate /// boom y coorinate]
for i in range(booms-Q):
    M_booms[i][booms] = i
    M_booms[i-1][i] = 1
    try:
        M_booms[i+1][i] = 1
    except IndexError:
        M_booms[0][i] = 1


if Q != 0:
    # adding and removing the connections lost in the computation
    M_booms[booms-1-Q][0]=1
    M_booms[0][booms-1-Q]=1
    M_booms[booms-1][0]=0
    M_booms[booms-Q][booms-Q-1]=0


#Making sure spar booms are numbered correctly
N_spar_boom_top = 6 + Q * 6
N_spar_boom_bottom = 12 + Q * 12

'''
# making all z coordinates NaN, so we can interpolate them later using a function
for k in range(booms): 
    M_booms[k][-2] = np.nan
'''

#z and y coordinates for boom areas for spar boom number, 6 and 12
M_booms[N_spar_boom_top][-2] = C_a-h/2
M_booms[N_spar_boom_bottom][-2] = C_a-h/2
M_booms[N_spar_boom_top][-1] = h
M_booms[N_spar_boom_bottom][-1] = -h

#z and y coordinates for the boom areas stringer 0-5
for i in range(6):
    M_booms[i+i*Q][-2] = z_cst[i]
    
    
start = N_spar_boom_bottom + Q + 1  
index = 0
#z and y coordinates for the boom areas stringer 13-18
for i in range(11,5,-1):  
    M_booms[start+index*Q+index][-2] = z_cst[i]
    index = index + 1

#asigninig the z_coorinate of the booms. z_coordinate taken from the centroid calculation.
#stringer boom number of stringer i=i+i*Q
M_booms[7*(Q+1)][-2]=z_cst[14]
M_booms[11*(Q+1)][-2]=z_cst[15]
M_booms[8*(Q+1)][-2]=z_cst[12]
M_booms[10*(Q+1)][-2]=z_cst[13]
M_booms[9*(Q+1)][-2]=z_cst[16]





while Q != 0:
    Q_loop = 911
    if Q == 1:
        Q_loop = 1   
    if Q == 3:
        Q_loop = 2
    if Q == 7:
        Q_loop = 3
    if Q == 15:
        Q_loop = 4
    if Q == 31:
        Q_loop = 5        
    if Q == 63:
        Q_loop = 6
    else:
        break

print "Q_loop, if this is 911, you have a problem:"  
print Q_loop

for i in range(Q_loop):
    flag_Nelson = 0
    while flag_Nelson != 1:
        for j in range(len(M_booms)-Q):
            interpolated_value = (M_booms[j+j*Q][-2]+M_booms[j+1+(j+1)*Q][-2])/2
            M_booms[(j+j*Q+j+1+(j+1)*Q)/2][-2] = interpolated_value
        flag_Nelson = flag_Nelson +1
            
        
















    
    
#print M_booms





