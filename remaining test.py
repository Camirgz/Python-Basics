seconds=input("Enter de am")
def convert_seconds(seconds):
    hours = (seconds//3600)
    minutes = (seconds - hours*3600)//60
    remaining_seconds = (seconds - hours*3600 - minutes*60)
    cake = [hours, minutes, remaining_seconds]
    return cake

convert_seconds(5000)
print(str(h) + " hours " + str(minutes) + " minutes and " + str( remaining_seconds) + " seconds" )