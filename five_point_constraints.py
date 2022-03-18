from sympy import *
from sympy.combinatorics import Permutation

x,y,z = symbols('x y z', reaL=True)
e11,e21,e31,e41,e51,e61,e71,e81,e91 = symbols('e11 e21 e31 e41 e51 e61 e71 e81 e91', real=True)
e12,e22,e32,e42,e52,e62,e72,e82,e92 = symbols('e12 e22 e32 e42 e52 e62 e72 e82 e92', real=True)
e13,e23,e33,e43,e53,e63,e73,e83,e93 = symbols('e13 e23 e33 e43 e53 e63 e73 e83 e93', real=True)
e14,e24,e34,e44,e54,e64,e74,e84,e94 = symbols('e14 e24 e34 e44 e54 e64 e74 e84 e94', real=True)

E1 = Matrix([[e11,e21,e31],[e41,e51,e61],[e71,e81,e91]]).transpose()
E2 = Matrix([[e12,e22,e32],[e42,e52,e62],[e72,e82,e92]]).transpose()
E3 = Matrix([[e13,e23,e33],[e43,e53,e63],[e73,e83,e93]]).transpose()
E4 = Matrix([[e14,e24,e34],[e44,e54,e64],[e74,e84,e94]]).transpose()

print(E1)
print(E2)
print(E3)
print(E4)

E = x*E1 +y*E2+z*E3+E4
# Constraints - Both lines are equal to 0
E_det = E.det()
E_c = 2*E*E.transpose()*E - (E*E.transpose()).trace()*E

E_c_1 = E_c[0,0]
E_c_2 = E_c[1,0]
E_c_3 = E_c[2,0]
E_c_4 = E_c[0,1]
E_c_5 = E_c[1,1]
E_c_6 = E_c[2,1]
E_c_7 = E_c[0,2]
E_c_8 = E_c[1,2]
E_c_9 = E_c[2,2]

poly_det = poly(E_det,x,y,z)
poly_c1 = poly(E_c_1,x,y,z)
poly_c2 = poly(E_c_2,x,y,z)
poly_c3 = poly(E_c_3,x,y,z)
poly_c4 = poly(E_c_4,x,y,z)
poly_c5 = poly(E_c_5,x,y,z)
poly_c6 = poly(E_c_6,x,y,z)
poly_c7 = poly(E_c_7,x,y,z)
poly_c8 = poly(E_c_8,x,y,z)
poly_c9 = poly(E_c_9,x,y,z)

E_det_coeffs = poly_det.coeffs()
E_det_monoms = poly_det.monoms()
E_c1_coeffs = poly_c1.coeffs()
E_c1_monoms = poly_c1.monoms()
E_c2_coeffs = poly_c2.coeffs()
E_c2_monoms = poly_c2.monoms()
E_c3_coeffs = poly_c3.coeffs()
E_c3_monoms = poly_c3.monoms()
E_c4_coeffs = poly_c4.coeffs()
E_c4_monoms = poly_c4.monoms()
E_c5_coeffs = poly_c5.coeffs()
E_c5_monoms = poly_c5.monoms()
E_c6_coeffs = poly_c6.coeffs()
E_c6_monoms = poly_c6.monoms()
E_c7_coeffs = poly_c7.coeffs()
E_c7_monoms = poly_c7.monoms()
E_c8_coeffs = poly_c8.coeffs()
E_c8_monoms = poly_c8.monoms()
E_c9_coeffs = poly_c9.coeffs()
E_c9_monoms = poly_c9.monoms()

print(len(E_det_coeffs))

print('-----')

print(E_c1_monoms)

#Permute the constraints such that they line up with the construction in Photogrammetric Computer Vision
P = Permutation([0,1,2,4,5,7,10,11,13,16,3,6,8,12,14,17,9,15,18,19])
E_det_coeffs_p = P(E_det_coeffs)
E_det_monoms_p = P(E_det_monoms)
E_c1_coeffs_p = P(E_c1_coeffs)
E_c1_monoms_p = P(E_c1_monoms)
E_c2_coeffs_p = P(E_c2_coeffs)
E_c2_monoms_p = P(E_c2_monoms)
E_c3_coeffs_p = P(E_c3_coeffs)
E_c3_monoms_p = P(E_c3_monoms)
E_c4_coeffs_p = P(E_c4_coeffs)
E_c4_monoms_p = P(E_c4_monoms)
E_c5_coeffs_p = P(E_c5_coeffs)
E_c5_monoms_p = P(E_c5_monoms)
E_c6_coeffs_p = P(E_c6_coeffs)
E_c6_monoms_p = P(E_c6_monoms)
E_c7_coeffs_p = P(E_c7_coeffs)
E_c7_monoms_p = P(E_c7_monoms)
E_c8_coeffs_p = P(E_c8_coeffs)
E_c8_monoms_p = P(E_c8_monoms)
E_c9_coeffs_p = P(E_c9_coeffs)
E_c9_monoms_p = P(E_c9_monoms)


print(E_c1_monoms_p)

assert(E_det_monoms_p == E_c1_monoms_p)
assert(E_det_monoms_p == E_c2_monoms_p)
assert(E_det_monoms_p == E_c3_monoms_p)
assert(E_det_monoms_p == E_c4_monoms_p)
assert(E_det_monoms_p == E_c5_monoms_p)
assert(E_det_monoms_p == E_c6_monoms_p)
assert(E_det_monoms_p == E_c7_monoms_p)
assert(E_det_monoms_p == E_c8_monoms_p)
assert(E_det_monoms_p == E_c9_monoms_p)