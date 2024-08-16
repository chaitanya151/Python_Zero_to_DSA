my_str = "python is a good language."

split_str = my_str.split()
r_string = split_str[::-1]
print(" ".join(ch[::-1] for ch in r_string))

# Another way
words = my_str.split()
words.reverse()
print(" ".join(word[::-1] for word in words))
