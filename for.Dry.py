i=int()
Nfac=int()
Nomb=str()
Ventas=float()
Pre=float()
PreS=float()
TipP=int()
TipS=int()
St=float()
Imp=float()
Tot=float()
i=1
ventas=0
for i in range (1, 4):
    print("Ingrese numero de factura")
    Nfac=int(input())
    print("Nombre del cliente")
    Nomb=str(input())
    print("")
    print("Tipos de productos")
    print("1. Camisas")
    print("2. Pantalones")
    print("3. Chaquetas")
    print("Seleccione el tipo de producto")
    TipP=int(input())
    print("")
    if TipP==1:
        Pre=100
        Prod="Camisa"
    elif TipP==2:
        Pre=150
        Prod="Pantalones"
    elif TipP==3:
        Pre=200
        Prod="Chaquetas"
        print("")
    print("Tipos de lavados")
    print("1.seco")
    print("2.tradicional")
    TipS=int(input())
    print("")
    if TipS==1:
     PreS=Pre*.10
    else:
     PreS=Pre*.05
    print("")
    St=Pre+PreS
    Imp=St*.15
    Tot=St+Imp
    Ventas=Ventas+Tot
    print(".................................Lavanderia Prestto..................................")
    print("Numero de factura..................................",Nfac)
    print("Nombre de cliente..................................",Nomb)
    print("Tipo de producto...................................",Prod)
    print("Precio de producto.................................",Pre)
    print("Precio de lavado...................................",PreS)
    print("Subtotal...........................................",St)
    print("Impuesto...........................................",Imp)
    print("Total..............................................",Tot)
    print("")
    print("Total de ventas.....................",Ventas)