"""
Split = String to list
Joining = List to String
"""

# my_list = ["m", "u", "r", "d", "l", "e"]
# res = " ".join(ch + "|" for ch in my_list)
# print(res)

my_list = [4, 5, 6, "m", "u", "r", "d", "l", "e"]
# print(
#     "".join(ch for ch in my_list)
# )  # TypeError: sequence item 0: expected str instance, int found

print("".join(str(ch) for ch in my_list))  # Int are converted to a str.
