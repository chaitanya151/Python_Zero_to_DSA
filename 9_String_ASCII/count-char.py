# my_string = "dhaw43789HGDSAK&*(#$  HDK486/*-+daw)"

# Alpha_count = 0
# Num_count = 0
# Sym_count = 0
# Space_count = 0


# def count_char(my_string: str):
#     for ch in my_string:
#         ascii_code = ord(ch)
#         if (ascii_code >= 65 and ascii_code <= 90) or (
#             ascii_code >= 97 and ascii_code <= 122
#         ):
#             Alpha_count += 1
#         elif "0" <= ch <= "9":
#             Num_count += 1
#         elif ch == " ":
#             Space_count += 1
#         else:
#             Sym_count += 1


# print(
#     f"Alpha_count -> {Alpha_count}, Num_count -> {Num_count}, Space_count -> {Space_count}, Sym_count -> {Sym_count}"
# )


def count_char(user_String: str):
    aplhabets = 0
    digits = 0
    spaces = 0
    symbols = 0
    for ch in user_String:
        ascii_code = ord(ch)
        if (97 <= ascii_code <= 122) or (65 <= ascii_code <= 90):
            aplhabets += 1
        elif ascii_code >= 48 and ascii_code <= 57:
            digits += 1
        elif ascii_code == 32:
            spaces += 1
        else:
            symbols += 1
    print(
        f"Aplhabets = {aplhabets}, digits = {digits}, spaces = {spaces}, symbols = {symbols}"
    )


my_string = "dhaw43789HGDSAK&*(#$  HDK486/*-+daw)"
