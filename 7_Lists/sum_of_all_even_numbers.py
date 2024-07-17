my_list = [4, 65, 321, 76876, 432, 65, 78, 54, 3454]

total = 0
n = len(my_list)
print(f"Length -> {n}")
for index in range(0, n):
    if my_list[index] % 2 == 0:
        total = total + my_list[index]

print(f"Total -> {total}")


# for num in my_list:
#     if num % 2 == 0:
#         total = total + num
# print(total)
