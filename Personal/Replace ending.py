sentence: str = input("Enter your sentence you´d like to change the last word to: ")
old = input("Enter the last word of your sentence: ")
new = input("Enter the replace for word: ")
new_string = ""
new_sentence = ""
last_word = ""
lenn_old = len(old)
len_old = lenn_old - 2*lenn_old
int_len_old = int(len_old)

for letter in sentence:
    if letter.lower() != "":
        new_string = "{}{}".format(new_string, letter).strip()
for last_word_num in range(len_old, 0):
    last_word = "{}{}".format(last_word, new_string[last_word_num])
if last_word == old:
    new_sentence = sentence[:int_len_old] + new
    print(new_sentence)
else:
   print(sentence)

