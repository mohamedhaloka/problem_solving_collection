
user_input = input().lower()

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

pointer_index = 0
left_list, right_list = [], []

minimum_round = 0

for i in range(len(user_input)):
    index = alphabet.index(user_input[i].upper())
    walk = abs(pointer_index - index)

    if walk < 13:
        minimum_round += walk
    else:
        minimum_round += len(alphabet) - walk

    pointer_index = index
