def procesar_palabra(palabra, opcion):
    """Crear una función que reciba una palabra y un número,
    y muestre el resultado en pantalla aplicando la transformación
    correspondiente (1, 2 o 3).
    """
    if opcion == 1:
        resultado = palabra.upper()
        print(f"Opción 1 (Mayúsculas): {resultado}")
    elif opcion == 2:
        resultado = palabra.lower()
        print(f"Opción 2 (Minúsculas): {resultado}")
    elif opcion == 3:
        resultado = palabra.capitalize()
        print(f"Opción 3 (Capitalización): {resultado}")
    else:
        print("Error: El número ingresado no es válido (debe ser 1, 2 o 3).")


mi_palabra = "ingeniería"

print(f"Palabra base: {mi_palabra}")
print("-" * 25)
procesar_palabra(mi_palabra, 1)
procesar_palabra(mi_palabra, 2)
procesar_palabra(mi_palabra, 3)
