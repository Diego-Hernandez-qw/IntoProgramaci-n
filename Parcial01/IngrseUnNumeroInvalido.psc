Algoritmo IngrseUnNumeroInvalido
	//5.	Crear un algoritmo que solicite un número entre 1 y 10 y continúe pidiendo hasta que el usuario ingrese un número inválido, 
	// usando la estructura Mientras (hacer mientras o hacer).
	Definir num Como Real
    
    Escribir "Ingrese un número entre 1 y 10 para continuar:"
    Leer num
    
    Mientras num >= 1 Y num <= 10 Hacer
        Escribir "¡Número válido! Ingrese otro (o uno fuera de rango para salir):"
        Leer num
    FinMientras
    
    Escribir "Número inválido detectado. El programa ha finalizado."
FinAlgoritmo
