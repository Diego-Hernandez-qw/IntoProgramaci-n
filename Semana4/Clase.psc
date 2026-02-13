Algoritmo Suma
	// Solicitar al usuario que ingrese dos numeros enteros y mostrar la suma de ambos.
	Definir NumeroEntrada1, NumeroEntrada2, numeroTotal Como Entero
	
	Escribir "Ingrese un numero para sumar "
	Leer NumeroEntrada1
	
	Escribir "Ingrese un numero para sumar "
	Leer NumeroEntrada2
	
	total = NumeroEntrada1 + NumeroEntrada2
	
	// Las condiciones lógicas son las que nos va a decir si es verdadero o falso
	// and  -unir, cosas en comun , verdadero 
	//  or -es una union entre los elementos pero no es necesario que los 2 sean verdaderos
	// not >
	si NumeroEntrada1	> 0 
		total = NumeroEntrada1 + NumeroEntrada2
	FinSi
	Escribir  " El total de la suma es " , total

FinAlgoritmo
