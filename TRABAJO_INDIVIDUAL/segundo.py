import numpy as np 
a = np.array([2, 3, 4])
b = np.array([1, 0, -1])

producto_punto = np.dot(a, b)
print("Producto punto:", producto_punto)

norma_a = np.linalg.norm(a)
print("Norma del vector a:", norma_a)
