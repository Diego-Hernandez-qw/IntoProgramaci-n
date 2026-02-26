Algoritmo ValidarCeroUno
	// Validar con O si número es 0 o 1 usando Hacer-Mientras
	Definir NumeroEntrada1 Como Entero
	Repetir
        Escribir "Ingrese cualquier numero:"
        Leer NumeroEntrada1
        Si NumeroEntrada1 <> 0 Y NumeroEntrada1 <> 1 Entonces
            Escribir "Error: Numero no valido."
        FinSi
        
    Hasta Que NumeroEntrada1 = 0 O NumeroEntrada1 = 1
    
    Escribir "¡Excelente! El número es: ", NumeroEntrada1
FinAlgoritmo
