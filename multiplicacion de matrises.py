filas = int(input("filas "))
columnas = int(input("columnas "))
matriz = []
matriz_2=[]
m_matrices=[]
for a in range(filas):
    matriz.append([None]*columnas)
    matriz_2.append([None]*columnas)
    m_matrices.append([None]*columnas)
for i in range(filas):
    for j in range(columnas):
        matriz[i][j]=int(input("ingrese los numeros "))
for i in range(filas):
    for j in range(columnas):
        matriz[i][j]=int(input("ingrese los numeros "))
for i in range(filas):
    for j in range(columnas):
        m_matrices[i][j] = matriz[i][j] * matriz_2[j][i]