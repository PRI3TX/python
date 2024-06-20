def multiplicar_matrices(a, b):
    # Verificar que las matrices puedan multiplicarse (número de columnas de a = número de filas de b)
    if len(a[0]) != len(b):
        raise ValueError("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")

    # Inicializar la matriz resultado con ceros
    filas_a = len(a)
    columnas_a = len(a[0])
    filas_b = len(b)
    columnas_b = len(b[0])

    resultado = [[0 for _ in range(columnas_b)] for _ in range(filas_a)]

    # Realizar la multiplicación
    for i in range(filas_a):
        for j in range(columnas_b):
            for k in range(columnas_a):
                resultado[i][j] += a[i][k] * b[k][j]

    return resultado

# Ejemplo de uso
matriz_1 = [[1, 2], [3,4]]
matriz_2 = [[5, 6],[7, 8]]

resultado = multiplicar_matrices(matriz_1, matriz_2)

# Imprimir el resultado
for fila in resultado:
    print(fila)
