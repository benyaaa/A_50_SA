from anal_deflection import *
import SVV_input
from centroid_MOI import *
from Idealised_structure2 import *
from Numerical_check_for_external_forces import *
from Numerical_stresses_and_deformations import *

print MOIZZAirfoil(t_st, h_st, w_st, BetaStringers, y_cst)

print MOIZZAirfoil(t_st, h_st, w_st, BetaStringers, y_cst)

print deflect(l_a)







z_cst = CentroidStringers(st_n, beta_sttr, C_a, h, S_st)[0]
y_cst = CentroidStringers(st_n, beta_sttr, C_a, h, S_st)[1]



print IdealisedStructure(Q, y_cst, z_cst)

zy = IdealisedStructure(Q, y_cst, z_cst)

print MOIYYBoom(IdealisedStructure,CentroidAirfoil)
print MOIZZBoom(IdealisedStructure,CentroidAirfoil)

print CentroidAirfoil(z_cst, A_st, z_ctr, A_tr, z_cse, A_se, z_csp, A_sp, n_st)







zzy = NumericalExternalForces(slicing, CentroidAirfoil, F_H1_z, F_H1_y, P_jam, F_H2_z, F_H2_y, P, F_H3_y, C_a, h, q)

M_booms = IdealisedStructure(Q, y_cst, z_cst)


print MOIYYBoom(IdealisedStructure,CentroidAirfoil)
print MOIZZBoom(IdealisedStructure,CentroidAirfoil)

zzzy = Numerical_stresses_and_deformations(zzy, M_booms, E, MOIYYBoom(IdealisedStructure,CentroidAirfoil), MOIZZBoom(IdealisedStructure,CentroidAirfoil))









