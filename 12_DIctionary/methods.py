from typing import Dict

marks: dict[str, int] = {
    "history": 78,
    "computer": 55,
    "science": 90,
    "Physics": 66,
    "Chemistry": 87,
}

# marks.clear()
# print(marks["history"])
print(
    marks.get("history", -1), marks.get("Bio", -1)
)  # if key is not present returns "None". 2nd arg we can give custom value.

# marks.pop("science")
# print(marks)

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 2}

dict1.update(dict2)
print(dict1)

# Add and update key
marks["computer"] = 50
marks["english"] = 100
# marks.update({"english": 100})  # add key
# marks.update({"Physics": 86}) # Update key

# from typing import Dict
# marks: Dict[str, int] = {
#     "history": 78,
#     "science": 16,
#     "computer": 99,
#     "chemistry": 65,
#     "sst": 25,
# }
# print(marks)
# # marks.clear()
# # print(marks["historyy"])
# # print(marks.get("historyy", 0))
# marks.pop("history")
# print(marks)
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 1, "d": 4, "a": 100}
# dict1.update(dict2)
# print(dict1)
