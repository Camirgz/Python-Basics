import random

# Starting
options = ["Rock", "Paper", "Scissors"]
user_points = 0
bot_points = 0
active = 1

print("Write Exit if you want to end the game")
while active == 1:
    user = input("Rock,paper or scissors?")
    bot = random.choice(options)
    if user.lower() == "rock":
        if bot == "Rock":
            print("Tie!")
            print(f"{user_points}-{bot_points}")
            print(f"The rival chose {bot}")
        elif bot == "Paper":
            bot_points += 1
            print("You lost!")
            print(f"{user_points}-{bot_points}")
            print(f"The rival chose {bot}")
        elif bot == "Scissors":
            user_points += 1
            print("You Win!")
            print(f"{user_points}-{bot_points}")
            print(f"The rival chose {bot}")
    elif user.lower() == "paper":
        if bot == "Paper":
            print("Tie!")
            print(f"{user_points}-{bot_points}")
            print(f"The rival chose {bot}")
        elif bot == "Scissors":
            bot_points += 1
            print("You lost!")
            print(f"{user_points}-{bot_points}")
            print(f"The rival chose {bot}")
        elif bot == "Rock":
            user_points += 1
            print("You Win!")
            print(f"{user_points}-{bot_points}")
            print(f"The rival chose {bot}")
    elif user.lower() == "scissors":
        if bot == "Scissors":
            print("Tie!")
            print(f"{user_points}-{bot_points}")
            print(f"The rival chose {bot}")
        elif bot == "Rock":
            bot_points += 1
            print("You lost!")
            print(f"{user_points}-{bot_points}")
            print(f"The rival chose {bot}")
        elif bot == "Paper":
            user_points += 1
            print("You Win!")
            print(f"{user_points}-{bot_points}")
            print(f"The rival chose {bot}")
    elif user.lower() == "exit":
        print("Thank you for playing!")
        active += 51
    else:
        print(f"Check Spelling!{user}it's not in the options")
