#Variables
n = int(input("Digite la cantidad: "))
user = 0

#Ciclo
for i in range (n):
	user = int(input("Digite un número: "))
	if user % 2 == 0:
		print("El número digitado es par")
	else:
		print("El número es impar")

#Final
print("Gracias!")

