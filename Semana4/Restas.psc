Algoritmo multiplicación
	Definir NumeroEntrada1, NumeroEntrada2, numeroTotal Como Entero
	//Pedir al usuario
	//dos números y mostrar
	// resultado de la multiplicación

	Escribir "Ingresa un numero para la multiplicación  "
	Leer NumeroEntrada1
	
	Escribir " Ingresa el otro numero para multiplicar "
	Leer NumeroEntrada2
	
	total = NumeroEntrada1 * NumeroEntrada2
	
	si NumeroEntrada1 > 0
		total = NumeroEntrada1 * NumeroEntrada2
	FinSi
	Escribir "El total de la muliplicación es " , total
FinAlgoritmo
