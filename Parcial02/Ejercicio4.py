palabra = "CANTANDO"

palabra_minuscula = palabra.lower()

palabra_final = palabra_minuscula.removesuffix("ando")

indice_t = palabra_final.find("t")

# Mostrar resultados
print(f"Palabra en minúsculas: {palabra_minuscula}")
print(f"Palabra después de quitar el sufijo: {palabra_final}")
print(f"La letra 't' se encuentra en el índice: {indice_t}")
