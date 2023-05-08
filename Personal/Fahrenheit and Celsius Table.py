#Celscius to Fahrenheit Table
c = 0
f = 0

while c <= 100:
    c += 5
    f = (c*9.0/5.0)+32
    print(str(c) + " " + str(f))
