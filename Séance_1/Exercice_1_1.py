import numpy as np
import cmath
import math as m

def define_Zr(value: int): #working

    return complex(value,0)

def define_Zc(value: int, frequency: int): #working

    return complex(0,-(1/(2*np.pi*frequency*value)))

def define_Zl(value: int, frequency: int): #working

    return complex(0,2*np.pi*frequency*value)

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



