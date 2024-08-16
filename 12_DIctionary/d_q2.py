"""
1
"""

from typing import Dict


def marks() -> Dict[str, int]:
    my_dict = {}
    num_of_subjects = int(input("Enter number of subjects: "))

    for i in range(num_of_subjects):
        subject = input("Ener subject name: ")
        marks = int(input("Enter marks: "))
        my_dict[subject] = marks

    return my_dict


print(marks())
