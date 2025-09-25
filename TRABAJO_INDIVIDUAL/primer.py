import numpy as np

v = np.array([1, 2, 3, 4, 5])
print("Vector v:", v)

M = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print("Matriz M:\n", M)

print("Transpuesta de M:\n", M.T)
print("Suma de todos los elementos de M:", M.sum())
print("Máximo de M:", M.max())
