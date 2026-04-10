texto = "Diego Alexander"

texto_normalizado = texto.casefold()


es_alfabetico = texto_normalizado.isalpha()

print(f"Texto normalizado: '{texto_normalizado}'")
print(f"¿Es solo alfabético?: {es_alfabetico}")
