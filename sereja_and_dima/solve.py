

num_of_stones = input()
stones = input()
stones_list = []
prop_of_solves = 0

for stone in stones:
    stones_list.append(stone)

for i in range(len(stones_list)):
    current_stone = stones_list[i]
    next_stone = ''
    if i < len(stones_list) - 1:
        next_stone = stones_list[i + 1]

    if current_stone == next_stone:
        prop_of_solves += 1

print(prop_of_solves)