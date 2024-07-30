def remove_vowels(my_string: str) -> str:
    r_str = ""
    for ch in my_string.lower():
        if ch not in ("aeiou"):
            r_str += ch
    return r_str


print(remove_vowels("India"))
