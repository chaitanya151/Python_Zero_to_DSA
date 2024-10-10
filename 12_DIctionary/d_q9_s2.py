from typing import Dict, List

details = {
    "Anirudh": {
        "age": 56,
        "gender": "Male",
        "marks": [3, 455, 64, 33],
        "adult": True,
    },
    "Muskan": {
        "age": 16,
        "gender": "Female",
        "marks": [34, 89, 70, 99, 43],
        "adult": False,
    },
    "Nihar": {
        "age": 24,
        "gender": "Male",
        "marks": [99, 100],
        "adult": True,
    },
}

for name, detail in details.items():
    if detail["marks"]:
        max_marks = 0
        for mark in detail["marks"]:
            if mark >= max_marks:
                max_marks = mark
        print(name, max_marks)
