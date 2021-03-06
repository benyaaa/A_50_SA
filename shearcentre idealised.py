#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 14:07:16 2018

@author: Roemer
"""

from SVV_input import *
from Idealised_structure2 import *
from centroid_MOI import *



B_r_1_6 = IdealisedStructure(Q, y_cst, z_cst)[[0,1,2,3,4,5],20]
B_y_1_6 = IdealisedStructure(Q, y_cst, z_cst)[[0,1,2,3,4,5],22]
B_r_10_8 = IdealisedStructure(Q, y_cst, z_cst)[[9,8,7],20]
B_y_10_8 = IdealisedStructure(Q, y_cst, z_cst)[[9,8,7],22]



S_spse = (((pi*(h/2) / S_st) - 4) / 2) * S_st
S_sptr = S_st - S_spse

S_stsp = np.append(S_st, S_st)
S_stsp = np.append(S_stsp, S_spse)
beta_st_10_8 = np.append(BetaStringers(beta_sttr, S_st, h)[12],BetaStringers(beta_sttr, S_st, h)[14])
beta_st_10_8 = np.append(beta_st_10_8, 0.5 * pi)

CS_b_y_10_8 = np.append(CentroidStringers(st_n, beta_sttr, C_a, h, S_st)[1][12], CentroidStringers(st_n, beta_sttr, C_a, h, S_st)[1][14])
CS_b_y_10_8 = np.append(CS_b_y_10_8, h/2)

CS_b_z_10_8 = np.append(CentroidStringers(st_n, beta_sttr, C_a, h, S_st)[0][12], CentroidStringers(st_n, beta_sttr, C_a, h, S_st)[0][14])
CS_b_z_10_8 = np.append(CS_b_z_10_8, C_a-h/2)


"""def ShearCentreIdealised(B_r_1_6, B_r_10_8, B_y_1_6, B_y_10_8, MOIZZBoom, beta_st_10_8, CS_b_y_10_8, CS_b_z_10_8, q_b_1_6):
    q_b_1_6 = B_r_1_6*B_y_1_6/(MOIZZBoom(IdealisedStructure,CentroidAirfoil))
    for i in range(1,6):
        q_b_1_6[i] = q_b_1_6[i-1] + q_b_1_6[i]
    
    q_b_10_8 = B_r_10_8 * B_y_10_8 / (MOIZZBoom(IdealisedStructure,CentroidAirfoil))
    
    for j in range(3):
        q_b_10_8[j] = q_b_10_8[j-1] + q_b_10_8[j] 
    q_b_7 = q_b_10_8[2] + q_b_1_6[5]
    F_b_10_8 = q_b_10_8 * S_stsp 
    #print beta_st_10_8
    #print F_b_10_8
    F_b_y_10_8 = np.cos(beta_st_10_8) * F_b_10_8
    F_b_z_10_8 = np.sin(beta_st_10_8) * F_b_10_8
    r_b_y_10_8 = CS_b_y_10_8
    r_b_z_10_8 = CS_b_z_10_8 
    M_b_x_10_8 = 2 * np.sum(F_b_y_10_8 * r_b_z_10_8 + F_b_z_10_8 * r_b_y_10_8)
    M_b_x_spar = (C_a-(h/2)) * h * q_b_7
    M_b_x = M_b_x_10_8 - M_b_x_spar
    
    return q_b_10_8, q_b_7, q_b_1_6, M_b_x

M_b_x = ShearCentreIdealised(B_r_1_6, B_r_10_8, B_y_1_6, B_y_10_8, MOIZZBoom, beta_st_10_8, CS_b_y_10_8, CS_b_z_10_8, q_b_1_6)[3]



def equations(p, M_b_x):
    q_s01, q_s02 = p
    return (q_s01 + q_s02 + M_b_x, 1/(2*((C_a-h/2)*(h/2))) * (2*(((S_st * (q_b_1_6[0] + q_s01))/t_sk) + ((S_st * (q_b_1_6[1] + q_s01))/t_sk) + ((S_st * (q_b_1_6[2] + q_s01))/t_sk) + ((S_st * (q_b_1_6[3] + q_s01))/t_sk) + ((S_st * (q_b_1_6[4] + q_s01))/t_sk) + ((S_sptr * (q_b_1_6[5] + q_s01))/t_sk)) + ((h * (q_b_7 + q_s01))/t_sp))-1)

q_s01, q_s02 =  fsolve(equations, (1, 1),M_b_x)

print equations((q_s01, q_s02), M_b_x)

"""

q_b_1_6 = B_r_1_6*B_y_1_6/(MOIZZBoom(IdealisedStructure,CentroidAirfoil))
for i in range(1,6):
    q_b_1_6[i] = q_b_1_6[i-1] + q_b_1_6[i]

q_b_10_8 = B_r_10_8 * B_y_10_8 / (MOIZZBoom(IdealisedStructure,CentroidAirfoil))

for j in range(3):
    q_b_10_8[j] = q_b_10_8[j-1] + q_b_10_8[j] 
q_b_7 = q_b_10_8[2] + q_b_1_6[5]
F_b_10_8 = q_b_10_8 * S_stsp 
F_b_y_10_8 = np.cos(beta_st_10_8) * F_b_10_8
F_b_z_10_8 = np.sin(beta_st_10_8) * F_b_10_8
r_b_y_10_8 = CS_b_y_10_8
r_b_z_10_8 = CS_b_z_10_8 
M_b_x_10_8 = 2 * np.sum(F_b_y_10_8 * r_b_z_10_8 + F_b_z_10_8 * r_b_y_10_8)
M_b_x_spar = (C_a-(h/2)) * h * q_b_7
M_b_x = M_b_x_10_8 - M_b_x_spar







"""q_b_10_8 = ShearCentreIdealised(B_r_1_6, B_r_10_8, B_y_1_6, B_y_10_8, MOIZZBoom, beta_st_10_8, CS_b_y_10_8, CS_b_z_10_8, q_b_1_6)[0]
q_b_7 = ShearCentreIdealised(B_r_1_6, B_r_10_8, B_y_1_6, B_y_10_8, MOIZZBoom, beta_st_10_8, CS_b_y_10_8, CS_b_z_10_8, q_b_1_6)[1]
q_b_1_6 =  ShearCentreIdealised(B_r_1_6, B_r_10_8, B_y_1_6, B_y_10_8, MOIZZBoom, beta_st_10_8, CS_b_y_10_8, CS_b_z_10_8, q_b_1_6)[2]
M_b_x = ShearCentreIdealised(B_r_1_6, B_r_10_8, B_y_1_6, B_y_10_8, MOIZZBoom, beta_st_10_8, CS_b_y_10_8, CS_b_z_10_8, q_b_1_6)[3]
"""
#print q_b_7

A = np.array([[((((10 * S_st + 2 * S_sptr)/t_sk) + (h / t_sp))/((C_a-(h/2))*h))  , - ((((4 * S_st + 2 * S_spse)/t_sk) + (h / t_sp))/(pi*(h/2)**2))],[2*((C_a-h/2)*(h/2)), pi * (h/2)**2 ]])
B = np.array([[-(((2*(q_b_1_6[4] + q_b_1_6[3] + q_b_1_6[2] + q_b_1_6[1] + q_b_1_6[0]) * S_st / t_sk) + (2 * q_b_1_6[5] * S_sptr / t_sk) + q_b_7 * h / t_sp)/((C_a-(h/2))*h)) + ((2 * (((q_b_10_8[0] + q_b_10_8[1]) * S_st + q_b_10_8[2] * S_spse) / t_sk) + q_b_7 * h / t_sp)/(pi*(h/2)**2)) ], [-M_b_x]])
q_s = np.linalg.solve(A,B)

#print q_s[0]


q_1_6 = q_b_1_6 + q_s[0]
q_10_8 = q_b_10_8 + q_s[1]
q_7 = q_b_7 + q_s[0] + q_s[1]

#print q_7


F_10_8 = q_10_8 * S_stsp
F_sp = h * q_7

F_y_10_8 = np.cos(beta_st_10_8) * F_10_8
F_z_10_8 = np.sin(beta_st_10_8) * F_10_8

r_y_10_8 = CS_b_y_10_8
r_z_10_8 = CS_b_z_10_8

M_x_10_8 = F_y_10_8 * r_z_10_8 + F_z_10_8 * r_y_10_8
M_x_sp = F_sp * (C_a - (h/2))

#print F_y_10_8
#print F_z_10_8
#print F_sp
#print r_y_10_8
#print r_z_10_8
#print (C_a - (h/2))
M_x =  2 * np.sum(M_x_10_8) - M_x_sp

print M_x








