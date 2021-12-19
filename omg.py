Trabajo_Cotidiano=float(input("Digite la nota del trabajo cotidiano:"))
Talleres=float(input("Digite la nota de talleres:"))
Proyectos=float (input("Digite la nota de proyectos:"))
Asistencia=float(input("Digite la nota de asistencia:"))
Porcentaje_Trabajo_Cotidiano=Trabajo_Cotidiano*0.55
Porcentaje_Talleres=Talleres*0.15
Porcentaje_Proyectos=Proyectos*0.25
Porcentaje_Asistencia=Asistencia*0.05
Porcentaje_Final=Porcentaje_Trabajo_Cotidiano+Porcentaje_Talleres+Porcentaje_Proyectos+Porcentaje_Asistencia
if Porcentaje_Final>=69.5:
    print ("Para la nota ",Porcentaje_Final,"su condición es aprobado")
else :
    print("Para la nota: ",Porcentaje_Final,"su condición es reprobado")
if Porcentaje_Final==100:
    print("Para la nota ",Porcentaje_Final,"Su condición es de nota perfecta")
    
