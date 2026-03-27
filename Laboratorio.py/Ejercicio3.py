def procesar_entrada(texto, opcion):
    """
    Solicitar al usuario un texto y un número.
    Enviar esos datos a una función que aplique la transformación
    según la opción elegida.
    """
    if opcion == 1:
        resultado = texto.upper()
        print(f"\n[Resultado Mayúsculas]: {resultado}")
    elif opcion == 2:
        resultado = texto.lower()
        print(f"\n[Resultado Minúsculas]: {resultado}")
    elif opcion == 3:
        resultado = texto.capitalize()
        print(f"\n[Resultado Capitalización]: {resultado}")
    else:
        print("\nError: La opción ingresada no es válida (1, 2 o 3).")


# --- Bloque Principal ---

# 1. Solicitamos el texto al usuario
usuario_texto = input("Ingrese el texto que desea transformar: ")

# 2. Solicitamos la opción y la convertimos a entero (int)
print("Opciones disponibles:")
print("1. Todo en mayúsculas")
print("2. Todo en minúsculas")
print("3. Primera letra en mayúscula")

usuario_opcion = int(input("Seleccione una opción (1-3): "))
