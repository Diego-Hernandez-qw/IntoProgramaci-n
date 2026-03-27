def transformar_con_validacion(texto, opcion):
    """
    Crear una función que reciba un texto y un número.
    Si el número no es 1, 2 o 3, debe mostrar un mensaje de
    “opción inválida”.
    """
    if opcion == 1:
        print(f"Resultado (Mayúsculas): {texto.upper()}")
    elif opcion == 2:
        print(f"Resultado (Minúsculas): {texto.lower()}")
    elif opcion == 3:
        print(f"Resultado (Capitalización): {texto.capitalize()}")
    else:
        print("Opción inválida")


mi_mensaje = "Sistemas Informáticos"

try:
    opcion_usuario = int(input("Ingrese una opción (1, 2 o 3): "))
    transformar_con_validacion(mi_mensaje, opcion_usuario)
except ValueError:
    print("Error: Por favor, ingrese un número entero.")
