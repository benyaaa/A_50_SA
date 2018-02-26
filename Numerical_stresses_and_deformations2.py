# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 11:50:32 2018

@author: Tim and Max
"""
import SVV_input
from anal_deflection import *
from centroid_MOI import *
from Idealised_structure2 import *
from Slicing import *
import matplotlib.pyplot as plt
from anal_deflection import *


#matrix[row][column]

def Numerical_stresses_and_deformations2(zzy, M_booms, E, MOIYYBoom_value, MOIZZBoom_value, MOIZZBoom, MOIYYBoom, CentroidAirfoil):
    # defining names of the rows of the matrix matrix_nsad
    z_deformation_due_to_bending	=	0
    y_deformation_due_to_bending	=	1
    x_co_undeformed	=	2
    y_co_undeformed	=	3
    z_co_undeformed	=	4
    x_co_deformed	=	5
    y_co_deformed	=	6
    z_co_deformed	=	7
    z_deformation_due_to_shear_flow = 9 
    y_deformation_due_to_shear_flow = 10
    shear_flow = 11
    



    
    #defining the names of the columns of the matrix: matrix zzy
    slice_number=-14
    begining=-13
    end=-12
    tickness=-11
    rib_flag=-10
    hinge_flag=-9 
    F_z_slice=-8
    F_y_slice=-7
    M_slice=-6
    F_z_total=-5
    F_y_total=-4
    T_total=-3
    Bending_moment_z=-2
    Bending_moment_y=-1

    # defining the names of the columns of the matrix: M_booms
    boom_number=-4
    area_boom =-3
    z_coordinate_boom=-2
    y_coordinate_boom=-1

    
    nslice = zzy.shape[0]
    nboom = M_booms.shape[0]
    
    # initializing matrix in 3 dimensions
    matrix_nsad = np.zeros((12, nslice, nboom))
    
    
    MOIZZBoom = MOIZZBoom(IdealisedStructure,CentroidAirfoil)
    MOIYYBoom = MOIYYBoom(IdealisedStructure,CentroidAirfoil)

    # for debugging correct once shear center is known
    z_coordinate_shear_center = CentroidAirfoil(z_cst, A_st, z_ctr, A_tr, z_cse, A_se, z_csp, A_sp, n_st)[0]




    for the_slice in range(0, nslice):
        for the_boom in range(0, nboom):
            
            #filling in the x, y and z coordinates of every boom
            #taking the middle of the slice as the x-coordinate
            matrix_nsad[x_co_undeformed][the_slice][the_boom] = ((zzy[the_slice][end] + zzy[the_slice][begining]))/2
            matrix_nsad[y_co_undeformed][the_slice][the_boom] = M_booms[the_boom][y_coordinate_boom]
            matrix_nsad[z_co_undeformed][the_slice][the_boom] = M_booms[the_boom][z_coordinate_boom]
            
            
            # calculating deflections due to bending
            x = matrix_nsad[x_co_undeformed][the_slice][the_boom]
            if x >= 0 and x <= x_1:
                v = (-1./24.)*(q*cos(theta))*x**4 + C*x + L
            elif x > x_1 and x <= (x_2-(x_a/2.)):
                v = (-1./24.)*(q*cos(theta))*x**4 + (1./6.)*F_H1_y*(x-x_1)**3 + C*x + L
            elif x > (x_2-(x_a/2.)) and x <= x_2:
                v = (-1./24.)*(q*cos(theta))*x**4 + (1./6.)*F_H1_y*(x-x_1)**3 + (1./6.)*P_jam*sin(theta)*(x-(x_2-(x_a/2.)))**3 + C*x + L
            elif x > x_2 and x <= (x_2+(x_a/2.)):
                v = (-1./24.)*(q*cos(theta))*x**4 + (1./6.)*F_H1_y*(x-x_1)**3 + (1./6.)*P_jam*sin(theta)*(x-(x_2-(x_a/2.)))**3 + (1./6.)*F_H2_y*(x-x_2)**3 + C*x +L
            elif x > (x_2+(x_a/2.)) and x <= x_3:
                v = (-1./24.)*(q*cos(theta))*x**4 + (1./6.)*F_H1_y*(x-x_1)**3 + (1./6.)*P_jam*sin(theta)*(x-(x_2-(x_a/2.)))**3 + (1./6.)*F_H2_y*(x-x_2)**3 - (1./6.)*P*sin(theta)*(x-(x_2+(x_a/2.)))**3 + C*x + L
            elif x > x_3 and x <= l_a:
                v = (-1./24.)*(q*cos(theta))*x**4 + (1./6.)*F_H1_y*(x-x_1)**3 + (1./6.)*P_jam*sin(theta)*(x-(x_2-(x_a/2.)))**3 + (1./6.)*F_H2_y*(x-x_2)**3 - (1./6.)*P*sin(theta)*(x-(x_2+(x_a/2.)))**3 + 1./2.*F_H3_y*(x-x_3)**3 + C*x + L        
            
            matrix_nsad[y_deformation_due_to_bending][the_slice][the_boom] = v/(E*MOIZZBoom_value)

            
            
            
            
            
            
            # calculating deformation due to shear
            # torsion: ccw positive
            #finding constant shear flows
            # calculating skin lenghts:
            l_skin = (((C_a-(h/2.))**2.)+((h/2.)**2.))**0.5
            a_1 = (h/2.) * (C_a - (h/2.))
            a_2 = (np.pi/2.) * ((h/2.))**2.
            T = zzy[the_slice][T_total] 
            
            #eq = (1./(2.*a_1)) * (  (  (2.*((T-(2.*a_2*x)*x)/(2.*a_1)))/(t_sk)  )      +      (((   ((T-(2.*a_2*x) )/(2.*a_1))   -x)*h)/(t_sp))  )\
            #- (1./(2.*a_2))  *  (  ((x*np.pi*(h/2))/(t_sk))   +   (((x - ((T - (2*a_2*x))/(2*a_1))) * h )/ (t_sp))       )    
            
            #shear_flow = nsolve(eq, x)
            
            temp_matrix = np.zeros((2,2))
            u_matrix = np.zeros((2,1))
            
            temp_matrix[0][0] = 2*a_1
            temp_matrix[0][1] = 2*a_2
            
            u_matrix[0][0] = T
            
            temp_matrix[1][0] = ((1.)/(2.*a_1)) * 2. * l_skin * ((1.)/(t_sk)) + ((1.)/(2.*a_1)) * (h/(t_sp)) + ((-1.)/(2.*a_2)) * ((-h)/(t_sp))
            temp_matrix[1][1] = - (1./(2.*a_2)) * ((np.pi * (h/2.))/(t_sk)) - ((1.)/(2.*a_2)) * (h/t_sp) + ((1.)/(2.*a_1)) *((-1*h)/(t_sp))
            
            u_matrix[1][0] = 0
            
            solution_matrix = np.linalg.solve(temp_matrix, u_matrix)
            
            q_1 = solution_matrix[0][0]
            q_2 = solution_matrix[1][0]
            
            
    for the_slice in range(0, nslice):
        matrix_nsad[shear_flow][the_slice][0] = 0
        for the_boom in range(1, nboom):    
            matrix_nsad[shear_flow][the_slice][the_boom] = matrix_nsad[shear_flow][the_slice][the_boom - 1]\
            + (zzy_[the_slice][F_y_total] / MOIZZBoom) * (M_booms[the_boom-1][area_boom] * M_booms[the_boom-1][y_coordinate_boom]) \
            + (zzy_[the_slice][F_z_total] / MOIYYBoom) * (M_booms[the_boom-1][area_boom] * (M_booms[the_boom-1][z_coordinate_boom]-z_coordinate_shear_center))
            
            if M_booms < 6 or M_booms > 13:
                matrix_nsad[shear_flow][the_slice][the_boom] = matrix_nsad[shear_flow][the_slice][the_boom] + q_1
            else:
                matrix_nsad[shear_flow][the_slice][the_boom] = matrix_nsad[shear_flow][the_slice][the_boom] + q_2
            
            
            
            
            
            
            #matrix_nsad[y_deformation_due_to_shear_flow][the_slice][the_boom]
            #matrix_nsad[z_deformation_due_to_bending][the_slice][the_boom]
            

            # finding deformed structure
            matrix_nsad[x_co_deformed][the_slice][the_boom] = matrix_nsad[x_co_undeformed][the_slice][the_boom]
            
            matrix_nsad[y_co_deformed][the_slice][the_boom] = matrix_nsad[y_co_undeformed][the_slice][the_boom] \
            + matrix_nsad[y_deformation_due_to_bending][the_slice][the_boom]\
            + matrix_nsad[y_deformation_due_to_shear_flow][the_slice][the_boom]
            
            matrix_nsad[z_co_deformed][the_slice][the_boom] = matrix_nsad[z_co_undeformed][the_slice][the_boom] \
            + matrix_nsad[z_deformation_due_to_shear_flow][the_slice][the_boom]\
            + matrix_nsad[z_deformation_due_to_bending][the_slice][the_boom]
    
    return matrix_nsad 
    





     
'''        
        for the_slice in range(1, nslice):
            for the_boom in range(0, nboom):            
                #testing something from Megson p 619, assuming 
                matrix_nsad[y_displacement_bending][the_slice][the_boom] = matrix_nsad[y_displacement_bending][the_slice -1][the_boom] \
                + (M_booms[the_boom][area_boom] * matrix_nsad[defor_bend_over_axis_z][the_slice][the_boom] \
                * matrix_nsad[stress_bend_over_axis_z][the_slice][the_boom] * zzy[the_slice][tickness]) 
        # this is giving unrealistic results, need more thinking
'''            
   
















