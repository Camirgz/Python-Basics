def pig_latin(text):
  first_letter = ""
  phrase = []
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    first_letter = word[0]
    rest = word[1:]
    new_word = "{}{}{}".format(rest, first_letter, "ay")
    phrase.append(new_word)
    sentence = str(" ".join(phrase))
    final = ("\"" + sentence + "\"")
  return final

print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"