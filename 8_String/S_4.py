def word_count(my_string: str) -> int:
    if not my_string:
        return 0
    count = 1
    for ch in my_string.lower():
        if ch == " ":
            count += 1
    return count


print(word_count("python is easy to learn"))
