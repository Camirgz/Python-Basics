secret_word = "giraffe"
guess = ""
times = 0

while guess != secret_word:
    guess = input("Enter your guess:  ")
    times += 1
    if times == 5:
        print("Out of guesses, you loose")
        break
else:
    print("You won")