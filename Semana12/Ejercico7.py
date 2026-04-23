monto = float(input("Ingresa el monto de la compra: "))
if monto > 100:
    total = monto * 0.80
elif 50 <= monto <= 100:
    total = monto * 0.90
else:
    total = monto
print(f"Total a pagar: {total}")
