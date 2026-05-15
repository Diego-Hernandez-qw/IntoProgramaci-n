def procesar_rastreo():
    etiqueta = input("Ingrese el código de rastreo (AÑO-CATEGORÍA-PAÍS): ")

    if not etiqueta:
        print("Error: El código no puede estar vacío. Programa finalizado.")
        return

    primer_guion = etiqueta.find("-")
    segundo_guion = etiqueta.rfind("-")

    if primer_guion != -1 and segundo_guion != -1:
        categoria = etiqueta[primer_guion + 1 : segundo_guion]
        print(f"Categoría extraída: {categoria}")
    else:
        print("Error: Formato de código inválido.")
        return

    resultado = "Ruta Local" if etiqueta.endswith("SV") else "Ruta Internacional"
    print(resultado)


procesar_rastreo()
