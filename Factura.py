lista_sumada=[]
total=0
fecha=input("Digite la fecha del día de hoy: ")
nombre=input("Digite su nombre: ")
while True:
    producto=input("Ingrese el nombre de su producto: ")
    precio=input("Ingrese el costo de su producto: ")
    total+=int(precio)
    lista_sumada.append(producto + " " + precio)
    continuar=input("Si desea continuar digite x: ")
    if continuar != "x":
        lista_linda_sumada=str("\n".join(lista_sumada))
        print("- - - - - - - - - - - - - - - - - - - - - - - ")
        print(nombre)
        print(str(fecha))
        print(lista_linda_sumada)
        print("El total es de: " + str(total))
        print("La cantidad de elementos que compró es de " +str(len(lista_sumada)))
        print("- - - - - - - - - - - - - - - - - - - - - - - ")
        break

