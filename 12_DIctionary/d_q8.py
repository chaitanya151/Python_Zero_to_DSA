from typing import Dict


def square_of_keys(d: Dict) -> Dict:
    for num in range(1, 16):
        if num not in d:
            d[num] = num**2
        else:
            print("Value exists.")
    return d


d = {}
print(square_of_keys(d))
