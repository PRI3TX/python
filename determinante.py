def determinante_3x3(x):
    """
    Calcula la determinante de una matriz 3x3 usando la regla de Sarrus.
    """
    # Asignar los elementos de la matriz a variables para facilitar la lectura
    a, b, c = x[0]
    d, e, f = x[1]
    g, h, i = x[2]

    # Usar la regla de Sarrus para calcular la determinante
    det = (a * e * i + b * f * g + c * d * h) - (c * e * g + b * d * i + a * f * h)
    return det

# Ejemplo de uso
matriz_3x3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Calcular y imprimir la determinante de la matriz 3x3
print(f"Determinante de la matriz 3x3: {determinante_3x3(matriz_3x3)}")