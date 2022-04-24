

num_of_events = input()
events = input().split()
events_int = []

for event in events:
    events_int.append(int(event))

i = 0
solved_events = 0
while i < len(events_int):
    current_event = events_int[i]

    if current_event != -1:
        i += current_event
    else:
        solved_events += 1
        i = i + 1


print(solved_events)