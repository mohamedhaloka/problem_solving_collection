

num_of_columns = input()
numbers_of_box_per_column = input().split()
numbers_of_box_per_column_int = []
for num in numbers_of_box_per_column:
    numbers_of_box_per_column_int.append(int(num))
numbers_of_box_per_column_int.sort()
print(str(numbers_of_box_per_column_int).replace('[', '').replace(']', '').replace(',', ' '))
