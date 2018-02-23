from anal_deflection import *
from SVV_input import *
from centroid_MOI import *
from Idealised_structure2 import *
from Numerical_check_for_external_forces import *

print MOIZZAirfoil(t_st, h_st, w_st, BetaStringers, y_cst)

print MOIZZAirfoil(t_st, h_st, w_st, BetaStringers, y_cst)


print deflect(l_a)




C_a = 0.547*10**3    #mm, chord length aileron
l_a = 2.771*10**3    #mm, span of the aileron
x_1 = 0.153*10**3    #mm, x-location of hinge 1
x_2 = 1.281*10**3    #mm, x-location of hinge 2
x_3 = 2.681*10**3    #mm, x-location of hinge 3
x_a = 280            #mm, distance between actuators 1 and 2
h = 225            #mm, aileron height
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


z_cst = CentroidStringers(st_n, beta_sttr, C_a, h, S_st)[0]
y_cst = CentroidStringers(st_n, beta_sttr, C_a, h, S_st)[1]



print IdealisedStructure(Q, y_cst, z_cst)

zy = IdealisedStructure(Q, y_cst, z_cst)

print MOIYYBoom(IdealisedStructure,CentroidAirfoil)
print MOIZZBoom(IdealisedStructure,CentroidAirfoil)

print CentroidAirfoil(z_cst, A_st, z_ctr, A_tr, z_cse, A_se, z_csp, A_sp, n_st)

zzy = NumericalExternalForces(slicing, CentroidAirfoil, F_H1_z, F_H1_y, P_jam, F_H2_z, F_H2_y, P, F_H3_y, C_a, h, q)

print zzy









