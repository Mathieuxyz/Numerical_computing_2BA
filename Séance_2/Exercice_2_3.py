import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg

def translation_matrix_2D(tx: int,  ty: int): #working
    
    identity_matrix = np.identity(3)

    identity_matrix[0,2] = tx
    
    identity_matrix[1,2] = ty
    
    return identity_matrix

#paramètres
t = np.linspace(1/16,15/16, 8)*2*np.pi
x = np.cos(t)
y = np.sin(t)
s = [1]*len(x)
tx = 1
ty = 4

#calculations
v1 = np.array([x,y,s]) #dans cette disposition uniquement cela fonctionne !
T = translation_matrix_2D(tx, ty)
v2 = T@v1 #translated matrix

#drawings
plt.fill(v1[0],v1[1],"g")
plt.fill(v2[0],v2[1],"r")

plt.show()