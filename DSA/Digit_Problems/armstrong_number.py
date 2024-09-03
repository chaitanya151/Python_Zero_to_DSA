"""
The idea is to first count the number of digits (or find the order). 
Algorithm: 
Below is the program to check whether the number is an Armstrong number or not.
if you have a number like 153, 
it's an Armstrong number because 1^3 + 5^3 + 3^3 equals 153.
Since 1634 is a four digit number, we can find out the sum of fourth power of each of its digits. 
Now, this sum turns out to be 1634. Hence, 1634 is an Armstrong number.
"""

num = 153


def is_armstrong(num: int) -> bool:
    n = num
    result = 0
    nod = int()
    while n > 0:
        ld = n % 10
        s = ld * ld * ld
        cube_sum += s
        n = n // 10
    return num == cube_sum


print(is_armstrong(num))
