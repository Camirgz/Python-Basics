seconds =input("Digite la cantidad de segundos: ")
hours = (int(seconds)//3600)
minutes = (int(seconds) - hours*3600)//60
remaining_seconds = (int(seconds) - hours*3600 - minutes*60)
if  int(hours) == 1:
    print(str(hours) + " hour " + str(minutes) + " minutes and " + str(remaining_seconds) + " seconds")
elif int(hours) >> 1:
    print(str(hours) + " hours " + str(minutes) + " minutes and " + str(remaining_seconds) + " seconds")

