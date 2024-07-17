my_list = [4, 65, 321, 76876, 432, 65, 78, 54, 3454]

total = 0
n = len(my_list)

for index in range(0, n):
    if index % 2 != 0:
        total = total + my_list[index]

print(f"Total -> {total}")
