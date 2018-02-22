from anal_deflection import *
from SVV_input import *
from centroid_MOI import *
from Idealised_structure2 import *


print MOIZZAirfoil(t_st, h_st, w_st, BetaStringers, y_cst)

z_cst = CentroidStringers(st_n, beta_sttr, C_a, h, S_st)[0]
y_cst = CentroidStringers(st_n, beta_sttr, C_a, h, S_st)[1]


print IdealisedStructure(Q, y_cst, z_cst)

zy = IdealisedStructure(Q, y_cst, z_cst)




print deflect(8)
















