"""
Program that takes two numbers as input 
and checks if the first number is 
divisible by the second.

"""

num_1 = int(input("Enter number 1: "))
num_2 = int(input("Enter number 2: "))

if num_1 % num_2 == 0:
    print(f"{num_1} is divisible by {num_2}.")
else:
    print(f"{num_1} is not divisible by {num_2}.")
