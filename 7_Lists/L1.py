# Total count of all odd numbers

my_list = [4, 8, 6, 5, 3, 12, 1, 3]

n = len(my_list)
count = 0

for index in range(0, n):
    if my_list[index] % 2 != 0:
        count += 1

print(f"Total odd numbers -> {count}")
