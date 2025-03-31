import numpy as np
from scipy import linalg
import cmath
import math as m

Ug = 230
fg = 50
R1 = 10
R2 = 3
C = 10*10**(-6)
L = 100*10**(-3)

def define_Zr(value: int): #working

    return complex(value,0)

def define_Zc(value: int, frequency: int): #working

    return complex(0,-(1/(2*np.pi*frequency*value)))

def define_Zl(value: int, frequency: int):

    return complex(0, 2*np.pi*frequency*value)

p = np.array([Ug, fg, define_Zr(R1), define_Zr(R2), define_Zc(C, fg), define_Zl(L, fg)])

A = np.array([[p[2], p[4], 0], [0, -p[4], p[3] + p[5]], [1,-1, -1]])
b = np.array([p[1], 0, 0])

x = np.linalg.inv(A)@b

print(x)

