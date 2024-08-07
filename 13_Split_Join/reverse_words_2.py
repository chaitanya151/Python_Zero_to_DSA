my_str = "python is a good language."
# reverse the characters in the str for each word

store = []
split_str = my_str.split(" ")
length = len(split_str)
for index in range(0, length):
    r_word = split_str[index][::-1]
    store.append(r_word)

print(" ".join(ch for ch in store))

# single line ans
print(" ".join(words[::-1] for words in split_str))
