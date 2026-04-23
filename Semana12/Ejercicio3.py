nota = float(input("Ingresa una nota (0-10): "))
if 9 <= nota <= 10:
    print("Excelente")
elif 7 <= nota < 9:
    print("Bueno")
elif nota == 6:
    print("Aprobado")
elif 0 <= nota <= 5:
    print("Reprobado")
