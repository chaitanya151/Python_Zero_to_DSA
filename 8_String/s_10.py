"""
Anagrams
str1 = "abc"
str2 = "bca"
"""

str1 = "abc"
str2 = "bcad"


def is_anagram(str1: str, str2: str) -> bool:
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False


print(is_anagram(str1, str2))
