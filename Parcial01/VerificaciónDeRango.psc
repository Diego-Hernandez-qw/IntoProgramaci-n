Algoritmo  VerificaciónDeRango
	//8.	Solicitar un número y mostrar Verdadero si es positivo y menor que 100, usando and. SI
	Definir num Como Real
	Definir resultado Como Logico
	
	Escribir "Ingrese un número:"
	Leer num
	
	Si num > 0 Y num < 100 Entonces
		resultado <- Verdadero
		Escribir "El resultado es: ", resultado
		Escribir "Explicación: El número es positivo y menor que 100."
	Sino
		resultado <- Falso
		Escribir "El resultado es: ", resultado
		Escribir "Explicación: El número no cumple con ambas condiciones."
	FinSi
	
	
	
FinAlgoritmo
