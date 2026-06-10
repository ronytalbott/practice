# Este codigo ha sido generado por el modulo psexport 20230904-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	nfac = int()
	tipmu = int()
	tipma = int()
	tippi = int()
	tipco = int()
	tipcoos = int()
	dom = int()
	nomc = str()
	prodmu = str()
	prodma = str()
	prodpi = str()
	premu = float()
	prema = float()
	prepi = float()
	predo = float()
	subt1 = float()
	print("Numero de factura")
	nfac = int(input())
	print("Nombre de cliente")
	nomc = input()
	print("Tipo de mueble")
	print("1.Juego de sala")
	print("2.Juego de comedor")
	print("3.Mesas decorativas")
	tipmu = int(input())
	if tipmu==1:
		premu = 40000
		prodmu = "Juego de sala"
	elif tipmu==2:
		premu = 20000
		prodmu = "Juego de comedor"
	elif tipmu==3:
		premu = 15000
		prodmu = "Mesas decorativas"
	print("Tipo de material")
	print("1.Madera")
	print("2.Plastico")
	print("3.Metal")
	tipma = int(input())
	if tipma==1:
		prema = 5000
		prodma = "Madera"
	elif tipma==2:
		prema = 2000
		prodma = "Plastico"
	elif tipma==3:
		prema = 1000
		prodma = "Metal"
	print("Tipos de pintado")
	print("1.Natural")
	print("2.Coaba")
	tippi = int(input())
	if tippi==1:
		prepi = 500
		prodpi = "Natural"
	elif tippi==2:
		print("Eliga tono")
		print("1.Claro")
		print("2.Oscuro")
		tipco = int(input())
		if tipco==1:
			prepi = 300
			prodpi = "Coaba:Claro"
		elif tipco==2:
			print("Eliga tipo de oscuro")
			print("1.Mate")
			print("2.Brillante")
			tipcoos = int(input())
			if tipcoos==1:
				prepi = 200
				prodpi = "Coaba:Oscuro:Mate"
			elif tipcoos==2:
				prepi = 250
				prodpi = "Coaba:Oscuro:Brillante"
	print("Desea a domicilio?")
	print("1.Si")
	print("2.No")
	dom = int(input())
	if dom==1:
		predo = 500
	elif dom==2:
		predo = 0
	subt1 = prema+premu+prepi+predo
	print("Ingrese su edad")
	ed = input()
	if ed>=60:
		desc = subt1*.25
		print("Descuento de tercera edad")
	else:
		desc = 0
	subt2 = subt1*.15
	imp = subt2
	tot = subt1+subt2-desc
	print("Numero de Factura_________________________",nfac)
	print("Nombre de Cliente_________________________",nomc)
	print("Precio de Mueble__________________________",premu)
	print("Precio de Materia_________________________",prema)
	print("Precio de Pintado_________________________",prepi)
	print("Precio de Domicilio_______________________",predo)
	print("--------------------------------------------------")
	print("Subtotal__________________________________",subt1)
	print("Descuento tercera edad.___________________",desc)
	print("Impuesto__________________________________",imp)
	print("Total_____________________________________",tot)

