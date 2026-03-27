def transformar_lista(lista_palabras, opcion):
    """
        Crear una función que reciba una lista de palabras y un número.
        La función debe transformar cada palabra de la lista según la opción
        seleccionada (1, 2 o 3).
    .
    """
    lista_transformada = []

    for palabra in lista_palabras:
        if opcion == 1:
            lista_transformada.append(palabra.upper())
        elif opcion == 2:
            lista_transformada.append(palabra.lower())
        elif opcion == 3:
            lista_transformada.append(palabra.capitalize())
        else:
            print("Error: Opción no válida.")
            return

    print(f"\nLista original: {lista_palabras}")
    print(f"Lista con opción {opcion}: {lista_transformada}")


mis_palabras = ["sistemas", "programacion", "algoritmos", "python"]

print("Seleccione transformación (1: MAYÚS, 2: minús, 3: Capitalizar)")
seleccion = int(input("Opción: "))
