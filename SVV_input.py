from math import *
import scipy as np
from numpy.linalg import inv
from sklearn.preprocessing import Imputer
import pandas as pd


C_a = 0.547*10**3    #mm, chord length aileron
l_a = 2.771*10**3    #mm, span of the aileron
x_1 = 0.153*10**3    #mm, x-location of hinge 1
x_2 = 1.281*10**3    #mm, x-location of hinge 2
x_3 = 2.681*10**3    #mm, x-location of hinge 3
x_a = 280            #mm, distance between actuators 1 and 2


h = 225              #mm, aileron height

h = 225            #mm, aileron height

h = 225              #mm, aileron height

t_sk = 1.1           #mm, skin thickness
t_sp = 2.9           #mm, spar thickness
t_st = 1.2          #mm, stiffener thickness
h_st = 1.5           #mm, height of stiffener
w_st = 20            #mm, width of stiffener
n_st = 17           #-, number of stiffeners equally spaced along cross-section
d_1 = 110.3          #mm, vertical displacement hinge 1
d_3 = 164.2          #mm, vertical displacement hinge 2

Q = 0               # Q = 0,1,3,7,15,31,63,127,255,511 Extra elements between booms

theta = radians(26)  #rad, maximum upward defelction
P = 9.17*10**3       #N, load in actuator 2
q = 4.53             #N, net aerodynamic load
E = 73.1*10**3       #N/mm^2, modulus of elasticity




theta = radians(26) #rad, maximum upward defelction
P = 9.17*10**3      #N, load in actuator 2
q = 4.53            #N, net aerodynamic load
E = 73.1*10**3      #N/mm^2, modulus of elasticity
Q = 0               # Q = 0,1,3,7,15,31,63,127,255,511 Extra elements between booms

#-------------------Centroid and MOI inputs---------------#

beta_sttr = atan((h/2)/(C_a-(h/2))) #the angle of the stiffeners in the triangular part
c_ai = 2*sqrt((h/2)**2+(C_a-(h/2))**2)+pi*(h/2) #circumference of airfoil
S_st = c_ai/n_st #stringer spacing
st_n = np.arange(1,7)

#centroid triangle (II)
z_ctr = (C_a-(h/2))/2 #in the middle of the triangular part
y_ctr = 0 #on the same line as the trailing edge, on the symmetry line
A_tr = (2*sqrt((h/2)**2+(C_a-(h/2))**2))*t_sk

#centroid spar (III)
z_csp = (C_a-(h/2)) #just the chord length minus the semi-circle
y_csp = 0 #on the symmetry line
A_sp = h*t_sp

#centroid semi-circle (I)
z_cse = 2*(h/2)/pi + C_a-(h/2) #according to the internet
y_cse = 0 #on the symmetry line
A_se = pi*(h/2)*t_sk

#the stiffeners

A_st = t_st*(h_st+w_st) #area per stiffener

#------------------------Slicing Input--------------------------------#
M = 100             #Number of slices, M>=4 since there are 4 ribs




