import numpy as np
datos = np.array([12, 13, 15, 14, 16, 17, 13, 95, 14, 15, 16, 200, 13, 14])

media = np.mean(datos)
desv = np.std(datos)

outliers = [x for x in datos if (x < media - 2*desv) or (x > media + 2*desv)]

print("Media:", media)
print("Desviación estándar:", desv)
print("Valores atípicos detectados:", outliers)
