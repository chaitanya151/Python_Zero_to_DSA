"""
Create a list of your own. 
Print the total count of 
all odd and even numbers.
"""

my_list = [4, 8, 6, 5, 3, 12, 1, 3, 6]

n = len(my_list)
e_total = 0
o_total = 0
for index in range(0, n):
    if my_list[index] % 2 == 0:
        e_total += 1
    else:
        o_total += 1

print(f"Even numbers -> {e_total}")
print(f"Odd numbers -> {o_total}")
