from anal_deflection import *
from SVV_input import *
from centroid_MOI import *

print MOIZZAirfoil(t_st, h_st, w_st, BetaStringers, y_cst)







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
q = 4.53            #N/mm, net aerodynamic load

E = 73.1*10**9      #Pa, modulus of elasticity

Q = 0               # Q = 0,1,3,7,15,31,63,127,255,511 Extra elements between booms


Q = int(0)          # number of skin booms (extra booms placed between the stringer booms to increase acc)


E = 73.1*10**3      #N/mm^2, modulus of elasticity


print deflect(8)

