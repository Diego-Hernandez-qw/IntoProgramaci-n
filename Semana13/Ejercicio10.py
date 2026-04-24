numeros_validos = []
suma_total = 0

while suma_total <= 100:
    num = float(input(f"Suma actual ({suma_total}). Ingresa un número: "))
    if num >= 0:
        suma_total += num
        numeros_validos.append(num)
    else:
        print("Número negativo ignorado.")

print("--- Límite superado ---")
print(f"Suma final: {suma_total}")
print("Números válidos ingresados:")
for n in numeros_validos:
    print(n)
