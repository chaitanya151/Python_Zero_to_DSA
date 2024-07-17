"""
Ask a number from user.
num is divisible by 3 -> FOO.
num is divisible by 5 -> BAR.

num is divisible by 3 and 5 -> FOOBAR
else
-> invalid
"""

num = int(input("Enter the number: "))
if (num % 3 == 0) and (num % 5 == 0):
    print("FOOBAR")
elif num % 3 == 0:
    print("FOO")
elif num % 5 == 0:
    print("BAR")
else:
    print("invalid")
