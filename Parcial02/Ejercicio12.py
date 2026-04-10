nombre_archivo = "ING. Su nombre.txt"
texto_sin_sufijo = nombre_archivo.removesuffix(".txt")
texto_limpio = texto_sin_sufijo.removeprefix("ING. ")

texto_minusculas = texto_limpio.lower()
lista_palabras = texto_minusculas.split()

print(f"Texto tras quitar extension y prefijo: '{texto_limpio}'")
print(f"Lista final de palabras: {lista_palabras}")
