"""
print the sum of numbers from 1 to 10  

"""

num = int(input("Number: "))


def sum_of_numbers(num: int) -> int:
    total = 0
    i = 1
    while i <= num:
        total = total + i
        i += 1
    return total


print(sum_of_numbers(num))
