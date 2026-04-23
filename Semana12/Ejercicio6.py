dia = int(input("Ingresa un número del 1 al 7: "))
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

if 1 <= dia <= 7:
    print(dias[dia - 1])
else:
    print("Error: El número no está en el rango.")
