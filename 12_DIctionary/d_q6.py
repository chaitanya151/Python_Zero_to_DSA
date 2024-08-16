d1 = {"apple": 3, "banana": 5, "cherry": 7}
d2 = {"banana": 8, "orange": 10, "apple": 9}

for k2, v2 in d2.items():
    d1[k2] = v2
print(d1)
