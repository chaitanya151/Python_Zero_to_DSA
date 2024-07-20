my_list = [4, 5, 8, 33, 65, 98, 12, 34]
# print(my_list)

# my_list[-1] = 200
# print(my_list)

"""
even number plus 1
odd number minus 1
"""

n = len(my_list)
for index in range(n):
    if my_list[index] % 2 == 0:
        my_list[index] = my_list[index] + 1
    else:
        my_list[index] = my_list[index] - 1

print(my_list)
