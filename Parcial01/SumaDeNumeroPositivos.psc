Algoritmo SumaDeNumeroPositivos
	//2.	Crear un programa que permita ingresar números continuamente hasta que se ingrese un número negativo,
	//y luego muestre la suma de todos los números positivos ingresados, utilizando la estructura repetir (Hacer o hacer mientras) .
	
	Definir num, suma Como Real
    suma <- 0
	
    Repetir
        Escribir "Ingrese un número (o uno negativo para terminar):"
        Leer num
        
        Si num >= 0 Entonces
            suma <- suma + num
        FinSi
        
    Hasta Que num < 0
	
    Escribir "La suma total de los números positivos es: ", suma
	
FinAlgoritmo
