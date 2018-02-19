import numpy as np
from math import *


#Inputs:
P = 9.17                #kN
q = 4.53                #kN
Pjamy = 1.0             #kN
FH1y = 1.0              #kN
FH2y = 1.0              #kN
FH3y = 1.0              #kN
x1 = 0.153              #m
x2 = 1.281              #m
x3 = 2.681              #m
xa = 0.28               #m
theta = radians(26)     #rad
E = 73.1                #GPa
I = 1.0                 #m^4
la = 2.771              #m
d1 = 0.1103             #m
d3 = 16.42              #m

#------------------------------------------#
qy = q*np.cos(theta)
Py = P*np.cos(theta)
#-----------Defelctions---------#

# For the sake of simplicity is the deflection formula used
# twice, left and right from hinge 2. See FIGURE
# Hence, v1 is the deflection at the right-end of hinge 1 and
# v3 is the deflection at the left-end of hinge 3.

# the variable x is different for v1 and v3

# Deflection 1
x = x2
v1 = (1./(E*I))*((1./(24.))*qy*x**4+(1./6.)*FH2y*(x)**3+(1./6.)*Pjamy*(x-0.5*xa)**3+(1./6.)*FH1y*(x-x1)**3)
print v1

# Deflection 3
x = la - x2
v3 = (1./(E*I))*((1./(24.))*qy*x**4+(1./6.)*FH2y*(x)**3 + (1./6.)*Py*(x-0.5*xa)**3+(1./6.)*FH1y*(x-(x3-x2))**3)
print v3
