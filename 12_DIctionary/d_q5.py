from typing import Dict


def is_dict(my_dict: dict[str, int], k: str):
    for _ in my_dict:
        if k in my_dict:
            return True
        return False


my_dict = {"a": 5, "b": 8, "c": 3, "d": 0}
k = str(input("Enter key value to check: ").lower())
print(is_dict(my_dict, k))

"""
def does_key_exists(dictnry, key) -> bool:
    return key in dictnry
"""
