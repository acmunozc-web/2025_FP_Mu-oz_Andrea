def ordenar_fila(matriz, fila):
    # Ordenar la fila utilizando el algoritmo de burbuja
    for i in range(len(matriz[fila])):
        for j in range(len(matriz[fila]) - 1):
            if matriz[fila][j] > matriz[fila][j + 1]:
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

# Definir la matriz bidimensional
matriz = [
    [10, 20, 30],
    [90, 40, 60],
    [70, 80, 50]
]

# Imprimir la matriz original
print("Matriz original:")
imprimir_matriz(matriz)

# Definir la fila a ordenar
fila_a_ordenar = 1

# Ordenar la fila
matriz_ordenada = ordenar_fila([fila[:] for fila in matriz], fila_a_ordenar)

# Imprimir la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
imprimir_matriz(matriz_ordenada)