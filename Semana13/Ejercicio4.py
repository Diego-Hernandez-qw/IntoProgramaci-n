impares = []
suma = 0
while True:
    num = int(input("Ingresa un número (0 para salir): "))
    if num == 0:
        break
    if num % 2 != 0:
        impares.append(num)
        suma += num

print(f"Suma total: {suma}")
print("Números impares ingresados:")
for n in impares:
    print(n)
