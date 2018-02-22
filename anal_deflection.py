import numpy as np
import matplotlib.pyplot as plt
from math import *
from SVV_input import *
from Reaction_Forces import *

#-----------Analytical Defelctions---------#

# For the sake of simplicity is the deflection formula used
# with the origin at the right-end of hinge 1, See FIGURE.

# the variable x is the input for the deflection calculation

# Deflection 
# v = (-1/24)*(q*cos(theta))*x^4 + (1/6)*F_H1_y*(x-x_1)^3 - (1/6)*P_jam*sin(theta)*(x-(x_2-(x_a/2)))^3 + (1/6)*F_H2_y*(x-x_2)^3 + (1/6)*P*sin(theta)(x-(x_2+(x_a/2)))^3 + 1/2*F_H3_y*(x-x_3)^3 + C*x + L

# The deflection, as depicted in EQ, is made out of step functions. Hence,
# step functions are depending on the magnitude of the variable x.

def deflect(x):
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
        v = (-1./24.)*(q*cos(theta))*x**4 + (1./6.)*F_H1_y*(x-x_1)**3 + (1./6.)*P_jam*sin(theta)*(x-(x_2-(x_a/2)))**3 + (1./6.)*F_H2_y*(x-x_2)**3 - (1./6.)*P*sin(theta)*(x-(x_2+(x_a/2.)))**3 + 1./2.*F_H3_y*(x-x_3)**3 + C*x + L        
    return v/(E*I_zz) 

# the deflection in hinge 2 should be zero, but is rightn now 5 mm
 
print deflect(x_2)

def deflectplot():
    deflect_list = []
    points = []
    for i in range(0,int(l_a),int(l_a)/100 + 1):
        d = deflect(float(i))
        points.append(i)
        deflect_list.append(d)
    plt.plot(points, deflect_list, 'r--')
    plt.show()

#deflectplot()

        
