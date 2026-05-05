def sistema_de_turnos():

    cola_activa = True

    print("--- SISTEMA DE GESTIÓN DE TURNOS ---")

    while cola_activa:
        print("\n--- Nuevo Cliente en Ventanilla ---")

        print("Tipos de servicio: 1. Caja | 2. Consultoría | 3. Reclamos")
        opcion = input("Seleccione el tipo de servicio (1-3): ")

        match opcion:
            case "1":
                servicio = "Caja"
            case "2":
                servicio = "Consultoría"
            case "3":
                servicio = "Reclamos"
            case _:
                servicio = "General"
                print("Opción no válida, asignado a General.")

        es_prioridad = input("¿Es cliente con prioridad? (s/n): ").lower()
        if es_prioridad == "s":
            prioridad_status = "ALTA (Atención inmediata)"
        else:
            prioridad_status = "Normal"

        print(f"\nGenerando turno para {servicio} - Prioridad: {prioridad_status}")

        print("Iniciando proceso...")
        pasos_atencion = [
            "Verificando identidad",
            "Procesando solicitud",
            "Finalizando turno",
        ]
        for paso in pasos_atencion:
            print(f" -> {paso}...")

        continuar = input("\n¿Hay más personas en la cola? (s/n): ").lower()
        if continuar != "s":
            cola_activa = False
            print("Cerrando sistema de atención. ¡Buen día!")


if __name__ == "__main__":
    sistema_de_turnos()
