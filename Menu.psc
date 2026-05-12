Algoritmo sin_titulo
	Definir opc Como Entero
	
	Escribir  "Seleccione una opción del siguiente menu"
	Escribir "1, Calcular el promedio de la clase"
	Escribir "2, Determinar si un numero es positivo o negativo"
	Escribir "3, Mostrar tabla de multiplicación"
	Escribir "4, Salir"
	Escribir "-------------------------------------------------------"
	Leer opc
	Segun opc Hacer
		1:
			Escribir  "Sistema para calcular promedio de la clase"
			// 1. Definir las variables como tipo Real para aceptar decimales
			Definir parcial1, parcial2, parcial3, promedio Como Real
			
			// 2. Pedir al usuario que ingrese las calificaciones
			Escribir "Ingrese la calificación del primer parcial:"
			Leer parcial1
			
			Escribir "Ingrese la calificación del segundo parcial:"
			Leer parcial2
			
			Escribir "Ingrese la calificación del tercer parcial:"
			Leer parcial3
			
			// 3. Calcular el promedio (se suman y se divide entre 3)
			promedio <- (parcial1 + parcial2 + parcial3) / 3
			
			// 4. Mostrar el resultado en pantalla
			Escribir "========================================"
			Escribir "El promedio final es: ", promedio
			
			// 5. Condición opcional para saber si aprobó o no (asumiendo base 60)
			Si promedio >= 60 Entonces
				Escribir "Estado: APROBADO"
			SiNo
				Escribir "Estado: REPROBADO"
			FinSi
			Escribir "========================================"
			//Distinción Honorifica
			Si prom >= 95 Entonces
				Distinción <- "Summa Cum Laude"
			SiNo
				Si prom >= 90 Entonces
					Distinción <- "Magna Cum Laude"
				SiNo
					Si prom >= 80 Entonces
						Destinción <- "Cum Laude"
					SiNo
						Si prom < 70 Entonces
							Distinción <- "Reprobatuos"
						SiNo
							Distinción <- "Bene Próbatus"
						Fin Si
					Fin Si
				Fin Si
			Fin Si
			Escribir "El promedio de la clase" n_clase "es de:" prom
		2:
			Escribir "Sistema para definir si un numero es positivo o negativo"
			//Determinar si un número es positivo o negativo
			Definir num Como Entero
			Escribir "Ingrese un número entero"
			Leer num
			
			Si num < 0 Entonces
				Escribir "El numero ingresado es negativo"
			SiNo
				Escribir "El numero ingresado es positivo"
			Fin Si
		3:
			Escribir "Sistema para ver tabla de multiplicación"
			//Mostrar los numeros del 1 al 10
			Definir num Como Entero
			leer num2
			num2 <- 8
			num <- 1
			Mientras num <= 10 Hacer
				Escribir num 
				num <- num + 1
				
			Fin Mientras
		4:
			Escribir "Muchas gracias por usar el programa"
		De Otro Modo:
			Escribir "Debe ingresar un numero del menú"
			
	Fin Segun
	Escribir  "Seleccione una opción del siguiente menu"
	Escribir "1, Calcular el promedio de la clase"
	Escribir "2, Determinar si un numero es positivo o negativo"
	Escribir "3, Mostrar tabla de multiplicación"
	Escribir "4, Salir"
	Escribir "-------------------------------------------------------"
FinAlgoritmo
