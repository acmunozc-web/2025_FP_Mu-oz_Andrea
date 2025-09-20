# Definimos la función CalcularDescuento
def CalcularDescuento(monto_total, porcentaje=25):
    """
    Calcula el descuento aplicando un porcentaje al monto total.

    Parámetros:
    monto_total (float): El valor total de la compra.
    porcentaje (float): Porcentaje de descuento (por defecto 25).

    Retorna:
    float: El valor del descuento calculado.
    """
    descuento = monto_total * (porcentaje / 100)
    return descuento


# Programa principal
def main():
    # Primera llamada: solo monto total (descuento por defecto 25%)
    monto1 = 200
    descuento1 = CalcularDescuento(monto1)
    total1 = monto1 - descuento1
    print("Compra 1:")
    print(f" Monto total: ${monto1:.2f}")
    print(f" Descuento aplicado: ${descuento1:.2f}")
    print(f" Total a pagar: ${total1:.2f}\n")

    # Segunda llamada: monto total con porcentaje definido (ejemplo 10%)
    monto2 = 500
    porcentaje2 = 10
    descuento2 = CalcularDescuento(monto2, porcentaje2)
    total2 = monto2 - descuento2
    print("Compra 2:")
    print(f" Monto total: ${monto2:.2f}")
    print(f" Descuento aplicado ({porcentaje2}%): ${descuento2:.2f}")
    print(f" Total a pagar: ${total2:.2f}")


# Ejecutamos el programa principal
if __name__ == "__main__":
    main()
