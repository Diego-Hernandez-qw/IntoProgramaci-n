notas = []
while True:
    nota = float(input("Ingresa una nota (0-10) o -1 para terminar: "))
    if nota == -1:
        break
    if 0 <= nota <= 10:
        notas.append(nota)
    else:
        print("Nota inválida, será ignorada.")

if len(notas) > 0:
    suma = 0
    for n in notas:
        suma += n
    promedio = suma / len(notas)
    print(f"El promedio de las {len(notas)} notas válidas es: {promedio:.2f}")
else:
    print("No se ingresaron notas válidas.")
