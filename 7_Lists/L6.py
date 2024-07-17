"""
print all the numbers divisible by 5 
but in reverse order.
"""

my_list = [5, 8, 10, 15, 2, 4, 95, 34, 25]

n = len(my_list)
print(f"n -> {n}")

for index in range(n - 1, -1, -1):
    if my_list[index] % 5 == 0:
        print(f"num -> {my_list[index]}")
