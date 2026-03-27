def transformar_y_contar(texto, opcion):
    """
    Crear una función que reciba un texto y un número,
    transforme el texto según la opción y luego devuelva la cantidad de
    caracteres del resultado.
    """
    if opcion == 1:
        resultado = texto.upper()
    elif opcion == 2:
        resultado = texto.lower()
    elif opcion == 3:
        resultado = texto.capitalize()
    else:
        print("Opción inválida")
        return 0  # Devolvemos 0 si la opción no es válida

    # Mostramos el texto transformado
    print(f"Texto transformado: {resultado}")

    # Devolvemos la cantidad de caracteres
    return len(resultado)


# --- Bloque de ejecución ---
usuario_texto = input("Escribe una palabra o frase: ")
usuario_opcion = int(input("Opción (1: Mayús, 2: minús, 3: Cap): "))

# Guardamos el valor que devuelve la función en una variable
cantidad = transformar_y_contar(usuario_texto, usuario_opcion)

if cantidad > 0:
    print(f"El resultado tiene {cantidad} caracteres.")
