#Variables
x = int(input("Digite el valor de x: "))
y = int(input("Digite el valor de y: "))

xpos = False
ypos = False


if x > 0: xpos = True
if y > 0: ypos = True

if x and y :
	print("I cuadrante")
elif x and not y:
	print("II cuadrante")
elif not x and not y:
	print("III cuadrante")
elif not y and not x :
	print("IV cuadrante")
