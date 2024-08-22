"""
print number of students who have scored more than
a specific number of marks
e.g. more than 75 in any subject
"""

from typing import List, Dict

details = {
    "Anirudh": [56, 78, 65],
    "Sanjay": [58, 78, 56, 12, 33, 56, 78],
    "Muskan": [87, 78, 65, 45],
    "Nihar": [32, 78, 32, 98, 33],
    "Akshay": [56, 40],
}


def more_than(details: Dict[str, List[int]]) -> Dict:
    my_dict = {}
    for name, marks in details.items():
        my_dict[name] = []
        for mark in marks:
            if mark >= 78:
                if name in my_dict:
                    m = my_dict[name]
                    m.append(mark)
                    my_dict[name] = m
    return my_dict


more_than(details)
