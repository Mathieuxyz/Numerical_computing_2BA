import numpy as np
import cmath
import math as m

R = 1000 #ohms
C = 20*10^(-9) #Farads
F = 50 #Hz

def define_Zr(value: int): #working

    return complex(value,0)

def define_Zc(value: int, frequency: int): #working

    return complex(0,-(1/(2*np.pi*frequency*value)))

def parrallel_impedence(Z1: complex, Z2: complex):

    final_impedance = Z1 + Z1

    norm = m.sqrt((final_impedance.real)**2 +(final_impedance.imag)**2)

    phase = m.atan(final_impedance.imag/final_impedance.real)

    return np.array([norm, phase])

def series_impedence(Z1: complex, Z2: complex):

    final_impedance = (Z1*Z2)/(Z1+Z2)

    norm = m.sqrt((final_impedance.real)**2 + (final_impedance.imag)**2)

    phase = m.atan(final_impedance.imag/final_impedance.real)

    return np.array([norm, phase])

Zr = define_Zr(R)
Zc = define_Zc(R,F)

print(np.array([series_impedence(Zr,Zc), parrallel_impedence(Zr,Zc)]))

