from SVV_input import *
from centroid_MOI import *

I_zz = MOIZZAirfoil(t_st, h_st, w_st, BetaStringers, y_cst)

# M*x=u
# M is an 10x10 matrix with all the coefficients
# x is the matrix with the unknowns ([F_H1_y, F_H2_y, F_H3_y, F_H1_z, F_H2_z, P_jam, C , L, W, U])
# u is the output matrix

# Eq 1: Force equilibrium in y-direction
m1 = np.mat([1.,1.,1.,0.,0.,sin(theta),0.,0.,0.,0.])     
u1 = np.mat([P*sin(theta)+q*l_a*cos(theta)])

# Eq 2: Force equilibrium in z-axis
m2 = np.mat([0.,0.,0.,1.,1.,cos(theta),0.,0.,0.,0.])
u2 = np.mat([P*cos(theta)-q*l_a*sin(theta)])

# Eq 3: Moment equilibrium x-axis
m3 = np.mat([0,0.,0.,0.,0.,(h/2.)*cos(theta)-(h/2.)*sin(theta),0.,0.,0.,0.])
u3 = np.mat([P*(h/2)*cos(theta)-P*(h/2)*sin(theta)+q*l_a*cos(theta)*(0.25*C_a-(h/2.))])

# Eq 4: Moment equilibrium y-axis
m4 = np.mat([0.,0.,0.,-(x_2-x_1),0.,-(x_a/2.)*cos(theta),0.,0.,0.,0.])
u4 = np.mat([-q*l_a*sin(theta)*((l_a/2.)-x_2)+P*cos(theta)*(x_a/2.)])

# Eq 5: Moment equilibrium z-axis
m5 = np.mat([-(l_a-x_1),-(l_a-x_2),-(l_a-x_3),0.,0.,-sin(theta)*(l_a-(x_2-(x_a/2.))),0.,0.,0.,0.])
u5 = np.mat([-P*sin(theta)*(l_a-(x_2+(x_a/2.))) - q*l_a*cos(theta)*(l_a/2.)])

# Note that deflections d1 and d3 need to be transformed to the aileron based axis system.
# d1 becomes d1*cos(theta) in the aileron y-coordinate and d1*sin(theta) in the aileron z-coordinate.
# The same applies to d3.
# There are in two types of delfection in the aileron based coordinate system and there are five equations.
# The follow constants of integration also need be determined for the two types of delflection:
# C and L for (aileron) y deflection; W and U for (ailron) z deflection.

# Eq 6: deflection d_1 (in aileron y-coordinate)
m6 = np.mat([0.,0.,0.,0.,0.,0.,x_1,1.,0.,0.])
u6 = np.mat([(1./24.)*q*cos(theta)*x_1**4+d_1*E*I_zz*cos(theta)])

# Eq 7: deflection d_1_z = 0 (in aileron z-coordinate)
m7 = np.mat([0.,0.,0.,0.,0.,0.,0.,0.,x_1,1.])
u7 = np.mat([-(1./24.)*q*sin(theta)*x_1**4])

# Eq 8: deflection d_2 = 0 (in aileron y-coordinate)
m8 = np.mat([(1./6.)*(x_2-x_1)**3,0.,0.,0.,0.,(1./6.)*sin(theta)*(x_2-(x_2-(x_a/2)))**3, x_2, 1. ,0.,0.])
u8 = np.mat([(1./24.)*q*cos(theta)*x_2**4])

# Eq 9: defelction d_2_z = 0 (in aileron z-coordinate)
m9 = np.mat([0.,0.,0.,(1./6.)*(x_2-x_1)**3,(1./6.)*(x_2-x_2)**3,0.,0.,0.,x_2,1.])
u9 = np.mat([(-1./24.)*q*sin(theta)*x_2**4])

# Eq 10: defelction d_3 (in aileron y-coordinate)
m10 = np.mat([(1./6.)*(x_3-x_1)**3,(1./6.)*(x_3-x_2)**3,0.,0.,0.,(1./6.)*sin(theta)*(x_3-(x_2-(x_a/2)))**3,x_3,1.,0.,0.])
u10 = np.mat([(1./24.)*q*cos(theta)*x_3**4 + P*sin(theta)*(x_3-(x_2+(x_a/2)))**3+d_3*E*I_zz*cos(theta)])


M = np.concatenate((m1,m2,m3,m4,m5,m6,m7,m8,m9,m10))
u = np.concatenate((u1,u2,u3,u4,u5,u6,u7,u8,u9,u10))

X = inv(M)*u

F_H1_y = float(X[0])
F_H2_y = float(X[1])
F_H3_y = float(X[2])
F_H1_z = float(X[3])
F_H2_z = float(X[4])
P_jam  = float(X[5])
C      = float(X[6])
L      = float(X[7])
W      = float(X[8])
U      = float(X[9])

print 'F_H1_y =', float(X[0])
print 'F_H2_y =', float(X[1])
print 'F_H3_y =', float(X[2])
print 'F_H1_z =', float(X[3])
print 'F_H2_z =', float(X[4])
print 'P_jam  =', float(X[5])
print 'C      =', float(X[6])
print 'L      =', float(X[7])
print 'W      =', W
print 'U      =', U
print 'Deflection_y_0 =', (L/(E*I_zz))/cos(theta) # in global cooridinate system
print 'Deflection_z_0 =', (U/(E*I_zz))/cos(theta) # in global coordinate system

