

problems_count = input("")

problems_solved_count = 0

for i in range(int(problems_count)):
    petya, vasya, tonya = input().split()

    sum = int(petya) + int(vasya) + int(tonya)

    if sum >= 2:
        problems_solved_count += 1


print(str(problems_solved_count))