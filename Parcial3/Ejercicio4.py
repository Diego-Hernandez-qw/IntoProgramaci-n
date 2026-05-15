def auditar_registros():
    print("Iniciando auditoría de registros...\n")

    for registro in range(1, 51):

        if registro == 42:
            print(f"!!! AMENAZA DE SEGURIDAD DETECTADA EN ID: {registro} !!!")
            print("Abortando sistema...")
            break

        if registro % 3 == 0:
            continue

        print(f"Procesando registro ID: {registro}")


auditar_registros()
