

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

first_String = input()
second_String = input()
match = 0

for i in range(len(first_String)):
    str1Index = alphabet.index(first_String[i].upper())
    str2Index = alphabet.index(second_String[i].upper())
    if str1Index < str2Index:
        match = -1
        break
    elif str1Index > str2Index:
        match = 1
        break