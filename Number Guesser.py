#Select Random Number
import random
n = random.randint(1,100)

#Variable Initialization
attempts = 10
done = True

#Greetings and Instructions
print("Welcome to the Number Guesser \n"
      "You´ll need to guess a hidden number between 1 and 100 \n"
      "You have 15 attempts, and every time you fail, the attempts will decrease and a new hint will be given"
      "\n-----------------------------------------------------------------------------------------------------")

#Code
while done:
    if attempts > 0:
        guess = int(input("Enter Your Guess: "))
        if guess != n:
            attempts -= 1
            if guess > n:
                print(f"The hidden number is smaller than {guess}")
            elif guess < n:
                print(f"The hidden number is greater than {guess}")
        print(f"You have {attempts} attempts left")
        if guess == n:
            print("You Win!")
            print(f"The Hidden Number was {n}")
            done = False
    if attempts == 0:
        print(f"You lost, the hidden number was {n}")
        done = False