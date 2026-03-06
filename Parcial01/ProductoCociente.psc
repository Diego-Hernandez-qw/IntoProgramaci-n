Algoritmo ProductoCociente
	//7.	Solicitar dos números y mostrar el producto y el cociente
	Definir num1, num2, producto, cociente Como Real
    
    Escribir "Ingrese el primer número:"
    Leer num1
    
    Escribir "Ingrese el segundo número (divisor):"
    Leer num2

    producto <- num1 * num2
    Escribir "El producto es: ", producto
    
    Si num2 <> 0 Entonces
        cociente <- num1 / num2
        Escribir "El cociente es: ", cociente
    Sino
        Escribir "Error: No se puede dividir entre cero."
    FinSi
	
FinAlgoritmo
