from typing import List


def max_frequency(my_list: List[int]) -> None:
    max_frequency = 0
    max_frequency_element = 0
    my_dict = {}
    for num in my_list:
        my_dict[num] = my_dict.get(num, 0) + 1
    for k, v in my_dict.items():
        if v > max_frequency:
            max_frequency = v
            max_frequency_element = k

    print(f"{max_frequency_element} has the highest frequency of {max_frequency}")


my_list = [4, 5, 6, 5, 4, 4, 7]
max_frequency(my_list)
