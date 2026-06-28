usuario="maria"
contraseña=1234
cliente=1
numero_factura=1
cupos_nacional=1000
cupos_internacional=2000
ventas=0
contador_vuelos_nacionales=0
contador_vuelos_internacionales=0
ingresos=0
while True:
      usuario_2=str(input("Ingrese usuario: "))
      contraseña_2=int(input("Ingrese contraseña (solo digitos): "))
      if usuario_2==usuario and contraseña_2==contraseña:
           print("Bienvenido al sistema")
      else:
           print("Usuario o contraseña incorrecta")
           print("Pruebe de nuevo")
           continue
      break

while cliente<=3:
     ingresos=ingresos+1
     
     print("---------Avianca Airlines---------")

     print("Numero de factura:",numero_factura)

     while True:
      nombre_pasajero=str(input("Ingrese el nombre del pasajero: ")).strip()
      if nombre_pasajero=="":
          print("El nombre del pasajero no puede estar vacio")
      elif not nombre_pasajero.replace(" ","").isalpha():
           print("El nombre del pasajero debe contener solo letras")
      else:
           break
     while True:
          try:
           print("""
           Tipos de vuelos: 
           1. Nacional 
           2. Internacional""")
           tipo_vuelo=int(input("Ingrese el tipo de vuelo: "))
           match tipo_vuelo:
                   case 1:
                       while True:
                          print("""
                          Seleccione un vuelo nacional
                          1.Tegucigalpa -> San Pedro Sula
                          2.Tegucigalpa -> Roatan
                          3.Tegucigalpa -> La Ceiba""")
                          vuelo_nacional=int(input("Ingrese el numero del vuelo: "))
                          match vuelo_nacional:
                           case 1: 
                               precio_vuelo=180
                               vuelo_elegido="Tegucigalpa -> San Pedro Sula"
                           case 2: 
                               precio_vuelo=200
                               vuelo_elegido="Tegucigalpa -> Roatan"
                           case 3: 
                               precio_vuelo=140
                               vuelo_elegido="Tegucigalpa -> La Ceiba"
                           case _: 
                               print("Opcion no valida")
                               continue
                          contador_vuelos_nacionales=contador_vuelos_nacionales+1
                          break
                   case 2:
                       while True:
                        if cupos_internacional>0:
                          print("""
                          Seleccione un vuelo internacional
                          1.Tegucigalpa -> Miami
                          2.Tegucigalpa -> Los Angeles""" )
                          vuelo_internacional=int(input("Ingrese el numero del vuelo: ")) 
                          match vuelo_internacional:
                               case 1:
                                    precio_vuelo=500
                                    vuelo_elegido="Tegucigalpa -> Miami"
                               case 2:
                                    precio_vuelo=600
                                    vuelo_elegido="Tegucigalpa -> Los Angeles"
                               case _:
                                    print("Opcion no valida")
                                    continue
                          cupos_internacional=cupos_internacional-1
                          contador_vuelos_internacionales=contador_vuelos_internacionales+1
                          break
                        else:
                          print("Lo sentimos, no hay cupos disponibles para vuelos internacionales")
                   case _:
                          print("Opcion no valida")
                          continue
           break
          except ValueError:
               print("Por favor, ingrese un número válido")

     peso_equipaje=float(input("Ingrese el peso del equipaje en kg: "))
     if peso_equipaje<=50:
      precio_equipaje=0
     elif peso_equipaje>50 and peso_equipaje<=100:
      precio_equipaje=50
     else:
      precio_equipaje=100

     subtotal=precio_vuelo+precio_equipaje

     edad_pasajero=int(input("Ingrese la edad del pasajero: "))
     if edad_pasajero>=60:
      descuento_tercera_edad=subtotal*0.25
     else:
      descuento_tercera_edad=0

     impuesto=subtotal*0.15
     subtotal_final=subtotal-descuento_tercera_edad
     total= subtotal_final+impuesto

     print("---------Factura---------")
     print("Nombre del pasajero................................",nombre_pasajero)
     print("Numero de factura..................................",numero_factura)
     print("Tipo de vuelo......................................",vuelo_elegido)
     print("Precio del vuelo..................................$",precio_vuelo)
     print("Precio del equipaje...............................$",precio_equipaje)
     print("Subtotal..........................................$",subtotal)
     print("Descuento por tercera edad........................$",descuento_tercera_edad)
     print("Impuesto..........................................$",impuesto)
     print("Subtotal final....................................$",subtotal_final)
     print("Total.............................................$",total)

     ventas=ventas+total
     promedio_ventas=ventas/ingresos

     while True:
      continuar=str(input("Desea realizar otra venta? (si/no): ")).lower()
      if continuar=="si":
          numero_factura=numero_factura+1
          cliente=cliente+1
          break
      elif continuar=="no":
          cliente=5
          print("Gracias por utilizar el sistema")
          break
      else:
          print("Opcion no valida")
          continue
     while cliente==4:
      print("Numero maximo de clientes alcanzado")
      break
     print ("Contador de vuelos nacionales....................",contador_vuelos_nacionales)
     print ("Contador de vuelos internacionales...............",contador_vuelos_internacionales)
print("total de ventas...................................$",ventas)
print("Promedio de ventas................................$",promedio_ventas) 