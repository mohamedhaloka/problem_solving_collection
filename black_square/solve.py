

calories = input().split()
s = input()

caloriesMap = {
    '1': calories[0],
    '2': calories[1],
    '3': calories[2],
    '4': calories[3],
}
total = 0
for char in s:
    total += int(caloriesMap[char])

print(total)