"""
Write a python program to find sum and average 
of List in Python.
"""

lst1 = [10, 25, 30, -10, 1, 9]


def sum_avg(lst: list):
    n = len(lst1)
    sum_1 = 0
    avg = 0
    for i in range(n):
        sum_1 = sum_1 + lst1[i]
    avg = sum_1 / n
    print(
        f"Sum of list -> {sum_1}\
           Avg. of list -> {avg:.2f}"
    )


sum_avg(lst1)
