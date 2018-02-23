from math import *
from SVV_input import *
from centroid_MOI import *

I_zz = MOIZZAirfoil(t_st, h_st, w_st, BetaStringers, y_cst)
I_yy = MOIYYAirfoil(t_st, h_st, w_st, BetaStringers, z_cst, CentroidAirfoil)

A_I = (h*(C_a-(h/2.)))/2
A_II = (pi*(h/2.)**2)/2
alpha = tan((h/2.)/(C_a-(h/2.)))
s_1 = sqrt((C_a-(h/2.))**2 + (h/2.)**2)
s_3 = h

def shear(S_y,S_z):
    Z = S_z/I_yy
    Y = S_y/I_zz
    delta = pi/2.
    

    q_s0_I = ((h/t_sp)+((2.*s_1)/t_sk))**-1 * (-((1./3.)*s_1**3*cos(alpha) + (1./(6.*t_sp))*s_1**3*t_sk*cos(alpha) + (1./(6.*t_sp))*h**3*t_sk)*Z - ((1./6.)*s_3**3 + (1./3.)*s_1**3*sin(alpha) + (1./(6.*t_sp))*s_1**3*t_sk*sin(alpha) + (1./(6.*t_sp))*h**3*t_sk)*Y) 

    q_s0_II = ((t_sk*t_sp)/(pi*h*t_sp + h*t_sk)) * ((-2./t_sk)*(-Z*t_sk*h**2 - Y*t_sk*(h**2/2.)) - (s_3/t_sp)*(-Z*t_sk*(h**2/2.) - Y*t_sk*(h**2/2.) - Z*t_sk*(s_1**2/2.)*cos(alpha) - Y*t_sk*(s_1**2/2.)*sin(alpha) - Y*t_sp*(s_3**2/6.)))
    
    q_13b = -Z*t_sk*(s_1**2/2.)*cos(alpha) - Y*t_sk*(s_1**2/2.)*sin(alpha)

    q_43b = -Z*t_sk*(h**2/2.)*sin(delta) - Y*t_sk*(h**2/2.)*(cos(delta)-1.)

    q_32b = -Y*t_sp*(s_3**2/2.) - Z*t_sk*(s_1**2/2.)*cos(alpha) - Y*t_sk*(s_1**2/2.)*sin(alpha) - Z*t_sk*(h**2/2.) - Y*t_sk*(h**2/2.)

    q_13 = q_13b + q_s0_I
    q_43 = q_43b + q_s0_II
    q_32 = q_32b + q_s0_I - q_s0_II

    T = 2*A_I*(2*q_13 + q_32) + 2*A_II*(2*q_43 + q_32)

    return q_13, q_43, q_32

def sc():
    S_z = 0
    S_y = 1
    Z = S_z/I_yy
    Y = S_y/I_zz

    q_s0_I = ((h/t_sp)+((2.*s_1)/t_sk))**-1 * (-((1./3.)*s_1**3*cos(alpha) + (1./(6.*t_sp))*s_1**3*t_sk*cos(alpha) + (1./(6.*t_sp))*h**3*t_sk)*Z - ((1./6.)*s_3**3 + (1./3.)*s_1**3*sin(alpha) + (1./(6.*t_sp))*s_1**3*t_sk*sin(alpha) + (1./(6.*t_sp))*h**3*t_sk)*Y) 
    q_s0_II = ((t_sk*t_sp)/(pi*h*t_sp + h*t_sk)) * ((-2./t_sk)*(-Z*t_sk*h**2 - Y*t_sk*(h**2/2.)) - (s_3/t_sp)*(-Z*t_sk*(h**2/2.) - Y*t_sk*(h**2/2.) - Z*t_sk*(s_1**2/2.)*cos(alpha) - Y*t_sk*(s_1**2/2.)*sin(alpha) - Y*t_sp*(s_3**2/6.)))

    eps = - (-Z*t_sk*(s_1**3/6.)*cos(alpha) - Y*t_sk*(s_1**3/6.)*sin(alpha))*s_1*sin(2.*alpha) - 2*A_I*q_s0_I - 2*A_II*q_s0_II
    return eps

print sc()

