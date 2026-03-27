def transformar_texto(texto, opcion):
    """
    Función que transforma un texto según el orden:
    1: Mayúsculas, 2: Minúsculas, 3: Capitalización
    """
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    else:
        return "Opción no válida"


# Ejemplo de uso:
mi_texto = "el amor es una magia que tiene muchos traumas"

print("1. Mayúsculas:", transformar_texto(mi_texto, 1))
print("2. Minúsculas:", transformar_texto(mi_texto, 2))
print("3. Primera letra en mayúscula:", transformar_texto(mi_texto, 3))
