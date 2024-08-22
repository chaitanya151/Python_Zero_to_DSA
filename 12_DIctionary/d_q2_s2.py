from typing import List, Dict

details = {
    "Anirudh": [56, 78, 65],
    "Sanjay": [58, 78, 56, 12, 33, 56, 78],
    "Muskan": [87, 78, 65, 45],
    "Nihar": [32, 78, 32, 98, 33],
    "Akshay": [56, 40],
}


def list_display(deatils: Dict[str, List[int]]):
    for names, marks in details.items():
        highest_marks = 0
        for m in marks:
            if m > highest_marks:
                highest_marks = m
        print(f"{names} : {highest_marks}")


list_display(details)
