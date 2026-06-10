Algoritmo Prueba_Technostart
	Definir NuFa, TipCoB, TipRef, Ext, TipExt, Ed, Fp Como Entero
	Definir NomCli Como Caracter
	Definir PreCoB, PreRef, PreExt, Subt, DescCon, DescFp, Imp, DescT, SubtD, Tot Como Real
	Escribir "Ingrese Numero de Factura"
	Leer NuFa
	Escribir "Ingrese Nombre de Cliente"
	Leer NomCli
	Escribir "Tipo de Componente Base"
	Escribir "1.Procesador de Alta Gama: L 8,000"
	Escribir "2.Tarjeta Gráfica Dedicada: L 12,000"
	Escribir "3.Placa Base Modular: L 4,500"
	Leer TipCoB
	Segun TipCoB Hacer
		1:
			PreCoB=8000
		2:
			PreCoB=12000
		3:
			PreCoB=4500
		De Otro Modo:
			Escribir "Opción Invalida"
	Fin Segun
	Escribir "Tipo de Refrigeración"
	Escribir "1.Refrigeración Líquida Custom: 40% del precio base"
	Escribir "2.Refrigeración por Aire Avanzada: 15% del precio base"
	Escribir "3.Refrigeración de Fábrica: 5% del precio base"
	Leer TipRef
	Segun TipRef Hacer
		1:
			PreRef=PreCoB*.40
		2:
			PreRef=PreCoB*.15
		3:
			PreRef=PreCoB*.05
		De Otro Modo:
			Escribir "Opción Invalida"
	Fin Segun
	Escribir "¿Desea un extra?"
	Escribir "1.Si"
	Escribir "2.No"
	Leer Ext
	Segun Ext Hacer
		1:
			Escribir "Tipos de Extra"
			Escribir "1.Memoria RAM Expandida: L 1,500"
			Escribir "2.Almacenamiento SSD NVMe: L 1,200"
			Escribir "3.Fuente de Alimentación Certificada: L 900"
			Leer TipExt
			Segun TipExt Hacer
				1:
					PreExt=1500
				2:
					PreExt=1200
				3:
					PreExt=900
				De Otro Modo:
					Escribir "Opción Invalida"
			Fin Segun
		2:
			PreExt=0
		De Otro Modo:
			Escribir "Opción Invalida"
	Fin Segun
	Subt=PreCoB+PreRef+PreExt
	Escribir "Ingrese su edad"
	Leer Ed
	Si Ed<=25 Entonces
		DescCon=Subt*.10
	SiNo
		DescCon=0
	Fin Si
	Escribir "Forma de pago"
	Escribir "1.Transferencia Bancaria"
	Escribir "2.Tarjeta de Credito"
	Leer Fp
	Segun Fp Hacer
		1:
			DescFp=Subt*.12
		2:
			DescFp=Subt*.03
		De Otro Modo:
			Escribir "Opción Invalida"
	Fin Segun
	Imp=Subt*.15
	DescT=DescCon+DescFp
	SubtD=Subt-DescT
	Tot=SubtD+Imp
	Escribir "Numero de factura...............................",NuFa
	Escribir "Nombre de cliente...............................",NomCli
	Escribir "Precio de Componente Base.......................",PreCoB
	Escribir "Precio de Refrigeracion.........................",PreRef
	Escribir "Precio de Extra.................................",PreExt
	Escribir "________________________________________________________"
	Escribir "Subtotal........................................",Subt
	Escribir "Descuento de Convenio de Estudiante.............",DescCon
	Escribir "Descuento de Forma de Pago......................",DescFp
	Escribir "Descuento Total.................................",DescT
	Escribir "Impuestos.......................................",Imp
	Escribir "Total a Pagar...................................",Tot
FinAlgoritmo