import numpy as np

# Crear una matriz de NumPy
matriz = np.array([[1, 2],[3, 4]])

# Mostrar la matriz
print("Matriz original:")
print(matriz)

# Realizar operaciones con la matriz
print("Suma:", matriz.sum())
print("Media:", matriz.mean())
print("Desviación estándar:", matriz.std())

# Crear una nueva matriz con valores aleatorios
matriz_aleatoria = np.random.rand(2, 2)
print("Matriz aleatoria:")
print(matriz_aleatoria)

# Calcular el determinante de la matriz
determinante = np.linalg.det(matriz)
print("Determinante:", determinante)

# Calcular la inversa de la matriz
inversa = np.linalg.inv(matriz)
print("Matriz inversa:")
print(inversa)
