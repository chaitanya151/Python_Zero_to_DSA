from typing import Dict


def max_frequncy(user_str: str) -> None:
    my_dict = {}
    max_frequncy = 0
    max_frequncy_element = None
    for ch in user_str:
        my_dict[ch] = my_dict.get(ch, 0) + 1
    print(my_dict)
    for k, v in my_dict.items():
        if v > max_frequncy:
            print(v)
            max_frequncy = v
            print(max_frequncy)
            max_frequncy_element = k
            print(max_frequncy_element)
    print(f"Character with max frequency = {max_frequncy_element}")


max_frequncy("hello world")
