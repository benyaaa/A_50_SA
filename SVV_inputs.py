from math import *

Ca = 0.547*10**3    #mm, chord length aileron
la = 2.771*10**3    #mm, span of the aileron
x1 = 0.153*10**3    #mm, x-location of hinge 1
x2 = 1.281*10**3    #mm, x-location of hinge 2
x3 = 2.681*10**3    #mm, x-location of hinge 3
xa = 280            #mm, distance between actuators 1 and 2
ha = 225            #mm, aileron height
tsk = 1.1           #mm, skin thickness
tsp = 2.9           #mm, spar thickness
hst = 1.5           #mm, height of stiffener
wst = 20            #mm, width of stiffener
nst = 17            #-, number of stiffeners equally spaced along cross-section
d1 = 110.3          #mm, vertical displacement hinge 1
d3 = 164.2          #mm, vertical displacement hinge 2
theta = radians(26) #rad, maximum upward defelction
P = 9.17*10**3      #N, load in actuator 2
q = 4.53*10**3      #N, net aerodynamic load
E = 73.1*10**9      #Pa, modulus of elasticity
