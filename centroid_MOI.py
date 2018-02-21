from math import *
import numpy as np
from SVV_input import *


def CentroidStringers(st_n, beta_sttr, C_a, h, S_st): #[0]returns array with centroids z location of stringers, [1]returns array with centroids z location of stringers array[1,2,3,4,5,6,17,16,15,14,13,12,8,10,7,11,9]
    
    z_cst = S_st*cos(beta_sttr)*st_n-0.5*S_st #stiffener 1-6&12-17
    z_cst = np.append(z_cst,z_cst)
    y_cst = S_st*sin(beta_sttr)*st_n-0.5*S_st #stiffener 1-6
    y_cst = np.append(y_cst,-(S_st*sin(beta_sttr)*st_n-0.5*S_st)) #stiffener 12-17 (negative wrt 1-6)
    #semi circular part
    z_cst = np.append(z_cst, cos(S_st*2*pi/(2*pi*(h/2)))*(h/2)+C_a-(h/2))#stiffener 8&10
    z_cst = np.append(z_cst, cos(S_st*2*pi/(2*pi*(h/2)))*(h/2)+C_a-(h/2))
    y_cst = np.append(y_cst,sin(S_st*2*pi/(2*pi*(h/2)))*(h/2)) #stiffener 8
    y_cst = np.append(y_cst,-sin(S_st*2*pi/(2*pi*(h/2)))*(h/2)) #stiffener 10
    z_cst = np.append(z_cst,cos(2*S_st*2*pi/(2*pi*(h/2)))*(h/2)+C_a-(h/2)) #stiffener 7&11
    z_cst = np.append(z_cst,cos(2*S_st*2*pi/(2*pi*(h/2)))*(h/2)+C_a-(h/2))
    y_cst = np.append(y_cst,sin(2*S_st*2*pi/(2*pi*(h/2)))*(h/2)) #stiffener 7
    y_cst = np.append(y_cst,-sin(2*S_st*2*pi/(2*pi*(h/2)))*(h/2)) #stiffener 11
    z_cst = np.append(z_cst,C_a) #stiffener 9
    y_cst = np.append(y_cst,0) #stiffener 9
    return z_cst, y_cst

z_cst = CentroidStringers(st_n, beta_sttr, C_a, h, S_st)[0]
y_cst = CentroidStringers(st_n, beta_sttr, C_a, h, S_st)[1]

def CentroidAirfoil(z_cst, A_st, z_ctr, A_tr, z_cse, A_se, z_csp, A_sp, n_st): #returns centroid of airfoil cross-section in (z,y)
    Zcairfoil = (sum(z_cst*A_st) + z_ctr*A_tr + z_cse*A_se + z_csp*A_sp)/(n_st*A_st + A_se + A_sp + A_tr)
    Ycairfoil = 0
    Centroidairfoil = [Zcairfoil,Ycairfoil]
    return Centroidairfoil

def BetaStringers(beta_sttr, S_st, h): #returns array with angles matching y_cst and z_cst array[1,2,3,4,5,6,17,16,15,14,13,12,8,10,7,11,9]
    beta_st = []
    for i in range(12):
        beta_st = np.append(beta_st, beta_sttr)
    beta_st = np.append(beta_st, S_st/(h/2)) #stringer 8
    beta_st = np.append(beta_st, -S_st/(h/2)) #stringer 10
    beta_st = np.append(beta_st, 2*S_st/(h/2)) #stringer 7
    beta_st = np.append(beta_st, -2*S_st/(h/2)) #stringer 11
    beta_st = np.append(beta_st, 0.5*pi) #stringer 9
    return beta_st

def MOIZZAirfoil(t_st, h_st, w_st, BetaStringers, y_cst): #returns I_zz of the airfoil cross-section
    I_zztr = 2*((1/12)*sqrt((C_a-(h/2))**2+(h/2)**2)*t_sk*(h/2)**2+sqrt((C_a-(h/2))**2+(h/2)**2)*t_sk*(h/4)**2)
    I_zzsp = (1/12)*h*t_sp*h**2
    I_zzsc = (pi*(h/2)**3*t_sk)/2
    I_zzstfl = (1./12.)*(t_st*h_st)*(h_st*np.sin(BetaStringers(beta_sttr, S_st, h)))**2+(t_st*h_st)*y_cst**2
    I_zzstba = (t_st*w_st)*y_cst**2
    I_zzst = np.sum(I_zzstfl + I_zzstba)
    I_zzairfoil = I_zzst + I_zztr + I_zzsp + I_zzsc 
    return I_zzairfoil

def MOIYYAirfoil(t_st, h_st, w_st, BetaStringers, z_cst, CentroidAirfoil): #returns I_yy of the airfoil cross-section
    I_yytr = 2*((1/12)*sqrt((C_a-(h/2))**2+(h/2)**2)*t_sk*(C_a-(h/2)**2)+sqrt((C_a-(h/2))**2+(h/2)**2)*t_sk*(CentroidAirfoil(z_cst, A_st, z_ctr, A_tr, z_cse, A_se, z_csp, A_sp, n_st)[0]-(C_a-(h/2))/2)**2)
    I_yysp = h*t_sp*(CentroidAirfoil(z_cst, A_st, z_ctr, A_tr, z_cse, A_se, z_csp, A_sp, n_st)[0]-(C_a-(h/2)))**2
    I_yysc = (pi*(h/2)**3*t_sk)/2+pi*(h/2)*t_sk*(CentroidAirfoil(z_cst, A_st, z_ctr, A_tr, z_cse, A_se, z_csp, A_sp, n_st)[0]-z_cse)**2
    I_yystfl = (t_st*h_st)*(z_cst-CentroidAirfoil(z_cst, A_st, z_ctr, A_tr, z_cse, A_se, z_csp, A_sp, n_st)[0])**2
    I_yystba = (1./12.)*(t_st*w_st)*(w_st*np.cos(BetaStringers(beta_sttr, S_st, h)))**2+(t_st*w_st)*(z_cst-CentroidAirfoil(z_cst, A_st, z_ctr, A_tr, z_cse, A_se, z_csp, A_sp, n_st)[0])**2
    I_yyst = np.sum(I_yystfl + I_yystba)
    I_yyairfoil = I_yyst + I_yytr + I_yysp + I_yysc 
    return I_yyairfoil








    

