numero_texto = "42"
numero_relleno = numero_texto.zfill(5)


termina_en_dos = numero_relleno.endswith("2")

print(f"Texto original: {numero_texto}")
print(f"Texto con relleno: {numero_relleno}")
print(f"¿Termina con '2'?: {termina_en_dos}")
