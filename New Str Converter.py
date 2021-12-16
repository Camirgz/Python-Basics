def remover (string):
    new_string = []
    for character in string:
        if character.isalpha() or character == " ":
            new_string.append(character)
    final_string = ''.join(new_string)
    return final_string.strip()

print(remover("1. Me ll21515amo Camil@@a Rodrígu///ez"))
print(remover("My favorite number is four"))
print(remover("My favorite number is 4"))
print(remover("4 is my favorite number"))
