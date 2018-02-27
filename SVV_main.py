from anal_deflection import *
import SVV_input
from centroid_MOI import *
from Idealised_structure2 import *
from Numerical_check_for_external_forces import *
from Numerical_stresses_and_deformations import *
from anal_shear import *

z_cst = CentroidStringers(st_n, beta_sttr, C_a, h, S_st)[0]
y_cst = CentroidStringers(st_n, beta_sttr, C_a, h, S_st)[1]

zy = IdealisedStructure(Q, y_cst, z_cst)

zzy = NumericalExternalForces(slicing, CentroidAirfoil, F_H1_z, F_H1_y, P_jam, F_H2_z, F_H2_y, P, F_H3_y, C_a, h, q)

M_booms = IdealisedStructure(Q, y_cst, z_cst)

zzzy = Numerical_stresses_and_deformations(zzy, M_booms, E, MOIYYBoom(IdealisedStructure,CentroidAirfoil), MOIZZBoom(IdealisedStructure,CentroidAirfoil))



#---------- Analytical model -------------#

# Shear flow:
q_rib_1 = shear(shear_distri(x_1)[0],shear_distri(x_1)[1])  # shear flow in rib 1, (q_13, q_43, q_32)
q_rib_2_a = shear(shear_distri(x_2-(x_a/2.))[0],shear_distri(x_2-(x_a/2.))[1])
q_rib_2_b = shear(shear_distri(x_2+(x_a/2.))[0],shear_distri(x_2+(x_a/2.))[1])
q_rib_3 = shear(shear_distri(x_3)[0],shear_distri(x_3)[1])

# Deflection:
delta_bend_0 = deflect(0) # the defelction due to bending and shear at point 0 (most inboard)
delta_bend_4 = deflect(l_a) # the defelction due to bending and shear at point 4 (most outboard)

# Twist angle:
twist_0 = twister(0.)
twist_4 = twister(l_a)

# Total deflection:
delta_le_0 = delta_bend_0 - eta*sin(twist_0)*cos(theta)
delta_te_0 = delta_bend_0 + (C_a-eta)*sin(twist_0)*cos(theta)

delta_le_4 = delta_bend_4 - eta*sin(twist_4)*cos(theta)
delta_te_4 = delta_bend_4 + (C_a-eta)*sin(twist_4)*cos(theta)

print M_booms