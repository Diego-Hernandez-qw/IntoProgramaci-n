Algoritmo División
	Definir num Como Real
	// Solicitar dos números
	// Mostrar el resultado de la división
	//  primero entre el segundo
	
	Escribir "Ingresa un numero para la división  "
	Leer NumeroEntrada1
	
	Escribir " Ingresa el otro numero para dividir "
	Leer NumeroEntrada2
	
	total = NumeroEntrada1 / NumeroEntrada2
	
	si NumeroEntrada1 > 0
		total = NumeroEntrada1 / NumeroEntrada2
	FinSi
	Escribir "El total de la division es " , total
	
	Repetir
        Escribir "Ingrese un número mayor a 0 y menor a 10:"
        Leer num
        Si num <= 0 O num >= 10 Entonces
            Escribir "Error: Número fuera de rango."
        FinSi
    Hasta Que num > 0 Y num < 10
    Escribir "Número válido: ", num
FinAlgoritmo
