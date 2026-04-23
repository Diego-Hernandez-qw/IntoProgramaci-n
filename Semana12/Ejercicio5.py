n1 = float(input("Primer número: "))
n2 = float(input("Segundo número: "))
op = input("Operación (+, -, *, /): ")

if op == "+":
    print(f"Resultado: {n1 + n2}")
elif op == "-":
    print(f"Resultado: {n1 - n2}")
elif op == "*":
    print(f"Resultado: {n1 * n2}")
elif op == "/":
    if n2 != 0:
        print(f"Resultado: {n1 / n2}")
    else:
        print("Error: División por cero")
