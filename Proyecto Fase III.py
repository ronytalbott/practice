inventario_pescado_entero=120
inventario_pescado_filete=45
inventario_camarones=30
inventario_langosta=15
inventario_curiles=50

nombres=[]
numeros_facturas=[]
libras_compradas=[]
productos=[]
total_pagos=[]
n_clientes=[]
n=0
factura=1010

print("="*40)
print("Bienvenido a Marisqueria Sirenita")
print("="*40)
while True:
   print("\n1. Agregar Cliente")
   print("2. Mostrar Clientes")
   print("3. Eliminar Cliente")
   print("4. Salir")
   try: 
      opcion=int(input("Seleccione una opcion: "))
   except ValueError:
      print("Valor invalido, intentelo de nuevo.")
      continue
   
   if opcion==1:
      print("\n")
      print("="*15)
      print("CLIENTE NUEVO")
      print("="*15)
      while True:
         nombre=input("\nEscriba su nombre: ").strip()
         if nombre=="":
            print("El nombre no puede estar vacio.")
            continue
         if not nombre.replace(" ","").isalpha():
            print("Nombre invalido, intente de nuevo.")
            continue
         break
      
      while True: 
       print("\nProductos Disponibles: ")
       print("1. Pescado entero")
       print("2. Filete de Pescado")
       print("3. Camarones")
       print("4. Langosta")
       print("5. Curiles")
       try:
        tipo_producto=int(input("Seleccione uno: "))
       except ValueError:
          print("Valor invalido, intente de nuevo.")
          continue
       if tipo_producto==1:
          while True:
           try:
            cantidad_lbs=float(input(f"Inventario disponible: {inventario_pescado_entero}Lbs. Ingrese la cantidad en libras: "))
           except ValueError:
              print("Valor invalido, intente de nuevo.")
              continue
           if 0<cantidad_lbs<=inventario_pescado_entero:
              precio=65*cantidad_lbs
              producto="Pescado entero"
              inventario_pescado_entero=inventario_pescado_entero-cantidad_lbs
              break
           else:
              print("Cantidad invalida, intente de nuevo")
              continue
          break
       if tipo_producto==2:
          while True:
           try:  
            cantidad_lbs=float(input(f"Inventario disponible: {inventario_pescado_filete}Lbs. Ingrense cantidad en libras: "))
           except ValueError:
              print("Valor invalid, intente de nuevo.")
              continue
           if 0<cantidad_lbs<=inventario_pescado_filete:
              precio=95*cantidad_lbs
              producto="Filete de pescado"
              inventario_pescado_filete=inventario_pescado_filete-cantidad_lbs
              break
           else:
              print("Cantidad invalida, intente de nuevo")
              continue
          break 
       if tipo_producto==3:
          while True:
           try:
            cantidad_lbs=float(input(f"Inventario disponible: {inventario_camarones}Lbs. Ingrense cantidad en libras: "))
           except ValueError:
              print("Valor invalido, intentelo de nuevo")
              continue
           if 0<cantidad_lbs<=inventario_camarones:
              precio=130*cantidad_lbs
              producto="Camarones"
              inventario_camarones=inventario_camarones-cantidad_lbs
              break
           else:
              print("Cantidad invalida, intente de nuevo")
              continue
          break
       if tipo_producto==4:
          while True:
           try:  
            cantidad_lbs=float(input(f"Inventario disponible: {inventario_langosta}Lbs. Ingrense cantidad en libras: "))
           except ValueError:
              print("Valor invalido, intentelo de nuevo.")
              continue
           if 0<cantidad_lbs<=inventario_langosta:
            precio=250*cantidad_lbs
            producto="Langosta"
            inventario_langosta=inventario_langosta-cantidad_lbs
            break
           else:
              print("Cantidad invalida, intente de nuevo.")
              continue
          break
       if tipo_producto==5:
          while True:
           try:
            cantidad_lbs=float(input(f"Inventario disponible: {inventario_curiles}Lbs. Ingrense cantidad en libras: "))
           except ValueError:
              print("Valor invalido, intente de nuevo.")
              continue
           if 0<cantidad_lbs<=inventario_curiles:
            precio=50*cantidad_lbs
            producto="Curiles"
            inventario_curiles=inventario_curiles-cantidad_lbs
            break
           else:
              print("Cantidad invalida, intente de nuevo.")
              continue
          break
       else:
          print("\nOpcion invalida, intente de nuevo.")
          continue
      
      while True:
         print("\nServicios extra: ")
         print("1. Limpieza ")
         print("2. Precocinado")
         try:
            tipo_extra=int(input("Seleccione una opcion: "))
         except ValueError:
            print("Valor invalido, intente de nuevo.")
            continue
         if tipo_extra==1:
            precio_extra=precio*.10
            break
         if tipo_extra==2:
            precio_extra=precio*.15
            break
         else:
            print("Opcion invalida, intente de nuevo.")
            continue
         
      subtotal=precio+precio_extra
      impuesto=subtotal*.15
      total=round(subtotal+impuesto,2)
      nombres.append(nombre)
      numeros_facturas.append(factura)
      libras_compradas.append(cantidad_lbs)
      productos.append(producto)
      total_pagos.append(total)
      n_clientes.append(n)
      
      print("\nFACTURA")
      print(f"Numero de factura.........{factura}")
      print(f"Nombre del cliente........{nombre}")
      print(f"Producto comprado.........{producto}")
      print(f"Precio de producto........{precio:.2f}")
      print(f"Precio de extra...........{precio_extra:.2f}")
      print("_"*48)
      print(f"Subtotal..................{subtotal:.2f}")
      print(f"Impuesto..................{impuesto:.2f}")
      print(f"Total a pagar.............{total}")
      factura+=1
      n+=1
      continue
   
   if opcion==2:
      if factura==1010:
         print("\nNingun cliente activo, agregue uno.")
         continue
      print(f"{'N* de cliente':<20} | {'Numero de factura':<20} | {'Nombre de cliente':<20} | {'Producto comprado':<20} | {'Libras compradas':20} | {'Total comprado':<20}")
      print("_"*130)
      for i in range(len(nombres)):
         print(f"{n_clientes[i]:<20} | {numeros_facturas[i]:<20} | {nombres[i]:<20} | {productos[i]:<20} | {libras_compradas[i]:<20} | {total_pagos[i]:<20}")
      continue
   
   if opcion==3:
      if factura==1010:
         print("\nNingun cliente activo, agregue uno.")
         continue
      print("\nCLIENTES DISPONIBLES A ELIMINAR")
      print(f"{'N* de cliente'} | {'Numero de factura':<20} | {'Nombre de cliente':<20} | {'Producto comprado':<20} | {'Libras compradas':20} | {'Total comprado':<20}")
      print("_"*130)
      for i in range(len(nombres)):
         print(f"{n_clientes[i]:<20} | {numeros_facturas[i]:<20} | {nombres[i]:<20} | {productos[i]:<20} | {libras_compradas[i]:<20} | {total_pagos[i]:<20}")
      
      while True:
         try:
            cliente_eliminado=int(input("Escriba el numero del cliente que quiere eliminar: "))
            if 0<=cliente_eliminado<len(nombres):
               numero_eliminado=numeros_facturas.pop(cliente_eliminado)
               nombre_eliminado=nombres.pop(cliente_eliminado)
               libras_eliminado=libras_compradas.pop(cliente_eliminado)
               producto_eliminado=productos.pop(cliente_eliminado)
               total_eliminado=total_pagos.pop(cliente_eliminado)
               n_eliminado=n_clientes.pop(-1)
               n=n-1
                           
               
               print(f"\nCliente {nombre_eliminado} eliminado con exito.")
               break
            else:
               print("\nNumero de factura invalido, intente de nuevo.")
               continue
         except ValueError:
            print("Valor invalido, intentelo de nuevo.")
            continue
      continue
   
   if opcion==4:
      print("\nGracias por utilizar nuestros servicios, vuelva pronto.")
      break
   
   else:
      print("Opcion invalida, intentelo de nuevo.")
      continue