import random

secreto = random.randint(1, 100)
intentos_realizados = []

print("¡Adivina el número secreto entre 1 y 100!")

while True:
    intento = int(input("Tu intento: "))
    intentos_realizados.append(intento)

    if intento == secreto:
        print("¡Felicidades! Acertaste.")
        break
    elif intento < secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")

print("Historial de intentos:")
for i in intentos_realizados:
    print(f"- {i}")
