#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 14:57:29 2018

@author: maxvansplunteren
"""

from SVV_input import *

def slicing(x_1,x_2,x_3,x_a,l_a):
    A = x_1
    B = x_2 - x_a/2.
    C = x_2 + x_a/2.
    D = x_3
    
    
    slice_A = M*A/l_a
    slice_B = M*(B-A)/l_a
    slice_C = M*(C-B)/l_a
    slice_D = M*(D-C)/l_a
    slice_end = M*(l_a-D)/l_a
    slices = [int(slice_A),int(slice_B),int(slice_C),int(slice_D),int(slice_end)]
    lst = [int(slice_A), 
           int(slice_A)+int(slice_B), 
           int(slice_A)+int(slice_B)+int(slice_C), 
           int(slice_A)+int(slice_B)+int(slice_C)+int(slice_D),
           int(slice_A)+int(slice_B)+int(slice_C)+int(slice_D)+int(slice_end)]
    
    spacing_A = A/int(slice_A)
    spacing_AB = (B-A)/int(slice_B)
    spacing_BC = (C-B)/int(slice_C)
    spacing_CD = (D-C)/int(slice_D)
    spacing_D = (l_a-D)/int(slice_end)
    lst1 = [spacing_A,spacing_AB,spacing_BC,spacing_CD,spacing_D]
    N = lst[4]
    
    total = 0
    for i in range(5):
        total = total + slices[i]*lst1[i]
    
    
    zero = np.zeros((1,6))
    M_slices = np.zeros((N,6))
       
    #adding thickness to the matrix
    loop = -1    
    counter = 0
    for j in slices:
        loop = loop + 1
        for i in range(j):
            M_slices[counter][-3] = lst1[loop]
            counter = counter + 1
    
    #adding the begin value and end value to the matrix       
    for i in range(N):
        M_slices[i][2] = M_slices[i][1] + M_slices[i][3]
        try:
            M_slices[i+1][1] = M_slices[i][2]
        except IndexError:
            continue
    
    #adding the hinge flag and rib flag to the matrix  
    hinge_1 = x_1
    hinge_2 = x_2
    hinge_3 = x_3
    
    for i in range(N):
        if i in lst:
            M_slices[i][-2] = 1 
        if M_slices[i][1] == hinge_1 or round(M_slices[i][1]) == hinge_2 or round(M_slices[i][1]) == hinge_3:
            M_slices[i][-1] = 1
    
    M_slices = np.vstack((zero,M_slices))
    
    #adding slice number to the matrix
    for i in range(N):
        M_slices[i][0]=i
    
     
    return M_slices, N
        

ss= slicing(x_1,x_2,x_3,x_a,l_a)[0]    
N = slicing(x_1,x_2,x_3,x_a,l_a)[1]    
        
        