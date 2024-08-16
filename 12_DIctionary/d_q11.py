d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "b": 200, "d": 400}

result = {}
result.update(d1)
print(result)

for k, v in d2.items():
    if k in result:
        # updates the value of key in the result dict.
        result[k] = result[k] + v
    else:
        # Add a new key with a value in the dict.
        result[k] = v

print(result)
