"""
Sum of list
"""

my_list = [4, 8, 6, 5, 3, 12, 1, 7, 6, 2]

p_sum = 0
for num in my_list:
    factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1
    if factors == 2 or factors == 1:
        p_sum = p_sum + num
print(f"Prime number total -> {p_sum}")
