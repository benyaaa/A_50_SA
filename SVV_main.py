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

# Deflection:
delta_bend_0 = deflect(0) # the defelction due to bending and shear at point 0 (most inboard)
delta_bend_4 = deflect(l_a) # the defelction due to bending and shear at point 4 (most outboard)

# Twist angle:
twist_0 = twister(0.)
twist_4 = twister(l_a)



