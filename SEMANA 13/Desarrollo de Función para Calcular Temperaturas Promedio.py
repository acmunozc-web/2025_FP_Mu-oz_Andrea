def calcular_temperatura_promedio_ciudades(datos_temperaturas):
    """
    Calcula la temperatura promedio para cada ciudad basada en datos de múltiples semanas.

    Parámetros:
    - datos_temperaturas (dict): Un diccionario donde las claves son nombres de ciudades
                                 y los valores son listas de listas de temperaturas (por semana y día).
                                 Ejemplo: {
                                     'Quito': [
                                         [18, 19, 20, 18, 22, 21, 20],  # Semana 1
                                         [19, 20, 21, 19, 23, 22, 21],  # Semana 2
                                     ],
                                     'Napo': [
                                         [25, 26, 27, 25, 28, 26, 27],  # Semana 1
                                         [26, 27, 28, 26, 29, 27, 28],  # Semana 2
                                     ],
                                     'Guayaquil': [
                                         [30, 31, 32, 30, 33, 31, 32],  # Semana 1
                                         [31, 32, 33, 31, 34, 32, 33],  # Semana 2
                                     ]
                                 }

    Retorna:
    - dict: Un diccionario con ciudades como claves y temperaturas promedio como valores.
    """
    promedios_ciudades = {}

    for ciudad, semanas in datos_temperaturas.items():
        total_temp = 0
        total_dias = 0

        for semana in semanas:
            total_temp += sum(semana)
            total_dias += len(semana)

        if total_dias > 0:
            promedio = total_temp / total_dias
            promedios_ciudades[ciudad] = round(promedio, 2)
        else:
            promedios_ciudades[ciudad] = None

    return promedios_ciudades


# Ejemplo de uso para Quito, Napo, Guayaquil
datos = {
    'Quito': [
        [18, 19, 20, 18, 22, 21, 20],  # Semana 1
        [19, 20, 21, 19, 23, 22, 21],  # Semana 2
        [20, 21, 22, 20, 24, 23, 22],  # Semana 3
        [21, 22, 23, 21, 25, 24, 23],  # Semana 4
    ],
    'Napo': [
        [25, 26, 27, 25, 28, 26, 27],  # Semana 1
        [26, 27, 28, 26, 29, 27, 28],  # Semana 2
        [27, 28, 29, 27, 30, 28, 29],  # Semana 3
        [28, 29, 30, 28, 31, 29, 30],  # Semana 4
    ],
    'Guayaquil': [
        [30, 31, 32, 30, 33, 31, 32],  # Semana 1
        [31, 32, 33, 31, 34, 32, 33],  # Semana 2
        [32, 33, 34, 32, 35, 33, 34],  # Semana 3
        [33, 34, 35, 33, 36, 34, 35],  # Semana 4
    ]
}

resultados = calcular_temperatura_promedio_ciudades(datos)
print("Temperaturas promedio por ciudad:")
for ciudad, promedio in resultados.items():
    if promedio is not None:
        print(f"{ciudad}: {promedio} °C")
    else:
        print(f"{ciudad}: No hay datos suficientes")