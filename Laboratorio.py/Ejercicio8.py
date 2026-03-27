def transformar_texto(texto, opcion):
    """
    Crear un programa con menú que permita al usuario ingresar un texto y
    elegir una opción (1, 2 o 3).
    El programa debe usar una función para aplicar la transformación
    seleccionada.
    """
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    else:
        return None


def mostrar_menu():
    print("\n--- MENÚ DE TRANSFORMACIÓN ---")
    print("1. Convertir a Mayúsculas")
    print("2. Convertir a Minúsculas")
    print("3. Capitalizar (Primera letra mayúscula)")
    print("4. Salir del programa")
    print("-" * 30)


while True:
    mostrar_menu()

    try:
        seleccion = int(input("Seleccione una opción (1-4): "))

        if seleccion == 4:
            print("Saliendo del programa... ¡Hasta pronto!")
            break

        if seleccion in [1, 2, 3]:
            frase = input("Ingrese el texto a transformar: ")
            resultado = transformar_texto(frase, seleccion)

            print("\n" + "=" * 40)
            print(f"RESULTADO: {resultado}")
            print("=" * 40)
        else:
            print("\n[!] Error: Por favor, elija una opción válida entre 1 y 4.")

    except ValueError:
        print("\n[!] Error: Debe ingresar un número entero.")
