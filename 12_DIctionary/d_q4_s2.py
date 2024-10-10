from typing import List, Dict

details = {
    "Anirudh": [56, 78, 65],
    "Sanjay": [58, 78, 56, 12, 33, 56, 78],
    "Muskan": [87, 78, 65, 45],
    "Nihar": [32, 78, 32, 98, 33],
    "Akshay": [56, 40],
}

avg = {}
# avg = sum of marks/length of marks
for name, marks in details.items():
    total = 0
    count = 0
    for mark in marks:
        total += mark
        count += 1
    avg = total / count
    print((f"{name}: {avg:.2f}"))
