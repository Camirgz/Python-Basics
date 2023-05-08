word = "Sequoia"
allowed_errors = 15
guesess = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesess:
            print(letter, end="")
        else:
            print("_", end="")
    print("")

    guess = input(f"Allowed Errors Left {allowed_errors}, Next guess: ")
    guesess.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_errors -= 1
        if allowed_errors == 0:
            break

    done = True
    for letter in word:
        if letter.lower() not in guesess:
            done = False
if done:
    print(f"You found the word! It was {word}")
else:
    print(f"Game over! It was {word}")
