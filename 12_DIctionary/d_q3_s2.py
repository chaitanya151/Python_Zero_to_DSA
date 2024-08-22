from typing import List, Dict

details = {
    "Anirudh": [56, 78, 65],
    "Sanjay": [58, 78, 56, 12, 33, 56, 78],
    "Muskan": [87, 78, 65, 45],
    "Nihar": [32, 78, 32, 98, 33],
    "Akshay": [56, 40],
}


# highest marks is 98, scored by Nihar
def print_top_scorer(details: Dict[str, List[int]]):
    highest_score = max(max(marks) for marks in details.values())
    for student, marks in details.items():
        if highest_score in marks:
            print(f"The highest mark is {highest_score}, scored by {student}.")


print_top_scorer(details)
