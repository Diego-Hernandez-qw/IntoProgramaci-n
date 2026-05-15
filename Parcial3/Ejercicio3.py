def monitorear_sensores():
    lecturas = []

    print("Ingrese 5 lecturas de temperatura (números enteros):")
    for i in range(5):
        try:
            temp = int(input(f"Lectura {i+1}: "))
            lecturas.append(temp)
        except ValueError:
            print("Error: Ingrese solo números enteros. Se registrará como 0.")
            lecturas.append(0)

    print("\n--- Reporte de Estado ---")

    for t in lecturas:
        match t:
            case 0:
                print(f"Temperatura {t}: Alerta: Punto de Congelación")
            case 100:
                print(f"Temperatura {t}: Alerta: Punto de Ebullición")
            case _:

                estado = "Estado: Estable" if 10 <= t <= 30 else "Estado: Crítico"
                print(f"Temperatura {t}: {estado}")


monitorear_sensores()
