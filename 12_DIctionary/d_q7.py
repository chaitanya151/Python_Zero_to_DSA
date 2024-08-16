"""
Update the values of a dictionary by 
multiplying them by a given factor 
only if the value is an integer.
"""

dict = {"a": 3, "b": "Hello", "c": 7.5, "d": 18}
multiplying_factor = int(input("Enter the multiplier: "))
for k, v in dict.items():
    print(k, v)
    if type(v) == int:
        dict[k] = v * multiplying_factor

print(dict)
