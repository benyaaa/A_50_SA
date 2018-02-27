from SVV_input import *
from Reaction_Forces import *
from centroid_MOI import *

I_zz = MOIZZAirfoil(t_st, h_st, w_st, BetaStringers, y_cst)
I_yy = MOIYYAirfoil(t_st, h_st, w_st, BetaStringers, z_cst, CentroidAirfoil)
z_cent = CentroidAirfoil(z_cst, A_st, z_ctr, A_tr, z_cse, A_se, z_csp, A_sp, n_st)[0]

x = l_a
y = -100
z = C_a
def bending_stress(x,y,z):
        if x >= 0 and x <= x_1:
                M_y = (1./2.)*(q*sin(theta))*x**2
                M_z = -(1./2.)*(q*cos(theta))*x**2
        elif x > x_1 and x <= (x_2-(x_a/2.)):
                M_y = (1./2.)*(q*sin(theta))*x**2 + F_H1_z*(x-x_1)
                M_z = (-1./2.)*(q*cos(theta))*x**2 + F_H1_y*(x-x_1)
        elif x > (x_2-(x_a/2)) and x <= x_2:
                M_y = (1./2.)*(q*sin(theta))*x**2 + F_H1_z*(x-x_1) + P_jam*cos(theta)*(x-(x_2-(x_a/2.)))
                M_z = (-1./2.)*(q*cos(theta))*x**2 + F_H1_y*(x-x_1) + P_jam*sin(theta)*(x-(x_2-(x_a/2.)))
        elif x > x_2 and x <= (x_2+(x_a/2)):
                M_y = (1./2.)*(q*sin(theta))*x**2 + F_H1_z*(x-x_1) + P_jam*cos(theta)*(x-(x_2-(x_a/2.))) + F_H2_z*(x-x_2)
                M_z = (-1./2.)*(q*cos(theta))*x**2 + F_H1_y*(x-x_1) + P_jam*sin(theta)*(x-(x_2-(x_a/2.))) + F_H2_y*(x-x_2)
        elif x > (x_2+(x_a/2)) and x <= x_3:
                M_y = (1./2.)*(q*sin(theta))*x**2 + F_H1_z*(x-x_1) + P_jam*cos(theta)*(x-(x_2-(x_a/2.))) + F_H2_z*(x-x_2) - P*cos(theta)*(x-(x_2+(x_a/2.)))
                M_z = (-1./2.)*(q*cos(theta))*x**2 + F_H1_y*(x-x_1) + P_jam*cos(theta)*(x-(x_2-(x_a/2.))) + F_H2_y*(x-x_2) - P*cos(theta)*(x-(x_2+(x_a/2.)))                                                                                       
        elif x > x_3 and x <= l_a:
                M_y = (1./2.)*(q*sin(theta))*x**2 + F_H1_z*(x-x_1) + P_jam*cos(theta)*(x-(x_2-(x_a/2.))) + F_H2_z*(x-x_2) - P*cos(theta)*(x-(x_2+(x_a/2.)))
                M_z = (-1./2.)*(q*cos(theta))*x**2 + F_H1_y*(x-x_1) + P_jam*sin(theta)*(x-(x_2-(x_a/2.))) + F_H2_y*(x-x_2) - P*sin(theta)*(x-(x_2+(x_a/2.))) + F_H3_y*(x-x_3)
        sigma_x = (M_z/I_zz)*y+(M_y/I_yy)*(z-z_cent)
        return sigma_x

