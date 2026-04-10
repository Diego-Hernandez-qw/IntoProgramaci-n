texto = "  el nido matinal  "
texto_limpio = texto.strip().title()

resultado_final = texto_limpio.center(30, "-")

print(f"Texto procesado: '{texto_limpio}'")
print(f"Resultado final: {resultado_final}")
