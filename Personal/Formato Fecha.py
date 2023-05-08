nombremes=0
numero=input("Ingrese un número con el formato DDMMAA: ")
día= str(numero[0] + numero[1])
mes= str(numero[2] + numero[3])
año= str(numero[4] + numero[5])
fecha=(día + "/" + mes + "/" + año)
print(fecha)
if mes == "01":
    nombremes="Enero"
elif mes == "02":
    nombremes="Febrero"
elif mes == "03":
    nombremes="Marzo"
elif mes == "04":
    nombremes = "Abril"
elif mes == "05":
    nombremes = "Mayo"
elif mes == "06":
    nombremes = "Junio"
elif mes == "07":
    nombremes = "Julio"
elif mes == "08":
    nombremes = "Agosto"
elif mes == "09":
    nombremes = "Septiembre"
elif mes == "10":
    nombremes="Octubre"
elif mes == "11":
    nombremes="Noviembre"
elif mes == "12":
    nombremes="Diciembre"
else:
    print("Mes inválido")

if int(día)<10:
    actual_día= str(día[1])
else:
    actual_día= str(día)

print("Hoy es " + str(actual_día) + " de " + nombremes + " del 20" + año)





