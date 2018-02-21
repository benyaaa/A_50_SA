from math import *

C_a = 0.547*10**3    #mm, chord length aileron
l_a = 2.771*10**3    #mm, span of the aileron
x_1 = 0.153*10**3    #mm, x-location of hinge 1
x_2 = 1.281*10**3    #mm, x-location of hinge 2
x_3 = 2.681*10**3    #mm, x-location of hinge 3
x_a = 280            #mm, distance between actuators 1 and 2
h_a = 225            #mm, aileron height
t_sk = 1.1           #mm, skin thickness
t_sp = 2.9           #mm, spar thickness
h_st = 1.5           #mm, height of stiffener
w_st = 20            #mm, width of stiffener
n_st = 17            #-, number of stiffeners equally spaced along cross-section
d_1 = 110.3          #mm, vertical displacement hinge 1
d_3 = 164.2          #mm, vertical displacement hinge 2
theta = radians(26) #rad, maximum upward defelction
P = 9.17*10**3      #N, load in actuator 2
q = 4.53*10**3      #N, net aerodynamic load
E = 73.1*10**3      #Pa, modulus of elasticity
