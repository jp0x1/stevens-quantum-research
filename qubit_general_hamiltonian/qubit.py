import numpy as np
import math
from matplotlib import pyplot as plt

#walkthrough the notebook, i have the work added in through a picture

#initialize with pauli matrices
o_x = np.matrix([[0,1],[1,0]])
o_y = np.matrix([[0,-1j],[1j,0]])
o_z = np.matrix([[1,0],[0,-1]])
#for the thing that looks like number 1
I = np.matrix([[1,0],[0,1]])
#initalize the vector sigma
o = [o_x,o_y,o_z]

wt = np.linspace(0, 4*np.pi, 120) #discretization of time variable(?)
down_state = np.matrix([[0],
                        [1]]) #down state, initial state of qubit

#Ut = cos(wt/2)I - isin(wt/2)u*o
def U(wt):
    #equation provided above!
    Ut = np.cos(wt/2) * I -1j/np.sqrt(2) * np.sin(wt/2)*(o_x+o_y)
    return Ut
def heisenberg_picture(operator, equation):
    #complex conjugate of U * o_z * U
    #getH() function returns complex conjugate
    s = equation.getH() * operator * equation
    return s
#calculate what we want <down| oz,H(t) |down>
def expectation_value(vector, operator):
    #calculate complex conjugate * operator * vector
    v = vector.getH() * operator * vector
    v = complex(v)
    return v
#generate list of expectation values to plot calculated values
values = [expectation_value(down_state, heisenberg_picture(o_z, U(i))) for i in wt]

#create figure
plt.figure(figsize = (11,4), dpi=300)
plt.plot(wt, [i.real for i in values], label='Real num.', c='coral', linewidth=5, alpha=0.5, zorder=2)
#if there's any imaginary value different than 0, plot the imaginary part at all times:
if not [i.imag for i in values]:
    plt.plot(wt, [i.imag for i in values], label='Imag. num.', c='paleturquoise', linewidth = 5, zorder = 1)


#WHAT DOES THE GRAPH SHOW???
#the graph shows the expectation value vs the period (i think)
#expectation value is the average of all possible outcomes weighted by probabilities
#expectation value of the heisenberg picture being in the down state(?)
plt.xlabel(r'$\omega t$')
plt.ylabel(r'$\langle \hat{\sigma}_{z,H} \rangle$')
plt.xticks([np.pi * i for i in range(5)], ['0', r'$\pi$']+[r'$'+str(i+2)+'\pi$' for i in range(3)])
plt.yticks([-1, -0.5, 0, 0.5, 1], [str(i/2 - 1) for i in range(5)])
plt.legend()
plt.tick_params(axis="both", direction="in")
#plt.savefig('1e.pdf', dpi=400)
plt.show()