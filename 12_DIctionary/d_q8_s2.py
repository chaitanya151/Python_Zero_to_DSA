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
        n = len(detail["marks"])
        total_marks = 0
        for m in detail["marks"]:  # Iterate through the actual marks
            total_marks += m
            avg = total_marks / n
        print(f"{name}: {avg}")
