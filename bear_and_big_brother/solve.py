

persons_count, fence_height = input("").split()

minimum_road_width = 0
all_persons_height = ''

person_height = input("").split()

for i in range(len(person_height)):
    if int(person_height[i]) <= int(fence_height):
        minimum_road_width += 1
    else:
        minimum_road_width += 2
    all_persons_height += str(person_height[i]) + '   '

print(str(minimum_road_width))