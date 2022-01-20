import random

#Value Initialization
done = True

while done:
    dice_result = random.randint(1,7)
    print(dice_result)
    answer = str(input("Would you like to roll the dice again?: "))
    if answer.lower() == "yes":
        continue
    elif answer.lower() == "no":
        print("Thank You for playing!")
        done = False