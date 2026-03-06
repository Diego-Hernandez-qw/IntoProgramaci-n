Algoritmo ClasificarNota
	// 1.	Crear un algoritmo que reciba la nota de un estudiante (0 a 10) y muestre la calificación correspondiente 
	//(6 o mayor aprobado, 4 o menor reprobado, 5 recuperación) usando la estructura SI
	Definir nota Como Real
    Escribir "Ingrese la nota del estudiante (0 a 10):"
    Leer nota
	
    Si nota >= 6 Entonces
        Escribir "Resultado: APROBADO"
    Sino
        Si nota == 5 Entonces
            Escribir "Resultado: RECUPERACIÓN"
        Sino
            Escribir "Resultado: REPROBADO"
        FinSi
    FinSi
	
FinAlgoritmo
