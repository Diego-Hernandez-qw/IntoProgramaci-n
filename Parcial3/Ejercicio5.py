def transformar_nombres():
    nombre_completo = input("Ingrese su nombre y apellido: ")

    partes_nombre = nombre_completo.split()[::-1]

    print("\n--- Nombre Formateado (Privacidad) ---")

    for palabra in partes_nombre:
        letras_formateadas = []

        for letra in palabra:
            letras_formateadas.append(letra)

        resultado_palabra = ".".join(letras_formateadas)
        print(resultado_palabra)


transformar_nombres()
