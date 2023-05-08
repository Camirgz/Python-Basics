texto=input("Ingrese el texto: ")
largo=int(len(texto))
print("El texto es: " + (texto.title()))
print("El texto es: " + (texto.upper()))
print("El texto es: " + (texto.lower()))
print("La primera letra es: " + texto[0])
print("El texto tiene: " + str(largo) + " caracteres")
while True:
    data=input("Seleccione un número entre 1 y " + str(largo) + ": ")
    if int(data) <= int(largo) and int(data)>=1:
        data_real=int(data)-1
        print("El caracter número " + str(data) + " en el texto de " + texto + " es " + str(texto[data_real]))
        break
    else:
        print("Intente de nuevo")
