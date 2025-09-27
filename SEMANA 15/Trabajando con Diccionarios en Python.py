# 1. Crear un Diccionario
informacion_personal = {
    "nombre": "Andrea",
    "edad": 22,
    "ciudad": "Quito",
    "profesión": "Ingeniera en TIC"
}

# 2. Acceder y Modificar Valores
informacion_personal["ciudad"] = "Cuenca"  # Cambio de ciudad
informacion_personal["profesión"] = "Ingeniera en TIC"  # Confirmación de profesión

# 3. Verificar Existencia de Clave
if "teléfono" not in informacion_personal:
    informacion_personal["teléfono"] = "099-456-7890"  # Número ficticio

# 4. Eliminar una Clave
informacion_personal.pop("edad", None)  # Eliminar edad

# 5. Imprimir el Diccionario Final
print(informacion_personal)
