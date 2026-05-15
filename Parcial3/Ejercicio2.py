from decimal import Decimal, InvalidOperation


def terminal_cobro_seguro():
    total_acumulado = Decimal("0.00")
    print("--- Terminal de Cobro Seguro ---")
    print("(Ingrese 0 para finalizar)")

    while True:
        entrada = input("Ingrese el precio del producto: ")

        try:

            precio = Decimal(entrada)

            if precio == 0:
                break

            total_acumulado += precio

        except (ValueError, InvalidOperation):
            print(
                "Advertencia: El valor ingresado no es un número válido. Intente de nuevo."
            )

    print(f"El total acumulado de la venta es: ${total_acumulado}")


terminal_cobro_seguro()
