clave_correcta = "python123"
fallidos = []
while True:
    intento = input("Ingresa la contraseña: ")
    if intento == clave_correcta:
        print("Acceso concedido.")
        break
    else:
        print("Incorrecta.")
        fallidos.append(intento)

print(f"Tuviste {len(fallidos)} intentos fallidos:")
for f in fallidos:
    print(f"- {f}")
