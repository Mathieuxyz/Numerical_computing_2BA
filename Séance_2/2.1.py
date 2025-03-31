import numpy as np

matrix_1 = np.array([1,7,3,8,5,2,7,4,9]).reshape(3,3)

inverse = np.linalg.inv(matrix_1)

determinent = np.linalg.det(matrix_1)

eigenvalues = np.linalg.eig(matrix_1)

matrix_2 = matrix_1**2

print(matrix_1[2,1]) #d'abord les lignes et seulement ensuite les colonnes !

matrix_4 = matrix_1[1:, :2]

print(matrix_4)
