my_string = "a%b@c9d_e.f"

# result = "abcdef"
result = ""
for i in my_string:
    if ord("a") <= ord(i) <= ord("z"):
        result += i
print(result)
