import numpy as np
from numpy.linalg import eig
#define constants
hw = 0.2
u = 1/np.sqrt(2) * np.array([[1,1,0]])
#define pauli matrices and the identity matrice
sigma_X = np.matrix([[0, 1], [1, 0]])
sigma_Y = np.matrix([[0, -1j], [1j, 0]])
sigma_Z = np.matrix([[1, 0], [0, -1]])
I = np.matrix([[1, 0], [0, 1]])

#define u sigma as the dot product between u and sigma
u_sigma = sum(u[0][0] * sigma_X, u[0][1]*sigma_Y, u[0][2]*sigma_Z)
###def part_a():
    #define with the equation
    #this is the hamiltonian
H = (hw/2) * u_sigma
H_square = H @ H
print(H_square)
#value of hw/2 to the power of 2 up to 8 decimals
hw_half_sq = round(((hw/2)**2).real, 8) + 1j * round(((hw/2)**2).imag, 8)
print('(h_bar * w/2)**2 =\n',hw_half_sq)
#is every matrix element of H*H equal to (hw/2)**2 and technically the identity matrix which is basiclaly multiplying by 1?:
#matrix with booleans in every matrix element according to the previous equality
elements_bool = (H_square == (hw_half_sq * I))
print('Boolean matrix =\n',elements_bool)

###def part_b():
down = np.array([0,1])
final_state = H * down

#if state down is an eigenstate, the det of the down state and vector H@down should be zero.
