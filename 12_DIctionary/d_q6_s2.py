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

# Print the name and age of each student

# for name, detail in details.items():
#     print(f"{name}:{detail['age']}")

for name, detail in details.items():
    if detail["adult"]:
        print(f"Adults -> {name}")

for name, detail in details.items():
    if detail["marks"]:
        for mark in detail["marks"]:
            

            