from SVV_input import *


I_zz = 1.0*10**6

I_zz = 1.0
I_zz = 0.1

from centroid_MOI import *

I_zz = MOIZZAirfoil(t_st, h_st, w_st, BetaStringers, y_cst)




# M*x=u
# M is an 8x8 matrix with all the coefficients
# x is the matrix with the unknowns ([F_H1_y, F_H2_y ,F_H3_y ,F_H1_z ,F_H2_z ,P_jam ,C ,L ])
# u is the output matrix

# Eq 1: Force equilibrium in y-direction
m1 = np.mat([1.,1.,1.,0.,0.,sin(theta),0.,0.])     
u1 = np.mat([P*sin(theta)+q*l_a*sin(theta)])

# Eq 2: Force equilibrium in z-axis
m2 = np.mat([0.,0.,0.,1.,1.,cos(theta),0.,0.])
u2 = np.mat([P*cos(theta)-q*l_a*sin(theta)])

# Eq 3: Moment equilibrium x-axis


m3 = np.mat([0.,0.,0.,0.,0.,(h/2.)*cos(theta)-(h/2.)*sin(theta),0.,0.])

m3 = np.mat([0,0,0,0,0,(h/2.)*cos(theta)-(h/2.)*sin(theta),0,0])


m3 = np.mat([0.,0.,0.,0.,0.,(h/2.)*cos(theta)-(h/2.)*sin(theta),0.,0.])
u3 = np.mat([P*(h/2)*cos(theta)-P*(h/2)*sin(theta)+q*l_a*cos(theta)*(0.25*C_a-(h/2.))])

# Eq 4: Moment equilibrium y-axis
m4 = np.mat([0.,0.,0.,(x_2-x_1),0,(x_a/2.)*cos(theta),0.,0.])
u4 = np.mat([q*l_a*sin(theta)*((l_a/2.)-x_2)-P*cos(theta)*(x_a/2.)])

# Eq 5: Moment equilibrium z-axis
m5 = np.mat([-(x_2-x_1),0,(x_3-x_2),0,0,-sin(theta)*(x_a/2.),0.,0.])
u5 = np.mat([P*sin(theta)*(x_a/2.)+q*l_a*cos(theta)*((l_a/2.)-x_2)])

# Eq 6: deflection d_1
m6 = np.mat([0.,0.,0.,0.,0.,0.,x_1,1.])
u6 = np.mat([(1./24.)*q*cos(theta)*x_1**4+d_1*cos(theta)*E*I_zz])

# Eq 7: deflection d_2 = 0
m7 = np.mat([(1./6.)*cos(theta)*(x_2-x_1)**3,0.,0.,0.,0.,-(1./6.)*sin(theta)*(x_2-(x_2-(x_a/2)))**3, x_2, 1.])
u7 = np.mat([(1./24.)*q*cos(theta)*x_2**4])

# Eq 8: defelction d_3
m8 = np.mat([(1./6.)*cos(theta)*(x_3-x_1)**3,(1./6.)*(x_3-x_2)**3,0.,0.,0.,-(1./6.)*sin(theta)*(x_3-(x_2-(x_a/2)))**3,x_3,1.])
u8 = np.mat([(1./24.)*q*cos(theta)*x_3**4 - P*sin(theta)*(x_3-(x_2+(x_a/2)))**3+d_3*cos(theta)*E*I_zz])


M = np.concatenate((m1,m2,m3,m4,m5,m6,m7,m8))
u = np.concatenate((u1,u2,u3,u4,u5,u6,u7,u8))

X = inv(M)*u




F_H1_y = X[0][0]
print float(F_H1_y)





F_H1_y = float(X[0])
F_H2_y = float(X[1])
F_H3_y = float(X[2])
F_H1_z = float(X[3])
F_H2_z = float(X[4])
P_jam  = float(X[5])
C      = float(X[6])
L      = float(X[7])

print 'F_H1_y =', float(X[0])
print 'F_H2_y =', float(X[1])
print 'F_H3_y =', float(X[2])
print 'F_H1_z =', float(X[3])
print 'F_H2_z =', float(X[4])
print 'P_jam  =', float(X[5])
print 'C      =', float(X[6])
print 'L      =', float(X[7])



print 'Deflection = ,', (L/(E*I_zz))/cos(theta) # in gloval cooridinate system


