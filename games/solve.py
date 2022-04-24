

num_of_games = input()

teams = []

for i in range(int(num_of_games)):
    team = input().split()
    teams.append(team)

current_team_index = 0
current_tem_index = 0
total = 0
for i in range(len(teams)):
    current_team = teams[0]
    teams.remove(teams[0])
    new_list = teams
    for tem in new_list:
        for item in tem:
            for new_item in current_team:
                in1 = current_team.index(new_item)
                in2 = tem.index(item)

                if (item == new_item) & (in2 != in1):
                    total += 1

print(total)