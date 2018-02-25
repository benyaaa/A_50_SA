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

#matrix[row][column]

def Numerical_stresses_and_deformations(zzy, M_booms, E, MOIYYBoom_value, MOIZZBoom_value):
    # defining names of the rows of the matrix matrix_nsad
    stress_bend_over_axis_z = 0
    stress_bend_over_axis_y = 1
    stress_shear_along_y = 2
    stress_shear_along_z = 3
    stress_torsion = 4
    defor_bend_over_axis_z = 5
    defor_bend_over_axis_y = 6
    defor_shear_along_y = 7
    defor_shear_along_z = 8
    defor_torsion_angle = 9
    x_co_undeformed = 10
    y_co_undeformed = 11
    z_co_undeformed = 12
    x_co_deformed	 = 13
    y_co_deformed	 = 14
    z_co_deformed	 = 15
    
    z_displacement_bending = 16
    y_displacement_bending = 17
    
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
    matrix_nsad = np.zeros((16+2, nslice, nboom))
    

    for the_slice in range(0, nslice):
        for the_boom in range(0, nboom):
            #calculating bending streses in every boom \sigma=(M/I)*y
            matrix_nsad[stress_bend_over_axis_z][the_slice][the_boom] = ((zzy[the_slice][Bending_moment_z])/(MOIZZBoom_value))*(M_booms[the_boom][y_coordinate_boom])
            matrix_nsad[stress_bend_over_axis_y][the_slice][the_boom] = ((zzy[the_slice][Bending_moment_y])/(MOIYYBoom_value))*(M_booms[the_boom][z_coordinate_boom])
            
            # calculating the deformation due to bending stress in every boom \varepsilon_x = \sigma/E
            matrix_nsad[defor_bend_over_axis_z][the_slice][the_boom] = matrix_nsad[stress_bend_over_axis_z][the_slice][the_boom]/E
            matrix_nsad[defor_bend_over_axis_y][the_slice][the_boom] = matrix_nsad[stress_bend_over_axis_y][the_slice][the_boom]/E
            
            #testing something from Megson p 619, assuming 
            matrix_nsad[y_displacement_bending][the_slice][the_boom] = matrix_nsad[y_displacement_bending][the_slice -1][the_boom] + M_booms[the_boom][area_boom] * matrix_nsad[defor_bend_over_axis_z][the_slice][the_boom] * matrix_nsad[stress_bend_over_axis_z][the_slice][the_boom] * zzy[the_slice][tickness]
            
            #We don't calculate shear flow at this time because we may decide that it is neglectable
            #calculating shear flow due to vertical and horizontal shear load
            
            
            #We don't calculate shear deformation at this time because we may decide that it is neglectable
            #calculating shear deformation due to vertical and horizontal shear load
    
    
            #torsion to be done on monday
            #calculating shear flow due to torsion
            
            
            #torsion to be done on monday
            #calculating deformation due to torsion
    
            
            
            #filling in the x, y and z coordinates of every boom
            #taking the middle of the slice as the x-coordinate
            matrix_nsad[x_co_undeformed][the_slice][the_boom] = ((zzy[the_slice][end] + zzy[the_slice][begining]))/2
            matrix_nsad[y_co_undeformed][the_slice][the_boom] = M_booms[the_boom][y_coordinate_boom]
            matrix_nsad[z_co_undeformed][the_slice][the_boom] = M_booms[the_boom][z_coordinate_boom]  
    
    
            #finding the x, y and z coordinates of every boom after deformation
        
        
        
        
        for the_slice in range(1, nslice):
            for the_boom in range(0, nboom):            
                #testing something from Megson p 619, assuming 
                matrix_nsad[y_displacement_bending][the_slice][the_boom] = matrix_nsad[y_displacement_bending][the_slice -1][the_boom] \
                + (M_booms[the_boom][area_boom] * matrix_nsad[defor_bend_over_axis_z][the_slice][the_boom] \
                * matrix_nsad[stress_bend_over_axis_z][the_slice][the_boom] * zzy[the_slice][tickness])
        # this is giving unrealistic results, need more thinking
            
    return matrix_nsad    
















