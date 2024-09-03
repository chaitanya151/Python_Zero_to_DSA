"""
Least Frequent Character in String
"""


def least_freq_character(test_str: str):
    d = {}
    min_char = None
    min_count = float("inf")
    for ch in test_str:
        d[ch] = d.get(ch, 0) + 1

    for k, v in d.items():
        if v < min_count:
            min_count = v
            min_char = k
    return min_char, min_count


test_str = "GeeksffoorrGeeks"
print(least_freq_character(test_str))
