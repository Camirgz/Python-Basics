def new_str_converter(string):
    for letter in string:
        if letter.isalpha() or letter == " ":
            print(letter, end="")
    return letter

print(new_str_converter("1. Me ll21515amo Camil@@a Rodrígu///ez"))
print(new_str_converter("My favorite number is four"))
print(new_str_converter("My favorite number is 4"))
print(new_str_converter("4 is my favorite number"))