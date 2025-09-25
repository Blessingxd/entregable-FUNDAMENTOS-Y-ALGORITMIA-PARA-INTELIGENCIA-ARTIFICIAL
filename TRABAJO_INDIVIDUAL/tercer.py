import numpy as np
A = np.array([[2, 1],
              [1, -1]])

b = np.array([5, 1])

sol = np.linalg.solve(A, b)
print("Solución del sistema: x =", sol[0], ", y =", sol[1])
