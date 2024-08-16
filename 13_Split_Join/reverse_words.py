my_str = "more killer puzzles murdle"
split_str = my_str.split()
print(split_str)

# reversed
r_words = split_str[::-1]
print(r_words)

ans = "".join(ch for ch in r_words)
print(type(ans))
print(ans)
