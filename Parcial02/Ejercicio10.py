texto = "Python2026"


if texto.isalnum():
    print("El texto es alfanumérico.")

    texto_minuscula = texto.lower()

    texto_limpio = texto_minuscula.replace("2026", "")

    print(f"Resultado final: '{texto_limpio}'")
else:
    print("El texto contiene símbolos o espacios y no se puede procesar.")
