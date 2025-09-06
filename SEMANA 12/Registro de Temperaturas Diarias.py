import numpy as np

# Definir las dimensiones de la matriz
ciudades = 3
dias_semana = 7
semanas = 4

# Crear la matriz 3D con datos de temperatura aleatorios
temperaturas = np.random.randint(15, 30, size=(ciudades, dias_semana, semanas))

# Definir los nombres de las ciudades y los días de la semana
nombres_ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias_semana_nombres = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Imprimir la matriz de temperaturas
for ciudad in range(ciudades):
    print(f"Ciudad: {nombres_ciudades[ciudad]}")
    for semana in range(semanas):
        print(f"Semana {semana+1}:")
        for dia in range(dias_semana):
            print(f"{dias_semana_nombres[dia]}: {temperaturas[ciudad, dia, semana]}°C")
        print()
    print()