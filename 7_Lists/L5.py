"""
sum and product in that list.
"""

my_list = [4, 8, 6, 5, 3, 12, 1, 7, 6, 2]

n = len(my_list)
print(f"Length of the list -> {n}")
total = 0
product = 1

for index in range(0, n):
    total = total + my_list[index]
    product = product * my_list[index]

print(f"total -> {total}")
print(f"Product -> {product}")
