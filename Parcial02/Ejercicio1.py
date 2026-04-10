animal = "  elefante  "

animal_limpio = animal.strip()

conteo_e = animal_limpio.count("e")

# Mostrar los resultados
print(f"Texto original: '{animal}'")
print(f"Texto limpio: '{animal_limpio}'")
print(f"La letra 'e' se repite {conteo_e} veces.")
