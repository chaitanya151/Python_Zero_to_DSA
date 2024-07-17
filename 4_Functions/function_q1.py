# def marks(maths: int, sci: int, hindi: int, eng: int, history: int) -> bool:
#     percentage = maths + sci + hindi + eng + history / 5
#     if percentage > 33:
#         return True
#     else:
#         return False


# print(marks(10, 30, 40, 55, 67))

"""
other way of writing boolean
"""


# def marks(maths: int, sci: int, hindi: int, eng: int, history: int) -> bool:
#     percentage = maths + sci + hindi + eng + history / 5
#     if percentage > 33:
#         return True
#     return False


# print(marks(10, 30, 40, 55, 67))

"""
More concise way
"""


def marks(maths: int, sci: int, hindi: int, eng: int, history: int) -> bool:
    percentage = maths + sci + hindi + eng + history / 5
    return percentage >= 33


print(marks(10, 30, 40, 55, 67))
