import numpy as np
from math import *


#Inputs:
P = 9.17    #kN
q = 4.53    #kN
Pjamy = 1.0
FH1y = 1.0
FH2y = 1.0
FH3y = 1.0
x1 = 0.153  #m
x2 = 1.281
x3 = 2.681
xa = 0.28   #m
theta = radians(26)
E = 73.1 # GPa
I = 1.0 #
la = 2.771 #m
d1 = 0.1103
d3 = 16.42

#------------------------------------------#
qy = q*np.cos(theta)
Py = P*np.cos(theta)
#-----------Defelctions---------#
x = x2
v1 = (1./(E*I))*((1./(24.))*qy*x**4+(1./6.)*FH2y*(x)**3+(1./6.)*Pjamy*(x-0.5*xa)**3+(1./6.)*FH1y*(x-x1)**3)
print v1

x = la - x2
v3 = (1./(E*I))*((1./(24.))*qy*x**4+(1./6.)*FH2y*(x)**3 + (1./6.)*Py*(x-0.5*xa)**3+(1./6.)*FH1y*(x-(x3-x2))**3)
print v3
