Algoritmo CalcularTotalCompra
	//Solicitar el precio de un producto y la cantidad comprada, luego calcular y mostrar el total a pagar.
	Definir precio, total Como Real
    Definir cantidad Como Entero
	

	Escribir "Ingrese el precio del producto:"
    Leer precio
    Escribir "Ingrese la cantidad comprada:"
    Leer cantidad
	total <- precio * cantidad
	
	Escribir "El total a pagar es: $", total
FinAlgoritmo
