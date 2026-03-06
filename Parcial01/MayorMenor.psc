Algoritmo MayorMenor
	//10.	Solicitar dos números y mostrar cuál es mayor y cuál es menor usando comparaciones (>, <, =). SI
	Definir num1, num2 Como Real
    
    Escribir "Ingrese el primer número:"
    Leer num1
    Escribir "Ingrese el segundo número:"
    Leer num2
    
    Si num1 > num2 Entonces
        Escribir "El número mayor es: ", num1
        Escribir "El número menor es: ", num2
    Sino
        Si num1 < num2 Entonces
            Escribir "El número mayor es: ", num2
            Escribir "El número menor es: ", num1
        Sino
            // Si no es mayor ni menor, por lógica son iguales
            Escribir "Ambos números son iguales (", num1, " = ", num2, ")"
        FinSi
    FinSi
FinAlgoritmo
