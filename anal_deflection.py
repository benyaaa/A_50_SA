import numpy as np
from math import *
from SVV_input import *

#-----------Analytical Defelctions---------#

# For the sake of simplicity is the deflection formula used
# with the origin at the right-end of hinge 1, See FIGURE.

# the variable x is the input for the deflection calculation

# Deflection 
# v = (-1/24)*(q*cos(theta))*x^4 + (1/6)*F_H1_y*(x-x_1)^3 - (1/6)*P_jam*sin(theta)*(x-(x_2-(x_a/2)))^3 + (1/6)*F_H2_y*(x-x_2)^3 + (1/6)*P*sin(theta)(x-(x_2+(x_a/2)))^3 + 1/2*F_H3_y*(x-x_3)^3 + C*x + L
def deflect(x):
    if x > x_1:
        v = (-1/24)*(q*cos(theta))*x^4 + (1/6)*F_H1_y*(x-x_1)^3 + C*x + L
    elif x > (x_2(x_a/2)):
        v = (-1/24)*(q*cos(theta))*x^4 + (1/6)*F_H1_y*(x-x_1)^3 - (1/6)*P_jam*sin(theta)*(x-(x_2-(x_a/2)))^3 + C*x + L
    elif x > x_2:
        v = (-1/24)*(q*cos(theta))*x^4 + (1/6)*F_H1_y*(x-x_1)^3 - (1/6)*P_jam*sin(theta)*(x-(x_2-(x_a/2)))^3 + (1/6)*F_H2_y*(x-x_2)^3 + C*x +L
    elif x > (x_2
    return v

