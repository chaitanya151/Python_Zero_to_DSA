"""
Find the unique words from the give input string
"""

str1 = "The sun rises in the east and sets in the west, but the sun always shines."


def unique_word(str1: str) -> None:
    str2 = str1.split()
    print(f"Splitted str1 : {str2}")
    d = {}  # empty dict
    for word in str2:
        # if word not in d:
        #     d[word] = 1
        # else:
        #     d[word] += 1
        d[word] = d.get(word, 0) + 1
    print(f"word count : {d}")

    for k, v in d.items():
        if v == 1:
            print(f"Unique words : {k}")


unique_word(str1)
