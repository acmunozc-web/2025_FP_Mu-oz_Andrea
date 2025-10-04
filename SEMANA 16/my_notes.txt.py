# Paso 1: Escritura de Archivo de Texto
with open("my_notes.txt", "w") as file:
    file.write("Primera línea: Recordar hacer backup semanal.\n")
    file.write("Segunda línea: Revisar logs de acceso cada viernes.\n")
    file.write("Tercera línea: Actualizar políticas de seguridad trimestralmente.\n")

# Paso 2: Lectura de Archivo de Texto
with open("my_notes.txt", "r") as file:
    # Leer línea por línea usando readline()
    linea = file.readline()
    while linea:
        print(linea.strip())  # Mostrar la línea sin saltos de línea extra
        linea = file.readline()

# Paso 3: Cierre de Archivos
# No es necesario cerrar manualmente porque usamos 'with', que lo hace automáticamente.
