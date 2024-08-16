from typing import Dict


def value_of_type_str(d: Dict, d2: Dict) -> Dict:
    for k, v in d.items():
        if type(v) == str:
            d2[k] = v
    return d2


d = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "birthday": "May 5",
}
d2 = {}
print(value_of_type_str(d, d2))
