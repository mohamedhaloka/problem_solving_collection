

word = input()

upper_word = []
lower_word = []

for char in word:
    if char.isupper():
        upper_word.append(char)
    else:
        lower_word.append(char)

if len(upper_word) > len(lower_word):
    print(word.upper())
else:
    print(word.lower())