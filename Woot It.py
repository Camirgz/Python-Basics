sistema="Woot It"
opción_1= "mensajería"
opción_2= "calendario"
opción_3= "aula virtual"
opción_4= "calificaciones"
print("Usted ha ingresado a " + sistema)
name=input("Digite el nombre de usuario: ")
if name =="crodriguez":
    password_1=input("Digite su contraseña: ")
    if password_1 =="camila3458":
        print("Acceso correcto cómo estudiante")
        print("Digite 1 para " + opción_1 + ", digite 2 para " + opción_2 + " ,digite 3 para " + opción_3 + ", digite 4 para " + opción_4)
        elección_1 = input("¿Qué desea hacer?")
        if elección_1 =="1":
            print("Usted ha seleccionado " + opción_1)
        elif elección_1 =="2":
            print("Usted ha seleccionado " + opción_2)
        elif elección_1 == "3":
            print("Usted ha seleccionado " + opción_3)
        elif elección_1 == "4":
            print("Usted ha seleccionado " + opción_4)
        else:
            print("Opción no existente")
    else:
        print("Contraseña incorrecta")
elif name =="aaguilad":
    password_2 = input("Digite su contraseña")
    if password_2=="burris2010":
        print("Acceso correcto de profesor")
        print("Digite 1 para " + opción_1 + ", digite 2 para " + opción_2 + " ,digite 3 para " + opción_3 + ", digite 4 para " + opción_4)
        elección_2 = input("¿Qué desea hacer?")
        if elección_2 == "1":
            print("Usted ha seleccionado " + opción_1)
        elif elección_2 == "2":
            print("Usted ha seleccionado " + opción_2)
        elif elección_2 == "3":
            print("Usted ha seleccionado " + opción_3)
        elif elección_2 == "4":
            print("Usted ha seleccionado " + opción_4)
        else:
            print("Opción no existente")
    else:
        print("Contraseña incorrecta")
elif name=="ifernandez":
    password_3 = input("Digite su contraseña")
    if password_3=="holiwis1234":
        print("Acceso correcto de dirección")
        print(
            "Digite 1 para " + opción_1 + ", digite 2 para " + opción_2 + " ,digite 3 para " + opción_3 + ", digite 4 para " + opción_4)
        elección_3 = input("¿Qué desea hacer?")
        if elección_3 == "1":
            print("Usted ha seleccionado " + opción_1)
        elif elección_3 == "2":
            print("Usted ha seleccionado " + opción_2)
        elif elección_3 == "3":
            print("Usted ha seleccionado " + opción_3)
        elif elección_3 == "4":
            print("Usted ha seleccionado " + opción_4)
        else:
            print("Opción no existente")
else:
    print("Usuario no existente")
