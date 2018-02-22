# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 15:08:00 2018

@author: Tim en Roemer
"""
from anal_deflection import *
from SVV_input import *
from centroid_MOI import *
from Idealised_structure2 import *

def NumericalExternalForces(CentroidAirfoil, N, matrix_max, F_H1_z, F_H1_y, P_jam, F_H2_z, F_H2_y, P, F_H3_y, C_a, h, q):
    
    matrix_zero = np.zeros([N][6])
    
    matrix_slice = hstack(matrix_max, matrix_zero)
    
    slice_number = 0
    beginning = 1
    end	= 2
    tickness	= 3
    rib_flag = 4
    hinge_flag = 5
    F_z_slice = 6
    F_y_slice = 7
    M_slice = 8
    F_z_total = 9
    F_y_total = 10
    M_total = 11
    
    rib_A_F_z = F_H1_z
    rib_A_F_y = F_H1_y
    
    rib_B_F_z = P_jam * cos(theta)
    rib_B_F_y = P_jam * sin(theta)
    
    Hinge_2_F_z = F_H2_z
    Hinge_2_F_y = F_H2_y
    
    rib_C_F_z = P * cos(theta)
    rib_C_F_y = P * sin(theta)
    
    rib_D_F_z = 0
    rib_D_F_y = F_H3_y
    
    F_R_array_z = [rib_A_F_z, rib_B_F_z, Hinge_2_F_z, rib_C_F_z, rib_D_F_z]
    F_R_array_y = [rib_A_F_y, rib_B_F_y, Hinge_2_F_y, rib_C_F_y, rib_D_F_y]
    
    u = 0
    w = 0
    Arm_act_z = C_a - CentroidAirfoil(z_cst, A_st, z_ctr, A_tr, z_cse, A_se, z_csp, A_sp, n_st)[0]
    Arm_act_y = h/2.
    Arm_hinge_z = C_a - h/2. - CentroidAirfoil(z_cst, A_st, z_ctr, A_tr, z_cse, A_se, z_csp, A_sp, n_st)[0]
    Arm_hinge_y = 0
    Arm_array_z = [Arm_hinge_z, Arm_act_z, Arm_hinge_z, Arm_act_z, Arm_hinge_z]
    Arm_array_y = [Arm_hinge_y, Arm_act_y, Arm_hinge_y, Arm_act_y, Arm_hinge_y]
    
    i = 0
    # calculating on all slices the forces produced by q (distributed force)
    for i in range(len(matrix_slice)):
        #assuming ccw positive for moments (in other words we follow a right handed coordinate system)
        matrix_slice[i][F_z_slice] = q * matrix_slice[i][thickness] * sin(theta)
        matrix_slice[i][F_y_slice] = q * matrix_slice[i][thickness] * cos(theta)
        matrix_slice[i][M_slice] = q * matrix_slice[i][thickness] * cos(theta) * ((0.75 * C_a) - CentroidAirfoil(z_cst, A_st, z_ctr, A_tr, z_cse, A_se, z_csp, A_sp, n_st)[0])
        # adding forces in the ribs and form hinge 2
        if matrix_slice[i][rib_flag] == 1 or matrix_slice[i][hinge_flag] == 1:
            matrix_slice[i][F_z_slice] = matrix_slice[i][F_z_slice] + F_R_array_z[u]  
            matrix_slice[i][M_slice] =  matrix_slice[i][M_slice] + F_R_array_z[u] * 
            u = u + 1
        if matrix_slice[i][rib_flag] == 1 or matrix_slice[i][hinge_flag] == 1:
            matrix_slice[i][F_y_slice] = matrix_slice[i][F_y_slice] + F_R_array_y[w]  
            w = w + 1

    i = 0
    for i in range(1, len(matrix_slice)):
        matrix_slice[i][F_z_total] = matrix_slice[i-1][F_z_total] + matrix_slice[i][F_z_slice]
        matrix_slice[i][F_y_total] = matrix_slice[i-1][F_y_total] + matrix_slice[i][F_y_slice]
        matrix_slice[i][M_total] = matrix_slice[i-1][M_total] + matrix_slice[i][M_slice]
    
    return matrix_slice
        
        
        

        
    






