#Inicialización de Variables
decision = True
user = 0 

#Ciclo
while decision:
	user = int(input("Digite un número: "))
	if user != -1:
		if user % 2 == 0:
			print("El número digitado es par")
		else:
			print("El número es impar")
	else:
		decision = False
#Final
print("Gracias!")

