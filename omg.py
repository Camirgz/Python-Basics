TC=float(input("Digite la nota del trabajo cotidiano:"))
T=float(input("Digite la nota de talleres:"))
P=float (input("Digite la nota de proyectos:"))
A=float(input("Digite la nota de asistencia:"))
PTC=TC*0.55
PT=T*0.15
PP=P*0.25
PA=A*0.05
PF=PTC+PT+PP+PA
if PF>=69.5:
    print ("Para la nota ",PF,"su condición es aprobado")
else :
    print("Para la nota: ",PF,"su condición es reprobado")
if PF>=100:
    print("Para la nota ",PF,"Su condición es de nota perfecta")
    
