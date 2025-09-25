import numpy as np

# Crear un vector
v = np.array([1, 2, 3, 4, 5])
print("Vector v:", v)

# Crear una matriz 3x3
M = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print("\nMatriz M:\n", M)

# Operaciones básicas
print("\nTranspuesta de M:\n", M.T)
print("Suma de todos los elementos de M:", M.sum())
print("Máximo de M:", M.max())
