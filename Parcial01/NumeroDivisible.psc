Algoritmo NumeroDivisible
	//9.	Solicitar un número y mostrar Verdadero si es divisible por 3 o divisible por 5, usando or. SI
	Definir num Como Entero
    Definir resultado Como Logico
    
    Escribir "Ingrese un número entero:"
    Leer num
    
    Si (num Mod 3 = 0) O (num Mod 5 = 0) Entonces
        resultado <- Verdadero
        Escribir "El resultado es: ", resultado
        Escribir "Explicación: El número es divisible por 3, por 5, o por ambos."
    Sino
        resultado <- Falso
        Escribir "El resultado es: ", resultado
        Escribir "Explicación: El número no es divisible ni por 3 ni por 5."
    FinSi
	
FinAlgoritmo
