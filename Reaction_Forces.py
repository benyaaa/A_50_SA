from math import *

import scipy as np
from SVV_main import *
a = np.mat([1,2])
b = np.mat([3,4])
np.concatenate((a,b))

# M*x=u
# M is an 8x8 matrix with all the coefficients
# x is the matrix with the unknowns ([F_H1_y, F_H2_y ,F_H3_y ,F_H1_z ,F_H2_z ,P_jam ,C ,L ])
# u is the output matrix

# Eq 1: Force equilibrium in y-direction
m1 = np.mat([1,1,1,0,0,sin(theta),0,0])     
u1 = np.mat([P*sin(theta)+q*l_a*sin(theta)])

# Eq 2:
m2 = np.mat([0,0,0,1,1,cos(theta),0,0])
u2 = np.mat([P*cos(theta)-q*l_a*sin(theta)])

# Eq 3: Moment equilibrium x-axis
m3 = np.mat([0,0,0,0,0,(h_a/2.)*cos(theta)-(h_a/2.)*sin(theta),0,0])
u3 = np.mat([P*(h_a/2)*cos(theta)-P*(h_a/2)*sin(theta)+q*l_a*cos(theta)*(0.25*C_a-(h_a/2.))])

# Eq 4: Moment equilibrium y-axis
m4 = np.mat([0,0,0,(x_2-x_1),0,(x_a/2)*cos(theta),0,0])
#u4 = np.mat([q*l_a*sin(theta)*
