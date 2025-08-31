def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"Valor {valor} encontrado en la posición ({i}, {j})"
    return f"Valor {valor} no encontrado en la matriz"

# Definir la matriz bidimensional
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Definir el valor a buscar
valor_a_buscar = 60

# Llamar a la función de búsqueda
resultado = buscar_valor(matriz, valor_a_buscar)

# Imprimir el resultado
print(resultado)