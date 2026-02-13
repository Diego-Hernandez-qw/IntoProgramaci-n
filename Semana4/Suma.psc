Algoritmo Suma
	//Pedir dos números
	// mostrar la suma
	Definir NumeroEntrada1, NumeroEntrada2, numeroTotal Como Entero
	
	Escribir "Ingrese un numero para sumar "
	Leer NumeroEntrada1
	
	Escribir "Ingrese un numero para sumar "
	Leer NumeroEntrada2
	
	total = NumeroEntrada1 + NumeroEntrada2
	si NumeroEntrada1	> 0 
		total = NumeroEntrada1 + NumeroEntrada2
	FinSi
	Escribir  " El total de la suma es " , total
	
	//Mostrar la resta
	
	Escribir "Ingrese un numero para restar "
	Leer NumeroEntrada1
	
	Escribir "Ingrese un numero para restar "
	Leer NumeroEntrada2
	
	total = NumeroEntrada1 - NumeroEntrada2
	
	si NumeroEntrada1	> 0 
		total = NumeroEntrada1 - NumeroEntrada2
	FinSi
	Escribir  " El total de la resta es " , total
	
	// Mostrar la Multiplicación
	
	Escribir "Ingresa un numero para la multiplicación  "
	Leer NumeroEntrada1
	
	Escribir " Ingresa el otro numero para multiplicar "
	Leer NumeroEntrada2
	
	total = NumeroEntrada1 * NumeroEntrada2
	si NumeroEntrada1 > 0
		total = NumeroEntrada1 * NumeroEntrada2
	FinSi
	Escribir "El total de la muliplicación es " , total
	
	// Mostrar la división
	
	Escribir "Ingresa un numero para la división  "
	Leer NumeroEntrada1
	
	Escribir " Ingresa el otro numero para dividir "
	Leer NumeroEntrada2
	
	total = NumeroEntrada1 / NumeroEntrada2
	si NumeroEntrada1 > 0
		total = NumeroEntrada1 / NumeroEntrada2
	FinSi
	Escribir "El total de la division es " , total
FinAlgoritmo
