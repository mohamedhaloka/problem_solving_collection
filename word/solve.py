

num_of_magnets = input()
magnets = []
num_of_groups = 1
for i in range(int(num_of_magnets)):
    magnet = input()
    magnets.append(magnet)

for i in range(len(magnets)):
    current_char = i
    next_char = 0
    if current_char + 1 != len(magnets):
        next_char = magnets.index(magnets[current_char + 1])
    else:
        next_char = i

    if magnets[current_char] != magnets[next_char]:
        num_of_groups = num_of_groups + 1

print(num_of_groups)