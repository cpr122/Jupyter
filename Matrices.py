import numpy as np

# Crear una matriz 3x3
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Acceder a un elemento
print(matriz[1, 2])  # Imprime 6

# Sumar dos matrices
otra_matriz = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
resultado = matriz + otra_matriz
print(resultado)
 
