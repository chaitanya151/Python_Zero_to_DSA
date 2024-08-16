string_1 = "SpiderMan"
# print(string_1[::-1])


# Using function
def reverse_string(string_1: str) -> str:
    r_string = ""
    for ch in string_1:
        if ch != "":
            r_string = ch + r_string
    return r_string


print(reverse_string(string_1))
