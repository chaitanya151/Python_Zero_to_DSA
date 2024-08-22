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
        print(f"{names} : {', '.join(str(m) for m in marks)}")


list_display(details)
