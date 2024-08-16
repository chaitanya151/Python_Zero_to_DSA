"""
Pass by refernce
"""


def printing_list(lst: list) -> None:
    lst[0] = 100


my_list = [1, 3, 55, 7, 8]
print(my_list)
printing_list(my_list)
print(my_list)
